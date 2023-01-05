import openai
import requests
import bs4

openai.api_key = "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"

def chatbot(prompt):
  # Use OpenAI's Completion API to generate a response
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    temperature=0.7,
  )
    # Extract the response text
  response_text = response["choices"][0]["text"]
  return response_text

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("/index.html")

@app.route("/ask", methods=["POST"])
def ask():
  question = request.form["question"]
  answer = chatbot(question)
  return render_template("/ask.html", question=question, answer=answer)

if __name__ == "__main__":
  app.run()
