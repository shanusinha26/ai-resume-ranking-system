from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return float(similarity[0][0])


def rank_candidate(candidate_skills, jd_skills, similarity):
    
    matched = set(candidate_skills) & set(jd_skills)
    skill_score = len(matched) / len(jd_skills) if jd_skills else 0

    skill_depth = len(candidate_skills) / 10

    final_score = (
        skill_score * 0.5 +
        similarity * 0.3 +
        skill_depth * 0.2
    ) * 100

    breakdown = {
        "skill_match": round(skill_score * 100, 2),
        "similarity": round(similarity * 100, 2),
        "skill_depth": round(skill_depth * 100, 2)
    }

    return round(final_score, 2), list(matched), breakdown