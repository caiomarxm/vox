from core.transcribe.transcribe import transcribe_audio

TEST_INPUT_AUDIO_PATH = "testdata/transcribe/20250408_test_transcription.wav"


def test_transcribe_audio():
    """Test the main transcribe_audio function with a real audio file."""
    transcription = transcribe_audio(TEST_INPUT_AUDIO_PATH)
    assert transcription is not None
    assert transcription != ""
