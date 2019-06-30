# FacialEmotionClassifierClient
Facial emotion classifier with your web camera and `MAX-Facial-Emotion-Classifier`. 

## Prerequisite
1. Prepare docker container of `MAX-Facial-Emotion-Classifier`. See `README` of [MAX-Facial-Emotion-Classifier](https://github.com/IBM/MAX-Facial-Emotion-Classifier). 

1. Change the URL of `MAX-Facial-Emotion-Classifier` in the script. 

    ```python
    # server url
    -SERVER_URL = 'http://localhost:5000/model/predict'
    +SERVER_URL = 'http://XX.XX.XX.XX:5000/model/predict'
    ```

---

## How to run App
1. Run `MAX-Facial-Emotion-Classifier`. 

    ```console
    $ docker run -it -p 5000:5000 max-facial-emotion-classifier
    ```

1. Execute the script.

    ```console
    $ python app.py
    ```

You can get the label list on your console like below: 

```console
-------------------------------------------------
label: neutral, prob: 90.637868642807 %
label: sadness, prob: 7.638801634311676 %
label: surprise, prob: 0.8172840811312199 %
label: anger, prob: 0.52631008438766 %
label: contempt, prob: 0.1814456656575203 %
label: fear, prob: 0.11854476761072874 %
label: disgust, prob: 0.045531484647654 %
label: happiness, prob: 0.03421727742534131 %
-------------------------------------------------
```

---