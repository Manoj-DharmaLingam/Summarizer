from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF"""
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    
    if request.method == "POST":
        text = request.form.get("text", "")
        pdf_file = request.files.get("pdf")
        mode = request.form.get("mode", "short")
        length = request.form.get("length", "medium")
        
        # Get text from PDF or input
        if pdf_file and pdf_file.filename:
            text = extract_text_from_pdf(pdf_file)
        
        if text.strip():
            # Simple prompts
            mode_prompts = {
                "short": "Summarize in 2-3 sentences.",
                "detailed": "Write detailed summary.",
                "bullets": "Summarize as bullet points.",
                "notes": "Create study notes.",
                "keypoints": "List key points."
            }
            
            length_prompts = {
                "short": "Max 100 words.",
                "medium": "Max 200 words.",
                "long": "Max 400 words."
            }
            
            prompt = f"{mode_prompts[mode]} {length_prompts[length]}\n\nText: {text}"
            
            try:
                response = model.generate_content(prompt)
                summary = response.text
            except:
                summary = "Error: Could not generate summary. Check your API key."
    
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)