import streamlit as st
import pandas as pd

from parser import extract_text_from_pdf, extract_text_from_docx, extract_email, extract_phone
from skills import extract_skills
from ranking import calculate_similarity, rank_candidate

st.set_page_config(page_title="AI Resume Ranking", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>📄 AI Resume Ranking System</h1>",
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🚀 Smart Resume Analyzer with Explainable Ranking")
st.markdown("Upload resumes and compare them with a Job Description")

# Job Description
jd_text = st.text_area("📌 Enter Job Description")

# Upload files
uploaded_files = st.file_uploader(
    "📂 Upload Resumes (PDF/DOCX)",
    accept_multiple_files=True,
    type=["pdf", "docx"]   # 👈 restrict formats
)

# 👉 MAIN LOGIC
if uploaded_files and jd_text:

    jd_skills = extract_skills(jd_text)
    all_candidates = []

    for file in uploaded_files:

        # Extract text
        if file.name.endswith(".pdf"):
            text = extract_text_from_pdf(file)

        elif file.name.endswith(".docx"):
             text = extract_text_from_docx(file)

        else:
            st.warning(f"Unsupported file format: {file.name}")
            continue

        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)

        similarity = calculate_similarity(text, jd_text)

        score, matched_skills, breakdown = rank_candidate(skills, jd_skills, similarity)

        missing_skills = list(set(jd_skills) - set(skills))

        all_candidates.append({
            "Name": file.name,
            "Email": email,
            "Phone": phone,
            "Skills": ", ".join(skills),
            "Matched Skills": ", ".join(matched_skills),
            "Missing Skills": ", ".join(missing_skills),
            "Score": score,
            "Breakdown": f"S:{breakdown['skill_match']} | Sim:{breakdown['similarity']}",
            "Reason": f"{len(matched_skills)} skills matched, similarity {round(similarity,2)}"
        })

    # ✅ EVERYTHING BELOW MUST BE INSIDE if

    df = pd.DataFrame(all_candidates)

    df = df.sort_values(by="Score", ascending=False)
    df["Rank"] = range(1, len(df) + 1)

    st.subheader("🏆 Ranked Candidates")

    if not df.empty:
        top_candidate = df.iloc[0]

        st.success("🏆 Top Candidate")

        col1, col2, col3 = st.columns(3)

        col1.metric("Name", top_candidate["Name"])
        col2.metric("Score", top_candidate["Score"])
        col3.metric("Matched Skills", top_candidate["Matched Skills"])

    st.divider()

    st.dataframe(df, use_container_width=True, hide_index=True)