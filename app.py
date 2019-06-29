import requests
import cv2
import json

# server url
SERVER_URL = 'http://localhost:5000/model/predict'

# color
DETECTION_BOX_COLOR = (0, 0, 255)

#
# main
#
if __name__ == '__main__':
    # video capture
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()

        # image size
        height, width = frame.shape[:2]

        # resize & gray scale
        small_image = cv2.resize(frame, None, fx=0.4, fy=0.4)
        gray_image = cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)
        
        # encode (.jpg)
        ret, buf = cv2.imencode('.jpg', gray_image)

        # analysis
        files = {
            'image': ('input_image', buf),
        }
        response = requests.post(SERVER_URL, files=files)

        # json parse
        json_dict = json.loads(response.text)

        predictions = json_dict['predictions']
        for prediction in predictions:
            # face detection
            detection_box = prediction['detection_box']
            ymin_factor, xmin_factor, ymax_factor, xmax_factor = detection_box[:4]
            cv2.rectangle(frame, (int(xmin_factor * width), int(ymin_factor * height)), (int(xmax_factor * width), int(ymax_factor * height)), DETECTION_BOX_COLOR, 3)

            # emotion
            print("-------------------------------------------------")
            emotion_predictions = prediction['emotion_predictions']
            for emotion_prediction in emotion_predictions:
                # results
                label_id = emotion_prediction['label_id']
                label = emotion_prediction['label']
                probability = emotion_prediction['probability']
                print("label: {}, prob: {} %".format(label, float(probability) * 100.0))               
            print("-------------------------------------------------")

        # displaying
        image = cv2.resize(frame, None, fx=0.5, fy=0.5)
        cv2.imshow('INPUT', image)

        # waiting next frame / exit
        if cv2.waitKey(1) == 27:
            break

    # release resources
    cap.release()
    cv2.destroyAllWindows()
