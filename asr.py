import whisper

# Load Whisper model
model = whisper.load_model("base")

# Transcribe audio file
def transcribe_audio(file_path="audio/Password_Rest.wav"):
    result = model.transcribe(file_path)
    return result["text"]
