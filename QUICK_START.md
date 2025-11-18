# Quick Start Guide

Get started with Architecture Design Agents in 5 minutes.

## Installation

```bash
git clone https://github.com/your-org/codingagents.git
cd codingagents
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Option 1: Autonomous Workflow (Recommended)

**Use case:** Complete architecture design automatically

```python
from autonomous.orchestrator import WorkflowOrchestrator

# Get orchestrator
orchestrator = WorkflowOrchestrator()

# Execute complete architecture design workflow
workflow = orchestrator.get_template('complete_architecture_design')
result = orchestrator.execute_workflow(workflow)

# View results
print(orchestrator.generate_report(result))
```

**Outputs:**
- Requirements analysis
- Architecture design
- Diagrams (Mermaid, C4, PlantUML)
- API specifications
- Database schema
- Infrastructure as Code
- CI/CD pipeline
- Test suite
- Work breakdown structure

## Option 2: Individual Agent

**Use case:** Quick diagram generation

```python
from agents.diagram_generator import DiagramGenerator, DiagramSpec, Node, Edge

generator = DiagramGenerator()

spec = DiagramSpec(
    title="My System",
    nodes=[
        Node(id="web", label="Web App"),
        Node(id="api", label="API"),
        Node(id="db", label="Database")
    ],
    edges=[
        Edge(source="web", target="api", label="HTTPS"),
        Edge(source="api", target="db", label="SQL")
    ]
)

diagram = generator.generate_mermaid_flowchart(spec)
print(diagram)
```

## Option 3: AI-Powered Goal

**Use case:** Natural language architecture design

```python
from autonomous.agentic import AgenticSystem

agentic = AgenticSystem()

task = agentic.execute_goal(
    goal="Design a microservices e-commerce platform for 5000 users"
)

print(task.result)
```

## Option 4: Scheduled Automation

**Use case:** Daily security scans

```python
from autonomous.runner import AgentRunner, TriggerType

runner = AgentRunner()

runner.schedule_job(
    name="daily_security_scan",
    agent="security_auditor",
    action="scan_vulnerabilities",
    trigger_type=TriggerType.SCHEDULE,
    interval_seconds=86400
)

runner.start(num_workers=2)
```

## Common Use Cases

### Code Review
```python
from agents.code_reviewer import CodeReviewer

reviewer = CodeReviewer()
review = reviewer.review_file("app/main.py", code, "python")
print(f"Quality Score: {review.quality_score}/100")
```

### Generate Tests
```python
from agents.test_generator import TestGenerator

generator = TestGenerator()
tests = generator.generate_unit_tests(code, "python")
```

### Security Audit
```python
from agents.security_auditor import SecurityAuditor

auditor = SecurityAuditor()
audit = auditor.audit_code(code, "python")
print(f"Security Score: {audit.security_score}/100")
```

### Generate Infrastructure
```python
from agents.iac_generator import IaCGenerator

generator = IaCGenerator()
terraform = generator.generate_terraform(architecture)
```

## Next Steps

- **Comprehensive Guide:** See `docs/COMPREHENSIVE_GUIDE.md`
- **Examples:** Run files in `examples/` directory
- **Integration:** See `docs/INTEGRATION_GUIDE.md`
- **NashTech Standards:** See `docs/NASHTECH_TA_GUIDELINES.md`
