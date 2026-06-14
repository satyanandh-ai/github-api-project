
# GitHub API Project

A FastAPI-based REST API that retrieves public GitHub user information using the GitHub REST API and returns clean, structured JSON responses.

## Features

- Fetch GitHub user details by username
- Display follower and following counts
- Show public repository statistics
- Clean JSON responses
- Error handling for invalid usernames
- Built with FastAPI

## Technologies Used

- Python
- FastAPI
- Requests
- GitHub REST API
- Uvicorn

## Project Structure

```text
github-api-project/
│
├── github_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/satyanandh-ai/github-api-project.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
uvicorn github_api:app --reload
```

## API Endpoints

### Home

```http
GET /
```

### About

```http
GET /about
```

### Get GitHub User

```http
GET /github/{username}
```

Example:

```http
GET /github/octocat
```

## Example Response

```json
{
  "username": "octocat",
  "name": "The Octocat",
  "followers": 18000,
  "following": 9,
  "public_repos": 8,
  "profile_url": "https://github.com/octocat"
}
```

## Learning Outcomes

This project helped me learn:

- FastAPI fundamentals
- Path Parameters
- Working with REST APIs
- Handling JSON responses
- Error handling in APIs
- Git and GitHub workflow

## Author
Satya Anandh


