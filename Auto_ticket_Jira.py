import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

load_dotenv()

# environment variables
JIRA_API_URL = os.getenv('JIRA_API_URL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')
JIRA_USER_EMAIL = os.getenv('JIRA_USER_EMAIL')
JIRA_PROJECT_KEY = os.getenv('JIRA_PROJECT_KEY')
JIRA_ISSUE_TYPE_ID = os.getenv('JIRA_ISSUE_TYPE_ID')

# for authentication using api token
auth = HTTPBasicAuth(JIRA_USER_EMAIL, JIRA_API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

@app.route('/createJira', methods=['POST'])
def create_jira():
    body_value = request.json
    #This condition returns a default status code of 200 for an appropriate /jira comment and handles other exceptions.
    if body_value.get('comment', {}).get('body') == "/jira":
        #From Jira official documentation for issues API: edited and selected required fields for this logic
        payload = {
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "project": {
                    "key": JIRA_PROJECT_KEY
                },
                "issuetype": {
                    "id": JIRA_ISSUE_TYPE_ID
                },
                "summary": "Successful Jira Automation",
            },
            "update": {}
        }

        try:
            response = requests.post(
                JIRA_API_URL,
                headers=headers,
                auth=auth,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return jsonify(response.json()), response.status_code
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Only /jira comments can create Jira tickets"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





