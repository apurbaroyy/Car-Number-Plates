import cv2
import easyocr
import os


harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)


cap.set(3, 480)
cap.set(4, 360)


reader = easyocr.Reader(['en'], gpu=False)


plate_cascade = cv2.CascadeClassifier(harcascade)


os.makedirs("plates", exist_ok=True)

min_area = 500
count = 0

frame_count = 0
plate_number = ""
img_roi = None


car_data = {

    "C06S0B38": {
        "name": "Ivan Petrov",
        "location": "Moscow",
        "country": "Russia"
    },

    "0007": {
        "name": "Rahim Ahmed",
        "location": "Dhaka",
        "country": "Bangladesh"
    },

    "CCC444": {
        "name": "Robin Rechard",
        "location": "Dhaka",
        "country": "Bangladesh"
    },
     "W659UEN": {
        "name": "Apurba",
        "location": "Tangail",
        "country": "Bangladesh"
    },
     "B505WLG": {
        "name": "Helex Devilan",
        "location": "Rome",
        "country": "Italy"
    },
     "SN66XMZ": {
        "name": "Shuvo Roy",
        "location": "Kolkata",
        "country": "India"
    },
     "XM32345": {
        "name": "Apurba Roy",
        "location": "Tangail",
        "country": "Bangladesh"
    }

}


while True:

    success, img = cap.read()

    if not success:
        break


    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    plates = plate_cascade.detectMultiScale(
        img_gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 40)
    )

    if len(plates) == 0:

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        continue

    for (x, y, w, h) in plates:

        area = w * h

        if area > min_area:

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(
                img,
                "Number Plate",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 255),
                2
            )

           
            img_roi = img[y:y+h, x:x+w]

        
            img_roi = cv2.resize(img_roi, (300, 100))

           
            gray_roi = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)

            gray_roi = cv2.bilateralFilter(
                gray_roi,
                11,
                17,
                17
            )


            frame_count += 1

            if frame_count % 10 == 0:

                result = reader.readtext(gray_roi)

                plate_number = ""

                for res in result:

                    text = res[1]
                    confidence = res[2]

                    if confidence > 0.4:
                        plate_number += text

             
                plate_number = ''.join(
                    filter(str.isalnum, plate_number)
                )

                plate_number = plate_number.upper()

            if plate_number != "":

                cv2.putText(
                    img,
                    plate_number,
                    (x, y+h+25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )


    cv2.imshow("Result", img)

    key = cv2.waitKey(1) & 0xFF


    if key == ord('s'):

        if img_roi is None:
            continue
        
        cv2.imwrite(
            f"plates/scan_{count}.jpg",
            img_roi
        )


        plate_number = ''.join(filter(str.isalnum, plate_number))
        plate_number = plate_number.strip().upper()

        print("\n========== DEBUG ==========")
        print("Detected Plate :", repr(plate_number))
        print("Database Plates:", list(car_data.keys()))
        print("===========================\n")

        matched_key = None
        for db_plate in car_data.keys():
            if db_plate.strip().upper() == plate_number:
                matched_key = db_plate
                break

        if matched_key:
            print("MATCH FOUND")
            info = car_data[matched_key]
        else:
            print("NOT FOUND")
            info = {
                "name": "Vehicle Not Found",
                "location": "N/A",
                "country": "N/A"
            }


        result_img = img.copy()

        cv2.rectangle(
            result_img,
            (0, 150),
            (480, 360),
            (0, 255, 0),
            cv2.FILLED
        )

        cv2.putText(
            result_img,
            "PLATE SAVED",
            (120, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        cv2.putText(
            result_img,
            f"Plate: {plate_number}",
            (20, 220),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )

        cv2.putText(
            result_img,
            f"Name: {info['name']}",
            (20, 250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )

        cv2.putText(
            result_img,
            f"Location: {info['location']}",
            (20, 280),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )

        cv2.putText(
            result_img,
            f"Country: {info['country']}",
            (20, 310),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )

        cv2.imshow("Result Info", result_img)

        cv2.waitKey(1500)

        count += 1


    if key == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()