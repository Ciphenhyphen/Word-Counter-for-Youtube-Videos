import sys
import json
import struct

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

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




while True:
    msg = getMessage()
    # getMessage returns the vidID
    