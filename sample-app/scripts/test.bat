@echo off
echo Running tests...
cd /app
pytest tests/ -v --junitxml=test-results.xml
echo Tests completed!