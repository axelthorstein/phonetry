import re
import json

from gcp import analyze_audio
from audio_utils import open_audiofile
from audio_utils import split_audio
from logging_utils import log_match


def get_boundaries(words, match_start, match_end):
    # Find the index of the first and last word in the word list.
    start = 0
    end = 0
    i = 0

    while end <= match_end:
        end += len(words[i].word)

        if start == match_start:
            start_index = i
        if end == match_end:
            end_index = i

        end += 1
        start = end
        i += 1

    return start_index, end_index


def match_audio(source_poem, poem_transcript, words):
    for line in source_poem:
        # How does this work for repeated lines?
        match = re.search(line, poem_transcript)

        if match:
            start, end = get_boundaries(words, match.start(), match.end())
            log_match(line, words, start, end)
            slice_audio(
                'assets/audio/poem.wav',
                line,
                words[start].start_time,
                words[end].end_time)


def main():
    content = open_audiofile('assets/audio/poem.mp3')
    with open('assets/text/poem.json') as file:
        source_poem = json.load(file)

    result = analyze_audio(content)
    transcript = result.transcript
    words = result.words

    match_audio(source_poem, result.transcript, result.words)


if __name__ == '__main__':
    main()
