import http.client, urllib.request, urllib.parse, urllib.error, base64,requests

#PreCondition: takes in a string of data
#PostCondition: returns keyphrases of that data
def keyWordsML(stringEmailData):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'b495fd0172454fe89baada62868354c7'
    }

    try:
        documents = {'documents' : [
      {'id': '1', 'language': 'en', 'text': stringEmailData }
      ]}

        response  = requests.post("https://eastus2.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases", headers=headers, json=documents)
        key_phrases = response.json()
        return key_phrases


    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
