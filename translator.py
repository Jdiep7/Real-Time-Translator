import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import re
from transformers import MarianMTModel, MarianTokenizer

# ---------------------------
# 1. Load models (only once)
# ---------------------------
print("Loading models...")
whisper_model = whisper.load_model("base")

model_name = "Helsinki-NLP/opus-mt-en-fr"  # Change language here
tokenizer = MarianTokenizer.from_pretrained(model_name)
translator_model = MarianMTModel.from_pretrained(model_name)

# ---------------------------
# 2. Record audio
# ---------------------------
import numpy as np


def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎤 Recording... Speak now!")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    write(filename, fs, audio)

    print("✅ Done recording")

# ---------------------------
# 3. Speech → Text
# ---------------------------
def transcribe(audio_file):
    print("🧠 Transcribing...")
    result = whisper_model.transcribe(audio_file)
    return result["text"]

# ---------------------------
# 4. Translate
# ---------------------------
def translate(text):
    print("🌍 Translating...")
    sentences = re.split(r'(?<=[.!?]) +', text)

    translated_sentences = []

    for sentence in sentences:
        if sentence.strip():
            inputs = tokenizer(sentence, return_tensors="pt", padding=True)
            outputs = translator_model.generate(**inputs)
            translated = tokenizer.decode(outputs[0], skip_special_tokens=True)
            translated_sentences.append(translated)

    return " ".join(translated_sentences)

# ---------------------------
# 5. Run pipeline
# ---------------------------
def main():
    record_audio()

    speech_text = transcribe("input.wav")
    print("\n📝 You said:", speech_text)

    translated_text = translate(speech_text)
    print("🌍 Translated:", translated_text)

if __name__ == "__main__":
    main()