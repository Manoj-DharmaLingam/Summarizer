# 🧠 AI Text Summarizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-orange.svg)](https://ai.google.dev/)

> A lightning-fast, minimalist web application that transforms lengthy texts and PDFs into concise, meaningful summaries using Google's Gemini AI.

## ✨ Features

- 📝 **Text & PDF Support** - Summarize text input or upload PDF documents
- ⚡ **Lightning Fast** - Powered by Gemini 1.5 Flash model
- 🎨 **Clean UI** - Modern, responsive design with smooth animations
- 🔧 **Customizable** - 5 summary modes and 3 length options
- 📋 **One-Click Copy** - Instantly copy summaries to clipboard
- 🚀 **Simple Setup** - Minimal dependencies, easy to deploy
- 💯 **Free & Open Source** - MIT licensed

## 🎯 Summary Modes

| Mode | Description |
|------|-------------|
| **Short** | Quick 2-3 sentence overview |
| **Detailed** | Comprehensive summary with key details |
| **Bullets** | Main points in bullet format |
| **Notes** | Organized study notes with headings |
| **Key Points** | Essential takeaways only |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get it here](https://aistudio.google.com/app/apikey))

## 📁 Project Structure
```
ai-text-summarizer/
├── app.py              # Flask application
├── templates/
│   └── index.html      # Frontend UI
├── .env                # Environment variables (create this)
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
```

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 1.5 Flash
- **PDF Processing**: PyPDF2
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6

## 📦 Dependencies
```txt
flask==3.0.0
python-dotenv==1.0.0
google-generativeai==0.8.3
PyPDF2==3.0.1
```

## 💡 Usage Examples

### Summarize Text
1. Click on the **Text** tab
2. Paste your content (articles, essays, documents)
3. Select summary mode and length
4. Click **Generate Summary**

### Summarize PDF
1. Click on the **PDF** tab
2. Click **Choose PDF File** and select your document
3. Choose your preferred mode and length
4. Click **Generate Summary**

## 🔑 Getting Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key**
4. Copy the key and add it to your `.env` file

## ⚙️ Configuration

You can customize the application by modifying these parameters in `app.py`:
```python
# Summary modes
mode_prompts = {
    "short": "Summarize in 2-3 sentences.",
    "detailed": "Write detailed summary.",
    "bullets": "Summarize as bullet points.",
    "notes": "Create study notes.",
    "keypoints": "List key points."
}

# Length limits
length_prompts = {
    "short": "Max 100 words.",
    "medium": "Max 200 words.",
    "long": "Max 400 words."
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Roadmap

- [ ] Add support for more file formats (DOCX, TXT)
- [ ] Implement summary history/bookmarks
- [ ] Add multi-language support
- [ ] Create REST API endpoints
- [ ] Add export options (PDF, DOCX, TXT)
- [ ] Implement user authentication
- [ ] Add batch processing for multiple files
- [ ] Dark mode toggle

## 🐛 Known Issues

- Large PDFs (>10MB) may take longer to process
- Some PDFs with complex formatting may not extract text correctly
- Image-based PDFs require OCR (not currently supported)

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for the powerful language model
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Font Awesome](https://fontawesome.com/) for the icons
- All contributors and users of this project

## 📧 Contact

Your Name - [D.S.Manoj](https://www.linkedin.com/in/ds-manoj-a67418327/)

---

## 🏷️ Tags

`#ai` `#machine-learning` `#nlp` `#text-summarization` `#flask` `#python` `#gemini-ai` `#google-ai` `#pdf-processing` `#web-app` `#natural-language-processing` `#text-processing` `#summarizer` `#ai-tool` `#automation` `#productivity` `#open-source` `#mit-license` `#rest-api` `#document-processing` `#pdf-summarizer` `#text-analysis` `#deep-learning` `#generative-ai` `#llm` `#chatgpt-alternative` `#free-ai-tools` `#study-tool` `#research-tool` `#content-summarization` `#academic-tool`

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ and Python

</div>
