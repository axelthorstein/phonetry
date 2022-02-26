import io

from pydub import AudioSegment
from pydub.silence import split_on_silence


def open_audiofile(file_name):
    with io.open(file_name, "rb") as audio_file:
        return audio_file.read()


def slice_audio(src, dst, t1, t2):
    buffer = 300
    millisecond_modifier = 1000

    t1 = t1.total_seconds() * millisecond_modifier + buffer
    t2 = t2.total_seconds() * millisecond_modifier + buffer

    newAudio = AudioSegment.from_wav(src)
    newAudio = newAudio[t1:t2]
    newAudio.export(f'assets/processed_audio/{dst}.wav', format="wav")
