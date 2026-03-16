import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    # Send the request
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response
    formatted_response = json.loads(response.text)

    # Add the IF-ELSE logic
    # If the response is successful (200), get the data
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    
    # If the response is an error (500), set values to None
    elif response.status_code == 500:
        label = None
        score = None

    # 4. Return the result dictionary
    return {'label': label, 'score': score}