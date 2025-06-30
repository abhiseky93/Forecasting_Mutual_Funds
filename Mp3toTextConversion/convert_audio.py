import speech_recognition as sr # type: ignore
from pydub import AudioSegment # type: ignore

# Convert MPEG to WAV (if needed)
audio_path = "audio.mpeg"  # Update this with your file path
wav_path = "converted_audio.wav"
sound = AudioSegment.from_file(audio_path)
sound.export(wav_path, format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("Converted Text:", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Could not request results from the speech recognition service.")
