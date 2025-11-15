# Getting Started with Architecture Design Agents

This guide will help you get started with using the Architecture Design Agents for your software architecture design needs.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/codingagents.git
cd codingagents
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
python main.py --help
```

## Quick Start

### Analyze Your Codebase

```bash
# Analyze current directory and generate Mermaid diagram
python main.py architecture --path . --format mermaid

# Generate C4 container diagram
python main.py architecture --path ./myproject --format c4 --output architecture.puml

# Deep analysis with PlantUML output
python main.py architecture --path ./myproject --format plantuml --depth deep
```

### Design an API

```bash
# Design REST API with resources
python main.py api --name "E-commerce API" --resources "Users,Products,Orders,Categories"

# Generate OpenAPI specification
python main.py api --name "My API" --resources "Users,Posts" --format openapi --output api-spec.json
```

### Visualize Database Schema

```bash
# Generate Mermaid ER diagram
python main.py database --format mermaid --output schema.mmd

# Generate PlantUML diagram
python main.py database --format plantuml --output schema.puml

# Generate DBML
python main.py database --format dbml --output schema.dbml
```

## Using the Python API

### Architecture Analysis

```python
from agents.architecture_analyzer.agent import ArchitectureAnalyzer

# Initialize analyzer
analyzer = ArchitectureAnalyzer()

# Analyze codebase
result = analyzer.analyze_codebase(
    path="./myproject",
    diagram_format="mermaid",
    depth="moderate"
)

# Access results
print(result['analysis']['architecture_pattern'])
print(result['diagram'])
```

### Diagram Generation

```python
from agents.diagram_generator.agent import DiagramGenerator, Node, Edge

generator = DiagramGenerator()

# Create nodes
nodes = [
    Node("web", "Web App", "service", "rounded"),
    Node("api", "API", "service"),
    Node("db", "Database", "database", "cylinder")
]

# Create edges
edges = [
    Edge("web", "api", "HTTPS"),
    Edge("api", "db", "SQL")
]

# Generate diagram
diagram = generator.generate_mermaid_flowchart(
    nodes, edges,
    title="Simple Architecture",
    direction="LR"
)

print(diagram)
```

### API Design

```python
from agents.api_designer.agent import APIDesigner

designer = APIDesigner()

# Design REST API
api_spec = designer.design_rest_api(
    name="E-commerce API",
    resources=["Users", "Products", "Orders"],
    version="1.0.0"
)

# Generate OpenAPI spec
openapi = designer.generate_openapi_spec(api_spec)

# Generate sequence diagram
sequence = designer.generate_sequence_diagram(api_spec.endpoints[0])
```

### Database Visualization

```python
from agents.database_visualizer.agent import DatabaseVisualizer

visualizer = DatabaseVisualizer()

# Create example schema
schema = visualizer.create_example_schema()

# Generate ER diagram
mermaid_er = visualizer.generate_er_diagram(schema, format="mermaid")
plantuml_er = visualizer.generate_er_diagram(schema, format="plantuml")

# Generate documentation
docs = visualizer.generate_schema_documentation(schema)
```

## Examples

Explore the `examples/` directory for complete working examples:

- `example_architecture_analysis.py` - Architecture analysis examples
- `example_diagram_generation.py` - Diagram generation examples
- `example_api_design.py` - API design examples
- `example_database_visualization.py` - Database visualization examples

Run examples:

```bash
# Run architecture analysis example
python examples/example_architecture_analysis.py

# Run diagram generation example
python examples/example_diagram_generation.py

# Run API design example
python examples/example_api_design.py

# Run database visualization example
python examples/example_database_visualization.py
```

## Viewing Diagrams

### Mermaid Diagrams

1. **Online Editor**: Copy diagram code to [mermaid.live](https://mermaid.live)
2. **GitHub/GitLab**: Paste in markdown files - renders automatically
3. **VS Code**: Install "Markdown Preview Mermaid Support" extension
4. **Obsidian**: Native support for Mermaid diagrams

### PlantUML Diagrams

1. **Online Editor**: [plantuml.com/online](http://www.plantuml.com/plantuml/uml/)
2. **VS Code**: Install "PlantUML" extension
3. **IntelliJ/PyCharm**: Built-in PlantUML support
4. **CLI**: Install PlantUML locally and run `plantuml diagram.puml`

### Draw.io Diagrams

1. **Online**: [app.diagrams.net](https://app.diagrams.net)
2. **Desktop**: Download Draw.io desktop app
3. **VS Code**: Install "Draw.io Integration" extension

## Common Use Cases

### 1. Documenting Existing System

```bash
# Analyze codebase
python main.py architecture --path ./myapp --format mermaid --output docs/architecture.mmd

# Generate database diagram
python main.py database --format mermaid --output docs/database.mmd
```

### 2. Designing New System

```python
from agents.diagram_generator.agent import DiagramGenerator

# Start with C4 context diagram
generator = DiagramGenerator()

context = generator.generate_c4_context(
    system_name="New System",
    users=[...],
    systems=[...],
    external_systems=[...],
    relationships=[...]
)

# Then create container diagram
# Then create component diagrams
# Design API
# Design database schema
```

### 3. API-First Development

```python
from agents.api_designer.agent import APIDesigner

designer = APIDesigner()

# Design API first
api_spec = designer.design_rest_api(
    name="My API",
    resources=["Resource1", "Resource2"]
)

# Generate OpenAPI spec for team
openapi = designer.generate_openapi_spec(api_spec)

# Generate sequence diagrams for flows
# Implement based on spec
```

### 4. Database Design

```python
from agents.database_visualizer.agent import (
    DatabaseVisualizer,
    DatabaseSchema,
    Table,
    Field,
    Relationship
)

# Define schema programmatically
schema = DatabaseSchema(
    name="My Database",
    tables=[...],
    relationships=[...]
)

# Generate ER diagram
visualizer = DatabaseVisualizer()
diagram = visualizer.generate_er_diagram(schema)

# Generate documentation
docs = visualizer.generate_schema_documentation(schema)
```

## Next Steps

- Read the [Agent Prompts](../agents/) to understand each agent's capabilities
- Explore [Examples](../examples/) for real-world usage patterns
- Check [Templates](../examples/templates/) for reusable patterns
- Review agent-specific documentation in each agent directory

## Troubleshooting

### Import Errors

Make sure you're running from the project root:

```bash
cd /path/to/codingagents
python examples/example_architecture_analysis.py
```

### Module Not Found

Install requirements:

```bash
pip install -r requirements.txt
```

### Diagram Not Rendering

- **Mermaid**: Check syntax at [mermaid.live](https://mermaid.live)
- **PlantUML**: Ensure PlantUML server is accessible
- **Draw.io**: Validate XML structure

## Getting Help

- Check documentation in `docs/`
- Review examples in `examples/`
- Open an issue on GitHub
- Read agent prompts for detailed capabilities

## Contributing

Contributions are welcome! See CONTRIBUTING.md for guidelines.
