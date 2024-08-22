import io
from io import BytesIO

import requests
import base64
import streamlit as st
import zipfile
from docx import Document


def test_bubble_post():
    url = 'https://app.fintalo.com/version-3zuq/api/1.1/obj/NDA%20Draft'
    headers = {'Authorization': 'Bearer 0976258289210c459e8375a21fc050fa'}

    data = open("/Users/luisgonzales/Desktop/doc-change-detector/highlighted_changes.docx", "rb").read()
    encoded = base64.b64encode(data)

    files = {
        "NDA Draft File": encoded
    }

    response = requests.post(url, headers=headers, files=files)
    print(response.status_code)
    return response

def test_bubble_get_doc():
    url = "https://67733159a0034ce5a72d4d185ce71bc3.cdn.bubble.io/f1723452333969x289717951185701760/NDA_Projekt_Green.docx"
    response = requests.get(url)

    with open('bubble_doc.docx', 'wb') as f:
        f.write(response.content)

    response_content = BytesIO(response.content)
    response_doc = Document(response_content)

    for paragraph in response_doc.paragraphs:
        print(paragraph.text)

    buffer = io.BytesIO()
    response_doc.save(buffer)
    buffer.seek(0)

    base64_encoded = base64.b64encode(buffer.read()).decode('utf-8')
    print(base64_encoded)

    return response

def test_bubble_put():
    url = 'https://app.fintalo.com/version-3zuq/api/1.1/obj/NDA%20Draft'
    headers = {'Authorization': 'Bearer 0976258289210c459e8375a21fc050fa'}

    data = open("/Users/luisgonzales/Desktop/doc-change-detector/highlighted_changes.docx", "rb").read()
    encoded = base64.b64encode(data)

    files = {
        "NDA Draft File": encoded,
        "Unique id": '1724316615554x985384440838156300'
    }

    response = requests.put(url, headers=headers, files=files)
    print(response.status_code)
    return response





if __name__ == '__main__':
    test_bubble_put()

