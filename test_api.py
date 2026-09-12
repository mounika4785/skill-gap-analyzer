import requests

response = requests.post(
    "http://127.0.0.1:5000/analyze",
    json={
        "job_description": "Python developer with SQL",
        "skills": "Python, Java"
    }
)

print(response.json())