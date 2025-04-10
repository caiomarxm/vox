# This uses https://github.com/m-bain/whisperXI

import torch
import whisperx
from tenacity import retry, stop_after_attempt, wait_fixed

# TODO: Put these in a config file
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
COMPUTE_TYPE = "int8"  # change to "float16" if high on GPU mem (to increase accuracy)

print("🔄 Loading WhisperX model...")
model = whisperx.load_model("base", device=DEVICE, compute_type=COMPUTE_TYPE)
print(f"✅ Model loaded successfully on {DEVICE} using {COMPUTE_TYPE}")


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1), reraise=True)
def transcribe_audio(file_path: str) -> str | None:
    print(f"🎯 Transcribing audio file: {file_path}")
    result = model.transcribe(file_path)
    print("✨ Transcription complete!")

    # NOTE: We don't need timestamps, so we can just join the text
    text = " ".join([segment["text"] for segment in result["segments"]]).strip()
    print("📝 Generated text")

    return text
