import requests
import base64
import streamlit as st
if __name__ == '__main__':
    url = 'https://app.fintalo.com/version-3zuq/api/1.1/obj/NDA%20Draft'
    headers = {'Authorization': 'Bearer 0976258289210c459e8375a21fc050fa'}

    data = open("/Users/luisgonzales/Desktop/doc-change-detector/highlighted_changes.docx", "rb").read()
    encoded = base64.b64encode(data)

    files = {
        "NDA Draft File": encoded
    }

    response = requests.post(url, headers=headers, files=files)
    print(response.status_code)
