import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import re
import time
from transformers import MarianMTModel, MarianTokenizer
import numpy as np

print("Loading models...")
whisper_model = whisper.load_model("base")

model_name = "Helsinki-NLP/opus-mt-en-fr"  # Change language here
tokenizer = MarianTokenizer.from_pretrained(model_name)
translator_model = MarianMTModel.from_pretrained(model_name)

# ---------------------------
# Record small chunk
# ---------------------------
def record_chunk(filename="input.wav", duration=2, fs=16000):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)

# ---------------------------
# Transcribe
# ---------------------------
def transcribe(audio_file):
    result = whisper_model.transcribe(audio_file)
    return result["text"].strip()

# ---------------------------
# 4. Translate
# ---------------------------
def translate(text):
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
    print("\n🎧 Real-time translator started (Ctrl+C to stop)\n")
    
    while True:
        try:
            record_chunk()
            speech_text = transcribe("input.wav")
        
            if speech_text:
                print("\n📝 You said:", speech_text)
                translated_text = translate(speech_text)
                print("🌍 Translated:", translated_text)
                print("-" * 50)
            
            time.sleep(0.2)
        
        except KeyboardInterrupt:
            print("\n🛑 Stopped")
            break
                
    

if __name__ == "__main__":
    main()