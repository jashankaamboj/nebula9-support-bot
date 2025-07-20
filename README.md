# Real-Time Customer Support Bot 
📌 Project Overview
This is a real-time customer support bot that uses speech-to-text and semantic search to help users get instant answers from a knowledge base. It uses Whisper for audio transcription, sentence transformers for finding the best match answer, and Streamlit for a web interface.
📁 Project Files
Main files and folders:
• app.py - Streamlit app
• asr.py - Speech recognition
• rag.py - Retrieval logic
• kb/ - Your .txt knowledge base
• venv/ - Python virtual environment
• requirements.txt - All needed libraries
📦 Key Libraries Used
- streamlit: Web interface
- whisper (openai-whisper): Converts voice to text
- torch: Required by Whisper
- sentence-transformers: Text similarity
- scikit-learn: Cosine similarity
- gtts or pyttsx3: Speak the bot's response
- faiss-cpu (optional): Faster search
- ffmpeg: Required by Whisper to handle audio
🛠 Installation Steps
1. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate

2. Install required libraries:
   pip install --upgrade pip
   pip install -r requirements.txt

3. Make sure ffmpeg is installed and added to system PATH.
🚀 How It Works
1. User speaks into the mic
2. Whisper transcribes the speech
3. Sentence transformer finds best answer from kb
4. Bot displays and optionally speaks the answer
❓ Troubleshooting
- ffmpeg not found? Install it and add to PATH
- whisper error? Reinstall torch and whisper
- Import errors? Delete venv and reinstall everything
- streamlit not working? Ensure venv is activated
👤 Author
Made by: Jashan Kamboj
Contact: jashankaamboj@gmail.com
