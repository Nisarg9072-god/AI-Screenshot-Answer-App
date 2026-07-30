# 🤖 AI Screenshot Answer Assistant!!

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green.svg">
  <img src="https://img.shields.io/badge/OCR-Tesseract-orange.svg">
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-red.svg">
  <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg">
</p>

An intelligent desktop application built with **Python** that allows users to capture any part of their screen, automatically extract text using **Tesseract OCR**, and instantly generate AI-powered answers using **Google Gemini**.

Whether you're solving programming questions, reading study material, or extracting text from images, this application provides a seamless workflow from screenshot to intelligent response within seconds.

---

# ✨ Features

### 📸 Smart Screenshot Capture
- Capture any selected area of the screen.
- Works similar to the Windows Snipping Tool.
- Fast and lightweight.

### 🔍 Optical Character Recognition (OCR)
- Automatically extracts text from screenshots.
- Powered by **Tesseract OCR**.
- Handles printed text efficiently.

### 🤖 AI-Powered Answer Generation
- Uses **Google Gemini API** to understand extracted questions.
- Generates concise, human-readable answers.
- Works with educational and programming-related questions.

### ✍️ Manual Question Input
- Users can manually type questions.
- Useful when OCR is not required.
- Instant AI-generated responses.

### 🌙 Modern Dark Theme
- Clean and elegant Tkinter interface.
- Comfortable for long usage.
- Responsive layout.

### 🧹 One-Click Reset
- Clear screenshots, extracted text, and AI responses.
- Start a new session instantly.

---

# 🎯 Use Cases

✅ Students solving assignments

✅ Developers understanding code snippets

✅ Competitive programming practice

✅ Interview preparation

✅ Reading questions from PDFs

✅ Extracting text from images

✅ Learning from screenshots

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Tkinter | Desktop GUI |
| Tesseract OCR | Text Extraction |
| pytesseract | Python OCR Wrapper |
| mss | High-Speed Screen Capture |
| Pillow | Image Processing |
| Google Gemini API | AI Question Answering |

---

# 📂 Project Structure

```text
AI-Screenshot-Answer-App/
│
├── assets/
│   ├── screenshots/
│   └── icons/
│
├── main.py
├── screenshot.py
├── ocr.py
├── gemini.py
├── ui.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Nisarg9072-god/AI-Screenshot-Answer-App.git
```

```bash
cd AI-Screenshot-Answer-App
```

---

## 2️⃣ Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Tesseract OCR

Download Tesseract:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path inside the application if necessary.

Example:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 5️⃣ Configure Gemini API

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 6️⃣ Run the Application

```bash
python main.py
```

---

# 🚀 How It Works

```text
Capture Screenshot
        │
        ▼
Extract Text using OCR
        │
        ▼
Identify Question
        │
        ▼
Send to Gemini AI
        │
        ▼
Receive Intelligent Answer
        │
        ▼
Display Result in Desktop App
```

---

# 📸 Screenshots

## Main Window

> Add screenshot here

```
assets/screenshots/home.png
```

---

## Screenshot Selection

> Add screenshot here

```
assets/screenshots/snipping.png
```

---

## OCR Extraction

> Add screenshot here

```
assets/screenshots/ocr.png
```

---

## AI Response

> Add screenshot here

```
assets/screenshots/answer.png
```

---

# 💡 Future Improvements

- Voice Input
- PDF Question Extraction
- Multiple Language OCR
- Answer History
- Export Answers as PDF
- Drag-and-Drop Images
- Clipboard Monitoring
- Markdown Response Support
- Code Formatting
- AI Explanation Modes

---

# 📈 Learning Outcomes

Through this project, I gained practical experience with:

- OCR using Tesseract
- Desktop GUI development with Tkinter
- Google Gemini API integration
- Environment variable management
- Image processing with Pillow
- Screen capture using mss
- Python application architecture
- Prompt engineering fundamentals

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes.

```bash
git commit -m "Add New Feature"
```

4. Push your branch.

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request.

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the project

🐞 Report bugs

💡 Suggest new features

---

# 👨‍💻 Author

## Nisarg Panchal

**AI | Machine Learning | Generative AI | Python Developer**

### GitHub

https://github.com/Nisarg9072-god

---

# 📄 License

This project is licensed under the MIT License.

---

## 🌟 If you like this project, don't forget to leave a ⭐ on the repository!
