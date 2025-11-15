# Quick Start: Using Architecture Design Agents with AI Tools

Fast-track guide to using these agents with Claude AI, GitHub Copilot, and Cursor.

## 🚀 Claude AI - Quick Start

### Option 1: Upload Agent Prompts (Easiest)

1. Go to [claude.ai](https://claude.ai)
2. Upload agent prompts as project knowledge:
   - `agents/requirements-analyzer/prompt.md`
   - `agents/diagram-generator/prompt.md`
   - `agents/api-designer/prompt.md`
   - `agents/database-visualizer/prompt.md`

3. Start designing:
   ```
   You: Analyze these requirements and generate a complete architecture
   [Upload requirements.docx]

   Claude: [Provides complete analysis with diagrams]
   ```

### Option 2: Use Claude Projects

**Create Project:**
```
Project Name: "Architecture Design - [Your Project]"

Project Instructions:
You are an expert technical architect using the Architecture Design
Agents framework. Generate complete, ready-to-use diagrams in Mermaid,
C4, and PlantUML formats. Provide best practices and alternatives.

Knowledge:
- Upload all agents/*/prompt.md files
- Upload your requirements documents
- Upload any existing architecture docs
```

**Example Session:**
```
You: Design a microservices architecture for an e-commerce platform

Claude:
I'll design a complete microservices architecture. Let me start with:

1. C4 Context Diagram [provides diagram]
2. C4 Container Diagram [provides diagram]
3. Service breakdown [lists all services]
4. API design for each service
5. Database schemas
6. Technology recommendations

[Provides complete architecture with all diagrams]
```

### Ready-to-Use Prompts

**Copy-paste these into Claude:**

**Requirements Analysis:**
```
Using the Requirements Analyzer agent capabilities:

Analyze these requirements and provide:
1. Complete list of functional requirements
2. Non-functional requirements categorized by type
3. Priority assignments (critical/high/medium/low)
4. Use case diagram in PlantUML format
5. Requirements traceability matrix
6. Gap analysis
7. Recommendations for missing requirements

[Attach your requirement documents]
```

**Architecture Design:**
```
Using the Architecture Design Agents:

Design a [describe your system] with:

1. C4 Context diagram showing:
   - All actors
   - Main system
   - External systems
   - Relationships

2. C4 Container diagram showing:
   - Frontend applications
   - Backend services
   - Databases
   - Message queues
   - External integrations
   - Technology choices for each

3. Sequence diagrams for:
   - User registration flow
   - Main business process flow
   - Payment processing flow

4. Architecture recommendations for:
   - Scalability
   - Security
   - Performance
   - Deployment
```

**API Design:**
```
Using the API Designer agent:

Design a REST API for [your service] with:

1. Resource identification and endpoints
2. Full CRUD operations
3. OpenAPI 3.0 specification
4. Request/response schemas
5. Authentication strategy (JWT)
6. Error handling patterns
7. Sequence diagrams for key operations
8. Rate limiting recommendations
9. Versioning strategy
```

---

## 💻 GitHub Copilot - Quick Start

### Setup (One-time)

**1. Add Copilot Instructions**

File: `.github/copilot-instructions.md` (already created in this repo)

**2. Import Agents in Your Code**

```python
# Add at the top of your Python files
from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator
from agents.api_designer import APIDesigner
from agents.database_visualizer import DatabaseVisualizer
```

Copilot will now understand the agent patterns!

### Usage Pattern

**Write detailed comments, Copilot generates code:**

```python
# Using the Architecture Design Agents framework
# Create a complete architecture design workflow that:
# 1. Reads requirements from docs/requirements.docx
# 2. Analyzes and categorizes all requirements
# 3. Generates use case diagrams in PlantUML
# 4. Creates C4 Context and Container diagrams
# 5. Designs REST APIs with OpenAPI specs
# 6. Generates database ER diagrams
# 7. Saves all outputs to architecture/ directory
# 8. Creates an index.html with all diagrams

from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator

# Copilot will suggest complete implementation here
```

### Copilot Chat Examples

**In your IDE, use Copilot Chat:**

```
@workspace /new Create a script that uses the Requirements Analyzer
to parse requirements.docx and generate a complete analysis report
with use case diagrams and traceability matrix
```

```
@workspace Using the Diagram Generator agent, create a function that
generates a C4 Container diagram for a microservices e-commerce platform
```

```
@workspace Design a REST API using the API Designer agent for a
task management system with projects, tasks, and comments
```

### Quick Commands (Copy-Paste)

**Requirements Analysis Script:**
```python
# File: scripts/analyze_requirements.py
# Analyze requirements from multiple documents and generate reports

from agents.requirements_analyzer import RequirementsAnalyzer
import sys

# Copilot will auto-complete based on agent patterns
```

**Diagram Generation Script:**
```python
# File: scripts/generate_diagrams.py
# Generate all architecture diagrams for the project

from agents.diagram_generator import DiagramGenerator
from agents.architecture_analyzer import ArchitectureAnalyzer

# Copilot will suggest complete diagram generation
```

---

## 🎯 Cursor - Quick Start

### Setup (One-time)

**Files already created in this repo:**
- `.cursorrules` - Main Cursor configuration
- `.vscode/settings.json` - VS Code/Cursor settings with custom commands

**Just open the project in Cursor and you're ready!**

### Using @ References

**In Cursor chat:**

```
@agents/requirements-analyzer/prompt.md

Analyze the requirements in docs/requirements.docx and generate:
1. Use case diagram
2. Traceability matrix
3. Full report
```

```
@agents/diagram-generator/prompt.md

Create a C4 Container diagram for a microservices architecture with
React frontend, Node.js API gateway, Python services, and PostgreSQL
```

```
@agents/api-designer/prompt.md

Design a REST API for user management with full CRUD, authentication,
and password reset. Generate OpenAPI spec and sequence diagrams.
```

### Using Cursor Composer (Cmd+I / Ctrl+I)

**Multi-file operations:**

```
Create a complete architecture design:

1. @agents/requirements-analyzer Parse docs/requirements.txt
2. @agents/diagram-generator Create C4 diagrams
3. @agents/api-designer Design APIs from requirements
4. @agents/database-visualizer Create ER diagrams
5. Save everything to architecture/ folder
6. Create architecture/README.md with all diagrams
```

### Using Custom Commands

**In Cursor, use the Command Palette (Cmd+Shift+P / Ctrl+Shift+P):**

Type "Cursor:" and you'll see:
- **Analyze Requirements** - Complete requirements analysis
- **Generate Architecture Diagrams** - All C4 diagrams
- **Design API** - Full API design with OpenAPI
- **Create Database Diagrams** - ER diagrams in multiple formats
- **Complete Architecture Documentation** - Everything!

### Quick Workflows

**Architecture Design Session:**

```
Step 1: Upload requirements
[Drag requirements.docx into Cursor]

Step 2: Analyze
Cmd+L (open chat)
Type: @agents/requirements-analyzer/prompt.md analyze this document

Step 3: Design architecture
Type: @agents/diagram-generator/prompt.md create C4 diagrams

Step 4: Design API
Type: @agents/api-designer/prompt.md design REST APIs

Step 5: Design database
Type: @agents/database-visualizer/prompt.md create ER diagrams
```

**Code Generation:**

```
Cursor Composer (Cmd+I):

"Using @codebase and @agents/requirements-analyzer/prompt.md,
create a Python script that analyzes all .docx files in docs/
and generates a complete architecture documentation site"

Cursor generates complete multi-file solution!
```

---

## 📋 Comparison: Which Tool When?

### Use Claude AI When:
✅ You need detailed explanations and alternatives
✅ You're exploring multiple architecture options
✅ You want interactive refinement of designs
✅ You need comprehensive documentation
✅ You're learning architecture patterns

**Best For:** Architecture design sessions, requirements analysis, design exploration

### Use GitHub Copilot When:
✅ You're writing Python code
✅ You want inline code suggestions
✅ You're implementing based on existing patterns
✅ You need quick code snippets
✅ You're following examples from the repo

**Best For:** Implementation, following existing patterns, quick code generation

### Use Cursor When:
✅ You want seamless code and chat integration
✅ You need multi-file edits
✅ You want @ references to files and folders
✅ You need codebase-aware suggestions
✅ You want custom commands for workflows

**Best For:** Full project work, multi-file operations, integrated development

---

## 🎨 Example: Complete Workflow

### Scenario: Design E-commerce Platform Architecture

**Using Claude AI:**

```
Session: "E-commerce Architecture Design"

Me: [Upload requirements.docx + all agent prompts]

"Design a complete microservices architecture for this e-commerce
platform. Include all diagrams, API specs, and database schemas."

Claude:
[Provides complete architecture with:
- Requirements analysis (15 functional, 8 non-functional)
- Use case diagrams
- C4 Context diagram
- C4 Container diagram
- 5 microservices defined
- API specifications for each service
- Database ER diagrams
- Technology recommendations
- Security considerations
- Scalability plan]

Me: "Now generate the actual code structure"

Claude: [Provides project structure and starter code]
```

**Using Cursor:**

```
1. Open Cursor in project folder
2. Cmd+Shift+P → "Cursor: Analyze Requirements"
   [Analyzes docs/requirements.docx]

3. Cmd+Shift+P → "Cursor: Generate Architecture Diagrams"
   [Creates all C4 diagrams in architecture/diagrams/]

4. Cmd+Shift+P → "Cursor: Design API"
   [Generates OpenAPI specs in architecture/api/]

5. Cmd+Shift+P → "Cursor: Create Database Diagrams"
   [Creates ER diagrams in architecture/database/]

6. Cmd+Shift+P → "Cursor: Complete Architecture Documentation"
   [Compiles everything into architecture/README.md]

7. Cmd+I → "Generate implementation scaffolding"
   [Creates full project structure with starter code]
```

**Using GitHub Copilot:**

```python
# File: scripts/architecture_design.py

# Complete architecture design automation
# Uses all Architecture Design Agents to:
# 1. Analyze requirements
# 2. Generate diagrams
# 3. Design APIs
# 4. Create database schemas
# 5. Generate documentation

from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator
from agents.api_designer import APIDesigner
from agents.database_visualizer import DatabaseVisualizer

# Copilot auto-completes the entire implementation!
def main():
    # Step 1: Analyze requirements
    # [Copilot suggests complete code]

    # Step 2: Generate diagrams
    # [Copilot suggests complete code]

    # Step 3: Design APIs
    # [Copilot suggests complete code]

    # Step 4: Database schemas
    # [Copilot suggests complete code]
```

---

## 💡 Pro Tips

### For Claude AI:
- Upload all agent prompts as project knowledge
- Be specific about output format
- Ask for alternatives and explanations
- Request validation of generated diagrams
- Save good responses for reuse

### For GitHub Copilot:
- Write detailed comments before code
- Import agent classes for context
- Use meaningful variable names
- Reference examples/ directory in comments
- Use Copilot Chat for complex requests

### For Cursor:
- Use @ to reference agent prompts
- Configure .cursorrules (already done!)
- Use Composer for multi-file operations
- Create custom commands (already done!)
- Leverage @codebase for context

---

## 🔥 Ready-to-Use Templates

### Claude AI Session Template

```
Project Setup:
1. Create new Claude Project
2. Name: "Architecture Design - [Project Name]"
3. Upload agents/*/prompt.md files
4. Upload requirements documents

First Prompt:
"Using the Architecture Design Agents framework:
1. Analyze requirements from [documents]
2. Design [microservices/monolith/serverless] architecture
3. Generate all necessary diagrams
4. Provide implementation recommendations

Requirements:
[Describe your system requirements]

Constraints:
[Any technology or business constraints]

Expected output:
- Requirements analysis with priorities
- C4 diagrams (Context, Container, Component)
- API designs with OpenAPI specs
- Database ER diagrams
- Security and scalability recommendations"
```

### Cursor Workflow Template

```bash
# 1. Open project in Cursor
cd /path/to/project

# 2. Ensure docs exist
mkdir -p docs architecture

# 3. Add requirements
cp requirements.docx docs/

# 4. Use custom commands (Cmd+Shift+P):
# - Analyze Requirements
# - Generate Architecture Diagrams
# - Design API
# - Create Database Diagrams
# - Complete Architecture Documentation

# 5. Review generated files in architecture/
```

### Copilot Code Template

```python
#!/usr/bin/env python3
"""
Architecture Design Automation
Uses Architecture Design Agents framework
"""

# Import all agents
from agents.requirements_analyzer import RequirementsAnalyzer
from agents.diagram_generator import DiagramGenerator
from agents.api_designer import APIDesigner
from agents.database_visualizer import DatabaseVisualizer
from agents.architecture_analyzer import ArchitectureAnalyzer

# Setup paths
DOCS_DIR = "docs"
OUTPUT_DIR = "architecture"

# Main workflow
# [Copilot will suggest complete implementation]
```

---

## 🎯 Next Steps

1. **Choose your AI tool** (or use all three!)
2. **Follow the quick start for your chosen tool**
3. **Try the example workflow**
4. **Customize for your project**
5. **Share your results!**

Happy architecting! 🚀
