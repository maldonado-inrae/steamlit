import streamlit as st
from mistralai import Mistral

st.title("Analyse d'Image")

prompt = st.text_input('Entrez un URL')

# Connexion à l'API
client = Mistral(api_key="1lFl56MeZF5OE8jCiGeIYAz28qzcrmM2")

if st.button("Envoyer"):

  # Analyse d'image unique
  chat_response = client.chat.complete(
      model = "pixtral-12b-2409",
      messages= [
      {
          "role": "user",
          "content": [
              {
                  "type": "text",
                  "text": "Que contient cette image ?"
              },
              {
                  "type": "image_url",
                  "image_url":prompt
              }
          ]
      }
  ]
  )
  
  st.write(chat_response.choices[0].message.content)
  
