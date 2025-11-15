# Architecture Design Agents

A comprehensive suite of AI agents and skills to help technical architects generate software architecture designs, diagrams, and documentation using Claude AI.

## Overview

This project provides specialized agents that can analyze codebases, generate architecture diagrams in multiple formats, design APIs, visualize databases, and create comprehensive architecture documentation.

## Features

### 🏗️ Agents

1. **Architecture Analyzer Agent** - Analyzes codebases and generates architecture diagrams
2. **Diagram Generator Agent** - Creates diagrams in multiple formats (Mermaid, C4, PlantUML, draw.io)
3. **API Design Agent** - Designs and documents APIs with sequence diagrams
4. **Database Visualizer Agent** - Creates ER diagrams from database schemas
5. **Requirements Analyzer Agent** - Extracts and analyzes requirements from multiple document formats (DOCX, Excel, PDF, TXT)

### 🎨 Diagram Formats Supported

- **Mermaid** - Flowcharts, sequence diagrams, class diagrams, ER diagrams, state diagrams
- **C4 Model** - Context, Container, Component, and Code diagrams
- **PlantUML** - UML diagrams, sequence diagrams, component diagrams
- **Draw.io XML** - Editable diagrams for Draw.io/diagrams.net

### 🛠️ Skills

- Diagram generation utilities
- Code analysis and pattern recognition
- Architecture pattern detection
- Documentation generation

## Project Structure

```
codingagents/
├── agents/                          # Agent implementations
│   ├── architecture-analyzer/       # Analyzes code and generates architecture
│   ├── diagram-generator/           # Generates diagrams in various formats
│   ├── api-designer/                # API design and documentation
│   ├── database-visualizer/         # Database schema visualization
│   └── requirements-analyzer/       # Requirements extraction and analysis
├── skills/                          # Reusable skills
│   └── diagram-skills/              # Diagram generation capabilities
├── utils/                           # Utility functions
├── examples/                        # Example usage and outputs
│   ├── templates/                   # Architecture templates
│   └── output/                      # Sample generated diagrams
└── docs/                            # Documentation
```

## Quick Start

### Using Architecture Analyzer Agent

```python
from agents.architecture_analyzer import ArchitectureAnalyzer

analyzer = ArchitectureAnalyzer()
architecture = analyzer.analyze_codebase(
    path="/path/to/project",
    diagram_format="mermaid"  # or "c4", "plantuml", "drawio"
)
```

### Generating Diagrams

```python
from agents.diagram_generator import DiagramGenerator

generator = DiagramGenerator()

# Generate Mermaid diagram
mermaid = generator.generate_mermaid_diagram(
    diagram_type="flowchart",
    components=["Frontend", "Backend", "Database"]
)

# Generate C4 diagram
c4 = generator.generate_c4_diagram(
    level="container",  # context, container, component, code
    system="E-commerce Platform"
)
```

### API Design

```python
from agents.api_designer import APIDesigner

designer = APIDesigner()
api_spec = designer.design_api(
    requirements="RESTful API for user management",
    include_sequence_diagram=True
)
```

### Requirements Analysis

```python
from agents.requirements_analyzer import RequirementsAnalyzer

analyzer = RequirementsAnalyzer()
analysis = analyzer.analyze_documents(
    file_paths=["requirements.docx", "specs.xlsx", "user_stories.pdf"],
    auto_categorize=True
)

# Generate use case diagram
use_case_diagram = analyzer.generate_use_case_diagram(analysis)

# Generate traceability matrix
matrix = analyzer.generate_traceability_matrix(analysis)

# Generate full report
report = analyzer.generate_requirement_report(analysis)
```

## Use Cases

### 1. Analyzing Existing Codebase
Automatically analyze your codebase and generate architecture diagrams showing:
- System components and their relationships
- Data flow
- Technology stack
- Architectural patterns used

### 2. Designing New Architecture
Use agents to help design new systems:
- Generate C4 diagrams for different abstraction levels
- Create sequence diagrams for API interactions
- Design database schemas with ER diagrams

### 3. Documentation Generation
Automatically generate comprehensive architecture documentation including:
- System overview
- Component descriptions
- Architecture decision records (ADRs)
- API documentation
- Deployment diagrams

### 4. Architecture Reviews
Analyze architecture and get suggestions for:
- Architectural patterns
- Scalability improvements
- Security considerations
- Best practices

## Agent Details

### Architecture Analyzer Agent

**Capabilities:**
- Scans codebase structure
- Identifies architectural patterns (MVC, microservices, layered, etc.)
- Detects technology stack
- Generates diagrams showing system structure
- Identifies dependencies between components

**Input:** Codebase path, analysis depth, diagram format preference
**Output:** Architecture diagrams, analysis report, technology stack summary

### Diagram Generator Agent

**Capabilities:**
- Mermaid diagrams (flowchart, sequence, class, ER, state, journey)
- C4 model diagrams (context, container, component, code)
- PlantUML diagrams (all UML types)
- Draw.io XML format

**Input:** Diagram specification, format preference, styling options
**Output:** Diagram code/XML, rendered preview (when applicable)

### API Design Agent

**Capabilities:**
- RESTful API design
- GraphQL schema design
- gRPC service definitions
- OpenAPI/Swagger specifications
- API sequence diagrams
- Request/response examples

**Input:** API requirements, design patterns, authentication needs
**Output:** API specification, sequence diagrams, documentation

### Database Visualizer Agent

**Capabilities:**
- ER diagram generation from schema
- Database relationship mapping
- Index and constraint visualization
- Migration planning diagrams

**Input:** Database schema (SQL, ORM models, existing DB connection)
**Output:** ER diagrams, schema documentation

### Requirements Analyzer Agent

**Capabilities:**
- Multi-format document parsing (DOCX, Excel, PDF, TXT, MD, JSON)
- Automatic requirement extraction and categorization
- Requirement type classification (functional, non-functional, security, performance)
- Priority analysis (critical, high, medium, low)
- Use case diagram generation
- Requirements traceability matrix
- Comprehensive requirement reports
- Gap analysis and recommendations

**Supported Document Formats:**
- **Word Documents (DOCX)**: Parse structured requirements with sections and headings
- **Excel Spreadsheets (XLSX, XLS)**: Extract requirements from tabular format
- **PDF Documents**: Extract text and identify requirements
- **Text/Markdown Files (TXT, MD)**: Parse plaintext requirements
- **JSON**: Import structured requirement data

**Input:** List of requirement document paths, categorization preferences
**Output:** Requirement analysis, use case diagrams, traceability matrix, detailed reports
**Output:** Comprehensive markdown documentation

## Example Outputs

### Mermaid Flowchart
```mermaid
graph TD
    A[Client] -->|HTTPS| B[Load Balancer]
    B --> C[Web Server 1]
    B --> D[Web Server 2]
    C --> E[Application Server]
    D --> E
    E --> F[(Database)]
    E --> G[(Cache)]
```

### C4 Context Diagram
```
System Context diagram for E-commerce Platform
- Users interact with Web Application
- Web Application uses Payment Gateway
- Web Application uses Email Service
- Web Application uses Analytics Service
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codingagents.git
cd codingagents

# Install dependencies
pip install -r requirements.txt
```

## Using with AI Tools

These agents work seamlessly with popular AI coding assistants:

### 🤖 Claude AI
Upload agent prompts to Claude Projects for interactive architecture design sessions.
[Complete Guide →](docs/CLAUDE_INTEGRATION.md) | [Quick Start →](docs/QUICK_START_AI_TOOLS.md#-claude-ai---quick-start)

### 💻 GitHub Copilot
Use detailed comments and agent imports to guide Copilot's code generation.
[Quick Start →](docs/QUICK_START_AI_TOOLS.md#-github-copilot---quick-start)

### 🎯 Cursor
Reference agent prompts with @ and use custom commands for integrated workflows.
[Quick Start →](docs/QUICK_START_AI_TOOLS.md#-cursor---quick-start)

**See [AI Tool Integration Guide](docs/AI_TOOL_INTEGRATION.md) for comprehensive usage with all AI tools.**

## Configuration

Each agent can be configured via:
1. Configuration files (`config/`)
2. Environment variables
3. Direct parameters in code

Example configuration:
```yaml
architecture_analyzer:
  default_diagram_format: mermaid
  analysis_depth: deep
  include_external_dependencies: true

diagram_generator:
  mermaid_theme: default
  c4_styling: true
  output_format: svg
```

## Contributing

Contributions are welcome! Please see CONTRIBUTING.md for details.

## License

MIT License - see LICENSE file for details.

## Resources

- [Mermaid Documentation](https://mermaid.js.org/)
- [C4 Model](https://c4model.com/)
- [PlantUML](https://plantuml.com/)
- [Draw.io](https://www.diagrams.net/)

## Support

For issues, questions, or contributions, please open an issue on GitHub.
