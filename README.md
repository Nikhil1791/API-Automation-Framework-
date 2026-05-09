# API Automation Framework

Hybrid API Automation Framework using Python, Pytest, Requests, Data Driven Testing, HTML Reporting and CI/CD Integration.

## Features

- REST API Automation
- GET/POST/PUT/DELETE Requests
- Reusable API Client
- Logging
- JSON Payload Handling
- HTML Reports
- CI/CD Integration
- Hybrid Framework Design

## Tech Stack

- Python
- Pytest
- Requests
- Faker
- GitHub Actions

## Run Tests

pytest


API AUTOMATION FRAMEWORK STRUCTURE :

api-automation-framework
│
├── .github
│   └── workflows
│       └── api-tests.yml
│
├── config
│   ├── config.py
│   └── test_data.json
│
├── payloads
│   ├── create_user_payload.json
│   └── update_user_payload.json
│
├── testdata
│   └── api_test_data.json
│
├── tests
│   ├── test_get_users.py
│   ├── test_single_user.py
│   ├── test_create_user.py
│   ├── test_update_user.py
│   └── test_delete_user.py
│
├── utils
│   ├── api_client.py
│   ├── logger.py
│   ├── data_util.py
│   ├── json_util.py
│   ├── common_util.py
│   └── assertions.py
│
├── reports
├── logs
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── run_tests.bat
└── README.md



Commands To Run :

1. Run All Tests :

pytest


2. Generate HTML Report :

pytest --html=reports/report.html


3. Suggested GitHub Description :

Hybrid API Automation Framework using Python, Pytest, Requests Library, HTML Reporting and CI/CD Integration.


