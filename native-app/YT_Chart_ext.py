import sys
import json
import struct

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def getMessage():
    raw = sys.stdin.buffer.read(4)
    
    if len(raw) == 0:
        sys.exit(0)
    
    messageLength = struct.unpack('@I', raw)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

def encodeMessage(messageContent):
    # https://docs.python.org/3/library/json.html#basic-usage
    # To get the most compact JSON representation, you should specify
    # (',', ':') to eliminate whitespace.
    # We want the most compact representation because the browser rejects
    # messages that exceed 1 MB.
    encodedContent = json.dumps(messageContent, separators=(',', ':')).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

def process_video_text(vidID):
    # Get VideoID from background.js
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(vidID)
    formatter = TextFormatter()
    formatter = formatter.format_transcript(transcript)

    return formatter

def read_words(formatted_text):
    unigrams = dict()
    
    read_words = formatted_text.split()
    # Do it like the unigram project, undupe (set) and dupe (vec)
    # Modify the character, but save the word post mod
    # Python doesn't allow a specific character to be removed, a new string is needed
    word_set = dict()
    for word in read_words:
        new_str = ""
        for i in range(len(word)):
            if word[i].isalnum() or word[i] == ' ':
                new_str += word[i].lower()

        if new_str in word_set:
            word_set[new_str] += 1
        else:
            word_set[new_str] = 1

        # Now to jsonify this.
    return json.dumps(word_set)
        



while True:
    msg = getMessage()
    # getMessage returns the vidID
    result_json = read_words(msg)
    sendMessage(encodeMessage(result_json));