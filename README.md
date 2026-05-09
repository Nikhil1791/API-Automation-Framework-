# API Automation Framework - Python

A scalable and maintainable Hybrid API Automation Framework developed using Python, Pytest, Requests Library, Data Driven Testing, HTML Reporting, Logging, and CI/CD Integration.

This framework is designed using industry-level standards and follows reusable automation framework architecture.

---

# Tech Stack

- Python
- Pytest
- Requests Library
- Pytest HTML Reports
- Data Driven Testing
- JSON Payload Management
- Logging
- GitHub Actions CI/CD

---

# Framework Features

- REST API Automation
- GET / POST / PUT / DELETE Operations
- Reusable API Client
- JSON Payload Handling
- Data Driven Testing
- HTML Reporting
- Logging Mechanism
- Utility Functions
- CI/CD Integration
- Scalable Framework Design
- Easy Maintenance

---

# Project Structure

```bash
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
│   ├── json_util.py
│   ├── data_util.py
│   ├── assertions.py
│   └── common_util.py
│
├── reports
├── logs
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── run_tests.bat
└── README.md
```

---

# API Used

Public API Used For Automation Practice:

```bash
https://reqres.in/
```

---

# Installation

## Clone Repository

```bash
git clone <your-github-repository-link>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\\Scripts\\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Test Cases

## Run All Tests

```bash
pytest
```

---

## Run Specific Test

```bash
pytest tests/test_create_user.py
```

---

## Run Tests With Verbose Output

```bash
pytest -v
```

---

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# Framework Components

## API Client

Centralized reusable API request handling:

- GET Requests
- POST Requests
- PUT Requests
- DELETE Requests

---

## Payload Management

Separate JSON payload files added for better maintainability.

Example:

```bash
payloads/create_user_payload.json
```

---

## Utility Files

Framework contains reusable utility classes:

- API Client Utility
- Logger Utility
- JSON Utility
- Assertions Utility
- Common Utility

---

## Logging

Centralized logging implemented using Python logging module.

Log File Path:

```bash
logs/api_framework.log
```

---

## Reporting

HTML reports generated automatically after execution.

Report Path:

```bash
reports/report.html
```

---

# Test Scenarios Covered

- Get All Users API
- Get Single User API
- Create User API
- Update User API
- Delete User API

---

# Sample Validations

- Status Code Validation
- Response Body Validation
- JSON Key Validation
- API Response Verification

---

# CI/CD Integration

GitHub Actions pipeline added for automated API execution.

Workflow Path:

```bash
.github/workflows/api-tests.yml
```

---

# Future Enhancements

- Allure Reporting
- Docker Integration
- Jenkins Integration
- Database Validation
- API Schema Validation
- Parallel Execution
- Environment Management
- Token Based Authentication
- API + UI Hybrid Framework

---

# Author

Nikhil Dhamange

QA Automation Engineer

Skills:
- Selenium
- Playwright
- API Automation
- Python
- Pytest
- Requests Library
- CI/CD
- Jenkins
- Docker
- Framework Development

---

# GitHub Repository Name

```bash
api-automation-framework-python
```

---

# GitHub Repository Description

```bash
Hybrid API Automation Framework using Python, Pytest, Requests Library, HTML Reporting and CI/CD Integration.
```

---

# Commands Summary

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Generate Report

```bash
pytest --html=reports/report.html
```

## Run Batch File

```bash
run_tests.bat
```

---

# Advantages Of This Framework

- Industry-level framework structure
- Reusable coding standards
- Easy scalability
- Better maintainability
- Real-time API automation implementation
- GitHub showcase ready
- Interview friendly project structure
