import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonData = { "raw_document": { "text": text_to_analyse } }
    resRaw = requests.post(url, json=jsonData, headers=headers)
    if resRaw.status_code == 400:
        return {"anger":None, "disgust":None,"fear":None,"joy":None,"sadness": None, "dominant_emotion":None}
    resjson = json.loads(resRaw.text)  
    emotions = {}
    for key,value in resjson.items():
        if key == 'emotionPredictions':
            for j in resjson[key][0]:
                if j == 'emotion':
                    for emo, rating in resjson[key][0][j].items():
                        emotions[emo] = rating            
                    
    emotionsList = sorted(emotions.items(), key=lambda x:x[1], reverse=True)
    emotions = dict(emotionsList)
    emotions['dominant_emotion'] = list(emotions.keys())[0] 
    return emotions