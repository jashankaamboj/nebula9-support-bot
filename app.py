import streamlit as st
from asr import transcribe_audio
from intent_classifier import detect_intent
from rag import load_kb, get_answer
from tts import speak
import os
import base64

# Page Config 
st.set_page_config(page_title="Nebula9 Support Bot", page_icon="assets/Nebula9-Logo.webp", layout="centered")

# Helper to encode logo 
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/webp;base64,{encoded}"

logo_base64 = get_base64_image("assets/Nebula9-Logo.webp")

# Custom CSS 
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        background: #f9fbff;
    }

    .logo-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: white;
        padding: 10px 30px;
        border-bottom: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .logo-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo-left img {
        height: 38px;
        border-radius: 6px;
    }

    .logo-left span {
        font-size: 18px;
        font-weight: 700;
        color: #003566;
    }

    .nav-right {
        display: flex;
        align-items: center;
        gap: 25px;
    }

    .nav-links {
        display: flex;
        gap: 20px;
        font-size: 15px;
    }

    .nav-links span {
        color: #333;
        font-weight: 500;
        cursor: pointer;
    }

    .consult-btn {
        background-color: #0077cc;
        color: white;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        border: none;
        cursor: pointer;
    }

    .title {
        font-size: 34px;
        text-align: center;
        color: #002b5b;
        margin-top: 20px;
        font-weight: 700;
    }

    .subtitle {
        font-size: 16px;
        text-align: center;
        color: #666;
        margin-bottom: 20px;
    }

    .stButton button {
        background-color: #0077cc;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        padding: 6px 14px;
        font-size: 14px;
    }

    .stAudio {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 0.5rem;
        background-color: #fff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }

    .stSpinner > div {
        color: #0077cc;
    }

    footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# Top Logo NavBar
st.markdown(f"""
    <div class="logo-bar">
        <div class="logo-left">
            <img src="{logo_base64}" alt="Nebula9 Logo">
            <span>Nebula9.ai</span>
        </div>
        <div class="nav-right">
            <div class="nav-links">
                <span>Services</span>
                <span>Industries</span>
                <span>Resources</span>
                <span>Company</span>
            </div>
            <button class="consult-btn">Book a Consultation</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Title
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <img src="{logo_base64}" alt="Nebula9 Logo" width="100" style="margin-bottom: 10px;">
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Nebula9.ai Support Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real-time voice query → intent detection → smart response</div>', unsafe_allow_html=True)

# Upload Section
uploaded_file = st.file_uploader("🎧 Upload a voice query (.wav)", type=["wav"])

if uploaded_file:
    audio_path = os.path.join("audio", uploaded_file.name)
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(audio_path)

    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(audio_path)
        st.success("✅ Transcription complete!")

    with st.expander("📝 Transcript", expanded=True):
        st.markdown(f"**User said:** `{transcript}`")

    with st.spinner("Analyzing intent..."):
        intent = detect_intent(transcript)

    with st.expander("🧠 Detected Intent", expanded=True):
        st.info(f"**Intent:** {intent}")

    with st.spinner("Fetching best response..."):
        questions, kb = load_kb("data/faqs.txt")
        answer = get_answer(transcript, questions, kb)

    with st.expander("💬 Bot Response", expanded=True):
        st.success(answer)

    speak(answer)

    st.markdown("---")
    st.caption("Built by Nebula9.ai | Powered by OpenAI Whisper, Transformers & Streamlit")
