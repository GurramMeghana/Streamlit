import requests
import os

# Replace these with your repository details and workflow information
OWNER = "GurramMeghana"
REPO = "Streamlit"
WORKFLOW_ID = "user_creation.yml"  # Use workflow ID or filename (e.g., "workflow.yml")
BRANCH = "dev"  # Branch to trigger the workflow

# GitHub Token (App Installation Token or PAT)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# API endpoint
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches"

# Headers for the request
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

# Payload for the request
PAYLOAD = {
    "ref": BRANCH,
    "inputs": {  # Optional inputs if your workflow_dispatch accepts inputs
        "URL": "abc"
        "Passwords":"abcad1"
        "User":"abc_sa"
        "User_password":"abcde2"
    }
}

def trigger_workflow():
    response = requests.post(API_URL, headers=HEADERS, json=PAYLOAD)
    if response.status_code == 204:
        print("Workflow triggered successfully!")
    else:
        print(f"Failed to trigger workflow: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    trigger_workflow()
