from pathlib import Path
import google.generativeai as genai
from gtts import gTTS
import multiprocessing as mp
import numpy as np
import pyttsx3
from voice_ids import getvoiceid
engine = pyttsx3.init()
# Api key
genai.configure(api_key="XXX")

# Set up the model vision
generation_config_Visionpro = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

# Set up the model writer
generation_config_LLM = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

# Set up the vision model
model_see = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config_Visionpro,
                              safety_settings=safety_settings)
# Set up the write model
model_write = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config_LLM,
                              safety_settings=safety_settings)


# import the playht SDK
from pyht import Client, TTSOptions, Format
import simpleaudio as sa

#Initialize PlayHT API with your credentials
client = Client("XXX", "XXX")

# configure your stream
options = TTSOptions(
    # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
    voice="s3://voice-cloning-zero-shot/f82faf7a-5bef-4d5f-90e3-57028822f5be/original/manifest.json",

    # you can pass any value between 8000 and 48000, 24000 is default
    sample_rate=44_100,
  
    # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
    format=Format.FORMAT_MP3,

    # playback rate of generated speech
    speed=0.9,
)
save_file_path = "output.mp3"

def read_image(image):
  image_parts = [
    {
      "mime_type": "image/webp",
      "data": image
    },
  ]
  return image_parts

def prompt1(image):
  image_parts = [
  {
    "mime_type": "image/webp",
    "data": image
  },
  ]
  prompt_captionGen = [
    "give all the features of the image that can be used for making a story of it,mention all the objects, people and activity\n",
    image_parts[0],
  ]
  


def get_caption(language,prompt1 = prompt1):
  image_parts = [
  {
    "mime_type": "image/webp",
    "data": image.read()
  }
  ]
  prompt_captionGen = [
    "generate a caption for this image,mention all the objects, people and activity in {} language".format(language),
    image_parts[0],
  ]
  response = model_see.generate_content(prompt_captionGen)
  return response.text


def prompt2():
  prompt_ficgen = [
    "generate a Interesting playful fictional story based on this prompt",response.text
  ]

def get_fic(Caption,option,option2,language,prompt2 =prompt2):
  prompt_ficgen = [
    "generate a fictional {} story for {} story based on this prompt where genre {} in {} language".format(length,option,option2,language),caption
  ]
  fic_story = model_write.generate_content(prompt_ficgen)
  return fic_story.text



import streamlit as st
# Configure stremlit page
st.set_page_config(
    page_title="Image Fiction Generatorrrr",
    page_icon=":smiley:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Page header
st.title("Image Fiction Generator")
st.subheader("Generate a Fictional story from an image")

# Upload image
image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
    help="Upload an image to generate a caption and a story.",
)

if image is None:
    st.warning("Please upload an image.")
    st.stop()
elif read_image(image) == False:
    st.error("Invalid image file. Please upload a valid image file.")
    st.stop()
else:
    st.success("Valid image file.")

st.markdown("""---""")


# Display image
# st.image(image, caption="Uploaded Image", use_column_width=True)

st.image(image, caption=None, width=500, use_column_width=False , clamp=False, channels="RGB", output_format="auto")

# Create Divider
st.markdown("""---""")

# Choose Language
language = st.selectbox(
    'Select Language',
    ('English', 'Hindi'))
st.write('You selected:', language)

# Generate caption
st.subheader("Caption")

caption = get_caption(language)
st.write(caption)


# # Test to speech(caption)
# cap = gTTS(caption, lang='en', slow=False)
# cap.save('cap.mp3')

# streamlit button to choose text or audio
# col1, col2 = st.columns([1,1])  # Adjust column ratios as needed
# button = 0
# with col1:
#     if st.button("Text Caption"):
#         button = 1

# with col2:
#     if st.button("Audio Caption"):
#         button = 2
# # streamlit button to choose text or audio
# if button == 1:
# st.write(caption)
# elif button == 2:
#   # Test to speech(caption)
#   audio_file = open('cap.mp3', 'rb')
#   audio_bytes = audio_file.read()

#   st.audio(audio_bytes, format='audio/mp3')

# # Test to speech (story)
# engine.setProperty('rate',125)
# engine.save_to_file(story, 'speech.mp3')
# engine.runAndWait


# audio_file = open('speech.mp3', 'rb')
# audio_bytes = audio_file.read()

# st.audio(audio_bytes, format='audio/mp3')
st.markdown("""---""")

# coll,colm = st.columns([1,1])
# with coll:
st.subheader("Story options")
Voice_id = st.selectbox(
    'Select Voice ?(only available for short stories)',
    ('Optimus Prime', 'Morgan Freeman', 'Priyanka Chopra','Shashi Tharoor','R Madhvan','Dr. Bahubali'))
  
st.write('You selected:', Voice_id)
  

options = getvoiceid(Voice_id)

#Demographic Checkbox
col1, col2 = st.columns([1,1])
with col1:
  option = st.selectbox(
      'Who is the story for ?',
      ('Children', 'Adult', 'Shakespheare'))

  st.write('You selected:', option)

with col2:
  option2 = st.selectbox(
      'Select Genre of the story',
      ('Action','Adventure','Comedy','Horror','Funny','Mystry','Thriller','Drama','Sports','Coming of Age',"Moral"))
  st.write('You selected:', option2)

st.markdown("""___""")
# Generate Story
st.subheader("Story")
length = "long(less than 3000 characters)"
story =""
colone,coltwo = st.columns([1,2])
with colone:
  if st.button('Generate Story'):
    length = "long"
    story = get_fic(length,caption,option,option2,language)
length = "long"
with coltwo:
  if st.button('Generate Short Story'):
    length = "short(250 words)"
    story = get_fic(length,caption,option,option2,language)

st.markdown("""---""")



text = story
#st.write(length)
st.write(story)
if length == "short(250 words)":
  save_file_path = "play.mp3"

  # Voice_id = st.selectbox(
  #     'Select Voice ?',
  #     ('Optimus Prime', 'Morgan Freeman', 'Priyanka Chopra','Shashi Tharoor','R Madhvan'))

  
  
  # st.write('You selected:', Voice_id)
  

  with open(save_file_path, "wb") as f:
    for chunk in client.tts(text=story, voice_engine="PlayHT2.0-turbo", options=options):
      if chunk:
        f.write(chunk)
  st.audio(data = "play.mp3",format="audio/wav")


# st.markdown("""---""")
# save_file_path = "play.mp3"
# sound_play=False
# if length=="short(250 words)":

#   if st.button('Generate Audio'):
#     sound_play = True

# if sound_play==True:
#   with open(save_file_path, "wb") as f:
#     for chunk in client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options):
#       if chunk:
#         f.write(chunk)
#         sound_play="ready"

# if sound_play=="ready":
#   st.audio(data = "play.mp3",format="audio/wav")


