import gradio as gr
import pandas as pd
import altair
import matplotlib as plt
import os
import openai
from dotenv import load_dotenv

load_dotenv()

def ai_chat(prompt, history):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    history = []
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system","content": "You are an data science tutor."},
        {"role": "user","content": prompt},
    ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(repsonse)
    return response


demo = gr.ChatInterface(
    fn=ai_chat, 
    submit_btn = 'Submit', 
    retry_btn = 'Retry',
    clear_btn = 'Clear',
    title = 'AI Tutor',
    )

demo.launch()