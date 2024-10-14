import speech_recognition as sr
from gtts import gTTS
import os
import streamlit as st

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
            st.write("Sorry, I did not understand your audio.")
        except sr.RequestError:
            st.write("Could not request result from Google Speech Recognition service.")
        return None

def text_to_voice(text):
    if text:
        st.write(f"Converting Text to Voice: {text}")
        tts = gTTS(text=text, lang='en')
        file_path = os.path.join(os.getcwd(), "output.mp3")
        tts.save(file_path)
        st.write(f"File saved at: {file_path}")

        # Play audio using Streamlit's st.audio
        with open(file_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

        os.remove(file_path)
    else:
        st.write("No text to convert to speech.")

def main():
    st.title("Speech Recognition and Text-to-Speech App")
    choice = st.selectbox("Choose an option:", ["Convert Voice to Text", "Convert Text to Voice"])

    if choice == "Convert Voice to Text":
        text = voice_to_text()
        if text:
            tts_choice = st.selectbox("Do you want to convert the recognized text to speech?", ["No", "Yes"])
            if tts_choice == "Yes":
                text_to_voice(text)
    elif choice == "Convert Text to Voice":
        text = st.text_input("Enter the text to convert to voice:")
        if text:
            text_to_voice(text)

if __name__ == "__main__":
    main()
