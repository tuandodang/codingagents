# Architecture Design Phases - Comprehensive Guide

A complete guide to software architecture design phases with tool-agnostic prompts and instructions for AI-assisted architecture design.

## Table of Contents

- [Overview](#overview)
- [Architecture Design Phases](#architecture-design-phases)
- [Phase 1: Requirements Gathering & Analysis](#phase-1-requirements-gathering--analysis)
- [Phase 2: System Context & Scope Definition](#phase-2-system-context--scope-definition)
- [Phase 3: Architecture Pattern Selection](#phase-3-architecture-pattern-selection)
- [Phase 4: Component Design](#phase-4-component-design)
- [Phase 5: API Design](#phase-5-api-design)
- [Phase 6: Data Architecture Design](#phase-6-data-architecture-design)
- [Phase 7: Infrastructure & Deployment Design](#phase-7-infrastructure--deployment-design)
- [Phase 8: Security & Quality Attributes](#phase-8-security--quality-attributes)
- [Phase 9: Documentation & Diagrams](#phase-9-documentation--diagrams)
- [Phase 10: Review & Validation](#phase-10-review--validation)
- [Using with AI Tools](#using-with-ai-tools)
- [Complete Workflow Examples](#complete-workflow-examples)
- [Best Practices](#best-practices)

---

## Overview

This guide provides a structured, phase-based approach to software architecture design. Each phase includes:

- **Objectives**: What you need to accomplish
- **AI Prompts**: Ready-to-use prompts for AI tools (Claude, Copilot, ChatGPT, Cursor, etc.)
- **Deliverables**: Expected outputs from the phase
- **Examples**: Sample outputs and diagrams
- **Tips**: Best practices and common pitfalls

### Why Use Phases?

1. **Structured Approach**: Systematic progression from requirements to implementation
2. **Complete Coverage**: Ensures no critical aspect is overlooked
3. **Tool Agnostic**: Works with any AI assistant or tool
4. **Iterative**: Can loop back to earlier phases as needed
5. **Scalable**: Works for projects of any size

---

## Architecture Design Phases

```
Phase 1: Requirements Gathering & Analysis
    ↓
Phase 2: System Context & Scope Definition
    ↓
Phase 3: Architecture Pattern Selection
    ↓
Phase 4: Component Design
    ↓
Phase 5: API Design
    ↓
Phase 6: Data Architecture Design
    ↓
Phase 7: Infrastructure & Deployment Design
    ↓
Phase 8: Security & Quality Attributes
    ↓
Phase 9: Documentation & Diagrams
    ↓
Phase 10: Review & Validation
```

---

## Phase 1: Requirements Gathering & Analysis

### Objectives
- Gather and document functional requirements
- Identify non-functional requirements (performance, security, scalability)
- Extract constraints and assumptions
- Prioritize requirements
- Create use case scenarios

### AI Prompts

#### Prompt 1.1: Extract Requirements from Documents
```
Analyze the following requirement documents and extract:
1. Functional requirements (categorized by feature area)
2. Non-functional requirements (performance, security, scalability, availability)
3. Business constraints (budget, timeline, compliance)
4. Technical constraints (existing systems, technology stack)
5. Assumptions being made

Documents:
[Paste your requirements documents, user stories, or descriptions]

Format the output as:
- Functional Requirements (FR-001, FR-002, etc.)
- Non-Functional Requirements (NFR-001, NFR-002, etc.)
- Constraints (CONST-001, CONST-002, etc.)
- Assumptions (ASSUM-001, ASSUM-002, etc.)
```

#### Prompt 1.2: Create Use Cases
```
Based on the following system description, create detailed use cases:

System: [Your system description]

For each use case, include:
1. Use case ID and name
2. Primary actor
3. Preconditions
4. Main flow (numbered steps)
5. Alternative flows
6. Postconditions
7. Business rules

Also generate a PlantUML use case diagram showing actors and use cases.
```

#### Prompt 1.3: Prioritize Requirements
```
Given these requirements, prioritize them using MoSCoW method:

Requirements:
[List your requirements]

Categorize each as:
- Must Have (critical for MVP)
- Should Have (important but not critical)
- Could Have (nice to have)
- Won't Have (out of scope for now)

Explain the rationale for each prioritization decision.
```

#### Prompt 1.4: Identify Quality Attributes
```
Analyze this system and identify key quality attributes:

System: [Description]

For each quality attribute, provide:
1. Attribute name (Performance, Security, Scalability, etc.)
2. Importance (Critical/High/Medium/Low)
3. Specific metrics or targets
4. Potential trade-offs
5. Design implications

Focus on: Performance, Security, Scalability, Availability, Maintainability, Usability
```

### Deliverables
- ✅ Categorized requirements list (FR, NFR)
- ✅ Use case diagrams and descriptions
- ✅ Prioritized requirements (MoSCoW)
- ✅ Quality attributes matrix
- ✅ Constraints and assumptions document

### Example Output

```markdown
## Functional Requirements

**FR-001**: User Authentication
- Priority: Must Have
- Description: Users must be able to register, login, and logout
- Acceptance Criteria: Support email/password and OAuth2 (Google, GitHub)

**FR-002**: Product Catalog
- Priority: Must Have
- Description: Display searchable product catalog with filters
- Acceptance Criteria: Support search, category filters, price range filters

## Non-Functional Requirements

**NFR-001**: Performance
- Response time < 200ms for 95% of requests
- Support 10,000 concurrent users
- Page load time < 2 seconds

**NFR-002**: Security
- HTTPS for all connections
- Password encryption (bcrypt)
- OWASP Top 10 compliance
```

---

## Phase 2: System Context & Scope Definition

### Objectives
- Define system boundaries
- Identify external systems and actors
- Document system interfaces
- Create context diagrams
- Define what's in scope vs out of scope

### AI Prompts

#### Prompt 2.1: Define System Context
```
Create a system context diagram for the following system:

System Name: [Your system name]
Purpose: [System purpose]
Users: [List of user types]
External Systems: [List of external integrations]

Generate:
1. Text description of system context
2. List of all actors (users and systems)
3. List of all external dependencies
4. C4 Context diagram in PlantUML format
5. Mermaid flowchart showing high-level interactions

Include: User types, external APIs, databases, third-party services, legacy systems
```

#### Prompt 2.2: Define Scope and Boundaries
```
Define clear scope and boundaries for this system:

System: [Description]

Provide:
1. In Scope: What the system WILL do
2. Out of Scope: What the system WILL NOT do
3. System Boundaries: Where the system starts and ends
4. Integration Points: How it connects to external systems
5. Data Ownership: What data this system owns vs consumes

Be specific about:
- Which features are included
- Which external systems are integrated
- What happens at system boundaries
```

#### Prompt 2.3: Identify Stakeholders
```
Identify all stakeholders for this system:

System: [Description]

For each stakeholder, document:
1. Stakeholder type (User, Administrator, External System, Business Owner)
2. Their goals and needs
3. How they interact with the system
4. Their level of influence (High/Medium/Low)
5. Key concerns or requirements

Categories: End Users, Administrators, Business Owners, Operations, Security, Compliance
```

#### Prompt 2.4: Map External Dependencies
```
Create a comprehensive map of external dependencies:

System: [Your system]

For each external dependency, document:
1. Dependency name and type (API, Database, Service, Library)
2. Purpose (what we use it for)
3. Integration method (REST API, SDK, Database connection)
4. Criticality (Critical/High/Medium/Low)
5. Failure impact and mitigation strategy
6. SLA requirements

Generate a dependency diagram showing the system and all external dependencies.
```

### Deliverables
- ✅ C4 Context diagram
- ✅ System boundary definition
- ✅ Stakeholder analysis
- ✅ External dependencies map
- ✅ Scope document (in/out of scope)

### Example Output

```
System Context: E-Commerce Platform

Actors:
- Customers (browse, purchase products)
- Administrators (manage products, orders)
- Payment Gateway (process payments)
- Email Service (send notifications)
- Inventory System (sync stock levels)

In Scope:
✅ Product catalog management
✅ Shopping cart and checkout
✅ Order management
✅ User authentication
✅ Payment processing integration

Out of Scope:
❌ Inventory warehouse management (handled by legacy system)
❌ Shipping label generation (handled by shipping provider)
❌ Customer service ticketing (separate system)
```

---

## Phase 3: Architecture Pattern Selection

### Objectives
- Evaluate architecture patterns
- Select appropriate pattern(s) for the system
- Document pattern rationale
- Identify pattern trade-offs

### AI Prompts

#### Prompt 3.1: Recommend Architecture Pattern
```
Recommend an architecture pattern for this system:

System Description:
- Purpose: [What the system does]
- Scale: [Expected users, data volume, transactions]
- Requirements: [Key functional and non-functional requirements]
- Constraints: [Technology, team, timeline constraints]
- Team: [Team size and expertise]

Evaluate these patterns:
1. Monolithic (Layered)
2. Microservices
3. Event-Driven
4. Serverless
5. Modular Monolith
6. Service-Oriented Architecture (SOA)

For each pattern, provide:
- Fit score (1-10)
- Advantages for this use case
- Disadvantages for this use case
- Implementation complexity
- Operational complexity
- Cost implications
- Scalability characteristics

Recommend the best pattern and explain why.
```

#### Prompt 3.2: Microservices Decomposition
```
Decompose this system into microservices:

System: [Description]
Business Capabilities: [List capabilities]

For each microservice, define:
1. Service name and purpose
2. Bounded context (domain)
3. Responsibilities (what it owns)
4. Data ownership (which data it manages)
5. Dependencies (which services it calls)
6. API endpoints (high-level)
7. Database (type and purpose)

Apply these principles:
- Single Responsibility Principle
- Bounded Context (DDD)
- Independent deployability
- Loose coupling
- High cohesion

Generate a service decomposition diagram.
```

#### Prompt 3.3: Evaluate Pattern Trade-offs
```
Create a detailed trade-off analysis for these architecture patterns:

System: [Description]
Candidate Patterns: [List 2-3 patterns you're considering]

For each pattern, evaluate:
1. Development Speed (time to first release)
2. Scalability (horizontal and vertical)
3. Maintainability (ease of changes)
4. Testability (unit, integration, e2e)
5. Deployment Complexity
6. Operational Overhead
7. Team Required (size and skills)
8. Cost (development and operations)
9. Technology Flexibility
10. Failure Isolation

Create a comparison matrix and recommend the best fit.
```

#### Prompt 3.4: Define Architectural Layers
```
Define the architectural layers for this system:

System: [Description]
Pattern: [Chosen pattern]

Define these layers:
1. Presentation Layer (UI, API Gateway)
   - Technologies
   - Responsibilities
   - Components

2. Application/Business Layer
   - Business logic organization
   - Service layer structure
   - Domain models

3. Data Access Layer
   - Repository pattern
   - ORM vs raw SQL
   - Data access strategies

4. Infrastructure Layer
   - Cross-cutting concerns
   - Logging, monitoring
   - Security, authentication

For each layer, specify:
- Purpose and responsibilities
- Technologies and frameworks
- Communication patterns
- Key components
```

### Deliverables
- ✅ Architecture pattern recommendation with rationale
- ✅ Pattern trade-off analysis
- ✅ Service decomposition (if microservices)
- ✅ Layer definitions and responsibilities
- ✅ High-level architecture diagram

### Example Output

```
Recommended Pattern: Modular Monolith

Rationale:
✅ Team size (5 developers) suits monolith better than microservices
✅ MVP timeline (3 months) requires faster initial development
✅ System complexity is moderate, doesn't justify microservices overhead
✅ Can evolve to microservices later if needed
✅ Simpler deployment and operations for early stage

Trade-offs Accepted:
⚠️ Less independent scalability (acceptable for current scale)
⚠️ Shared database (manageable with good module boundaries)
⚠️ Longer deployment times (acceptable with good CI/CD)

Architecture Layers:
1. API Layer (REST, GraphQL)
2. Application Services Layer
3. Domain Layer (modules: User, Product, Order, Payment)
4. Infrastructure Layer (Database, Cache, Email)
```

---

## Phase 4: Component Design

### Objectives
- Identify major components/modules
- Define component responsibilities
- Design component interactions
- Create component diagrams

### AI Prompts

#### Prompt 4.1: Identify System Components
```
Identify and define all major components for this system:

System: [Description]
Architecture Pattern: [Your chosen pattern]
Requirements: [Key requirements]

For each component, provide:
1. Component name
2. Type (Service, Module, Library, Gateway, etc.)
3. Primary responsibility
4. Key functionalities
5. Data it owns or manages
6. Dependencies (what it needs)
7. Dependents (what needs it)
8. Technology/framework recommendation

Organize by:
- Frontend components
- Backend components
- Data components
- Infrastructure components

Generate a C4 Container diagram showing all components.
```

#### Prompt 4.2: Design Component Interactions
```
Design how components interact in this system:

Components:
[List your components]

Key Scenarios:
[List key user scenarios or use cases]

For each scenario, document:
1. Sequence of component interactions
2. Communication protocol (REST, gRPC, Event, Message Queue)
3. Data exchanged
4. Error handling approach
5. Performance considerations

Generate:
- Sequence diagrams for 3-5 key scenarios
- Component interaction matrix
- Communication pattern summary
```

#### Prompt 4.3: Define Component APIs
```
Define the API/interface for each component:

Component: [Component name]
Responsibilities: [What it does]
Dependencies: [What it needs]

For each component, specify:
1. Public API/Interface
   - Methods/endpoints
   - Input parameters
   - Return types
   - Error responses

2. Events Published (if event-driven)
   - Event names
   - Event payloads
   - When published

3. Events Consumed (if event-driven)
   - Event names
   - Handler logic
   - Side effects

Format as interface definitions or API specifications.
```

#### Prompt 4.4: Design Module Structure
```
Design the internal module structure for this component:

Component: [Component name]
Type: [Service/Module/Application]
Pattern: [Layered/Clean/Hexagonal/DDD]

Define:
1. Package/Folder Structure
2. Key Classes/Modules
3. Responsibilities of each class
4. Design patterns used (Repository, Factory, Strategy, etc.)
5. Dependency injection approach
6. Configuration management

Provide a class diagram or module structure diagram.
```

### Deliverables
- ✅ Component catalog with descriptions
- ✅ C4 Container diagram
- ✅ Component interaction diagrams
- ✅ Component API/interface definitions
- ✅ Module structure diagrams

### Example Output

```
Component: Order Service

Responsibilities:
- Create and manage customer orders
- Calculate order totals and taxes
- Coordinate with Payment and Inventory services
- Track order status and history

Public API:
POST   /api/orders          - Create new order
GET    /api/orders/{id}     - Get order details
PUT    /api/orders/{id}     - Update order
DELETE /api/orders/{id}     - Cancel order
GET    /api/orders/user/{userId} - Get user's orders

Events Published:
- OrderCreated (orderId, userId, items, total)
- OrderConfirmed (orderId, paymentId)
- OrderCancelled (orderId, reason)

Events Consumed:
- PaymentCompleted (orderId, paymentId) → Confirm order
- PaymentFailed (orderId, reason) → Mark order failed

Dependencies:
- Product Service (validate products, check prices)
- Inventory Service (check stock, reserve items)
- Payment Service (process payments)
- Notification Service (send order confirmations)
```

---

## Phase 5: API Design

### Objectives
- Design RESTful/GraphQL/gRPC APIs
- Define endpoints and operations
- Specify request/response formats
- Document API contracts
- Generate OpenAPI specifications

### AI Prompts

#### Prompt 5.1: Design RESTful API
```
Design a RESTful API for this service:

Service: [Service name]
Resources: [List of resources/entities]
Operations: [CRUD and custom operations needed]

For each resource, define:
1. Resource path (e.g., /api/users)
2. HTTP methods (GET, POST, PUT, PATCH, DELETE)
3. Request format (headers, body, query params)
4. Response format (success and error responses)
5. Status codes (200, 201, 400, 401, 404, 500)
6. Authentication/Authorization requirements
7. Pagination strategy (for lists)
8. Filtering and sorting options

Generate:
- Complete endpoint list
- OpenAPI 3.0 specification
- Request/response examples
- Error response formats
```

#### Prompt 5.2: Design API Security
```
Design security mechanisms for this API:

API: [API description]
Sensitivity: [Public/Internal/Highly Sensitive]
Users: [Who accesses this API]

Design:
1. Authentication method
   - OAuth 2.0 / JWT / API Keys / Basic Auth
   - Token format and lifetime
   - Refresh token strategy

2. Authorization approach
   - RBAC (Role-Based Access Control)
   - ABAC (Attribute-Based Access Control)
   - Resource-level permissions

3. Rate limiting
   - Limits per user/API key
   - Strategy (token bucket, sliding window)

4. API security best practices
   - Input validation
   - SQL injection prevention
   - XSS prevention
   - CORS configuration
   - Encryption (TLS/SSL)

Generate security configuration and examples.
```

#### Prompt 5.3: Design GraphQL Schema
```
Design a GraphQL schema for this service:

Service: [Service name]
Entities: [List entities]
Relationships: [How entities relate]
Operations: [Queries and mutations needed]

Define:
1. Types (Object types for each entity)
2. Queries (read operations)
3. Mutations (write operations)
4. Subscriptions (real-time updates)
5. Input types (for mutations)
6. Enums (for fixed value sets)
7. Interfaces (for polymorphism)
8. Resolvers (data fetching logic)

Include:
- Pagination (relay cursor or offset-based)
- Filtering and sorting arguments
- Error handling approach
- Authentication directives

Generate complete GraphQL schema file (.graphql).
```

#### Prompt 5.4: Design API Versioning Strategy
```
Design an API versioning strategy:

API: [API name]
Current Version: [v1, v2, etc.]
Change Frequency: [How often API changes]
Consumers: [Mobile app, Web app, Third-party]

Recommend versioning approach:
1. URI versioning (/api/v1/users)
2. Header versioning (Accept: application/vnd.api.v1+json)
3. Query parameter versioning (/api/users?version=1)

For the chosen approach, define:
- How to introduce breaking changes
- How to deprecate old versions
- Migration path for consumers
- Documentation strategy
- Sunset policy (when to retire versions)

Include:
- Version compatibility matrix
- Deprecation announcement template
- Migration guide template
```

### Deliverables
- ✅ Complete API specification (OpenAPI/GraphQL schema)
- ✅ Endpoint documentation with examples
- ✅ Authentication and authorization design
- ✅ API versioning strategy
- ✅ Sequence diagrams for key API flows

### Example Output

```yaml
# OpenAPI 3.0 Specification
openapi: 3.0.0
info:
  title: Order Management API
  version: 1.0.0
  description: API for managing customer orders

paths:
  /api/orders:
    post:
      summary: Create new order
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                userId:
                  type: string
                  format: uuid
                items:
                  type: array
                  items:
                    type: object
                    properties:
                      productId:
                        type: string
                      quantity:
                        type: integer
                      price:
                        type: number
      responses:
        '201':
          description: Order created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          description: Invalid request
        '401':
          description: Unauthorized
```

---

## Phase 6: Data Architecture Design

### Objectives
- Design database schema
- Define data models and relationships
- Plan data storage strategy
- Design data access patterns
- Create ER diagrams

### AI Prompts

#### Prompt 6.1: Design Database Schema
```
Design a database schema for this system:

System: [System description]
Entities: [List main entities]
Data Volume: [Expected data volume]
Query Patterns: [Common query patterns]

For each entity, define:
1. Table/Collection name
2. Fields/Columns
   - Name, Type, Constraints
   - Primary key
   - Foreign keys
   - Indexes
3. Relationships (one-to-one, one-to-many, many-to-many)
4. Constraints (unique, not null, check)

Generate:
- SQL DDL (CREATE TABLE statements)
- ER diagram (Mermaid or PlantUML)
- Index strategy
- Normalization level (1NF, 2NF, 3NF)

Database type: [PostgreSQL/MySQL/MongoDB/etc.]
```

#### Prompt 6.2: Design Data Access Patterns
```
Design data access patterns for this application:

Application: [Description]
Database: [Database type]
Entities: [List entities]
Use Cases: [List key use cases]

For each use case, define:
1. Query pattern (SELECT, JOIN, aggregation)
2. Expected frequency (reads/sec)
3. Response time requirement
4. Data volume returned
5. Indexing strategy
6. Caching strategy
7. Pagination approach (if applicable)

Optimize for:
- Read-heavy vs write-heavy
- Complex queries vs simple lookups
- Real-time vs batch processing

Generate query examples and performance considerations.
```

#### Prompt 6.3: Choose Database Technology
```
Recommend database technology for this system:

Requirements:
- Data type: [Structured/Semi-structured/Unstructured]
- Scale: [Data volume, transactions/sec]
- Consistency needs: [Strong/Eventual]
- Query patterns: [Simple lookups/Complex queries/Analytics]
- Relationships: [Heavy relationships/Mostly independent]

Evaluate:
1. Relational (PostgreSQL, MySQL)
   - Pros/Cons for this use case
   - Schema design implications

2. Document (MongoDB, Couchbase)
   - Pros/Cons for this use case
   - Document structure

3. Key-Value (Redis, DynamoDB)
   - Pros/Cons for this use case
   - Use cases

4. Graph (Neo4j, Amazon Neptune)
   - Pros/Cons for this use case
   - When to use

5. Time-Series (InfluxDB, TimescaleDB)
   - Pros/Cons for this use case
   - Metrics and events

Recommend primary database and explain rationale.
Include potential secondary databases for specific use cases.
```

#### Prompt 6.4: Design Data Migration Strategy
```
Design a data migration strategy:

Source: [Current data storage]
Target: [New data storage]
Data Volume: [Amount of data to migrate]
Downtime Allowed: [Zero downtime/Limited downtime/Flexible]

Design:
1. Migration approach
   - Big bang (all at once)
   - Phased (incremental)
   - Parallel run (dual write)

2. Migration steps
   - Schema migration
   - Data transformation rules
   - Validation strategy
   - Rollback plan

3. Data integrity
   - Consistency checks
   - Validation queries
   - Reconciliation process

4. Timeline and phases
5. Risk mitigation
6. Testing strategy

Provide detailed migration plan and scripts.
```

### Deliverables
- ✅ Database schema (DDL scripts)
- ✅ ER diagrams
- ✅ Data access patterns documentation
- ✅ Database technology selection with rationale
- ✅ Data migration plan (if applicable)

### Example Output

```sql
-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    category_id UUID REFERENCES categories(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_price ON products(price);

-- Orders Table
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created ON orders(created_at DESC);
```

---

## Phase 7: Infrastructure & Deployment Design

### Objectives
- Design cloud infrastructure
- Plan deployment strategy
- Design CI/CD pipeline
- Plan scaling strategy
- Design monitoring and observability

### AI Prompts

#### Prompt 7.1: Design Cloud Infrastructure
```
Design cloud infrastructure for this system:

System: [Description]
Cloud Provider: [AWS/Azure/GCP/Multi-cloud]
Architecture: [Monolith/Microservices/Serverless]
Scale: [Expected traffic and data volume]

Design:
1. Compute Resources
   - VM instances / Containers / Serverless functions
   - Instance types and sizes
   - Auto-scaling configuration

2. Networking
   - VPC/Network design
   - Subnets (public/private)
   - Load balancers
   - API Gateway
   - CDN

3. Storage
   - Database instances
   - Object storage (S3/Blob)
   - File storage
   - Cache (Redis/Memcached)

4. Security
   - Firewall rules
   - Security groups
   - IAM roles and policies
   - Secrets management
   - Encryption (at rest and in transit)

Generate infrastructure diagram and IaC configuration (Terraform/CloudFormation).
```

#### Prompt 7.2: Design Deployment Strategy
```
Design deployment strategy for this application:

Application: [Description]
Architecture: [Type]
Team Size: [Number of developers]
Release Frequency: [Daily/Weekly/Monthly]

Define:
1. Deployment Pattern
   - Blue-Green deployment
   - Canary deployment
   - Rolling deployment
   - Feature flags

2. Environments
   - Development
   - Staging
   - Production
   - DR (Disaster Recovery)

3. Deployment Process
   - Build and package
   - Test stages (unit, integration, e2e)
   - Approval gates
   - Rollback procedure

4. Zero-Downtime Strategy
   - How to achieve zero downtime
   - Database migration during deployment
   - Traffic switching

Generate deployment pipeline diagram and configuration.
```

#### Prompt 7.3: Design CI/CD Pipeline
```
Design a complete CI/CD pipeline:

Project: [Description]
Tech Stack: [Languages, frameworks]
Repository: [GitHub/GitLab/Bitbucket]
CI/CD Tool: [Jenkins/GitLab CI/GitHub Actions/CircleCI]

Pipeline Stages:
1. Source Control
   - Branch strategy (GitFlow/Trunk-based)
   - PR requirements
   - Code review process

2. Build Stage
   - Compile/transpile
   - Dependency management
   - Artifact creation

3. Test Stage
   - Unit tests
   - Integration tests
   - E2E tests
   - Security scanning
   - Code quality checks

4. Deploy Stage
   - Environment-specific configs
   - Infrastructure provisioning
   - Application deployment
   - Health checks

5. Post-Deployment
   - Smoke tests
   - Monitoring alerts
   - Rollback triggers

Generate pipeline configuration file (e.g., .gitlab-ci.yml, github-actions.yml).
```

#### Prompt 7.4: Design Monitoring and Observability
```
Design monitoring and observability strategy:

System: [Description]
Components: [List of services/components]
SLA: [Uptime target, response time targets]

Design:
1. Metrics Collection
   - Infrastructure metrics (CPU, memory, disk, network)
   - Application metrics (requests/sec, latency, errors)
   - Business metrics (orders, revenue, conversions)
   - Custom metrics

2. Logging Strategy
   - Log levels (DEBUG, INFO, WARN, ERROR)
   - Structured logging format (JSON)
   - Log aggregation (ELK, Splunk, CloudWatch)
   - Retention policy

3. Distributed Tracing
   - Trace spans across services
   - Trace sampling strategy
   - Tools (Jaeger, Zipkin, AWS X-Ray)

4. Alerting
   - Critical alerts (downtime, errors)
   - Warning alerts (performance degradation)
   - Alert channels (email, Slack, PagerDuty)
   - On-call rotation

5. Dashboards
   - Infrastructure dashboard
   - Application performance dashboard
   - Business metrics dashboard
   - SLA dashboard

Generate monitoring configuration and dashboard specifications.
```

### Deliverables
- ✅ Infrastructure architecture diagram
- ✅ IaC configuration (Terraform/CloudFormation)
- ✅ Deployment strategy document
- ✅ CI/CD pipeline configuration
- ✅ Monitoring and alerting setup

### Example Output

```yaml
# GitHub Actions CI/CD Pipeline
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run unit tests
        run: npm run test:unit

      - name: Run integration tests
        run: npm run test:integration

      - name: Build application
        run: npm run build

      - name: Security scan
        run: npm audit

  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: |
          echo "Deploying to staging..."
          # Deployment commands here

  deploy-production:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          # Deployment commands here
```

---

## Phase 8: Security & Quality Attributes

### Objectives
- Design security architecture
- Implement security best practices
- Address quality attributes (performance, reliability, etc.)
- Design disaster recovery

### AI Prompts

#### Prompt 8.1: Design Security Architecture
```
Design comprehensive security architecture:

System: [Description]
Sensitivity: [Public/Internal/Highly Sensitive]
Compliance: [GDPR/HIPAA/PCI-DSS/SOC2]

Design security for:
1. Authentication & Authorization
   - Identity provider (Auth0, Cognito, Okta)
   - Multi-factor authentication (MFA)
   - Single Sign-On (SSO)
   - Role-based access control (RBAC)

2. Network Security
   - Firewall rules
   - DDoS protection
   - VPN access
   - Network segmentation

3. Data Security
   - Encryption at rest (AES-256)
   - Encryption in transit (TLS 1.3)
   - Key management (KMS)
   - PII/PHI handling
   - Data masking/anonymization

4. Application Security
   - Input validation
   - XSS prevention
   - CSRF protection
   - SQL injection prevention
   - Secure headers
   - Security scanning (SAST/DAST)

5. API Security
   - API authentication (OAuth 2.0, JWT)
   - Rate limiting
   - API key rotation
   - Request signing

6. Audit & Compliance
   - Audit logging
   - Access logs
   - Compliance monitoring
   - Security incident response

Generate security architecture diagram and security checklist.
```

#### Prompt 8.2: Design for Performance
```
Design for high performance:

System: [Description]
Performance Targets:
- Response time: [e.g., < 200ms p95]
- Throughput: [e.g., 10K req/sec]
- Concurrent users: [e.g., 50K]

Optimization strategies:
1. Caching
   - Cache layers (CDN, Application, Database)
   - Cache strategies (Cache-aside, Write-through, Write-back)
   - Cache invalidation
   - TTL policies

2. Database Optimization
   - Query optimization
   - Indexing strategy
   - Connection pooling
   - Read replicas
   - Sharding/Partitioning

3. Application Optimization
   - Async processing
   - Batch operations
   - Lazy loading
   - Code profiling hotspots

4. Content Delivery
   - CDN configuration
   - Static asset optimization
   - Image optimization
   - Compression (gzip, brotli)

5. Load Balancing
   - Load balancer configuration
   - Health checks
   - Session affinity
   - Geographic routing

Generate performance optimization plan and benchmarking strategy.
```

#### Prompt 8.3: Design for Reliability & Resilience
```
Design for high reliability and resilience:

System: [Description]
SLA Target: [e.g., 99.9% uptime]
RTO: [Recovery Time Objective]
RPO: [Recovery Point Objective]

Design:
1. High Availability
   - Multi-AZ deployment
   - Database replication
   - Stateless application design
   - Health checks and auto-recovery

2. Fault Tolerance
   - Circuit breaker pattern
   - Retry mechanisms (exponential backoff)
   - Timeout configurations
   - Bulkhead pattern (isolation)
   - Graceful degradation

3. Disaster Recovery
   - Backup strategy (frequency, retention)
   - DR site (hot/warm/cold standby)
   - Failover procedures
   - Data replication
   - Recovery testing

4. Monitoring & Alerting
   - Error rate monitoring
   - Latency monitoring
   - Resource utilization
   - Automated alerts
   - Incident response runbooks

Generate reliability architecture diagram and DR runbook.
```

#### Prompt 8.4: Design Compliance & Governance
```
Design for compliance and governance:

System: [Description]
Regulations: [GDPR/HIPAA/PCI-DSS/SOC2/etc.]
Data Types: [PII/PHI/Payment/etc.]

Compliance Requirements:
1. Data Privacy
   - User consent management
   - Right to access data
   - Right to deletion (GDPR)
   - Data retention policies
   - Privacy by design

2. Data Residency
   - Geographic restrictions
   - Cross-border data transfer
   - Data localization

3. Audit Requirements
   - Activity logging
   - Access logging
   - Change tracking
   - Audit reports

4. Security Controls
   - Encryption requirements
   - Access controls
   - Vulnerability management
   - Penetration testing

5. Documentation
   - Data processing agreements
   - Privacy policy
   - Terms of service
   - Security documentation

Generate compliance checklist and implementation guide.
```

### Deliverables
- ✅ Security architecture diagram
- ✅ Security implementation checklist
- ✅ Performance optimization plan
- ✅ Reliability and DR strategy
- ✅ Compliance documentation

---

## Phase 9: Documentation & Diagrams

### Objectives
- Create comprehensive architecture documentation
- Generate all required diagrams
- Document design decisions
- Create Architecture Decision Records (ADRs)

### AI Prompts

#### Prompt 9.1: Generate Complete Architecture Documentation
```
Generate comprehensive architecture documentation:

System: [System name and description]

Documentation Structure:
1. Executive Summary
   - System purpose and goals
   - Key stakeholders
   - Success metrics

2. Architecture Overview
   - Architecture pattern
   - High-level architecture diagram
   - Key components
   - Technology stack

3. Detailed Design
   - Component descriptions
   - API specifications
   - Data models
   - Integration points

4. Quality Attributes
   - Performance characteristics
   - Security measures
   - Scalability approach
   - Reliability features

5. Deployment
   - Infrastructure architecture
   - Deployment process
   - Environments
   - CI/CD pipeline

6. Operations
   - Monitoring and alerting
   - Logging strategy
   - Incident response
   - Backup and recovery

7. Appendices
   - Glossary
   - References
   - ADRs (Architecture Decision Records)

Format as comprehensive markdown document with diagrams.
```

#### Prompt 9.2: Create All Architecture Diagrams
```
Generate complete set of architecture diagrams:

System: [Description]

Create these diagrams:
1. C4 Model Diagrams
   - Level 1: System Context
   - Level 2: Container Diagram
   - Level 3: Component Diagram (for main components)
   - Level 4: Code Diagram (for critical parts)

2. Deployment Diagram
   - Infrastructure components
   - Network topology
   - Security zones

3. Sequence Diagrams
   - User authentication flow
   - Order creation flow
   - Payment processing flow
   - [Other key flows]

4. Data Flow Diagram
   - How data moves through the system
   - Data transformations
   - Data storage points

5. ER Diagram
   - Database schema
   - Relationships
   - Cardinality

6. Network Diagram
   - VPC/network structure
   - Subnets
   - Firewalls and security groups
   - Load balancers

Generate in Mermaid and PlantUML formats where applicable.
```

#### Prompt 9.3: Write Architecture Decision Records (ADRs)
```
Create Architecture Decision Records:

For each major decision, document:
- Decision: [What was decided]
- Context: [What is the issue we're facing]
- Considered Options: [What alternatives were considered]
- Decision Outcome: [What we decided to do]
- Rationale: [Why we chose this option]
- Consequences: [Positive and negative impacts]
- Status: [Proposed/Accepted/Deprecated/Superseded]
- Date: [When the decision was made]

Create ADRs for:
1. Architecture pattern selection (Monolith vs Microservices)
2. Database technology choice
3. API design approach (REST vs GraphQL)
4. Cloud provider selection
5. Programming language/framework choice
6. Authentication mechanism
7. Caching strategy
8. [Other major decisions]

Format: markdown files (ADR-001.md, ADR-002.md, etc.)
```

#### Prompt 9.4: Create API Documentation
```
Generate comprehensive API documentation:

APIs: [List of APIs]

For each API, document:
1. Overview
   - Purpose
   - Base URL
   - Authentication method
   - Rate limits

2. Endpoints
   - Endpoint path
   - HTTP method
   - Description
   - Request parameters
   - Request body (with schema)
   - Response body (with schema)
   - Status codes
   - Example requests
   - Example responses

3. Authentication
   - How to obtain tokens
   - How to use tokens
   - Token expiration
   - Refresh token flow

4. Error Handling
   - Error response format
   - Common error codes
   - Troubleshooting guide

5. Examples and Tutorials
   - Common use cases
   - Code examples (curl, JavaScript, Python)
   - Integration guides

Generate as:
- OpenAPI 3.0 specification (YAML)
- Markdown documentation
- Interactive API documentation (Swagger UI compatible)
```

### Deliverables
- ✅ Complete architecture documentation
- ✅ Full set of diagrams (C4, sequence, ER, deployment)
- ✅ Architecture Decision Records (ADRs)
- ✅ API documentation
- ✅ Operational runbooks

---

## Phase 10: Review & Validation

### Objectives
- Review architecture against requirements
- Validate design decisions
- Identify risks and mitigation strategies
- Get stakeholder sign-off

### AI Prompts

#### Prompt 10.1: Architecture Review Checklist
```
Create comprehensive architecture review checklist:

System: [Description]

Review Categories:
1. Requirements Coverage
   ✓ All functional requirements addressed
   ✓ All non-functional requirements addressed
   ✓ Constraints acknowledged and handled
   ✓ Assumptions documented

2. Architecture Principles
   ✓ Scalability (horizontal and vertical)
   ✓ Maintainability (code organization, documentation)
   ✓ Testability (unit, integration, e2e)
   ✓ Security (authentication, authorization, encryption)
   ✓ Performance (caching, optimization)
   ✓ Reliability (fault tolerance, disaster recovery)
   ✓ Observability (logging, monitoring, tracing)

3. Design Quality
   ✓ Loose coupling between components
   ✓ High cohesion within components
   ✓ Clear separation of concerns
   ✓ SOLID principles followed
   ✓ DRY (Don't Repeat Yourself)
   ✓ YAGNI (You Ain't Gonna Need It)

4. Technology Choices
   ✓ Appropriate for requirements
   ✓ Team has expertise
   ✓ Well-supported and maintained
   ✓ Cost-effective
   ✓ Scalable and performant

5. Risks Identified
   ✓ Technical risks
   ✓ Operational risks
   ✓ Security risks
   ✓ Business risks
   ✓ Mitigation strategies for each

Generate detailed review checklist with scoring system.
```

#### Prompt 10.2: Identify Architecture Risks
```
Identify architecture risks and mitigation strategies:

Architecture: [Description]

For each risk category, identify specific risks:
1. Technical Risks
   - Technology immaturity
   - Integration complexity
   - Performance bottlenecks
   - Scalability limitations
   - Technical debt

2. Operational Risks
   - Deployment complexity
   - Operational overhead
   - Monitoring gaps
   - Disaster recovery gaps
   - Dependency on external services

3. Security Risks
   - Authentication vulnerabilities
   - Data breach possibilities
   - Compliance violations
   - API security gaps

4. Business Risks
   - Time to market delays
   - Cost overruns
   - Vendor lock-in
   - Team capability gaps

For each risk, provide:
- Risk description
- Likelihood (High/Medium/Low)
- Impact (High/Medium/Low)
- Risk score (Likelihood × Impact)
- Mitigation strategy
- Contingency plan

Generate risk register and mitigation plan.
```

#### Prompt 10.3: Validate Against Quality Attributes
```
Validate architecture against quality attributes:

Architecture: [Description]
Quality Attribute Targets: [List targets]

Validate each quality attribute:
1. Performance
   - Target: [e.g., < 200ms response time]
   - How architecture achieves this
   - Potential bottlenecks
   - Validation method (load testing)
   - Confidence level

2. Scalability
   - Target: [e.g., 100K concurrent users]
   - Horizontal scaling approach
   - Vertical scaling limits
   - Validation method (scaling tests)
   - Confidence level

3. Security
   - Target: [e.g., OWASP Top 10 compliance]
   - Security measures implemented
   - Potential vulnerabilities
   - Validation method (security audit)
   - Confidence level

4. Availability
   - Target: [e.g., 99.9% uptime]
   - HA architecture components
   - SPOF (Single Points of Failure)
   - Validation method (chaos engineering)
   - Confidence level

5. Maintainability
   - Target: [e.g., easy to add features]
   - Code organization approach
   - Documentation completeness
   - Validation method (code review)
   - Confidence level

Generate validation report with confidence scores and gaps.
```

#### Prompt 10.4: Create Architecture Presentation
```
Create architecture presentation for stakeholders:

Audience: [Executives/Technical Team/Business Stakeholders]
System: [Description]

Presentation Structure:
1. Introduction (2-3 slides)
   - Business problem and goals
   - Success criteria
   - Presentation agenda

2. Current State (if applicable) (1-2 slides)
   - Existing system
   - Pain points
   - Why change is needed

3. Proposed Architecture (3-5 slides)
   - High-level architecture diagram
   - Key components
   - Technology choices
   - How it solves the problem

4. Quality Attributes (2-3 slides)
   - Performance characteristics
   - Security features
   - Scalability approach
   - Reliability measures

5. Implementation Plan (2-3 slides)
   - Phases and timeline
   - Key milestones
   - Resource requirements
   - Dependencies

6. Risks and Mitigation (1-2 slides)
   - Top 5 risks
   - Mitigation strategies
   - Contingency plans

7. Cost Analysis (1-2 slides)
   - Development costs
   - Infrastructure costs
   - Operational costs
   - ROI projection

8. Next Steps (1 slide)
   - Immediate actions
   - Decision points
   - Timeline

Generate presentation outline with key talking points.
```

### Deliverables
- ✅ Architecture review checklist with results
- ✅ Risk register with mitigation plans
- ✅ Quality attribute validation report
- ✅ Stakeholder presentation
- ✅ Sign-off documentation

---

## Using with AI Tools

### Claude AI

```
1. Start a new conversation or project
2. Upload this guide as context
3. Specify your project and phase
4. Use the prompts from each phase
5. Iterate based on Claude's responses
```

**Example:**
```
I'm working on Phase 1 (Requirements Analysis) for an e-commerce platform.
Use Prompt 1.1 to help me extract requirements from this document:
[paste your requirements]
```

### GitHub Copilot

```
1. Add this guide to your repository
2. Reference it in comments: "Following ARCHITECTURE_DESIGN_PHASES.md Phase 3..."
3. Use prompts in code comments
4. Let Copilot suggest based on the context
```

**Example:**
```javascript
// Following Phase 5 (API Design), design RESTful API for orders
// Include CRUD operations, authentication, and pagination
```

### Cursor IDE

```
1. Add this guide to your project
2. Use @ to reference: "@ARCHITECTURE_DESIGN_PHASES.md Phase 4"
3. Use Cmd+K with prompts
4. Iterate in the chat panel
```

**Example:**
```
@ARCHITECTURE_DESIGN_PHASES.md Help me with Phase 4 (Component Design)
for a microservices e-commerce system. Use Prompt 4.1 to identify components.
```

### ChatGPT

```
1. Start conversation with: "I'm following a structured architecture design guide"
2. Share relevant phase description
3. Use prompts from this guide
4. Build on previous responses
```

---

## Complete Workflow Examples

### Example 1: E-Commerce Platform (Microservices)

```
Phase 1: Requirements
→ Extract requirements from business documents
→ Create use cases for customer shopping journey
→ Prioritize: Must have (checkout), Should have (reviews), Could have (recommendations)

Phase 2: System Context
→ Define: Customers, Admin, Payment Gateway, Email Service, Inventory System
→ Create C4 Context diagram
→ Define scope: In (catalog, cart, checkout) / Out (shipping, warehouse)

Phase 3: Pattern Selection
→ Choose Microservices (high scale, team size, independent deployment)
→ Identify services: User, Product, Cart, Order, Payment, Notification

Phase 4: Component Design
→ Design each microservice with domain boundaries
→ Define APIs for inter-service communication
→ Create service interaction diagrams

Phase 5: API Design
→ Design REST APIs for each service
→ Create OpenAPI specifications
→ Design API Gateway routing

Phase 6: Data Design
→ Database per service (PostgreSQL for transactional, MongoDB for catalog)
→ Design schemas with proper relationships
→ Plan event sourcing for order history

Phase 7: Infrastructure
→ Design Kubernetes cluster architecture
→ Setup CI/CD with GitLab
→ Configure monitoring with Prometheus + Grafana

Phase 8: Security
→ Implement OAuth 2.0 with JWT
→ Setup API Gateway security
→ Design PCI-DSS compliance for payments

Phase 9: Documentation
→ Create all C4 diagrams
→ Write ADRs for microservices choice
→ Generate API documentation

Phase 10: Review
→ Validate against performance targets (500ms checkout)
→ Review security with OWASP checklist
→ Present to stakeholders
```

### Example 2: Internal Dashboard (Monolith)

```
Phase 1: Requirements
→ Internal users only, 100 users max
→ Data visualization and reporting
→ Integration with existing MySQL database

Phase 2: System Context
→ Users: Analysts, Managers
→ External: MySQL Database, LDAP for auth
→ Scope: Read-only reporting (no data modification)

Phase 3: Pattern Selection
→ Choose Modular Monolith (small team, simple deployment)
→ Layers: API, Business Logic, Data Access, UI

Phase 4: Component Design
→ Components: Auth, Dashboard, Reports, Charts, Export
→ MVC pattern with React frontend

Phase 5: API Design
→ REST API with GraphQL for complex queries
→ Read-only endpoints
→ Excel/PDF export endpoints

Phase 6: Data Design
→ Read from existing MySQL
→ Add PostgreSQL for dashboard metadata
→ Redis for caching report results

Phase 7: Infrastructure
→ Deploy on AWS EC2 with RDS
→ Simple CI/CD with GitHub Actions
→ CloudWatch for monitoring

Phase 8: Security
→ LDAP authentication
→ Role-based access (Analyst, Manager, Admin)
→ Audit logging for compliance

Phase 9: Documentation
→ Create system architecture diagram
→ API documentation for report endpoints
→ User guide for dashboard features

Phase 10: Review
→ Validate performance (reports < 5 seconds)
→ Security review with IT team
→ User acceptance testing
```

---

## Best Practices

### General Guidelines

1. **Iterate, Don't Waterfall**
   - Don't try to complete all phases perfectly before moving on
   - Go through phases quickly first, then iterate
   - Circle back as you learn more

2. **Start Simple**
   - Begin with simplest solution that meets requirements
   - Add complexity only when needed
   - Avoid over-engineering

3. **Document Decisions**
   - Use Architecture Decision Records (ADRs)
   - Explain WHY, not just WHAT
   - Include alternatives considered

4. **Validate Early**
   - Build proof-of-concepts for risky decisions
   - Test critical paths early
   - Get feedback from stakeholders frequently

5. **Think Evolution**
   - Design for change
   - Plan migration paths
   - Consider future scaling

### Working with AI Tools

1. **Be Specific**
   - Provide context about your system
   - Specify constraints and requirements
   - Include scale and performance targets

2. **Iterate**
   - Start with high-level, refine gradually
   - Ask follow-up questions
   - Request alternatives

3. **Validate AI Outputs**
   - Review generated designs critically
   - Check against best practices
   - Validate with team and experts

4. **Combine Phases**
   - Some phases can be done together
   - Small projects may skip some phases
   - Adjust to your project needs

### Common Pitfalls to Avoid

❌ **Over-Architecture**
- Don't design for 1M users if you have 100
- Don't use microservices for small teams
- Don't add complexity without clear benefit

❌ **Under-Architecture**
- Don't ignore non-functional requirements
- Don't skip security considerations
- Don't forget about operations and maintenance

❌ **Ignoring Constraints**
- Team size and skills matter
- Budget and timeline are real constraints
- Existing systems must be considered

❌ **Copying Solutions**
- Netflix architecture doesn't fit everyone
- Consider your specific context
- Understand trade-offs before adopting patterns

✅ **Right-Size Your Architecture**
- Match complexity to actual needs
- Consider team capabilities
- Plan for evolution, not perfection

---

## Phase Customization Guide

### For Small Projects (< 5 developers, < 6 months)

**Focus on:**
- Phase 1: Requirements (lightweight)
- Phase 3: Pattern (probably monolith)
- Phase 5: API Design (simple REST)
- Phase 6: Data Design (single database)
- Phase 9: Documentation (essential diagrams only)

**Skip or simplify:**
- Phase 7: Infrastructure (use PaaS like Heroku)
- Phase 8: Security (use established libraries)
- Phase 10: Review (informal reviews)

### For Medium Projects (5-20 developers, 6-18 months)

**Use all phases but:**
- Phase 1-2: Spend adequate time (1-2 weeks)
- Phase 3: Careful pattern selection
- Phase 4-6: Detailed design needed
- Phase 7: Full infrastructure design
- Phase 8: Comprehensive security review
- Phase 9: Complete documentation
- Phase 10: Formal review process

### For Large/Enterprise Projects (20+ developers, 18+ months)

**All phases with maximum rigor:**
- Phase 1: Formal requirements process (2-4 weeks)
- Phase 2: Detailed system context with all stakeholders
- Phase 3: Multiple pattern evaluations with POCs
- Phase 4: Detailed component design with standards
- Phase 5: API governance and versioning strategy
- Phase 6: Data governance and compliance
- Phase 7: Multi-region infrastructure
- Phase 8: Comprehensive security and compliance
- Phase 9: Architecture review board (ARB)
- Phase 10: Formal sign-offs and approvals

---

## Quick Reference

### Phase Summary

| Phase | Key Question | Primary Output |
|-------|-------------|----------------|
| 1. Requirements | What are we building? | Requirements document |
| 2. System Context | What's the boundary? | Context diagram |
| 3. Pattern Selection | How do we architect it? | Pattern selection + rationale |
| 4. Component Design | What are the parts? | Component diagrams |
| 5. API Design | How do parts communicate? | API specifications |
| 6. Data Design | How do we store data? | Database schema |
| 7. Infrastructure | Where does it run? | Infrastructure diagram |
| 8. Security | How do we secure it? | Security architecture |
| 9. Documentation | How do we explain it? | Complete documentation |
| 10. Review | Is it right? | Review report + sign-off |

### Essential Diagrams by Phase

- **Phase 2**: C4 Context Diagram
- **Phase 3**: Architecture Pattern Diagram
- **Phase 4**: C4 Container Diagram, Component Diagrams
- **Phase 5**: Sequence Diagrams (API flows)
- **Phase 6**: ER Diagram
- **Phase 7**: Infrastructure/Deployment Diagram
- **Phase 8**: Security Architecture Diagram
- **Phase 9**: All diagrams compiled
- **Phase 10**: Review summary diagram

### Time Allocation (Example)

For a typical 12-week architecture design phase:

- Phase 1: 1 week (8%)
- Phase 2: 1 week (8%)
- Phase 3: 1 week (8%)
- Phase 4: 2 weeks (17%)
- Phase 5: 2 weeks (17%)
- Phase 6: 1.5 weeks (12%)
- Phase 7: 1.5 weeks (12%)
- Phase 8: 1 week (8%)
- Phase 9: 1 week (8%)
- Phase 10: 0.5 weeks (4%)

*Adjust based on project complexity and team size*

---

## Resources and Templates

### Related Documentation
- [CLAUDE.md](../CLAUDE.md) - AI assistant guide for this codebase
- [GETTING_STARTED.md](GETTING_STARTED.md) - Setup guide
- [CLAUDE_INTEGRATION.md](CLAUDE_INTEGRATION.md) - Claude AI workflows
- [AI_TOOL_INTEGRATION.md](AI_TOOL_INTEGRATION.md) - Multi-tool integration

### Diagram Tools
- [Mermaid Live Editor](https://mermaid.live/)
- [PlantUML Online](http://www.plantuml.com/plantuml/)
- [Draw.io](https://app.diagrams.net/)
- [C4 Model Tools](https://c4model.com/#tooling)

### Architecture Resources
- [C4 Model](https://c4model.com/)
- [Architecture Decision Records](https://adr.github.io/)
- [Microsoft Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)

### API Design Resources
- [OpenAPI Specification](https://swagger.io/specification/)
- [API Design Guide](https://cloud.google.com/apis/design)
- [REST API Best Practices](https://restfulapi.net/)

---

## Conclusion

This guide provides a comprehensive, phase-based approach to software architecture design. By following these phases and using the provided prompts with AI tools, you can:

✅ Create well-structured architecture designs
✅ Make informed decisions with proper rationale
✅ Produce comprehensive documentation
✅ Validate designs against requirements
✅ Communicate effectively with stakeholders

Remember: **Architecture is about making trade-offs**. There's no perfect architecture, only the right architecture for your specific context, constraints, and requirements.

Start with Phase 1, use the prompts as guides (not rigid scripts), iterate based on what you learn, and always validate your decisions against your specific needs.

Good luck with your architecture design! 🏗️
