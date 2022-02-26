import logging

LOG = logging.getLogger("phonetry")


def log_match(line, poem_words, start_index, end_index):
    first = poem_words[start_index]
    last = poem_words[end_index]

    LOG.info(line)
    LOG.info(f"{first.word} ... {last.word}")
    LOG.info(f"{first.start_time}s - {last.end_time}s")
