import speech_recognition as sr
from gtts import gTTS
import os
import streamlit as st
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Function to convert voice to text
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Please speak something.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I did not understand your audio.")
        except sr.RequestError:
            st.error("Could not request result from Google Speech Recognition service.")
        return None

# Function to convert text to speech
def text_to_voice(text):
    if text:
        st.write(f"Converting Text to Voice: {text}")
        tts = gTTS(text=text, lang='en')
        file_path = os.path.join(os.getcwd(), "output.mp3")
        tts.save(file_path)
        st.write(f"File saved at: {file_path}")

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        os.remove(file_path)
    else:
        st.error("No text to convert to speech.")

# Streamlit app structure
def main():
    st.title("Speech Recognition & Text-to-Speech App")
    
    option = st.selectbox("Choose an option", ["Convert Voice to Text", "Convert Text to Voice"])

    if option == "Convert Voice to Text":
        if st.button("Start Listening"):
            text = voice_to_text()
            if text:
                tts_choice = st.radio("Do you want to convert the recognized text to speech?", ("Yes", "No"))
                if tts_choice == "Yes":
                    text_to_voice(text)

    elif option == "Convert Text to Voice":
        text = st.text_input("Enter the text to convert to voice:")
        if st.button("Convert to Voice"):
            text_to_voice(text)

if __name__ == "__main__":
    main()
