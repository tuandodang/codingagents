# GitHub Copilot Instructions - Architecture Design Agents

## Project Overview

This project provides AI-powered agents for technical architecture design. When generating code, follow these guidelines to maintain consistency with the Architecture Design Agents framework.

## Available Agents

### 1. Requirements Analyzer
**Location:** `agents/requirements-analyzer/`
**Purpose:** Extract and analyze requirements from documents

**Common Patterns:**
```python
from agents.requirements_analyzer import RequirementsAnalyzer

analyzer = RequirementsAnalyzer()
analysis = analyzer.analyze_documents(
    file_paths=["requirements.docx", "specs.xlsx"],
    auto_categorize=True
)

# Generate outputs
use_case = analyzer.generate_use_case_diagram(analysis)
matrix = analyzer.generate_traceability_matrix(analysis)
report = analyzer.generate_requirement_report(analysis)
```

### 2. Diagram Generator
**Location:** `agents/diagram-generator/`
**Purpose:** Create diagrams in multiple formats

**Common Patterns:**
```python
from agents.diagram_generator import DiagramGenerator, Node, Edge

generator = DiagramGenerator()

# Mermaid flowchart
nodes = [Node("id", "Label", "type", "shape"), ...]
edges = [Edge("from", "to", "label"), ...]
diagram = generator.generate_mermaid_flowchart(nodes, edges, "Title", "TB")

# C4 diagrams
c4_diagram = generator.generate_c4_context(
    system_name="System Name",
    users=[...],
    systems=[...],
    external_systems=[...],
    relationships=[...]
)
```

### 3. API Designer
**Location:** `agents/api-designer/`
**Purpose:** Design and document APIs

**Common Patterns:**
```python
from agents.api_designer import APIDesigner

designer = APIDesigner()

# Design REST API
api_spec = designer.design_rest_api(
    name="API Name",
    resources=["Users", "Products", "Orders"],
    version="1.0.0"
)

# Generate OpenAPI
openapi = designer.generate_openapi_spec(api_spec)

# Generate sequence diagram
sequence = designer.generate_sequence_diagram(api_spec.endpoints[0])
```

### 4. Database Visualizer
**Location:** `agents/database-visualizer/`
**Purpose:** Visualize database schemas

**Common Patterns:**
```python
from agents.database_visualizer import DatabaseVisualizer

visualizer = DatabaseVisualizer()
schema = visualizer.create_example_schema()  # or define custom

# Generate diagrams
mermaid_er = visualizer.generate_er_diagram(schema, format="mermaid")
plantuml_er = visualizer.generate_er_diagram(schema, format="plantuml")
docs = visualizer.generate_schema_documentation(schema)
```

### 5. Architecture Analyzer
**Location:** `agents/architecture-analyzer/`
**Purpose:** Analyze codebases and generate architecture diagrams

**Common Patterns:**
```python
from agents.architecture_analyzer import ArchitectureAnalyzer

analyzer = ArchitectureAnalyzer()
result = analyzer.analyze_codebase(
    path=".",
    diagram_format="mermaid",
    depth="moderate"
)
```

## Code Style Guidelines

### 1. Imports
```python
# Specific imports from agents
from agents.requirements_analyzer import RequirementsAnalyzer, Requirement
from agents.diagram_generator import DiagramGenerator, Node, Edge

# Standard library
from pathlib import Path
from typing import List, Dict, Optional

# Data structures
from dataclasses import dataclass
from enum import Enum
```

### 2. Type Hints
Always include type hints:
```python
def analyze_requirements(
    file_paths: List[str],
    output_dir: str = "output"
) -> Dict[str, Any]:
    """Analyze requirements from documents."""
    pass
```

### 3. Error Handling
```python
try:
    with open(file_path, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: File not found: {file_path}")
    return None
except Exception as e:
    print(f"Error processing file: {e}")
    return None
```

### 4. Documentation
```python
def generate_architecture_diagram(
    path: str,
    format: str = "mermaid"
) -> str:
    """
    Generate architecture diagram from codebase.

    Args:
        path: Path to codebase directory
        format: Output format (mermaid, c4, plantuml, drawio)

    Returns:
        Diagram code as string

    Example:
        >>> analyzer = ArchitectureAnalyzer()
        >>> diagram = analyzer.analyze_codebase(".", "mermaid")
    """
    pass
```

## Diagram Generation Standards

### Mermaid
```python
# Always include proper structure
diagram = "graph TB\n"
diagram += "    %% Title\n\n"
diagram += "    A[Node A]\n"
diagram += "    B[Node B]\n"
diagram += "    A --> B\n\n"
diagram += "    %% Styling\n"
diagram += "    classDef service fill:#4A90E2\n"
diagram += "    class A,B service\n"
```

### C4 Model
```python
# Include imports and layout
diagram = "@startuml\n"
diagram += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml\n\n"
diagram += "LAYOUT_WITH_LEGEND()\n\n"
diagram += "title Container Diagram\n\n"
# ... diagram content
diagram += "@enduml"
```

### PlantUML
```python
diagram = "@startuml\n"
diagram += "title Diagram Title\n\n"
# ... diagram content
diagram += "@enduml"
```

## File Organization

When creating new files:

### Scripts
Place in `scripts/` directory:
```python
# scripts/analyze_requirements.py
# scripts/generate_diagrams.py
# scripts/design_api.py
```

### Examples
Place in `examples/` directory:
```python
# examples/example_custom_workflow.py
```

### Output
Save to `examples/output/` or create `architecture/`:
```python
output_dir = "examples/output"
os.makedirs(output_dir, exist_ok=True)
with open(f"{output_dir}/diagram.mmd", "w") as f:
    f.write(diagram)
```

## Common Workflows

### Complete Architecture Design
```python
from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator
from agents.api_designer import APIDesigner
from agents.database_visualizer import DatabaseVisualizer

# 1. Analyze requirements
analyzer = RequirementsAnalyzer()
analysis = analyzer.analyze_documents(["requirements.docx"])

# 2. Generate use case diagram
use_case = analyzer.generate_use_case_diagram(analysis)

# 3. Design architecture (create nodes/edges from requirements)
generator = DiagramGenerator()
# ... create architecture diagram

# 4. Design APIs
designer = APIDesigner()
api_spec = designer.design_rest_api("My API", ["Users", "Products"])

# 5. Design database
visualizer = DatabaseVisualizer()
# ... create database schema

# 6. Save all outputs
```

### Requirements to Implementation
```python
# Step 1: Parse requirements
analyzer = RequirementsAnalyzer()
analysis = analyzer.analyze_documents(file_paths)

# Step 2: Extract functional requirements
functional_reqs = [
    r for r in analysis.requirements
    if r.type == RequirementType.FUNCTIONAL
]

# Step 3: Generate API endpoints from requirements
designer = APIDesigner()
# Design based on functional requirements

# Step 4: Generate data model from requirements
# Extract entities and relationships from requirements
```

## CLI Integration

When creating CLI scripts:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Architecture Design Tool"
    )
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', default='output')
    parser.add_argument('--format', choices=['mermaid', 'c4', 'plantuml'])

    args = parser.parse_args()

    # Use agents based on arguments
```

## Testing Patterns

When writing tests:

```python
import unittest
from agents.requirements_analyzer import RequirementsAnalyzer

class TestRequirementsAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = RequirementsAnalyzer()

    def test_parse_text_file(self):
        # Test implementation
        pass
```

## Quality Standards

Before considering code complete:

1. **Imports:** All imports are valid and organized
2. **Type Hints:** All functions have type annotations
3. **Docstrings:** All public functions documented
4. **Error Handling:** Comprehensive try-except blocks
5. **File Operations:** Check file existence before reading
6. **Path Handling:** Use Path from pathlib
7. **Output Validation:** Verify diagram syntax
8. **Examples:** Include usage examples

## Resources

- **Examples:** `examples/` directory
- **Agent Code:** `agents/*/agent.py`
- **Agent Prompts:** `agents/*/prompt.md`
- **Documentation:** `docs/` directory
- **Templates:** `examples/templates/`

## Diagram Syntax References

- **Mermaid:** https://mermaid.js.org/
- **C4 Model:** https://c4model.com/
- **PlantUML:** https://plantuml.com/
- **OpenAPI:** https://swagger.io/specification/

## When in Doubt

Reference the example files in `examples/` directory for complete patterns and best practices.
