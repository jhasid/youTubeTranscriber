import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv() #load all env variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def extract_transcript_api(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]  #get the video id from youtube url after "="
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id) #This will return a list of dictionaries 

        #append all transcript text
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript    

    except Exception as e:
        raise e


# calling gemini ai and summarizing the transcript
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response
