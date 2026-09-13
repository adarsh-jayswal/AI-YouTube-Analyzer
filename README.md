# 🎥 AI YouTube Analyzer

AI YouTube Analyzer is a simple web application that helps you understand YouTube videos using AI.

Just enter a YouTube video URL, and the application analyzes the video and gives you useful information in an easy-to-read format.

## ✨ Features

- 🔗 Analyze any supported YouTube video
- 🤖 AI-powered video analysis
- 📝 Get a simple summary of the video
- ⏱️ Get important timestamps
- 📌 Find key points and useful information
- 📚 Understand the main topics of the video
- 🎨 Simple and clean Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Agno
- Google Gemini
- YouTubeTools
- python-dotenv

## 📂 Project Structure

```text
AI-YouTube-Analyzer/
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
├── README.md
├── requirements.txt
├── ui.py
└── youtube_analyzer.py
```

> The `.env` file is not included in the repository because it contains the Google API key.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/adarsh-jayswal/AI-YouTube-Analyzer.git
```

### 2. Open the Project

```bash
cd AI-YouTube-Analyzer
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Add Your Google API Key

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_api_key_here
```

> Keep your API key private. Never upload the `.env` file to GitHub.

### 5. Run the Application

```bash
streamlit run ui.py
```

The application will open in your browser.

## 💡 How It Works

1. Enter a YouTube video URL.
2. The application sends the request to the AI agent.
3. YouTubeTools gets information from the video.
4. Google Gemini analyzes the video.
5. The analysis is displayed on the screen.

## 📌 Example

Enter a YouTube video URL and get information such as:

- Video overview
- Important points
- Timestamps
- Main topics
- Key learning points

## 🛠️ Project Files

| File | Description |
|------|-------------|
| `ui.py` | Streamlit user interface |
| `youtube_analyzer.py` | AI YouTube analyzer agent |
| `requirements.txt` | Required Python libraries |
| `.streamlit/config.toml` | Streamlit configuration |
| `.gitignore` | Files ignored by Git |

## 🔐 Environment Variables

This project uses a Google Gemini API key.

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

The `.env` file is included in `.gitignore`, so your API key stays private.

## 🔗 Links

**GitHub:**  
https://github.com/adarsh-jayswal/AI-YouTube-Analyzer

**LinkedIn:**  
https://www.linkedin.com/in/adarsh-jaiswal-1bbbbb328/

## 👨‍💻 Author

**Adarsh Jaiswal**

Computer Science & Engineering Student

---

⭐ If you like this project, consider giving it a star!