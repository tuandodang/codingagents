# Using Architecture Design Agents with AI Tools

This guide shows how to integrate and use the Architecture Design Agents with popular AI coding assistants: Claude AI, GitHub Copilot, and Cursor.

## Table of Contents

1. [Using with Claude AI](#using-with-claude-ai)
2. [Using with GitHub Copilot](#using-with-github-copilot)
3. [Using with Cursor](#using-with-cursor)
4. [Best Practices](#best-practices)

---

## Using with Claude AI

Claude AI can directly use these agents through conversation. You can share agent prompts or use the Python implementations.

### Method 1: Share Agent Prompts (Recommended)

Share the agent prompt files with Claude to enable specialized capabilities:

**Upload to Claude:**
1. Go to [claude.ai](https://claude.ai)
2. Start a new conversation
3. Upload agent prompt files from the `agents/*/prompt.md` directory
4. Ask Claude to act as that agent

**Example Conversation:**

```
You: [Upload agents/requirements-analyzer/prompt.md]
I have these requirement documents. Please analyze them and extract
all requirements.

[Upload your requirement documents]

Claude: I'll analyze these requirement documents as a Requirements
Engineer. Let me extract and categorize the requirements...

[Provides detailed analysis with categorization, priorities, and
recommendations]
```

### Method 2: Reference Agent Code

Share the Python implementation for Claude to understand and use:

```
You: [Upload agents/diagram-generator/agent.py]
Using the DiagramGenerator class, create a C4 container diagram
for a microservices e-commerce platform with:
- React frontend
- Node.js API Gateway
- Python order service
- PostgreSQL database
- Redis cache

Claude: [Generates complete C4 PlantUML code based on the agent's patterns]
```

### Method 3: Interactive Architecture Design Session

**Step-by-step workflow:**

```
1. Upload requirement documents
   You: [Upload requirements.docx, specs.pdf]
   "Analyze these requirements"

2. Generate use case diagram
   You: "Generate a PlantUML use case diagram from these requirements"
   Claude: [Creates use case diagram]

3. Design architecture
   You: "Design a microservices architecture for these requirements"
   Claude: [Suggests architecture]

4. Create C4 diagrams
   You: "Create C4 Context and Container diagrams"
   Claude: [Generates C4 diagrams]

5. Design APIs
   You: "Design REST APIs for the user management service"
   Claude: [Creates OpenAPI specification]

6. Design database
   You: "Create ER diagrams for the database schema"
   Claude: [Generates ER diagrams]
```

### Claude AI Projects Feature

Use Claude Projects to maintain context across conversations:

1. **Create a Project**: "Architecture Design for [Project Name]"
2. **Add Agent Prompts**: Upload all `prompt.md` files as project knowledge
3. **Add Your Documents**: Upload requirements, existing code, diagrams
4. **Set Instructions**:
   ```
   You are an expert technical architect using the Architecture Design
   Agents framework. You have access to:
   - Requirements Analyzer capabilities
   - Diagram Generator (Mermaid, C4, PlantUML)
   - API Designer
   - Database Visualizer

   Always provide:
   - Clear, actionable recommendations
   - Complete, ready-to-use diagram code
   - Best practices and alternatives
   ```

### Example Prompts for Claude

**Requirements Analysis:**
```
Analyze these requirements and:
1. Extract all functional and non-functional requirements
2. Categorize by type (functional, security, performance)
3. Assign priorities (critical, high, medium, low)
4. Generate a use case diagram
5. Create a traceability matrix
6. Provide recommendations for gaps or improvements
```

**Architecture Design:**
```
Design a complete architecture for this system:
1. Generate a C4 Context diagram showing actors and external systems
2. Create a C4 Container diagram showing runtime components
3. Suggest technology stack
4. Identify architectural patterns (microservices, event-driven, etc.)
5. Create sequence diagrams for critical flows
6. Provide scalability and security recommendations
```

**API Design:**
```
Design a REST API for this service:
1. List all endpoints with HTTP methods
2. Generate OpenAPI 3.0 specification
3. Create sequence diagrams for key flows
4. Design request/response schemas
5. Include authentication strategy
6. Provide best practices for versioning and error handling
```

---

## Using with GitHub Copilot

GitHub Copilot works best with code comments and context. Use these agents by:

### Method 1: Code Comments as Prompts

Use detailed comments to guide Copilot:

**Example: Generate Architecture Diagram**

```python
# Using the Architecture Design Agents framework
# Generate a Mermaid flowchart for a microservices e-commerce system with:
# - Web frontend (React)
# - Mobile app (React Native)
# - API Gateway (Kong)
# - Auth Service (Node.js)
# - Product Service (Python)
# - Order Service (Python)
# - PostgreSQL databases
# - Redis cache
# - Payment gateway (Stripe)
# - Email service (SendGrid)
#
# The diagram should show:
# - All services as nodes
# - Communication flows as edges
# - Proper styling (blue for services, green for databases, red for external)

from agents.diagram_generator import DiagramGenerator, Node, Edge

generator = DiagramGenerator()

# Copilot will suggest the complete implementation based on the comment
```

### Method 2: Context Files

Create a `.copilot-context` directory with agent prompts:

```bash
mkdir .copilot-context
cp agents/*/prompt.md .copilot-context/
```

Then reference in your code:

```python
# Context: Using Architecture Design Agents
# See .copilot-context/diagram-generator-prompt.md for capabilities
# Generate a C4 Container diagram

# Copilot now has context from the prompt file
```

### Method 3: Use Agent Code as Reference

Import the agents in your code, and Copilot will understand the patterns:

```python
from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator

# Copilot learns from the imported agent structure

# Analyze requirements from multiple documents
# and generate use case diagrams

analyzer = RequirementsAnalyzer()
# Copilot suggests: analysis = analyzer.analyze_documents(...)

generator = DiagramGenerator()
# Copilot suggests: diagram = generator.generate_use_case_diagram(...)
```

### GitHub Copilot Chat

Use Copilot Chat with agent context:

```
@workspace /new Create a requirements analysis script using the
RequirementsAnalyzer agent that:
1. Parses requirements.docx and specs.xlsx
2. Generates a use case diagram
3. Creates a traceability matrix
4. Saves all outputs to ./output/
```

### Copilot Workspace Prompts

Create workspace-level prompts in `.github/copilot-instructions.md`:

```markdown
# Architecture Design Agents Context

This project uses Architecture Design Agents for technical architecture tasks.

## Available Agents

1. **RequirementsAnalyzer**: Parse DOCX, XLSX, PDF, TXT files for requirements
2. **DiagramGenerator**: Create Mermaid, C4, PlantUML diagrams
3. **APIDesigner**: Generate OpenAPI specs and API documentation
4. **DatabaseVisualizer**: Create ER diagrams from schemas

## Code Style

When generating architecture-related code:
- Use the agent classes from `agents/` directory
- Follow the patterns in `examples/` directory
- Generate complete, ready-to-use diagram code
- Include proper error handling and validation

## Example Usage Patterns

See examples/ directory for complete patterns.
```

---

## Using with Cursor

Cursor has excellent integration capabilities for these agents.

### Method 1: Add Agents to Cursor Context

**Step 1: Configure Cursor Rules**

Create `.cursorrules` file in your project root:

```
# Architecture Design Agents - Cursor Rules

You are an expert technical architect with access to Architecture Design Agents.

## Available Agents

1. Requirements Analyzer (@agents/requirements-analyzer/prompt.md)
2. Diagram Generator (@agents/diagram-generator/prompt.md)
3. API Designer (@agents/api-designer/prompt.md)
4. Database Visualizer (@agents/database-visualizer/prompt.md)

## Capabilities

- Parse requirements from DOCX, XLSX, PDF, TXT files
- Generate Mermaid, C4, PlantUML, Draw.io diagrams
- Design REST APIs with OpenAPI specs
- Create database ER diagrams
- Analyze architecture patterns

## Output Format

When asked to generate diagrams:
1. Provide complete, syntactically correct code
2. Include proper styling and formatting
3. Add comments explaining key sections
4. Offer alternatives when appropriate

## Code Generation

When generating code:
- Use the agent classes from agents/ directory
- Follow patterns from examples/ directory
- Include comprehensive error handling
- Add type hints and docstrings
```

**Step 2: Use @ to Reference Agents**

In Cursor chat:

```
@agents/requirements-analyzer/prompt.md

Analyze the requirements in requirements.docx and generate:
1. Use case diagram
2. Traceability matrix
3. Full report with recommendations
```

### Method 2: Cursor Composer

Use Cursor Composer for multi-file operations:

```
Cmd+I (or Ctrl+I) to open Composer

Prompt:
"Using the Architecture Design Agents:
1. Read requirements from docs/requirements.docx
2. Generate Python script to analyze requirements
3. Create output directory structure
4. Save use case diagram, traceability matrix, and report
5. Update README.md with analysis results"
```

### Method 3: Cursor Chat with Context

**Architecture Design Session:**

```
You: @codebase Analyze this codebase and generate architecture diagrams

Cursor: [Analyzes codebase structure]

You: Using @agents/architecture-analyzer/prompt.md, create a C4
Container diagram showing all services, databases, and external systems

Cursor: [Generates C4 diagram based on analysis and agent prompt]

You: Now use @agents/api-designer/prompt.md to design REST APIs
for the user service

Cursor: [Generates OpenAPI specification]

You: Create database ER diagrams using @agents/database-visualizer/prompt.md

Cursor: [Generates ER diagrams]
```

### Method 4: Cursor AI Rules per Directory

Create `.cursor/` directory with agent-specific rules:

**`.cursor/requirements-analysis.md`:**
```markdown
When working on requirements analysis:
1. Use RequirementsAnalyzer from agents/requirements-analyzer/
2. Support DOCX, XLSX, PDF, TXT, MD, JSON formats
3. Generate use case diagrams in PlantUML
4. Create traceability matrices in Markdown
5. Provide gap analysis and recommendations
```

**`.cursor/diagram-generation.md`:**
```markdown
When generating diagrams:
1. Use DiagramGenerator from agents/diagram-generator/
2. Support Mermaid, C4, PlantUML, Draw.io formats
3. Apply proper styling and themes
4. Include legends and documentation
5. Validate syntax before output
```

### Method 5: Cursor Commands

Create custom Cursor commands in `.vscode/settings.json`:

```json
{
  "cursor.commands": [
    {
      "name": "Analyze Requirements",
      "prompt": "Using @agents/requirements-analyzer/prompt.md, analyze requirement documents in docs/ and generate a complete report with use case diagrams, traceability matrix, and recommendations"
    },
    {
      "name": "Generate Architecture Diagrams",
      "prompt": "Using @agents/architecture-analyzer/prompt.md and @agents/diagram-generator/prompt.md, analyze the codebase and generate C4 Context, Container, and Component diagrams"
    },
    {
      "name": "Design API",
      "prompt": "Using @agents/api-designer/prompt.md, design a complete REST API with OpenAPI specification and sequence diagrams for the selected service"
    },
    {
      "name": "Create Database Diagrams",
      "prompt": "Using @agents/database-visualizer/prompt.md, create ER diagrams in Mermaid and PlantUML formats from the database schema"
    }
  ]
}
```

### Cursor Notebook Mode

Use Cursor's notebook mode for interactive architecture design:

```python
# Cell 1: Setup
from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator

# Cell 2: Analyze Requirements
analyzer = RequirementsAnalyzer()
# Cursor suggests complete analysis code

# Cell 3: Generate Diagrams
generator = DiagramGenerator()
# Cursor suggests diagram generation

# Cell 4: Export Results
# Cursor suggests file export code
```

---

## Best Practices

### 1. Provide Clear Context

**Good:**
```
Using the Requirements Analyzer agent, analyze requirements.docx and:
1. Extract all functional requirements
2. Identify security requirements
3. Assign priorities based on keywords (must, should, could)
4. Generate a use case diagram in PlantUML
5. Create a traceability matrix
```

**Bad:**
```
Analyze the requirements
```

### 2. Reference Specific Agents

**Good:**
```
@agents/diagram-generator/prompt.md
Create a C4 Container diagram for microservices architecture
```

**Bad:**
```
Create a diagram
```

### 3. Specify Output Format

**Good:**
```
Generate a Mermaid ER diagram with:
- Crow's foot notation
- All tables and relationships
- Primary keys marked as PK
- Foreign keys marked as FK
- Proper styling with colors
```

**Bad:**
```
Make a database diagram
```

### 4. Iterative Refinement

Start broad, then refine:

```
1. "Generate a basic architecture diagram"
2. "Add authentication service"
3. "Include caching layer with Redis"
4. "Show external API integrations"
5. "Convert to C4 Container diagram"
```

### 5. Use Multiple Agents Together

**Complete workflow:**

```
1. Requirements Analysis → Use case diagrams
2. Architecture Design → C4 diagrams
3. API Design → OpenAPI specs + sequence diagrams
4. Database Design → ER diagrams
5. Documentation → Complete architecture docs
```

### 6. Maintain Agent Context

For long sessions, periodically remind the AI:

```
Continuing with the Architecture Design Agents framework:
- We have analyzed requirements (10 functional, 5 non-functional)
- Created C4 Context and Container diagrams
- Now design the database schema using the Database Visualizer agent
```

### 7. Validate Outputs

Always validate generated diagrams:

- **Mermaid**: Test at [mermaid.live](https://mermaid.live)
- **PlantUML**: Test at [plantuml.com](http://plantuml.com/online)
- **C4**: Verify C4-PlantUML syntax
- **OpenAPI**: Validate with [Swagger Editor](https://editor.swagger.io/)

---

## Integration Examples

### Example 1: Complete Architecture Design (Claude AI)

```
Session Start:
You: [Upload all agent prompts + requirements.docx]

"I need to design a complete architecture for an e-commerce platform.
Please use the Architecture Design Agents to:

1. Analyze requirements from requirements.docx
2. Generate use case diagrams
3. Design microservices architecture with C4 diagrams
4. Design REST APIs for each service
5. Create database schemas with ER diagrams
6. Provide implementation recommendations"

Claude: [Provides complete architecture design with all diagrams]
```

### Example 2: Code Generation (GitHub Copilot)

```python
# File: scripts/generate_architecture_docs.py

# Using Architecture Design Agents to automatically generate
# complete architecture documentation from requirements

from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator
from agents.api_designer import APIDesigner
from agents.database_visualizer import DatabaseVisualizer

# Step 1: Analyze requirements
# Copilot suggests complete implementation

# Step 2: Generate C4 diagrams
# Copilot suggests diagram generation

# Step 3: Design APIs
# Copilot suggests API design code

# Step 4: Create database diagrams
# Copilot suggests DB visualization
```

### Example 3: Interactive Design (Cursor)

```
Cursor Composer:

"Create a complete architecture design workflow:

1. Create script that reads requirements from docs/*.docx
2. Use @agents/requirements-analyzer to extract requirements
3. Use @agents/diagram-generator to create C4 diagrams
4. Use @agents/api-designer to generate OpenAPI specs
5. Use @agents/database-visualizer for ER diagrams
6. Save all outputs to architecture/ directory
7. Generate index.html showing all diagrams
8. Update project README with architecture section"

Cursor: [Generates complete multi-file solution]
```

---

## Tips for Each Tool

### Claude AI Tips
✅ Upload agent prompts as project knowledge
✅ Use Projects feature for persistent context
✅ Ask for alternatives and best practices
✅ Request explanations of architectural decisions
✅ Validate outputs and iterate

### GitHub Copilot Tips
✅ Write detailed comments before code
✅ Import agent classes for context
✅ Use meaningful variable names
✅ Reference patterns from examples/
✅ Use Copilot Chat for complex requests

### Cursor Tips
✅ Use @ to reference agent prompts
✅ Configure .cursorrules for project context
✅ Use Composer for multi-file operations
✅ Create custom commands for common tasks
✅ Leverage codebase indexing with @codebase

---

## Common Workflows

### Workflow 1: Requirements to Architecture

```
1. Upload/Reference requirements documents
2. Use Requirements Analyzer → Extract & categorize
3. Use Diagram Generator → Create use case diagrams
4. Use Architecture Analyzer → Suggest architecture
5. Use Diagram Generator → Generate C4 diagrams
6. Validate and iterate
```

### Workflow 2: API-First Design

```
1. Define requirements
2. Use API Designer → Generate OpenAPI spec
3. Use Diagram Generator → Create sequence diagrams
4. Use Database Visualizer → Design data models
5. Use Architecture Analyzer → Plan implementation
6. Generate code scaffolding
```

### Workflow 3: Documentation Generation

```
1. Analyze existing codebase
2. Use Architecture Analyzer → Identify patterns
3. Use Diagram Generator → Create all diagram types
4. Use API Designer → Document APIs
5. Use Database Visualizer → Document schemas
6. Compile into comprehensive documentation
```

---

## Troubleshooting

### Issue: AI doesn't understand agent capabilities

**Solution:** Explicitly reference the agent prompt file:
```
@agents/requirements-analyzer/prompt.md
[or upload the file]
```

### Issue: Generated code doesn't match agent patterns

**Solution:** Reference example files:
```
@examples/example_requirements_analysis.py
Follow this pattern to analyze requirements
```

### Issue: Diagrams have syntax errors

**Solution:** Ask for validation:
```
Generate a Mermaid diagram and validate the syntax.
Ensure it will render correctly on mermaid.live
```

### Issue: Missing context in long sessions

**Solution:** Provide context summary:
```
Context: We're designing an e-commerce platform.
So far: requirements analyzed (15 items), C4 context created.
Next: Design the Order Service API using API Designer agent.
```

---

## Resources

- **Agent Prompts**: `agents/*/prompt.md`
- **Examples**: `examples/example_*.py`
- **Templates**: `examples/templates/`
- **Documentation**: `docs/`
- **Getting Started**: `docs/GETTING_STARTED.md`
- **Claude Integration**: `docs/CLAUDE_INTEGRATION.md`

---

## Next Steps

1. **Choose your AI tool** (Claude, Copilot, or Cursor)
2. **Set up agent context** (upload prompts, configure rules)
3. **Start with requirements analysis**
4. **Generate architecture diagrams**
5. **Design APIs and databases**
6. **Iterate and refine**
7. **Generate documentation**

Happy architecting! 🎉
