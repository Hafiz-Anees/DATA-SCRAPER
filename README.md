# 🌐 AI-Powered Web Scraper

Turn any website into a clean, readable summary in seconds using **AI + Web Scraping** 🚀

---

## ✨ Overview

This project is a simple yet powerful **Streamlit web app** that:

* 🔍 Extracts meaningful text from any website
* 🧹 Removes unwanted elements (scripts, styles, ads, etc.)
* 🤖 Uses AI to generate a **clear and concise summary**
* 📄 Displays both **raw extracted content** and **formatted summary**

Perfect for students, developers, and researchers who want to quickly understand web content without reading everything.

---

## 🎯 Features

✅ Clean and minimal UI using Streamlit
✅ Smart web scraping with BeautifulSoup
✅ AI-powered summarization (OpenAI GPT model)
✅ Markdown-rendered output for readability
✅ Handles long content with truncation
✅ Expandable section for extracted text

---

## 🖼️ Demo Preview

[https://a-web-scraper.streamlit.app/](https://a-web-scraper.streamlit.app/)

---

## ⚙️ Tech Stack

* 🐍 Python
* 🌐 Streamlit
* 🧠 OpenAI API
* 🍲 BeautifulSoup
* 📡 Requests
* 🔐 Python-dotenv

---

## 📁 Project Structure

```
web_summarizer/
│── app.py              # Streamlit UI
│── scraper.py          # Scraping + AI logic
│── .env                # API key (not pushed to GitHub)
│── requirements.txt
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hafiz-Anees/DATA-SCRAPER.git

```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add Your API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a website URL
2. App fetches HTML content using `requests`
3. `BeautifulSoup` cleans and extracts readable text
4. AI model summarizes the content
5. Results are displayed in a clean Markdown format

---

## 📸 Output Sections

### 📄 Extracted Content

* Raw cleaned text from the website
* Displayed in a collapsible Markdown block

### 🤖 AI Summary

* Short, structured summary
* Highlights key points, news, and announcements

---

## 💡 Future Improvements

* 🔗 Multi-page crawling
* 📥 Export summary as PDF
* 🎨 Advanced UI/UX design
* 🌍 Language translation support
* ⚡ Faster scraping & caching

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🙌 Author

**Anees Ur Rehman**
💻 BSCS Student | AI Enthusiast | Flutter Developer

---

## ⭐ Support

If you like this project:

👉 Give it a **star** on GitHub
👉 Share it with others

---

> 💡 *"Save time. Extract knowledge. Let AI do the reading."*
