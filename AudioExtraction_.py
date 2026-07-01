from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

"""

The program will be in command line interface, where user's input the link of a video, then a word. 
The program will return the amount of time's the word has been said throughout the video. 
This program should be available as an .exe file, to be readily available. 


"""

def ExtractContent(Input):
    # Additions to be made: Catch errors, 
    yt_api = YouTubeTranscriptApi()
    transcript = yt_api.fetch(Input)    
    
    formatter = TextFormatter()

    text_format = formatter.format_transcript(transcript)
    
    return text_format
    

def Transcript_to_String(Transcript):
    pass

def Analyze():
    pass

print("Enter a video ID (11 characters): ")
identification = input()

while len(identification) < 11 or len(identification) > 11:
    print("Please re-enter a youtube ID (Before the & and after v= ): ")
    identification = input()
transcript = ExtractContent(identification)