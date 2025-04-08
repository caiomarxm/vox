# This uses https://github.com/m-bain/whisperXI

import torch
import whisperx

# TODO: Put these in a config file
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
COMPUTE_TYPE = "int8"  # change to "float16" if high on GPU mem (to increase accuracy)


def transcribe_audio(file_path: str) -> str | None:
    model = whisperx.load_model("base", device=DEVICE, compute_type=COMPUTE_TYPE)
    result = model.transcribe(file_path)
    return result
