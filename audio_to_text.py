import speech_recognition as sr

# initialize the recognizer
def audioss(path):
    r = sr.Recognizer()

    # open the audio file
    # with sr.AudioFile("audio_file.wav") as source:
    with sr.AudioFile(path) as source:
        audio_data = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)
    return text
print     

    # print the transcribed text
