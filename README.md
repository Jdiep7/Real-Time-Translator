# 🎧 Real-Time Speech Translator

## 🚀 Overview
This project is an early-stage prototype of a **real-time speech translation system**.  

The goal is to build something that allows a user to:
- Speak into a microphone  
- Have their speech transcribed  
- Translate it into another language  
- Eventually hear the translated speech in real time  

Long-term, this could evolve into an **earbud-style live translator** with natural voice output and context-aware translations.

---

## 🧠 Current Features

- 🎤 Audio recording from microphone  
- 📝 Speech-to-text using Whisper  
- 🌍 Text translation (English → French) using MarianMT  
- 🔁 End-to-end pipeline (record → transcribe → translate)

---

## 🛠️ Tech Stack

- Python  
- Whisper (speech recognition)  
- Hugging Face Transformers (translation)  
- SoundDevice (audio input)  
- SciPy (audio file handling)  

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg (required for Whisper)
Make sure `ffmpeg` is installed and added to your PATH.

Test:
```bash
ffmpeg -version
```

---

## ▶️ How to Run

```bash
python translator.py
```

You will:
1. Record audio from your microphone  
2. See the transcribed text  
3. See the translated output  

---

## ⚠️ Current Limitations

- ❌ Not real-time (records fixed duration audio)  
- ❌ Translation may miss parts of sentences  
- ❌ No audio playback (text output only)  
- ❌ No context awareness or tone handling  

---

## 🧩 Roadmap

### ✅ Phase 1: Basic Pipeline (Current)
- [x] Record audio  
- [x] Transcribe speech  
- [x] Translate text  

---

### 🔄 Phase 2: Real-Time Translation (Next Step)
- [ ] Record audio in small chunks (1–2 seconds)  
- [ ] Process continuously in a loop  
- [ ] Reduce latency (faster Whisper model)  
- [ ] Smooth output (combine partial sentences)  

---

### 🌍 Phase 3: Better Translation
- [ ] Improve sentence handling (split + merge)  
- [ ] Replace MarianMT with LLM API  
- [ ] Add context-aware translation  

---

### 🔊 Phase 4: Audio Output
- [ ] Convert translated text to speech (TTS)  
- [ ] Play translated audio in real time  
- [ ] Experiment with different voices  

---

### 🎭 Phase 5: Advanced Features
- [ ] Tone/emotion detection  
- [ ] Natural phrasing improvements  
- [ ] Slang and idiom handling  

---

### 🎧 Phase 6: Final Vision
- [ ] Real-time streaming pipeline  
- [ ] Low-latency processing  
- [ ] Voice cloning (optional)  
- [ ] Mobile or wearable integration  

---

## 💡 Future Ideas

- Live conversation translation  
- Multi-language switching  
- Speaker identification  
- Offline mode  

---

## 📌 Notes

This project is a learning and exploration project focused on:
- Speech processing  
- Machine translation  
- Real-time systems  

---

## 🙌 Acknowledgements

- OpenAI Whisper  
- Hugging Face Transformers  
- Open-source audio tools  