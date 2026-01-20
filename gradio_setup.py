from Chatbot import chat
import gradio as gr
gr.ChatInterface(fn=chat).launch()
