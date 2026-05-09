@echo off

title API Automation Framework

echo ===================================
echo API AUTOMATION FRAMEWORK EXECUTION
echo ===================================

IF NOT EXIST reports (
    mkdir reports
)

IF NOT EXIST logs (
    mkdir logs
)

call venv\Scripts\activate

pytest -v --html=reports/report.html --self-contained-html

start reports\report.html

pause

