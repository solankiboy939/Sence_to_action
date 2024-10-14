import speech_recognition as sr
from gtts import gTTS
import os
import pygame

def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak something.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand your audio.")
        except sr.RequestError:
            print("Could not request result from Google Speech Recognition service.")
        return None

def text_to_voice(text):
    if text:
        print(f"Converting Text to Voice: {text}")
        tts = gTTS(text=text, lang='en')
        file_path = os.path.join(os.getcwd(), "output.mp3")
        tts.save(file_path)
        print(f"File saved at: {file_path}")

        pygame.mixer.init()
    
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        os.remove(file_path)
    else:
        print("No text to convert to speech.")

def main():
    print("1. Convert Voice to Text")
    print("2. Convert Text to Voice")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        text = voice_to_text()
    elif choice == "2":
        text = input("Enter the text to convert to voice: ")
    else:
        print("Invalid choice.")
        return

    if choice == "1" and text:
        tts_choice = input("Do you want to convert the recognized text to speech? (y/n): ").lower()
        if tts_choice == "y":
            text_to_voice(text)
    elif choice == "2":
        text_to_voice(text)

if __name__ == "__main__":
    main()
