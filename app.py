
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from openai import OpenAI
import json

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def ask_llm(prompt):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )
    return response.output_text


def normalize_skill(skill):
    skill = skill.lower().strip()

    skill = skill.replace(" framework", "")
    skill = skill.replace(" library", "")
    skill = skill.replace(" technology", "")

    aliases = {
        "rest api": "rest apis",
        "restful api": "rest apis",
        "java script": "javascript",
        "react js": "react.js",
        "reactjs": "react.js",
        "dsa": "data structures and algorithms",
        "data structures & algorithms": "data structures and algorithms",
        "data structures and algorithm": "data structures and algorithms",
        "ml": "machine learning",
        "ai": "artificial intelligence",
        "artificial intelligence (ai)": "artificial intelligence"
    }

    return aliases.get(skill, skill)


def generate_roadmap(missing_skills):

    if not missing_skills:
        return "You already have all the required skills!"

    learning_response = ask_llm(f"""
Create a short, beginner-friendly learning roadmap for these missing skills:

{missing_skills}

For each skill, give:

Skill Name
Topics: 3 to 5 important topics
Practice Project: 1 small project
Learning Time: approximate time

IMPORTANT:
- Keep the roadmap short and practical.
- Use plain text only.
- Do NOT use Markdown.
- Do NOT use #, ##, -, *, backticks, or other Markdown symbols.
- Put each item on a separate line.
- Keep explanations very short.
""")

    return learning_response


def analyze_job(job_description, my_skills):

    response_text = ask_llm(f"""
Extract the technical skills required from this job description.

Return only a JSON object with a "required_skills" list.

Job Description:
{job_description}
""")

    result = json.loads(response_text)

    required_skills = list(set(
        normalize_skill(skill)
        for skill in result["required_skills"]
    ))

    missing_skills = []

    for skill in required_skills:
        if skill not in my_skills:
            missing_skills.append(skill)

    learning_roadmap = generate_roadmap(missing_skills)

    return {
        "required_skills": required_skills,
        "your_skills": my_skills,
        "missing_skills": missing_skills,
        "learning_roadmap": learning_roadmap
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    my_skills = list(set(
        normalize_skill(skill)
        for skill in data["skills"].split(",")
    ))

    result = analyze_job(
        data["job_description"],
        my_skills
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

