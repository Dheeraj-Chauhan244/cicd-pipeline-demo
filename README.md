"# Update"

\# CI/CD Pipeline Automation System



\## Overview

Automated CI/CD pipeline that builds, tests, and deploys code on Git push.



\## Tools Used

\- \*\*Jenkins\*\*: Pipeline automation

\- \*\*Docker\*\*: Containerization

\- \*\*GitHub\*\*: Version control and triggers



\## Pipeline Stages

1\. \*\*Checkout\*\*: Clone code from GitHub

2\. \*\*Setup\*\*: Install dependencies

3\. \*\*Test\*\*: Run unit and integration tests

4\. \*\*Build\*\*: Create Docker image

5\. \*\*Push\*\*: Push to Docker registry

6\. \*\*Deploy\*\*: Deploy to production

7\. \*\*Verify\*\*: Health check deployment



\## Quick Start



\### Prerequisites

\- Docker

\- Jenkins

\- Git



\### Run Locally

```bash

\# Clone repository

git clone https://github.com/YOUR\_USERNAME/cicd-pipeline-demo.git



\# Build Docker image

docker build -t cicd-demo-app ./sample-app



\# Run container

docker run -d -p 5000:5000 cicd-demo-app



\# Test

curl http://localhost:5000/

