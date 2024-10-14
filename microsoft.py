import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

def voice_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Read the entire audio file
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I did not understand your audio.")
        except sr.RequestError:
            st.error("Could not request result from Google Speech Recognition service.")
    return None

def text_to_voice(text):
    if text:
        tts = gTTS(text=text, lang='en')
        file_path = os.path.join(os.getcwd(), "output.mp3")
        tts.save(file_path)
        return file_path
    return None

def main():
    st.title("Voice Recognition App")

    st.subheader("Convert Voice to Text")
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    if audio_file:
        st.audio(audio_file, format='audio/wav')  # Preview audio
        recognized_text = voice_to_text(audio_file)
        if recognized_text:
            st.write(f"Recognized Text: {recognized_text}")

            if st.button("Convert Text to Voice"):
                file_path = text_to_voice(recognized_text)
                if file_path:
                    st.audio(file_path, format='audio/mp3')

if __name__ == "__main__":
    main()
