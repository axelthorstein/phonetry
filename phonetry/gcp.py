import logging

from google.cloud import speech

LOG = logging.getLogger("phonetry.gcp")


def analyze_audio(content):
    # TODO: Discard audiofile if below a certain threshold.
    # TODO: Deal with audio that's longer than 60s.

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=44100,
        language_code="en-US",
        enable_word_time_offsets=True,
    )

    response = speech.SpeechClient().recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        LOG.info(u"Transcript: {}".format(result.alternatives[0].transcript))

    LOG.info("More than one alternative found: {}".format(result.alternatives))
    LOG.info("Only returning the first.")

    return result.alternatives[0]
