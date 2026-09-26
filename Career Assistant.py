import streamlit as st
from transformers import pipeline
from pypdf import PdfReader

# 1. PAGE SETTINGS
st.set_page_config(
    page_title="Career_Gen AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PROFESSIONAL UI STYLING
st.markdown("""
<style>
    .stApp {
        background: cream;
    }

    .hero {
        padding: 42px 35px;
        border-radius: 24px;
        background: linear-gradient(135deg, #111827, #312e81);
        color: white;
        text-align: center;
        margin-bottom: 28px;
        box-shadow: 0 12px 35px rgba(31, 41, 55, 0.18);
    }

    .hero-title {
        font-size: 44px;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 18px;
        opacity: 0.9;
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 7px 15px;
        border-radius: 999px;
        background: rgba(255,255,255,0.14);
        border: 1px solid rgba(255,255,255,0.25);
        font-size: 14px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #111827;
        margin: 8px 0 4px 0;
    }

    .section-subtitle {
        color: #6b7280;
        margin-bottom: 18px;
    }

    .feature-card {
        padding: 20px;
        border-radius: 16px;
        background: white;
        border: 1px solid #e5e7eb;
        min-height: 125px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .feature-card h4 {
        margin: 0 0 8px 0;
        color: #111827;
    }

    .feature-card p {
        margin: 0;
        color: #6b7280;
        font-size: 14px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        min-height: 48px;
        font-weight: 700;
        border: none;
    }

    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# PROFESSIONAL HOME PAGE
st.markdown("""
<div class="hero">
    <div class="hero-title">✦ Career_Gen AI</div>
    <div class="hero-subtitle">
        Your intelligent career roadmap assistant
    </div>
    <span class="badge">🤖 Generative AI • 📄 Resume Analysis • 🎯 Career Planning</span>
</div>
""", unsafe_allow_html=True)

# QUICK VALUE PROPOSITION
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="feature-card">
        <h4>📄 Resume Analysis</h4>
        <p>Analyze your resume and identify existing skills and improvement areas.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="feature-card">
        <h4>🎯 Skill Gap</h4>
        <p>Compare your profile with the requirements of your target job.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="feature-card">
        <h4>🚀 Career Roadmap</h4>
        <p>Get a practical learning roadmap, projects and interview preparation.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">🎯 Build Your Personalized Career Plan</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Enter your target role, job description and optionally upload your resume.</div>', unsafe_allow_html=True)

# 2. LOAD AI MODEL
@st.cache_resource
def load_ai_model():
    ai = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct",
        device=-1
    )
    return ai

# Preload the model with a visible spinner so the page never looks blank
# on the first run while weights are downloading/loading in the background.
if "model_ready" not in st.session_state:
    with st.spinner("🤖 Loading AI model for the first time (this can take a minute)..."):
        load_ai_model()
    st.session_state.model_ready = True

# 3. AI FUNCTION
# FIX: Qwen2.5-Instruct is a CHAT model. Feeding it one big raw string (the old
# code) skips its chat template, so it often returns an almost-empty
# completion — the script "runs fine" but there's nothing to show.
# Calling it with a proper messages list makes it actually use the
# instruct template and produce real output.
def generate_answer(prompt):
    ai = load_ai_model()

    messages = [
        {"role": "system", "content": "You are an AI career mentor. Follow the user's formatting instructions exactly."},
        {"role": "user", "content": prompt}
    ]

    result = ai(
        messages,
        max_new_tokens=700,
        do_sample=True,
        repetition_penalty=1.1,
        temperature=0.7,
    )

    output = result[0]["generated_text"]

    # With chat-style input, generated_text comes back as the full message
    # list; the model's reply is the last entry.
    if isinstance(output, list):
        return output[-1]["content"].strip()
    return str(output).strip()

# 4. USER INPUT
career = st.text_input(
    "🎯 Target Career",
    placeholder="Example: AI Developer"
)

Job_Description = st.text_area(
    "📋 Job Description",
    placeholder="Paste the job description here...",
    height=160
)

resume_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"],
    help="Upload your resume in PDF format for personalized resume analysis."
)

# Resume preview/status
resume_text = ""
if resume_file is not None:
    try:
        reader = PdfReader(resume_file)
        pages_text = []
        for page in reader.pages:
            text = page.extract_text() or ""
            pages_text.append(text)
        resume_text = "\n".join(pages_text).strip()

        if resume_text:
            st.success(f"✅ Resume uploaded successfully — {len(reader.pages)} page(s) detected.")
        else:
            st.warning("The PDF was uploaded, but no readable text was found.")
    except Exception as e:
        st.error(f"Unable to read the resume PDF: {e}")

st.markdown("<br>", unsafe_allow_html=True)

# FIX: keep the last generated plan in session_state so it doesn't disappear
# the moment Streamlit reruns the script for any other reason.
if "career_plan" not in st.session_state:
    st.session_state.career_plan = ""

# 5. GENERATE CAREER PLAN
if st.button("🚀 Generate My Career Plan", type="primary"):

    if career.strip() == "" or Job_Description.strip() == "":
        st.warning("Please enter your target career and job description.")

    else:
        resume_section = resume_text if resume_text else "No resume uploaded."

        prompt = f"""
TARGET CAREER:
{career}

JOB DESCRIPTION:
{Job_Description}

RESUME:
{resume_section}

Create a short personalized career plan based on the target career, job description, and resume when available.

Give exactly these sections, using Markdown headings (##):

## 1. 🎯 Goal
Explain the target role in 2 short lines.

## 2. 📄 Resume Analysis
If a resume is provided, give:
- Key strengths
- Skills already present
- Important missing skills
If no resume is provided, say resume analysis is unavailable.

## 3. 🔍 Skill Gap
Compare the resume/current skills with the job description and list the most important skills to learn.

## 4. 📚 Skills to Learn
List 6-8 skills in learning order.

## 5. 🗓️ 4-Week Roadmap
Week 1: ...
Week 2: ...
Week 3: ...
Week 4: ...

## 6. 💻 Projects
Suggest 3 projects from beginner to advanced based on the target role.

## 7. 🎤 Interview Preparation
Give 5 important topics/questions to practice.

## 8. 🚀 Next Step
Tell the user exactly what to start learning today.

Use simple language and short points.
Be practical and personalized.
Do not repeat the full resume or job description.
"""

        with st.spinner("🤖 AI is analyzing your profile and creating your career plan..."):
            try:
                answer = generate_answer(prompt)
            except Exception as e:
                answer = ""
                st.error(f"Generation failed: {e}")

        if answer:
            st.session_state.career_plan = answer
            st.success("Career plan generated!")
        else:
            st.warning("The model returned an empty response. Try a shorter job description or click Generate again.")

# Always render the last generated plan (survives reruns)
if st.session_state.career_plan:
    st.markdown('<div class="section-title">📋 Your AI Career Plan</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(st.session_state.career_plan)

# 6. FOOTER
st.divider()
st.caption("Career_Gen AI | Generative AI Project | Runs locally")
