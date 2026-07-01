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
    

# Removed Transcript_To_String, .formatter provided string format


def Analyze_and_Modify(formatted_text, word_to_search):
    # Search and match formatted text with word to search
    # return an int of all the occurrences of word to search
    
    count = 0

    # for every word in formatted text,
    # if a word in an index matches word_to_search, increment count

    words = formatted_text.split()

    for word in words:
        if word == word_to_search:
            count += 1
    
    return count

print("Enter a video ID (11 characters): ")
identification = input()

while len(identification) < 11 or len(identification) > 11:
    print("Please re-enter a youtube ID (Before the & and after v= ): ")
    identification = input()

print("Enter a word to be searched for in the video: ")
word_to_search = input()

transcript = ExtractContent(identification)

occurrences = Analyze_and_Modify(transcript, word_to_search)

print(f"The total amount of times: \n{word_to_search} \n was said is: {occurrences}")