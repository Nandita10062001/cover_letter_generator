# 📝 AI Cover Letter Generator

<div align="center">
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Firecrawl](https://img.shields.io/badge/Firecrawl-FF6B35?style=for-the-badge&logo=fire&logoColor=white)

**Generate personalized cover letters in seconds using AI**

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage)

</div>

---

## 🎯 About

An automated tool that generates personalized cover letters by combining your resume with job posting details. Simply upload your resume (PDF) and provide a job URL - AI handles the rest!

**Built with:**
- **Streamlit** - Web interface
- **Google Gemini API** - AI-powered content generation
- **Firecrawl** - Intelligent job posting scraper

---

## 🎬 Demo

### Main Interface
![Application Interface](./screenshots/demo-main.png)

### Generated Cover Letter
![Cover Letter Output](./screenshots/demo-output.png)

---

## ✨ Features

- 📄 **PDF Resume Upload** - Upload your resume (up to 200MB)
- 🔗 **URL Scraping** - Paste job URLs from LinkedIn, Indeed, Naukri, etc.
- 📝 **Manual Input Option** - Paste job description text directly if URL doesn't work
- 🤖 **AI Generation** - Powered by Google Gemini for professional, personalized letters
- 📋 **One-Click Copy** - Copy generated cover letter instantly
- 💾 **Download** - Save as text file

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Firecrawl API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nandita10062001/cover_letter_generator.git
   cd cover_letter_generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**
   
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   FIRECRAWL_API_KEY=your_firecrawl_api_key_here
   ```

   **Get API Keys:**
   - Gemini: https://makersuite.google.com/app/apikey
   - Firecrawl: https://www.firecrawl.dev/

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

   Open your browser at `http://localhost:8501`

---

## 💻 Usage

### How to Use

1. **Upload Resume**: Choose your resume PDF file (text-based, not scanned images)

2. **Provide Job Details** - Choose one option:
   - **Paste Job URL**: From LinkedIn, Indeed, Naukri, or company websites
   - **Paste Job Description**: Manual text input if URL fails

3. **Generate**: Click "✨ Generate Cover Letter" button

4. **Download or Copy**: Save the generated cover letter

### Tips

💡 **URLs work for most sites** including LinkedIn, Indeed, Naukri

💡 **If URL fails**, use the paste text option

💡 **Use text-based PDF resumes** (not scanned images) for best results

---

## 📁 Project Structure

```
cover_letter_generator/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                   # API keys (not in repo)
├── .gitignore
├── README.md
├── utils/
│   ├── scraper.py         # Firecrawl integration
│   └── generator.py       # Gemini AI integration
└── screenshots/           # Demo images
    ├── demo-main.png
    └── demo-output.png
```

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** - Web framework for Python
- **[Google Gemini](https://ai.google.dev/)** - AI language model
- **[Firecrawl](https://www.firecrawl.dev/)** - Web scraping API
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variables

---

## 🗺️ Roadmap

- [x] Basic cover letter generation
- [x] Resume PDF upload
- [x] Job URL scraping
- [x] Manual job description input
- [ ] Multiple cover letter templates
- [ ] Export to PDF/Word format
- [ ] Save candidate profiles
- [ ] Cover letter history
- [ ] Browser extension

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

**Nandita Nandakumar**

GitHub: [@Nandita10062001](https://github.com/Nandita10062001)

Project Link: [https://github.com/Nandita10062001/cover_letter_generator](https://github.com/Nandita10062001/cover_letter_generator)

---

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) - AI language model
- [Firecrawl](https://www.firecrawl.dev/) - Web scraping API
- [Streamlit](https://streamlit.io/) - Python web framework
- [Shields.io](https://shields.io/) - README badges

---

<div align="center">

**Built with ❤️ • Powered by Google Gemini AI & Firecrawl**

⭐ Star this repo if you found it helpful!

</div>
