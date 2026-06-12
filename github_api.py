from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(
    title="GitHub API Project",
    description="Fetch GitHub user information using FastAPI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "GitHub API Project is running"
    }


@app.get("/about")
def about():
    return {
        "project": "GitHub API Project",
        "developer": "Satya Anandh",
        "technology": "FastAPI"
    }


@app.get("/github/{username}")
def get_github_user(username: str):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="GitHub user not found"
        )

    data = response.json()

    return {
        "username": data["login"],
        "name": data["name"],
        "bio": data["bio"],
        "followers": data["followers"],
        "following": data["following"],
        "public_repos": data["public_repos"],
        "profile_url": data["html_url"]
    }