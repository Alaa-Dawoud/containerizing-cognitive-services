import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key here}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories,Description',
    'details': 'Celebrities,Landmarks',
    'language': 'en',
    'model-version': 'latest',
})
def get_analytics(img_url):
    body = {"url":img_url}
    try:
        conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v3.2/analyze?%s" % params, f"{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data
