#we can add more skills according to updates#
SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "data analysis", "pandas",
    "numpy", "tensorflow", "pytorch", "react",
    "node.js", "aws", "docker", "flask", "django"
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))