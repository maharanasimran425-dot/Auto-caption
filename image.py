from google import genai
from google.genai import types
import streamlit as st

st.title("Autocaption")

def answer(image):
    image_bytes = image.read()

    client = genai.Client(api_key= "AIzaSyDGz6iyIiT_V9yjOa4xNETr7oBEzAwBlC8")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type=image.type ,
        ),
        '''You are an expert in modern aesthetic caption expert,
        -make content of this file by following these rules:
        -use catchy words, 
        - give only 1 line caption
        -give a short heading according to the picture, bold , large
        -only 3 caption of different types
        -use simple english and emojis
        
          '''
        ]
    )
    return response

image = st.file_uploader("Upload a image to generate a caption", type=["jpg", "jpeg", "png"])
if st.button("REVEAL"):
    if image:
        with st.spinner("Processing your file....almost there⏳"):
            result = answer(image)
            st.write(result.text)
    else:
        st.warning("⚠️ File Error: Unable to retrive the file. Re-upload needed.")