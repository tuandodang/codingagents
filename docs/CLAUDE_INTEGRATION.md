# Integrating with Claude AI

This document explains how to use these architecture design agents with Claude AI for interactive architecture design sessions.

## Overview

These agents are designed to work seamlessly with Claude AI. Each agent has:
- **Agent Implementation** (`agent.py`) - Standalone Python code
- **Agent Prompt** (`prompt.md`) - Detailed instructions for Claude

## Using Agents with Claude

### Method 1: Share Agent Prompts

Share the agent prompt files with Claude to enable specialized architecture design capabilities:

1. **Architecture Analyzer**: Share `agents/architecture-analyzer/prompt.md`
2. **Diagram Generator**: Share `agents/diagram-generator/prompt.md`
3. **API Designer**: Share `agents/api-designer/prompt.md`
4. **Database Visualizer**: Share `agents/database-visualizer/prompt.md`

### Method 2: Interactive Sessions

Have a conversation with Claude using the context of these agents:

```
User: I'm working with the Architecture Design Agents system.
I need to design a microservices architecture for an e-commerce platform.

Claude: [Uses context from agent prompts to help design]
- Analyzes requirements
- Suggests architecture patterns
- Generates C4 diagrams
- Creates API specifications
- Designs database schemas
```

### Method 3: Code Generation with Claude

Ask Claude to generate architecture diagrams using the agent implementations:

```
User: Using the DiagramGenerator agent, create a C4 container diagram
for a microservices e-commerce platform with React frontend, Node.js
API gateway, Python services, and PostgreSQL databases.

Claude: [Generates complete C4 PlantUML code with proper syntax]
```

## Example Workflows

### Workflow 1: Complete System Design

**Step 1: Analyze Requirements**
```
User: I need to design an e-commerce platform with these requirements:
- Customer-facing web and mobile apps
- Product catalog with search
- Shopping cart and checkout
- Order management
- Payment processing
- Email notifications

Please analyze and suggest an architecture.
```

**Step 2: Generate Architecture Diagram**
```
User: Generate a C4 Context diagram for this system using Mermaid format.
```

**Step 3: Design API**
```
User: Design a REST API for this system with OpenAPI specification.
Focus on the Order Management service.
```

**Step 4: Design Database**
```
User: Create a database schema ER diagram for the order management
service including users, products, orders, and payments.
```

### Workflow 2: Iterative Design

```
User: Start with a basic 3-tier architecture diagram for a blog platform.

Claude: [Generates basic flowchart]

User: Now add caching layer and CDN.

Claude: [Updates diagram with Redis and CDN]

User: Convert this to a C4 Container diagram.

Claude: [Generates C4 diagram with more detail]

User: Generate API endpoints for the blog service.

Claude: [Creates REST API specification]
```

### Workflow 3: Documentation Generation

```
User: I have an existing microservices system. Help me document it.

Claude: I'll help you document your system. Please provide:
1. List of services
2. Technologies used
3. How services communicate
4. Database structure

User: [Provides information]

Claude: [Generates]:
- Architecture overview diagram
- Service component diagrams
- API documentation
- Database ER diagrams
- Deployment diagram
```

## Agent-Specific Use Cases

### Architecture Analyzer Agent

**Best for:**
- Analyzing existing codebases
- Identifying architecture patterns
- Technology stack documentation
- Architecture recommendations

**Example prompts:**
```
"Analyze this microservices architecture and generate a Mermaid diagram"
"Identify the architecture pattern used in this codebase"
"Generate recommendations for improving this architecture"
```

### Diagram Generator Agent

**Best for:**
- Creating diagrams from descriptions
- Converting between diagram formats
- Visualizing system flows
- Creating sequence diagrams

**Example prompts:**
```
"Create a sequence diagram showing the login flow"
"Generate a Mermaid flowchart for this CI/CD pipeline"
"Convert this architecture description to a C4 diagram"
"Show me a state diagram for order processing"
```

### API Designer Agent

**Best for:**
- Designing RESTful APIs
- Creating OpenAPI specifications
- GraphQL schema design
- API documentation

**Example prompts:**
```
"Design a REST API for user management with CRUD operations"
"Generate an OpenAPI 3.0 spec for this e-commerce API"
"Create a GraphQL schema for a blog platform"
"Show me the sequence diagram for the checkout API flow"
```

### Database Visualizer Agent

**Best for:**
- Database schema design
- ER diagram generation
- Database documentation
- Normalization analysis

**Example prompts:**
```
"Create an ER diagram for an e-commerce database"
"Generate a Mermaid ER diagram with users, posts, and comments"
"Design a database schema for a social media platform"
"Show relationships between tables in DBML format"
```

## Best Practices

### 1. Be Specific

❌ Bad: "Design an API"
✅ Good: "Design a REST API for user management with endpoints for CRUD operations, authentication, and password reset"

### 2. Specify Format

❌ Bad: "Create a diagram"
✅ Good: "Create a Mermaid flowchart showing the data flow from client to database"

### 3. Iterate

Start simple, then add complexity:
```
1. "Create a basic architecture diagram"
2. "Add authentication service"
3. "Add caching layer"
4. "Convert to C4 Container diagram"
```

### 4. Request Multiple Views

```
"For this e-commerce system, create:
1. C4 Context diagram
2. C4 Container diagram for the order service
3. Sequence diagram for checkout flow
4. ER diagram for the database"
```

### 5. Ask for Explanations

```
"Create a microservices architecture diagram and explain:
- Why this pattern was chosen
- How services communicate
- Scalability considerations
- Security best practices"
```

## Advanced Techniques

### Multi-Agent Workflow

Use multiple agents in sequence for comprehensive design:

```
1. Architecture Analyzer: Understand current system
2. Diagram Generator: Visualize current state
3. API Designer: Design new APIs
4. Database Visualizer: Design new schema
5. Diagram Generator: Create updated architecture diagrams
```

### Custom Styling

Request specific styling:

```
"Create a Mermaid diagram with:
- Blue for services
- Green for databases
- Red for external systems
- Include a legend"
```

### Documentation Bundle

Request complete documentation set:

```
"Create complete architecture documentation including:
1. System context diagram (C4)
2. Container diagram (C4)
3. Component diagram for core service
4. API specification (OpenAPI)
5. Database ER diagram
6. Deployment diagram
7. Sequence diagrams for 3 key flows"
```

## Integration Examples

### Example 1: Architecture Review

```python
# Share codebase structure with Claude
User: Here's my project structure:
myapp/
  frontend/
    - React app
  backend/
    - Node.js API
    - Python ML service
  database/
    - PostgreSQL

Claude: Based on your structure, this appears to be a layered architecture
with microservices elements. Let me generate a C4 Container diagram...

[Generates diagram using Diagram Generator agent capabilities]
```

### Example 2: API-First Design

```
User: I'm starting a new project API-first. Design a REST API for
a task management system with projects, tasks, comments, and users.

Claude: [Using API Designer agent]:
1. [Generates resource list]
2. [Creates endpoint structure]
3. [Generates OpenAPI spec]
4. [Creates sequence diagrams for key flows]
5. [Provides best practices and recommendations]
```

### Example 3: Database Migration Planning

```
User: I need to migrate from this database schema [provides schema]
to support multi-tenancy. Show me the before and after ER diagrams.

Claude: [Using Database Visualizer agent]:
1. [Generates current schema ER diagram]
2. [Designs multi-tenant schema]
3. [Generates new ER diagram]
4. [Provides migration plan]
5. [Shows SQL migration scripts]
```

## Tips for Success

1. **Provide Context**: Share relevant information about your system
2. **Be Iterative**: Start simple, refine iteratively
3. **Specify Format**: Always mention desired diagram format
4. **Ask Questions**: Claude can explain design decisions
5. **Request Alternatives**: Ask for multiple architecture options
6. **Validate Output**: Check generated diagrams in appropriate tools

## Common Patterns

### Pattern: Microservices Design

```
1. Start with C4 Context diagram
2. Create Container diagram for each service
3. Design APIs for inter-service communication
4. Design database per service
5. Add infrastructure components (API Gateway, Service Mesh)
6. Create sequence diagrams for critical flows
```

### Pattern: Monolith to Microservices

```
1. Analyze current monolith architecture
2. Identify service boundaries
3. Generate target microservices architecture
4. Design APIs for extracted services
5. Design databases for extracted services
6. Create migration plan diagrams
```

### Pattern: API Documentation

```
1. Design API with resources and endpoints
2. Generate OpenAPI specification
3. Create sequence diagrams for each endpoint
4. Generate request/response examples
5. Document authentication flows
6. Create error handling guide
```

## Resources

- [Mermaid Documentation](https://mermaid.js.org/)
- [C4 Model](https://c4model.com/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [PlantUML](https://plantuml.com/)
- [DBML](https://www.dbml.org/)

## Next Steps

- Explore agent prompts in `agents/*/prompt.md`
- Try example workflows
- Customize for your specific needs
- Integrate into your development workflow
