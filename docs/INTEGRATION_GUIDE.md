# Integration Guide

Integrate Architecture Design Agents with your existing tools and workflows.

## CI/CD Integration

### GitHub Actions

```yaml
name: Architecture Review
on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run Code Review
        run: |
          python -c "
          from agents.code_reviewer import CodeReviewer
          reviewer = CodeReviewer()
          # Review changed files
          "
      - name: Run Security Audit
        run: |
          python -c "
          from agents.security_auditor import SecurityAuditor
          auditor = SecurityAuditor()
          # Audit code
          "
```

### GitLab CI

```yaml
code_review:
  stage: test
  script:
    - pip install -r requirements.txt
    - python -c "from agents.code_reviewer import CodeReviewer; ..."

security_audit:
  stage: test
  script:
    - pip install -r requirements.txt
    - python -c "from agents.security_auditor import SecurityAuditor; ..."
```

### Jenkins

```groovy
pipeline {
    agent any
    stages {
        stage('Code Review') {
            steps {
                sh 'python -c "from agents.code_reviewer import CodeReviewer; ..."'
            }
        }
        stage('Security Audit') {
            steps {
                sh 'python -c "from agents.security_auditor import SecurityAuditor; ..."'
            }
        }
    }
}
```

## Git Hooks

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running code review..."
python -c "
from agents.code_reviewer import CodeReviewer
reviewer = CodeReviewer()
# Review staged files
"

if [ $? -ne 0 ]; then
    echo "Code review failed"
    exit 1
fi
```

### Pre-push Hook

```bash
#!/bin/bash
# .git/hooks/pre-push

echo "Running security audit..."
python -c "
from agents.security_auditor import SecurityAuditor
auditor = SecurityAuditor()
# Audit code
"
```

## IDE Integration

### VS Code Extension

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Review Code",
            "type": "shell",
            "command": "python -c 'from agents.code_reviewer import CodeReviewer; ...'"
        },
        {
            "label": "Generate Tests",
            "type": "shell",
            "command": "python -c 'from agents.test_generator import TestGenerator; ...'"
        }
    ]
}
```

## Notification Integration

### Slack

```python
import requests

def send_slack(message):
    webhook = "https://hooks.slack.com/services/YOUR/WEBHOOK"
    requests.post(webhook, json={"text": message})

# Use with Agent Runner
from autonomous.runner import AgentRunner

def on_complete(job, result):
    send_slack(f"✅ {job.name} completed")

runner = AgentRunner()
runner.schedule_job(..., on_complete=on_complete)
```

### Email

```python
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'noreply@company.com'
    msg['To'] = 'team@company.com'

    with smtplib.SMTP('smtp.company.com') as server:
        server.send_message(msg)
```

## Monitoring Integration

### Prometheus Metrics

```python
from prometheus_client import Counter, Gauge, start_http_server

# Metrics
reviews_total = Counter('code_reviews_total', 'Total code reviews')
quality_score = Gauge('code_quality_score', 'Current quality score')

# Expose metrics
start_http_server(8000)

# Use in agents
reviews_total.inc()
quality_score.set(review.quality_score)
```

### Grafana Dashboard

Create dashboards tracking:
- Code quality scores over time
- Security vulnerabilities found
- Test coverage trends
- Architecture review frequency

## Database Integration

Store agent results in database:

```python
import sqlite3

def save_review(review):
    conn = sqlite3.connect('agents.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reviews (timestamp, quality_score, issues)
        VALUES (?, ?, ?)
    ''', (datetime.now(), review.quality_score, len(review.issues)))
    conn.commit()
    conn.close()
```

## API Integration

Expose agents via REST API:

```python
from flask import Flask, request, jsonify
from agents.code_reviewer import CodeReviewer

app = Flask(__name__)
reviewer = CodeReviewer()

@app.route('/api/review', methods=['POST'])
def review_code():
    data = request.json
    review = reviewer.review_file(
        data['file_path'],
        data['code'],
        data['language']
    )
    return jsonify({
        'quality_score': review.quality_score,
        'issues': [
            {'severity': i.severity.value, 'title': i.title}
            for i in review.issues
        ]
    })

app.run(port=5000)
```

## Docker Integration

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "autonomous.runner"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  agent-runner:
    build: .
    environment:
      - SCHEDULE_INTERVAL=86400
    volumes:
      - ./src:/app/src
```

## Kubernetes Integration

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-security-scan
spec:
  schedule: "0 0 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: security-auditor
            image: codingagents:latest
            command: ["python", "-m", "agents.security_auditor"]
          restartPolicy: OnFailure
```

## Best Practices

1. **Start Small** - Integrate one agent at a time
2. **Test Locally** - Verify before deploying to CI/CD
3. **Monitor Performance** - Track execution time and resource usage
4. **Handle Failures** - Implement retry logic and error notifications
5. **Version Control** - Keep agent configurations in git
6. **Security** - Don't expose API keys or credentials
7. **Logging** - Log all agent executions for auditing
8. **Metrics** - Track quality improvements over time

## Troubleshooting

**Issue:** Slow execution in CI/CD
**Solution:** Use caching for dependencies, run agents in parallel

**Issue:** False positives in code review
**Solution:** Configure agent context and severity thresholds

**Issue:** High resource usage
**Solution:** Limit concurrent workers, use smaller models

For more help, see `docs/COMPREHENSIVE_GUIDE.md`.
