# CLAUDE.md - AI Assistant Guide

This document provides comprehensive guidance for AI assistants (Claude AI and others) working with the Architecture Design Agents codebase.

## Table of Contents

- [Project Overview](#project-overview)
- [Codebase Structure](#codebase-structure)
- [Architecture & Design Patterns](#architecture--design-patterns)
- [Development Conventions](#development-conventions)
- [Working with Agents](#working-with-agents)
- [Common Tasks](#common-tasks)
- [Code Quality Standards](#code-quality-standards)
- [Testing Guidelines](#testing-guidelines)
- [Git Workflow](#git-workflow)
- [Key Files Reference](#key-files-reference)

---

## Project Overview

**Architecture Design Agents** is a comprehensive suite of AI-powered agents for software architecture design, diagram generation, and documentation. The project enables technical architects and developers to analyze codebases, design systems, create APIs, visualize databases, and generate architecture documentation through both programmatic APIs and natural language interactions.

### Core Purpose

- Analyze existing codebases and identify architectural patterns
- Generate diagrams in multiple formats (Mermaid, C4, PlantUML, Draw.io)
- Design RESTful/GraphQL/gRPC APIs with OpenAPI specifications
- Visualize database schemas and relationships
- Extract and analyze requirements from multiple document formats
- Create work breakdown structures and presale proposals
- Enable AI-assisted architecture design through natural language

### Technology Stack

- **Language:** Python 3.8+
- **Core Library:** Anthropic Claude API (`anthropic>=0.18.0`)
- **Key Dependencies:** sqlparse, pyyaml, python-docx, openpyxl, pdfplumber
- **Dev Tools:** pytest, black, flake8, mypy
- **License:** MIT

---

## Codebase Structure

```
codingagents/
├── agents/                          # Core agent implementations
│   ├── architecture-analyzer/       # Codebase analysis & pattern detection
│   │   ├── __init__.py
│   │   ├── agent.py                # Implementation (~650 lines)
│   │   └── prompt.md               # Claude AI instructions
│   ├── diagram-generator/          # Multi-format diagram generation
│   │   ├── __init__.py
│   │   ├── agent.py                # Implementation (~850 lines)
│   │   └── prompt.md
│   ├── api-designer/               # REST/GraphQL/gRPC API design
│   │   ├── __init__.py
│   │   ├── agent.py                # Implementation (~700 lines)
│   │   └── prompt.md
│   ├── database-visualizer/        # Database schema & ER diagrams
│   │   ├── __init__.py
│   │   ├── agent.py                # Implementation (~600 lines)
│   │   └── prompt.md
│   ├── requirements-analyzer/      # Multi-document requirements extraction
│   │   ├── __init__.py
│   │   ├── agent.py                # Implementation (~750 lines)
│   │   └── prompt.md
│   └── wbs-generator/              # Work breakdown structure & presale
│       ├── __init__.py
│       ├── agent.py                # Implementation (~900 lines)
│       └── prompt.md
├── docs/                           # Documentation
│   ├── CLAUDE_INTEGRATION.md       # Claude AI integration workflows
│   ├── GETTING_STARTED.md          # Setup and quick start
│   ├── AI_TOOL_INTEGRATION.md      # AI tool integration guide
│   └── QUICK_START_AI_TOOLS.md     # Quick start for various AI tools
├── examples/                       # Working code examples
│   ├── example_architecture_analysis.py
│   ├── example_diagram_generation.py
│   ├── example_api_design.py
│   ├── example_database_visualization.py
│   ├── example_requirements_analysis.py
│   ├── example_wbs_generation.py
│   └── templates/                  # Reusable architecture templates
├── .github/
│   └── copilot-instructions.md     # GitHub Copilot integration guide
├── main.py                         # CLI interface orchestrator
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview
├── CONTRIBUTING.md                 # Contribution guidelines
├── .cursorrules                    # Cursor IDE integration rules
├── .gitignore
└── LICENSE
```

### Directory Organization Principles

1. **Agents Directory**: Each agent is a self-contained package with implementation, initialization, and prompt files
2. **Docs Directory**: User-facing documentation, integration guides, and tutorials
3. **Examples Directory**: Working code examples demonstrating each agent's capabilities
4. **Root Level**: Project configuration, main CLI, and documentation

---

## Architecture & Design Patterns

### Agent-Based Architecture

The project follows a **specialized agent pattern** where each agent:

- Has a **single, well-defined responsibility** (SRP)
- Provides both **programmatic Python API** and **natural language prompt interface**
- Uses **dataclasses** for structured data representation
- Implements **enum-based type systems** for consistent categorization
- Returns **string outputs** (diagram code, specifications, reports)

### Design Patterns Used

#### 1. Dataclass Pattern

All data structures use Python `@dataclass` decorator for clean, type-safe data models:

```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Component:
    """Represents an architecture component"""
    name: str
    type: str
    description: Optional[str] = None
    dependencies: List[str] = None
```

#### 2. Enum Pattern

Type-safe enumerations for categorization:

```python
from enum import Enum

class ArchitecturePattern(Enum):
    MICROSERVICES = "microservices"
    MVC = "mvc"
    LAYERED = "layered"
    MONOLITHIC = "monolithic"
```

#### 3. Factory Pattern

Format-specific generation methods:

```python
class DiagramGenerator:
    def generate_diagram(self, spec: DiagramSpec, format: str) -> str:
        if format == "mermaid":
            return self._generate_mermaid(spec)
        elif format == "plantuml":
            return self._generate_plantuml(spec)
        elif format == "drawio":
            return self._generate_drawio(spec)
```

#### 4. Strategy Pattern

Different parsing strategies for different document types in Requirements Analyzer:

```python
def parse_document(self, file_path: str) -> List[str]:
    if file_path.endswith('.docx'):
        return self._parse_docx(file_path)
    elif file_path.endswith('.xlsx'):
        return self._parse_xlsx(file_path)
    elif file_path.endswith('.pdf'):
        return self._parse_pdf(file_path)
```

### Agent Implementations

#### Architecture Analyzer Agent
- **Purpose:** Analyze codebases and identify architectural patterns
- **Key Classes:** `Component`, `ArchitectureAnalysis`, `ArchitectureAnalyzer`
- **Patterns Detected:** Microservices, MVC, Layered, Clean Architecture, Monolithic
- **Output Formats:** Mermaid, C4, PlantUML, Draw.io

#### Diagram Generator Agent
- **Purpose:** Generate diagrams from specifications in multiple formats
- **Key Classes:** `Node`, `Edge`, `DiagramSpec`, `DiagramGenerator`
- **Diagram Types:** Flowchart, Sequence, Class, ER, State, Gantt, Journey, C4, Component, Deployment
- **Output Formats:** Mermaid, PlantUML, Draw.io XML

#### API Designer Agent
- **Purpose:** Design RESTful, GraphQL, and gRPC APIs
- **Key Classes:** `APIEndpoint`, `APISpecification`, `APIDesigner`
- **Features:** Auto-generate CRUD endpoints, OpenAPI 3.0 specs, sequence diagrams
- **Patterns:** REST, GraphQL, gRPC, WebSocket

#### Database Visualizer Agent
- **Purpose:** Visualize database schemas as ER diagrams
- **Key Classes:** `Field`, `Table`, `Relationship`, `DatabaseSchema`
- **Field Types:** Integer, String, Text, Boolean, Decimal, Date, DateTime, JSON, UUID
- **Relationships:** One-to-One, One-to-Many, Many-to-One, Many-to-Many
- **Output Formats:** Mermaid ER, PlantUML ER, DBML

#### Requirements Analyzer Agent
- **Purpose:** Extract, categorize, and analyze requirements from documents
- **Key Classes:** `Requirement`, `RequirementAnalysis`, `RequirementsAnalyzer`
- **Document Formats:** DOCX, XLSX, PDF, TXT, MD, JSON
- **Classification:** Functional, Non-functional, Security, Performance, Usability, Compliance
- **Outputs:** Use case diagrams, traceability matrices, comprehensive reports

#### WBS Generator Agent
- **Purpose:** Create work breakdown structures, estimates, and presale proposals
- **Key Classes:** `WBSGenerator`, `WBSProject`, `Task`, `Resource`, `Estimation`
- **Task Types:** Phase, Deliverable, Work Package, Task, Subtask, Milestone
- **Resource Types:** Developer, Architect, QA Engineer, DevOps, Designer, PM, BA, Technical Writer
- **Estimation:** PERT method (Optimistic, Likely, Pessimistic), multiple units
- **Outputs:** Mermaid Gantt charts, WBS trees, Markdown docs, JSON, presale proposals

---

## Development Conventions

### Code Style Guidelines

#### Type Hints (Required)

Use comprehensive type hints for all functions and methods:

```python
from typing import List, Dict, Optional

def generate_diagram(
    nodes: List[Node],
    edges: List[Edge],
    title: str = "Diagram"
) -> str:
    """Generate a diagram from nodes and edges."""
    pass
```

#### Docstrings (Required)

Use Google-style docstrings for all public functions and classes:

```python
def analyze_codebase(self, path: str, depth: str = "moderate") -> ArchitectureAnalysis:
    """
    Analyze a codebase and identify architectural patterns.

    Args:
        path: Path to the codebase directory
        depth: Analysis depth ("basic", "moderate", "deep")

    Returns:
        ArchitectureAnalysis object with detected patterns and components

    Raises:
        FileNotFoundError: If the path does not exist
        ValueError: If depth is not a valid option
    """
    pass
```

#### Naming Conventions

- **Classes:** PascalCase (`ArchitectureAnalyzer`, `DiagramGenerator`)
- **Functions/Methods:** snake_case (`generate_diagram`, `analyze_codebase`)
- **Constants:** UPPER_SNAKE_CASE (`DEFAULT_FORMAT`, `MAX_DEPTH`)
- **Private Methods:** Leading underscore (`_parse_structure`, `_generate_mermaid`)

#### Import Organization

```python
# Standard library imports
import os
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

# Third-party imports
import yaml
from anthropic import Anthropic

# Local imports
from agents.diagram_generator import DiagramGenerator
```

### Error Handling Pattern

```python
def parse_file(self, file_path: str) -> List[str]:
    """Parse a file and extract content."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return self._process_content(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except Exception as e:
        # Log error and provide graceful fallback
        print(f"Warning: Could not parse {file_path}: {e}")
        return []
```

### Data Flow Pattern

```
Input (file/text/specification)
    ↓
Parse/Validate
    ↓
Analyze/Process/Categorize
    ↓
Generate Output (diagram/spec/report)
    ↓
Optional: Save to file
```

### Common Method Names Across Agents

- `__init__()` - Initialize agent with optional configuration
- `analyze_*()` / `generate_*()` / `design_*()` - Main processing methods
- `_parse_*()` - Format-specific parsing (private)
- `_generate_*_diagram()` - Format-specific generation (private)
- `*_recommendations()` - Analysis-based suggestions

---

## Working with Agents

### Agent Structure Pattern

Each agent follows this consistent structure:

```python
"""
Agent Name

Description of agent capabilities and purpose.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum


@dataclass
class AgentInput:
    """Input data structure"""
    field1: str
    field2: Optional[str] = None


@dataclass
class AgentOutput:
    """Output data structure"""
    result: str
    metadata: Dict[str, str]


class AgentName:
    """
    Agent description and capabilities.

    Features:
    - Feature 1
    - Feature 2
    - Feature 3
    """

    def __init__(self):
        """Initialize the agent."""
        pass

    def process(self, input: AgentInput) -> AgentOutput:
        """
        Main processing method.

        Args:
            input: Agent input data

        Returns:
            Processed output
        """
        pass

    def _private_method(self, data: str) -> str:
        """Private helper method."""
        pass
```

### Using Agents Programmatically

```python
# Example: Architecture Analyzer
from agents.architecture_analyzer import ArchitectureAnalyzer

analyzer = ArchitectureAnalyzer()
analysis = analyzer.analyze_codebase(
    path="/path/to/project",
    diagram_format="mermaid",
    depth="moderate"
)
print(analysis.diagram_code)

# Example: Diagram Generator
from agents.diagram_generator import DiagramGenerator, DiagramSpec, Node, Edge

generator = DiagramGenerator()
spec = DiagramSpec(
    title="System Architecture",
    nodes=[
        Node(id="frontend", label="React Frontend"),
        Node(id="backend", label="Node.js API"),
    ],
    edges=[
        Edge(source="frontend", target="backend", label="HTTPS")
    ]
)
diagram = generator.generate_mermaid_flowchart(spec)
```

### Using Agents via Natural Language

Reference agent prompts in Claude conversations:

```
User: Using the Architecture Analyzer agent, analyze a microservices
e-commerce platform with React frontend, Node.js gateway, Python
services, and PostgreSQL databases. Generate a C4 Container diagram.

Claude: [Uses knowledge from agent prompt to generate appropriate output]
```

---

## Common Tasks

### Adding a New Agent

1. **Create agent directory:**
   ```bash
   mkdir -p agents/new-agent
   ```

2. **Create required files:**
   ```bash
   touch agents/new-agent/__init__.py
   touch agents/new-agent/agent.py
   touch agents/new-agent/prompt.md
   ```

3. **Implement agent.py** following the agent structure pattern

4. **Create prompt.md** with detailed instructions for Claude

5. **Add example:**
   ```bash
   touch examples/example_new_agent.py
   ```

6. **Add tests:**
   ```bash
   touch tests/test_new_agent.py
   ```

7. **Update documentation:**
   - Add to README.md Features section
   - Add to GETTING_STARTED.md
   - Update docs/CLAUDE_INTEGRATION.md

### Adding Support for a New Diagram Format

1. **Add format to appropriate agent** (typically DiagramGenerator)

2. **Implement generator method:**
   ```python
   def _generate_new_format(self, spec: DiagramSpec) -> str:
       """Generate diagram in new format."""
       # Implementation
       pass
   ```

3. **Add format to enum:**
   ```python
   class DiagramFormat(Enum):
       MERMAID = "mermaid"
       PLANTUML = "plantuml"
       NEW_FORMAT = "new_format"
   ```

4. **Add tests** for the new format

5. **Add example** in examples/

6. **Update documentation**

### Modifying an Existing Agent

1. **Read the agent implementation** in `agents/agent-name/agent.py`

2. **Check the prompt** in `agents/agent-name/prompt.md` for AI integration

3. **Make changes** following existing patterns

4. **Update tests** if needed

5. **Run quality checks:**
   ```bash
   black agents/agent-name/
   flake8 agents/agent-name/
   mypy agents/agent-name/
   pytest tests/test_agent_name.py
   ```

6. **Update documentation** if adding new features

### Testing Your Changes

```bash
# Run specific agent tests
pytest tests/test_architecture_analyzer.py -v

# Run all tests with coverage
pytest --cov=agents

# Run a specific test function
pytest tests/test_diagram_generator.py::test_mermaid_generation

# Check code coverage
pytest --cov=agents --cov-report=html
```

---

## Code Quality Standards

### Required Tools

```bash
# Install development dependencies
pip install pytest black flake8 mypy
```

### Code Formatting (Black)

```bash
# Format all code
black .

# Format specific directory
black agents/

# Check without modifying
black --check .
```

**Standard:** Line length of 88 characters (Black default)

### Linting (Flake8)

```bash
# Lint all code
flake8 .

# Lint specific file
flake8 agents/diagram_generator/agent.py

# With custom config
flake8 --max-line-length=88 .
```

**Standards:**
- Follow PEP 8 guidelines
- Max line length: 88 characters
- No unused imports
- No undefined variables

### Type Checking (MyPy)

```bash
# Type check agents
mypy agents/

# Strict mode
mypy --strict agents/

# Specific file
mypy agents/architecture_analyzer/agent.py
```

**Standards:**
- All functions must have type hints
- Use `Optional[T]` for nullable values
- Use `List[T]`, `Dict[K, V]` for collections
- Return types required

### Pre-commit Checks

Before committing, run:

```bash
# Format code
black .

# Lint
flake8 .

# Type check
mypy agents/

# Run tests
pytest

# If all pass, commit
git commit -m "Your message"
```

---

## Testing Guidelines

### Test File Organization

```
tests/
├── test_architecture_analyzer.py
├── test_diagram_generator.py
├── test_api_designer.py
├── test_database_visualizer.py
└── test_requirements_analyzer.py
```

### Test Structure

```python
import pytest
from agents.diagram_generator import DiagramGenerator, DiagramSpec, Node, Edge


class TestDiagramGenerator:
    """Test suite for DiagramGenerator agent"""

    def setup_method(self):
        """Set up test fixtures"""
        self.generator = DiagramGenerator()

    def test_mermaid_flowchart_generation(self):
        """Test basic Mermaid flowchart generation"""
        spec = DiagramSpec(
            title="Test Diagram",
            nodes=[Node(id="a", label="Node A")],
            edges=[]
        )
        result = self.generator.generate_mermaid_flowchart(spec)
        assert "graph TD" in result
        assert "Node A" in result

    def test_invalid_input_raises_error(self):
        """Test that invalid input raises appropriate error"""
        with pytest.raises(ValueError):
            self.generator.generate_diagram(None, "mermaid")
```

### Testing Best Practices

1. **Test public methods** - Focus on public API, not private methods
2. **Test edge cases** - Empty inputs, None values, invalid formats
3. **Use fixtures** - Set up common test data in `setup_method()`
4. **Descriptive names** - Test names should explain what they test
5. **One assertion per test** - Keep tests focused (when possible)
6. **Test error handling** - Verify errors are raised appropriately

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_diagram_generator.py

# Run specific test
pytest tests/test_diagram_generator.py::TestDiagramGenerator::test_mermaid_flowchart_generation

# Run with coverage
pytest --cov=agents --cov-report=term-missing

# Run and stop on first failure
pytest -x
```

---

## Git Workflow

### Branch Naming

- Feature branches: `feature/description` or `claude/feature-description-sessionid`
- Bug fixes: `fix/description` or `bugfix/description`
- Documentation: `docs/description`
- Refactoring: `refactor/description`

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**

```
feat: Add support for Draw.io XML format to Diagram Generator

- Implement _generate_drawio_xml method
- Add DrawioNode and DrawioEdge dataclasses
- Add tests for Draw.io generation
- Update documentation with Draw.io examples

Closes #123
```

### Commit Best Practices

1. **Clear subject line** - Concise summary (50 chars or less)
2. **Detailed body** - Explain what and why, not how
3. **Reference issues** - Link to GitHub issues when applicable
4. **Atomic commits** - One logical change per commit
5. **Working code** - Ensure tests pass before committing

### Pull Request Workflow

1. **Create feature branch:**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make changes and commit:**
   ```bash
   git add .
   git commit -m "feat: Add new feature"
   ```

3. **Run quality checks:**
   ```bash
   black .
   flake8 .
   mypy agents/
   pytest
   ```

4. **Push to remote:**
   ```bash
   git push origin feature/new-feature
   ```

5. **Create Pull Request** with:
   - Clear description of changes
   - Reference to related issues
   - Test results
   - Documentation updates

### Git Commands for AI Assistants

When working with git as an AI assistant:

```bash
# Check current status
git status

# View recent commits
git log --oneline -10

# View changes
git diff

# Stage changes
git add <files>

# Commit with message
git commit -m "type: description"

# Push to remote (use branch provided in instructions)
git push -u origin <branch-name>

# Create and push to remote with retry logic
git push -u origin <branch-name> || (sleep 2 && git push -u origin <branch-name>)
```

---

## Key Files Reference

### Configuration Files

| File | Purpose | When to Modify |
|------|---------|----------------|
| `requirements.txt` | Python dependencies | Adding new dependencies |
| `.gitignore` | Git ignore patterns | Adding new file types to ignore |
| `.cursorrules` | Cursor IDE integration | Updating Cursor-specific rules |
| `.github/copilot-instructions.md` | Copilot guidance | Improving Copilot integration |

### Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Project overview, quick start | General users, new contributors |
| `CLAUDE.md` | AI assistant guide (this file) | AI assistants (Claude, etc.) |
| `CONTRIBUTING.md` | Contribution guidelines | Contributors |
| `docs/GETTING_STARTED.md` | Installation and setup | New users |
| `docs/CLAUDE_INTEGRATION.md` | Claude AI workflows | Claude users |
| `docs/AI_TOOL_INTEGRATION.md` | Multi-tool integration | AI tool users |

### Agent Files

| Path | Purpose | When to Reference |
|------|---------|-------------------|
| `agents/*/agent.py` | Agent implementation | Understanding agent logic |
| `agents/*/prompt.md` | Claude AI instructions | Natural language interactions |
| `agents/*/__init__.py` | Package exports | Importing agents |
| `examples/example_*.py` | Working examples | Learning agent usage |

### Important Code Locations

**Main CLI Entry Point:**
- `main.py` - Command-line interface orchestrator

**Example Usage:**
- `examples/example_architecture_analysis.py` - Architecture Analyzer usage
- `examples/example_diagram_generation.py` - Diagram Generator usage
- `examples/example_api_design.py` - API Designer usage
- `examples/example_database_visualization.py` - Database Visualizer usage
- `examples/example_requirements_analysis.py` - Requirements Analyzer usage
- `examples/example_wbs_generation.py` - WBS Generator usage

**Templates:**
- `examples/templates/` - Reusable architecture templates

---

## Workflow Patterns for AI Assistants

### Pattern 1: Complete System Design

```
1. Requirements Analysis (Requirements Analyzer)
   ↓
2. Architecture Design (Architecture Analyzer)
   ↓
3. API Design (API Designer)
   ↓
4. Database Design (Database Visualizer)
   ↓
5. Diagram Generation (Diagram Generator)
```

### Pattern 2: Codebase Documentation

```
1. Analyze existing codebase (Architecture Analyzer)
   ↓
2. Generate architecture diagrams (Diagram Generator)
   ↓
3. Document APIs (API Designer)
   ↓
4. Document database (Database Visualizer)
   ↓
5. Consolidate into comprehensive docs
```

### Pattern 3: Microservices Design

```
1. C4 Context diagram (Diagram Generator)
   ↓
2. C4 Container diagram per service (Diagram Generator)
   ↓
3. API specifications per service (API Designer)
   ↓
4. Database schema per service (Database Visualizer)
   ↓
5. Sequence diagrams for flows (Diagram Generator)
```

### Pattern 4: Requirements to Implementation

```
1. Extract requirements (Requirements Analyzer)
   ↓
2. Generate use case diagrams (Requirements Analyzer)
   ↓
3. Design architecture (Architecture Analyzer)
   ↓
4. Design APIs (API Designer)
   ↓
5. Design database (Database Visualizer)
   ↓
6. Create traceability matrix (Requirements Analyzer)
```

---

## Important Principles for AI Assistants

### When Modifying Code

1. **Always read before writing** - Use Read tool to view existing code first
2. **Follow existing patterns** - Match the style and structure of existing code
3. **Preserve type hints** - All functions must maintain type annotations
4. **Update tests** - Add/modify tests when changing functionality
5. **Run quality checks** - Format, lint, and type-check before committing
6. **Update documentation** - Keep docs in sync with code changes

### When Creating New Features

1. **Check for similar implementations** - Look at existing agents for patterns
2. **Use dataclasses** - All data structures should use @dataclass
3. **Use enums for categories** - Type-safe categorization with Enum
4. **Provide docstrings** - Comprehensive Google-style documentation
5. **Add examples** - Create working example in examples/
6. **Write tests** - Test coverage for new functionality

### When Assisting Users

1. **Reference specific files** - Use `file_path:line_number` format
2. **Provide working code** - All code examples should be runnable
3. **Explain patterns** - Help users understand the architecture
4. **Suggest best practices** - Guide users toward project conventions
5. **Link to documentation** - Reference relevant docs files

### When Using Git

1. **Check git status first** - Understand current state before changes
2. **Use descriptive commits** - Follow commit message format
3. **Push to correct branch** - Use branch specified in instructions
4. **Verify before pushing** - Run tests and quality checks

---

## Quick Reference

### Common Commands

```bash
# Setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Development
black .                      # Format code
flake8 .                     # Lint code
mypy agents/                 # Type check
pytest                       # Run tests
pytest --cov=agents          # With coverage

# Git
git status                   # Check status
git add .                    # Stage changes
git commit -m "msg"          # Commit
git push -u origin branch    # Push
```

### Import Patterns

```python
# Architecture Analyzer
from agents.architecture_analyzer import ArchitectureAnalyzer, Component, ArchitectureAnalysis

# Diagram Generator
from agents.diagram_generator import DiagramGenerator, DiagramSpec, Node, Edge

# API Designer
from agents.api_designer import APIDesigner, APIEndpoint, APISpecification

# Database Visualizer
from agents.database_visualizer import DatabaseVisualizer, Table, Field, Relationship

# Requirements Analyzer
from agents.requirements_analyzer import RequirementsAnalyzer, Requirement, RequirementAnalysis

# WBS Generator
from agents.wbs_generator import WBSGenerator, WBSProject, Task, Resource, Estimation, TaskType, ResourceType, EstimationUnit
```

### Agent Prompt Locations

- Architecture Analyzer: `agents/architecture-analyzer/prompt.md`
- Diagram Generator: `agents/diagram-generator/prompt.md`
- API Designer: `agents/api-designer/prompt.md`
- Database Visualizer: `agents/database-visualizer/prompt.md`
- Requirements Analyzer: `agents/requirements-analyzer/prompt.md`
- WBS Generator: `agents/wbs-generator/prompt.md`

---

## Resources

### Documentation Links
- [Mermaid Diagrams](https://mermaid.js.org/)
- [C4 Model](https://c4model.com/)
- [PlantUML](https://plantuml.com/)
- [Draw.io / diagrams.net](https://www.diagrams.net/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [DBML Database Markup](https://www.dbml.org/)

### Internal Documentation
- [README.md](README.md) - Project overview
- [GETTING_STARTED.md](docs/GETTING_STARTED.md) - Setup guide
- [CLAUDE_INTEGRATION.md](docs/CLAUDE_INTEGRATION.md) - Claude AI workflows
- [AI_TOOL_INTEGRATION.md](docs/AI_TOOL_INTEGRATION.md) - Multi-tool integration
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

## Summary

This codebase is a well-structured, agent-based framework for AI-assisted software architecture design. Key characteristics:

- **Modular Architecture:** 6 specialized agents with clear responsibilities
- **Type Safety:** Comprehensive use of type hints, dataclasses, and enums
- **Multi-Format Support:** Diagrams in Mermaid, C4, PlantUML, Draw.io
- **AI-First Design:** Built for integration with Claude AI and other AI tools
- **Workflow-Oriented:** End-to-end processes from requirements to implementation
- **High Code Quality:** Testing, linting, type checking, and formatting standards
- **Extensible:** Clear patterns for adding agents, formats, and features

When working with this codebase, always prioritize code quality, follow existing patterns, maintain comprehensive documentation, and ensure all changes include appropriate tests.

For questions or clarifications, reference the documentation files in `docs/` or examine existing implementations in `agents/` and `examples/`.
