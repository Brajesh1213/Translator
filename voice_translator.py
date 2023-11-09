import googletrans
import speech_recognition
import gtts
import playsound


recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language='hi')  # Set the language to the language you're speaking in
    print(text)

translator = googletrans.Translator()
translation = translator.translate(text, dest="bn")
print(translation)
print(translation.text)

converted_audio = gtts.gTTS(translation.text, lang="bn")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")
