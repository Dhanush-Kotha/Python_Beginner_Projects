# ✦ Career_Gen AI

## 🤖 AI-Powered Career Roadmap Assistant

Career_Gen AI is a beginner-friendly Generative AI application that helps students create a personalized career roadmap based on their **target career, job description, and resume**.

The application analyzes the uploaded resume, identifies existing skills and potential skill gaps, and generates a practical learning roadmap, project ideas, interview preparation topics, and the next step to take.

## 🎯 Problem Statement

Students often know the job role they want but are unsure about:
- Which skills they already have
- Which skills are missing
- What they should learn first
- Which projects they should build
- What topics they should prepare for interviews

Career_Gen AI brings these requirements together in one simple assistant.

## 💡 Solution

The user provides:

1. 🎯 Target Career
2. 📋 Job Description
3. 📄 Resume PDF

The AI then generates:

- 🎯 Career Goal
- 📄 Resume Analysis
- 🔍 Skill Gap
- 📚 Skills to Learn
- 🗓️ 4-Week Learning Roadmap
- 💻 Project Suggestions
- 🎤 Interview Preparation
- 🚀 Next Step

## 🔄 How It Works

User Input
→ Resume + Job Description + Career Goal
→ Resume Text Extraction
→ AI Prompt Generation
→ Local Generative AI Model
→ Personalized Career Analysis
→ Learning Roadmap & Career Recommendations

## 🧠 Generative AI

This project uses:

**Qwen/Qwen2.5-0.5B-Instruct**

The model runs locally through Hugging Face Transformers.

This means the project does not require an OpenAI API key or paid API credits.

> Note: The first run may require an internet connection to download the model. After downloading, the model can be loaded from the local Hugging Face cache.

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct
- PyTorch
- Accelerate
- pypdf

## 📂 Project Structure

```text
Career_Gen_AI/
│
├── Career_assistant_updated.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scriptsctivate
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Run the application

```powershell
python -m streamlit run Career_assistant_updated.py
```

The application will open in your browser.

## 📄 Resume Upload

Upload your resume in **PDF format**.

The application extracts text from the PDF using `pypdf` and sends the extracted content to the local AI model for personalized analysis.

## 🎤 Hackathon Presentation

### 30-Second Explanation

> Career_Gen AI is a Generative AI-powered career assistant designed for students. It takes the student's target career, job description, and resume, analyzes their current skills and skill gaps, and generates a personalized 4-week learning roadmap along with project ideas, interview preparation, and an immediate next step. It uses a lightweight Qwen model locally, so it does not require paid API credits.

## 🌟 Key Features

- Professional Streamlit interface
- Resume PDF upload
- Resume text extraction
- Job-description-based analysis
- Personalized skill-gap analysis
- 4-week learning roadmap
- Project recommendations
- Interview preparation
- Local Generative AI inference
- No OpenAI API credits required

## 🚀 Future Scope

Possible future improvements include:

- Resume scoring
- ATS compatibility analysis
- Real-time job matching
- Course recommendations
- Progress tracking
- AI mock interviews
- Larger and more capable language models
- Multi-agent career assistance

## ⚠️ Limitations

The application uses a lightweight local language model so it can run without paid API services. Its generated responses may therefore be less detailed or accurate than those from larger cloud-based models.

## 👨‍💻 Project

**Career_Gen AI**  
Generative AI Hackathon Project
