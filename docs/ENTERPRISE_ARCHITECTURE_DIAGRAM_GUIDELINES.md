# Enterprise Architecture Diagram Guidelines

Comprehensive standards for creating professional, enterprise-grade architecture diagrams following NashTech best practices and industry standards.

## Table of Contents

- [Overview](#overview)
- [Role and Principles](#role-and-principles)
- [Analysis Framework](#analysis-framework)
- [Diagram Organization](#diagram-organization)
- [Visual Standards](#visual-standards)
- [Component Specifications](#component-specifications)
- [Security Boundaries](#security-boundaries)
- [Technology Stack Labeling](#technology-stack-labeling)
- [Data Flow Specifications](#data-flow-specifications)
- [Legend Requirements](#legend-requirements)
- [Architecture Notes Panel](#architecture-notes-panel)
- [Draw.io XML Format](#drawio-xml-format)
- [Quality Checklist](#quality-checklist)

---

## Overview

### Purpose
Create production-grade enterprise architecture diagrams that demonstrate:
- Superior design thinking and technical expertise
- Comprehensive security implementation
- Scalability and performance optimization
- Cost-awareness and operational excellence
- Clear separation of responsibilities (NashTech vs Client)

### Target Audience
- **Technical Stakeholders**: Architects, developers, DevOps engineers
- **Business Stakeholders**: Project managers, executives
- **Security Teams**: Security architects, compliance officers
- **Operations Teams**: SREs, infrastructure teams

---

## Role and Principles

### Primary Role
**You are a Principal Cloud Architect and Cloud Security Specialist** producing production-grade architectures with clear trade-offs and security-first design.

### Core Principles

#### 1. High Availability by Default
- **Multi-AZ/Multi-Region**: Always design for zone/region failure
- **Redundancy**: No single points of failure
- **Auto-Scaling**: Horizontal scale-out configured by default
- **Health Checks**: Automated monitoring and self-healing

#### 2. Security-First Design
- **Private-by-Default Networking**: No public data-plane access
- **Least Privilege**: Minimal permissions for all components
- **Managed Identities**: No hardcoded credentials
- **Zero Trust Architecture**: Verify everything, trust nothing

#### 3. Observability Built-In
- **Logging**: Application and infrastructure logs
- **Metrics**: Performance and business metrics
- **Traces**: Distributed tracing across services
- **Alerting**: Actionable alerts with clear SLOs
- **Central Platform**: Unified observability platform

#### 4. Disaster Recovery Explicit
- **RTO/RPO Defined**: Clear recovery objectives
- **Backup Strategy**: Automated backups with retention
- **Runbooks**: Documented recovery procedures
- **Testing**: Regular DR drills

#### 5. Cost Awareness
- **Sizing**: Small/Medium/Large tiers documented
- **SKU Selection**: Appropriate instance types
- **Resource Counts**: Explicit instance counts
- **Optimization**: Reserved instances, auto-shutdown

#### 6. Vendor Neutrality
- **No Invention**: Never invent vendor product capabilities
- **Stay Generic**: Unless user names specific cloud/service
- **Standards-Based**: Use open standards where possible

---

## Analysis Framework

### 1. Deep Requirements Analysis

#### Functional Requirements
Extract from client documents:
- **User Journeys**: End-to-end user workflows
- **Business Processes**: Core business logic and rules
- **Data Flows**: How data moves through the system
- **Integration Touchpoints**: External system connections

**Analysis Questions:**
- What are the primary user types and their workflows?
- What business processes must the system support?
- What data needs to flow between components?
- What external systems require integration?

#### Non-Functional Requirements
Extract from client documents:
- **Performance Metrics**: Response times, throughput, latency
- **Security Compliance**: GDPR, SOX, HIPAA, PCI-DSS, ISO 27001
- **Scalability Targets**: User growth, data volume, transaction rates
- **Availability SLAs**: Uptime requirements, RTO/RPO

**Analysis Questions:**
- What are the performance targets (response time, throughput)?
- What compliance requirements must be met?
- What is the expected growth trajectory?
- What is the acceptable downtime?

#### Stakeholder Mapping
Identify all stakeholders:
- **User Types**: End users, administrators, auditors
- **Access Patterns**: How each user type interacts
- **Privilege Levels**: Read-only, read-write, admin
- **Geographic Distribution**: Where users are located

#### Volume Analysis
Quantify system load:
- **Transaction Volumes**: Requests/second, transactions/day
- **Concurrent Users**: Peak and average concurrent users
- **Data Growth**: Current size, growth rate, projections
- **Peak Load**: Seasonal or event-driven peaks

#### Integration Landscape
Map all integrations:
- **Existing Systems**: Legacy systems requiring integration
- **External APIs**: Third-party service dependencies
- **Data Sources**: Where data originates
- **Compliance Requirements**: Data residency, encryption

### 2. Security-First Architecture Assessment

#### Threat Modeling
Identify security risks:
- **Attack Vectors**: How could the system be compromised?
- **Data Classification**: Public, internal, confidential, restricted
- **Compliance Requirements**: GDPR, HIPAA, PCI-DSS, SOC 2

**STRIDE Analysis:**
- **S**poofing: Identity verification mechanisms
- **T**ampering: Data integrity protection
- **R**epudiation: Audit logging and non-repudiation
- **I**nformation Disclosure: Encryption and access controls
- **D**enial of Service**: Rate limiting and DDoS protection
- **E**levation of Privilege**: RBAC and least privilege

#### Zero Trust Principles
Implement zero trust:
- **Identity Verification**: Multi-factor authentication
- **Least Privilege Access**: Role-based access control
- **Network Segmentation**: Security zones and micro-segmentation
- **Assume Breach**: Defense in depth

#### Data Protection Strategy
Protect data at all stages:
- **Encryption at Rest**: AES-256 for stored data
- **Encryption in Transit**: TLS 1.3 for network traffic
- **Key Management**: Hardware Security Module (HSM) or cloud KMS
- **Data Residency**: Geographic restrictions for compliance

#### Compliance Mapping
Map requirements to controls:
- **Regulatory Requirements**: Specific regulations (GDPR Article 32, HIPAA §164.312)
- **Security Controls**: Technical controls implementing requirements
- **Audit Trails**: Logging for compliance verification
- **Data Governance**: Policies and procedures

### 3. Multi-Alternative Solution Design

#### Option A: Cloud-Native Microservices
**Approach**: Full PaaS adoption with managed services
**Pros**: Minimal operational overhead, auto-scaling, managed updates
**Cons**: Potential vendor lock-in, higher ongoing costs
**Best For**: Greenfield projects, rapid development

#### Option B: Hybrid Architecture
**Approach**: Cloud services with on-premises integration
**Pros**: Leverage existing infrastructure, gradual migration
**Cons**: Complex networking, dual management overhead
**Best For**: Legacy modernization, regulated industries

#### Option C: Multi-Cloud / Edge Computing
**Approach**: Distribute across multiple clouds or edge locations
**Pros**: Vendor independence, geographic distribution
**Cons**: Increased complexity, cross-cloud networking costs
**Best For**: Global scale, disaster recovery requirements

#### Trade-off Analysis Framework
Evaluate each option:
| Criteria | Option A | Option B | Option C |
|----------|----------|----------|----------|
| **Cost** | High ongoing, low upfront | Medium ongoing, high upfront | Very high ongoing |
| **Complexity** | Low | High | Very high |
| **Performance** | Good | Excellent (for on-prem data) | Excellent (for edge) |
| **Security** | Good (if configured) | Excellent (for sensitive data) | Complex |
| **Vendor Lock-in** | High | Medium | Low |
| **Time to Market** | Fast | Slow | Very slow |

---

## Diagram Organization

### Zone-Based Architecture (NOT Layers)

Traditional layered architecture is replaced with **security zone-based organization**.

#### Subscription/Tenant Structure
```
Corporate Tenant
├── Production Subscription
│   ├── Compute Resources
│   ├── Data Resources
│   └── Networking Resources
├── Non-Production Subscription
│   ├── Development Environment
│   ├── Testing Environment
│   └── UAT Environment
├── Security & Compliance Subscription
│   ├── Security Monitoring (SIEM)
│   ├── Key Vault
│   └── Backup Vault
└── Shared Services Subscription
    ├── Active Directory
    ├── Monitoring Platform
    └── CI/CD Infrastructure
```

#### Network Segmentation Zones

##### 1. Internet/Edge Zone
**Purpose**: Public-facing services and content delivery
**Components**:
- Content Delivery Network (CDN)
- Web Application Firewall (WAF)
- DDoS Protection
- Public DNS

**Security Controls**:
- Rate limiting (1000 req/min per IP)
- Geo-blocking (block high-risk countries)
- SSL/TLS termination (TLS 1.3 only)
- Bot protection

**Data Flows**:
- Incoming: HTTPS (443) from internet
- Outgoing: HTTPS to internal load balancer

##### 2. DMZ/Perimeter Zone
**Purpose**: Controlled entry point for external traffic
**Components**:
- Application Gateway / Load Balancer
- API Gateway
- Reverse Proxy
- Public-facing endpoints

**Security Controls**:
- Network Security Groups (NSGs)
- Authentication (OAuth 2.0, JWT)
- Authorization checks
- Traffic inspection

**Data Flows**:
- Incoming: From Internet/Edge zone
- Outgoing: To Application zone (internal only)

##### 3. Application Zone
**Purpose**: Business logic and application services
**Components**:
- Microservices (containerized)
- Application servers
- Message queues
- Cache layer

**Security Controls**:
- Private endpoints (no public access)
- Service-to-service authentication (mTLS)
- API security (rate limiting, validation)
- Network policies (Kubernetes NetworkPolicies)

**Data Flows**:
- Incoming: From DMZ zone
- Outgoing: To Data zone, Integration zone
- Internal: Service mesh communication

##### 4. Data Zone
**Purpose**: Data storage and processing
**Components**:
- Databases (SQL, NoSQL)
- Data lakes
- Analytics services
- Backup systems

**Security Controls**:
- Private Link (no internet access)
- Encryption at rest (AES-256, TDE)
- Column-level encryption for PII
- Access policies (RBAC)
- Audit logging (all queries logged)

**Data Flows**:
- Incoming: From Application zone only
- Outgoing: Backup to secondary region
- No direct internet access

##### 5. Management Zone
**Purpose**: Administrative and operational tools
**Components**:
- Monitoring platform (Azure Monitor, Prometheus)
- Log aggregation (ELK Stack, Splunk)
- CI/CD pipelines
- Administrative bastion hosts
- Key Vault / Secrets management

**Security Controls**:
- Azure AD Privileged Identity Management (PIM)
- Conditional access policies
- Just-in-time (JIT) access
- Multi-factor authentication mandatory

**Data Flows**:
- Monitoring data from all zones
- Deployment artifacts to Application zone
- Encrypted secrets distribution

##### 6. Integration Zone
**Purpose**: External system connectivity
**Components**:
- API connectors to external systems
- Message brokers (Kafka, RabbitMQ)
- Event hubs
- ETL/data sync services

**Security Controls**:
- Mutual TLS for external connections
- API key rotation (90 days)
- Network egress filtering
- Payload encryption

**Data Flows**:
- Incoming: From external partners (HTTPS, SFTP)
- Outgoing: To external APIs (authenticated)
- Internal: To Application zone via message queue

---

## Visual Standards

### Color Coding Schema

Use consistent colors to indicate component types and ownership:

#### Component Colors
- **🟠 Orange (#FF6B35)**: New/Proposed services (NashTech scope)
  - Use for: All components being built as part of this project
  - Example: New microservices, new databases, new APIs

- **🔵 Blue (#74B9FF)**: Existing systems (client's legacy/current)
  - Use for: Systems that already exist and will be integrated
  - Example: Legacy ERP, existing CRM, on-premises databases

- **🟢 Green (#00B894)**: External/3rd party services
  - Use for: Services not controlled by client or NashTech
  - Example: Payment gateways, email services, cloud provider services

- **🟡 Yellow (#FDCB6E)**: Security controls and boundaries
  - Use for: Firewalls, WAF, load balancers, security groups
  - Example: Azure Firewall, Network Security Groups, API Gateway

- **🟣 Purple (#A29BFE)**: Data storage and processing
  - Use for: All data-related components
  - Example: Databases, data lakes, caches, backups

- **🔴 Red (#E17055)**: Critical/high-security components
  - Use for: Components requiring special security attention
  - Example: Payment processing, PII storage, authentication services

#### Fill and Border
- **Fill**: Use 20% opacity of the base color
- **Border**: Use 100% opacity of the base color (3px width)
- **Text**: Use dark gray (#2D3436) for readability

### Arrow Flow Specifications

#### Arrow Types and Meanings
- **Solid Blue Arrows (3px)**: User-initiated traffic
  - Protocol: HTTPS/TLS 1.3
  - Example: User browser → Load balancer
  - Label: "HTTPS (443)"

- **Dashed Green Arrows (2px)**: API integrations
  - Protocol: REST, GraphQL, gRPC
  - Authentication: OAuth 2.0, JWT
  - Example: Service A → Service B
  - Label: "REST API (OAuth 2.0)"

- **Solid Purple Arrows (3px)**: Database connections
  - Protocol: Encrypted database protocol (TLS)
  - Example: Application → Database
  - Label: "PostgreSQL (TLS)"

- **Dotted Orange Arrows (2px)**: Monitoring and logging
  - Protocol: Various (HTTPS, syslog, etc.)
  - Example: Service → Monitoring platform
  - Label: "Metrics/Logs"

- **Solid Red Arrows (4px)**: Critical security flows
  - Protocol: Varies (always encrypted)
  - Example: Service → Key Vault, MFA flow
  - Label: "Key retrieval (mTLS)"

- **Dashed Yellow Arrows (2px)**: Management/administrative
  - Protocol: SSH, RDP, HTTPS
  - Example: Admin → Bastion host
  - Label: "Admin access (SSH + MFA)"

#### Arrow Labels
Always label arrows with:
1. **Protocol**: What protocol is used
2. **Port** (if applicable): Which port
3. **Authentication** (if applicable): How it's secured
4. **Data Type** (if applicable): What data flows

**Examples**:
- "HTTPS (443) - TLS 1.3"
- "PostgreSQL (5432) - TLS + cert auth"
- "REST API - OAuth 2.0 JWT"
- "Event Stream - Kafka (SSL)"

### Security Boundary Styles

#### Boundary Line Types
- **Solid Line (3px, Yellow)**: Hard security boundaries
  - Use for: Firewalls, WAF, Network Security Groups
  - Example: Internet → DMZ boundary

- **Dashed Line (3px, Yellow)**: Soft security boundaries
  - Use for: Logical separation, subnet boundaries
  - Example: Application subnet → Data subnet

- **Double Line (2px, Red)**: Compliance boundaries
  - Use for: PCI zones, HIPAA zones, GDPR-sensitive areas
  - Example: Payment processing zone

- **Dotted Line (2px, Gray)**: Administrative boundaries
  - Use for: Resource groups, subscriptions, projects
  - Example: Subscription A boundary

#### Security Zone Shading
- Use subtle background shading for security zones
- 5% opacity of zone color
- Helps visually group related components

---

## Component Specifications

### Detailed Component Breakdown

Each component in the diagram must include:

#### Component Structure
```
┌─────────────────────────┐
│  Component Name         │ ← Title (14pt, bold)
├─────────────────────────┤
│  Icon                   │ ← Technology icon (32x32px)
├─────────────────────────┤
│  Technology Stack       │ ← e.g., "Node.js 18 + Express"
│  Deployment Target      │ ← e.g., "AKS (3-10 pods)"
│  Specifications         │ ← e.g., "4 vCPU, 16 GB RAM"
└─────────────────────────┘
```

#### Example: Complete Component Specification

**Frontend Web Application**
```xml
Component: Web Application
├── Technology: React 18.2 + TypeScript 5.0
├── Build Tool: Vite 4.0
├── Hosting: Azure Static Web Apps
├── CDN: Azure Front Door Premium
├── Specifications:
│   ├── Bundle Size: < 500 KB (gzipped)
│   ├── Performance: Lighthouse score > 90
│   ├── Browsers: Chrome 90+, Firefox 88+, Safari 14+
│   └── Responsive: Mobile-first, 320px - 2560px
└── Security:
    ├── CSP: Content Security Policy enabled
    ├── HTTPS: Enforced with HSTS
    └── Authentication: OAuth 2.0 PKCE flow
```

**Backend Microservice**
```xml
Component: Order Service
├── Technology: Java 17 + Spring Boot 3.1
├── Framework: Spring Cloud
├── Deployment: Azure Kubernetes Service (AKS)
├── Container: Docker (multi-stage build)
├── Specifications:
│   ├── Pods: Min 3, Max 10 (auto-scale)
│   ├── Resources: 2 vCPU, 4 GB RAM per pod
│   ├── Storage: 10 GB SSD per pod
│   └── Health: /actuator/health endpoint
├── Database: PostgreSQL 15 (Azure Database)
├── Cache: Redis 7.0 (Azure Cache)
└── Security:
    ├── Authentication: JWT tokens (1hr expiry)
    ├── Authorization: RBAC via Spring Security
    ├── Secrets: Azure Key Vault integration
    └── Network: Private endpoint only
```

**Database**
```xml
Component: Primary Database
├── Technology: PostgreSQL 15.2
├── Hosting: Azure Database for PostgreSQL
├── Tier: Business Critical (99.99% SLA)
├── Specifications:
│   ├── vCores: 8 vCores (Gen 5)
│   ├── Memory: 32 GB RAM
│   ├── Storage: 1 TB SSD (auto-grow enabled)
│   ├── IOPS: 20,000 read / 5,000 write
│   └── Connections: Max 500 concurrent
├── High Availability:
│   ├── Multi-AZ: 3 availability zones
│   ├── Replication: Synchronous to standby
│   ├── Failover: Automatic (< 60 seconds)
│   └── Read Replicas: 2 replicas (read scaling)
├── Backup:
│   ├── Automated: Hourly snapshots
│   ├── Retention: 30 days point-in-time restore
│   ├── Geo-Redundant: Replicated to paired region
│   └── RPO: 15 minutes, RTO: 1 hour
└── Security:
    ├── Encryption: TDE (Transparent Data Encryption)
    ├── Column Encryption: Always Encrypted for PII
    ├── Network: Private Link (no public access)
    ├── Firewall: IP whitelisting enabled
    └── Auditing: All queries logged to Log Analytics
```

### Zone-Based Component Organization

#### Example: Multi-AZ Application Zone

```
┌─ Availability Zone A (us-east-1a) ─────────────┐
│                                                 │
│ Frontend Services:                              │
│ ├── Web App (React SPA) - Node.js 18           │
│ │   ├── 3 pods (2 vCPU, 4 GB each)            │
│ │   └── CDN: CloudFront                        │
│ └── Admin Portal (Angular) - TypeScript        │
│     ├── 2 pods (2 vCPU, 4 GB each)            │
│     └── Auth: Azure AD B2C                     │
│                                                 │
│ Application Services:                           │
│ ├── User Service (.NET 8.0)                    │
│ │   ├── 5 pods (4 vCPU, 8 GB each)            │
│ │   └── DB: Azure SQL (S3, 100 DTU)           │
│ ├── Order Service (Java 17 + Spring)          │
│ │   ├── 5 pods (2 vCPU, 4 GB each)            │
│ │   └── DB: PostgreSQL (P2, 250 DTU)          │
│ └── Payment Service (Python 3.11 + FastAPI)   │
│     ├── 3 pods (2 vCPU, 4 GB each)            │
│     └── PCI DSS compliant zone                │
│                                                 │
│ Infrastructure Services:                        │
│ ├── API Gateway (Kong) - 3 instances           │
│ ├── Service Mesh (Istio 1.19) - mTLS enabled  │
│ ├── Container Registry (ACR) - Premium         │
│ └── Secrets (Key Vault) - HSM protected        │
│                                                 │
│ Data Access Layer:                              │
│ ├── Connection Pool (PgBouncer) - 3 instances  │
│ ├── Cache (Redis Cluster) - 3 nodes            │
│ └── Search (Elasticsearch) - 3 nodes           │
│                                                 │
└─────────────────────────────────────────────────┘

[Identical structure repeated for Zones B and C]
```

---

## Security Boundaries

### Boundary Specifications

Each security boundary must clearly define:

#### 1. Internet Boundary

**Components**:
- Azure Front Door Premium
- Web Application Firewall (WAF)
- DDoS Protection Standard

**Security Controls**:
- **Rate Limiting**: 1000 requests/minute per IP
- **Geo-Blocking**: Block traffic from high-risk countries
- **SSL Termination**: TLS 1.3 only, strong cipher suites
- **Bot Protection**: Challenge-response for suspicious traffic
- **IP Reputation**: Block known malicious IPs

**Data Flows**:
- **Incoming**: HTTPS (443) from internet
- **Outgoing**: HTTPS to DMZ load balancer (internal)
- **Logging**: All requests logged to SIEM

#### 2. Perimeter Boundary

**Components**:
- Application Gateway (Layer 7)
- Network Security Groups (NSGs)
- Azure Firewall (if needed)

**Security Controls**:
- **Authentication**: OAuth 2.0 token validation
- **Authorization**: Role-based access control (RBAC)
- **Traffic Inspection**: Deep packet inspection
- **Certificate Validation**: Mutual TLS for B2B
- **Request Validation**: JSON schema validation

**Data Flows**:
- **Incoming**: From Internet boundary (load-balanced)
- **Outgoing**: To Application zone (authenticated)
- **Health Checks**: Every 10 seconds

#### 3. Application Boundary

**Components**:
- Private Endpoints
- Service Endpoints
- VNet Integration

**Security Controls**:
- **Micro-Segmentation**: Kubernetes NetworkPolicies
- **Service Mesh**: Istio with mTLS
- **API Security**: Rate limiting (100 req/sec per user)
- **Input Validation**: All API inputs validated
- **Output Encoding**: XSS prevention

**Data Flows**:
- **Incoming**: From Perimeter boundary
- **Outgoing**: To Data zone (encrypted)
- **Service-to-Service**: mTLS with cert rotation

#### 4. Data Boundary

**Components**:
- Private Link
- Always Encrypted
- Transparent Data Encryption (TDE)

**Security Controls**:
- **Encryption at Rest**: AES-256 (TDE enabled)
- **Encryption in Transit**: TLS 1.3 for all connections
- **Column-Level Encryption**: Always Encrypted for PII fields
- **Access Policies**: RBAC with least privilege
- **Audit Logging**: All data access logged

**Data Flows**:
- **Incoming**: From Application zone only (private endpoint)
- **Outgoing**: Backup to geo-redundant storage
- **No Internet Access**: Air-gapped from internet

#### 5. Management Boundary

**Components**:
- Azure Monitor
- Log Analytics Workspace
- Azure Key Vault
- Azure AD Privileged Identity Management (PIM)

**Security Controls**:
- **RBAC**: Role-based access control
- **Conditional Access**: MFA + device compliance required
- **Privileged Access Management**: Just-in-time (JIT) access
- **Activity Logging**: All administrative actions logged
- **Secret Rotation**: Automatic rotation every 90 days

**Data Flows**:
- **Monitoring Data**: From all zones to central platform
- **Configuration**: To all zones (encrypted)
- **Alerts**: To operations team (email, SMS, Teams)

---

## Technology Stack Labeling

### Labeling Standards

Every component in the architecture diagram must display:

#### Component Label Format

```
┌────────────────────────────────┐
│  [Component Name]              │  ← Primary name (16pt bold)
├────────────────────────────────┤
│  [Icon]                        │  ← Technology icon (32x32px)
├────────────────────────────────┤
│  Tech: [Stack]                 │  ← e.g., "Node.js 18 + Express"
│  Deploy: [Target]              │  ← e.g., "AKS (3-10 pods)"
│  Spec: [Size]                  │  ← e.g., "4 vCPU, 16 GB RAM"
└────────────────────────────────┘
```

### Technology Stack Examples

#### Frontend Components

**React Single Page Application**
```
Component: Web Application
Tech: React 18.2 + TypeScript 5.0
Build: Vite 4.0 + ESLint + Prettier
Deploy: Azure Static Web Apps + CDN
Spec: Serverless, < 500 KB bundle (gzipped)
Browsers: Chrome 90+, Firefox 88+, Safari 14+
```

**Angular Enterprise Application**
```
Component: Admin Portal
Tech: Angular 16 + TypeScript 5.0
Build: Angular CLI + Webpack 5
Deploy: Azure App Service (Linux)
Spec: 2 instances, 4 vCPU, 8 GB RAM each
Auth: Microsoft Entra ID (Azure AD)
```

#### Backend Components

**Node.js Microservice**
```
Component: User Service
Tech: Node.js 18 LTS + Express 4.18
Language: TypeScript 5.0
Framework: NestJS 10.0
Deploy: Azure Kubernetes Service (AKS)
Spec: 3-10 pods, 2 vCPU, 4 GB RAM per pod
Database: PostgreSQL 15 (Azure Database)
Cache: Redis 7.0 (Azure Cache)
```

**Java Spring Boot Service**
```
Component: Order Processing Service
Tech: Java 17 + Spring Boot 3.1
Framework: Spring Cloud 2022.0.4
Deploy: Amazon EKS
Spec: 5-15 pods, 4 vCPU, 8 GB RAM per pod
Database: PostgreSQL 15 (RDS Multi-AZ)
Messaging: Apache Kafka 3.5
```

**.NET Core Service**
```
Component: Payment Service
Tech: .NET 8.0 + C# 12
Framework: ASP.NET Core Web API
Deploy: Azure App Service (Windows)
Spec: P3v3 tier, 4 instances (auto-scale)
Database: Azure SQL Database (P4)
Compliance: PCI DSS v4.0
```

**Python FastAPI Service**
```
Component: Analytics Engine
Tech: Python 3.11 + FastAPI 0.104
Data: Pandas 2.1, NumPy 1.26
Deploy: AWS Fargate
Spec: 4 vCPU, 16 GB RAM, GPU (optional)
Database: MongoDB 7.0 (DocumentDB)
Queue: AWS SQS
```

#### Database Components

**PostgreSQL (Managed)**
```
Component: Primary Database
Tech: PostgreSQL 15.2
Hosting: Azure Database for PostgreSQL
Tier: Business Critical (99.99% SLA)
Spec: 8 vCores (Gen 5), 32 GB RAM
Storage: 1 TB SSD (auto-grow enabled)
IOPS: 20,000 read / 5,000 write
Max Connections: 500 concurrent
Replication: Multi-AZ synchronous
Backup: Hourly (30-day retention)
Encryption: TDE + Always Encrypted for PII
```

**MongoDB (Managed)**
```
Component: Document Store
Tech: MongoDB 7.0 Enterprise
Hosting: MongoDB Atlas (AWS)
Tier: M60 (Dedicated cluster)
Spec: 64 GB RAM, 1.6 TB SSD
Sharding: 3 shards, 3 replicas per shard
Backup: Continuous (PITR 7 days)
Encryption: At rest (AES-256), In transit (TLS 1.3)
```

**Redis Cache Cluster**
```
Component: Distributed Cache
Tech: Redis 7.0 Enterprise
Hosting: Azure Cache for Redis
Tier: Premium P4 (26 GB)
Topology: 3-node cluster
Eviction: LRU (least recently used)
Persistence: AOF (append-only file)
Replication: Active-passive
Failover: Automatic (< 60 seconds)
```

#### Message Brokers

**Apache Kafka**
```
Component: Event Streaming Platform
Tech: Apache Kafka 3.5
Hosting: Confluent Cloud / AWS MSK
Spec: 6 brokers, m5.2xlarge
Storage: 2 TB SSD per broker
Partitions: 100 per topic
Replication Factor: 3
Retention: 7 days (configurable)
Throughput: 500 MB/sec write, 1 GB/sec read
```

**RabbitMQ**
```
Component: Message Queue
Tech: RabbitMQ 3.12
Hosting: Self-managed on AKS
Spec: 3 nodes, 4 vCPU, 16 GB RAM each
Clustering: Mirrored queues across 3 nodes
Throughput: 50,000 messages/sec
Persistence: Durable queues to disk
Monitoring: Prometheus + Grafana
```

#### Load Balancers & API Gateways

**Azure Application Gateway**
```
Component: Application Load Balancer
Tech: Azure Application Gateway v2
WAF: Enabled (OWASP 3.2 ruleset)
Capacity: 10 capacity units (auto-scale)
SSL: TLS 1.3 termination
Features: URL routing, session affinity, health probes
Zones: Multi-AZ (Zone-redundant)
```

**Kong API Gateway**
```
Component: API Gateway
Tech: Kong Gateway 3.4 Enterprise
Deploy: Kubernetes (6 pods)
Spec: 2 vCPU, 4 GB RAM per pod
Plugins: OAuth 2.0, rate limiting, caching, CORS
Database: PostgreSQL (control plane)
Throughput: 100,000 requests/sec
```

#### Observability Components

**Monitoring Stack**
```
Component: Monitoring Platform
Metrics: Prometheus 2.47
Visualization: Grafana 10.1
Alerts: Alertmanager 0.26
Spec: 16 vCPU, 64 GB RAM
Retention: 90 days (metrics), 180 days (logs)
Storage: 5 TB SSD
```

**Logging Stack (ELK)**
```
Component: Centralized Logging
Elasticsearch: 8.10
Logstash: 8.10
Kibana: 8.10
Filebeat: 8.10
Spec: 9 ES nodes (3 master, 6 data), m5.2xlarge
Storage: 20 TB SSD (hot), 100 TB S3 (warm/cold)
Retention: 90 days hot, 7 years total
Ingestion: 50 GB/day
```

---

## Data Flow Specifications

### Arrow Labeling Requirements

Every arrow (data flow) in the architecture diagram must include:

#### Mandatory Arrow Labels

1. **Protocol**: HTTP, HTTPS, WebSocket, gRPC, Kafka, AMQP, etc.
2. **Port** (if applicable): 443, 5432, 6379, etc.
3. **Authentication Method**: OAuth 2.0, JWT, mTLS, API key, etc.
4. **Data Type** (optional): JSON, Protobuf, Avro, XML, etc.

#### Arrow Label Format

```
Protocol (Port) - Auth
e.g., "HTTPS (443) - OAuth 2.0 JWT"
e.g., "PostgreSQL (5432) - TLS + cert auth"
e.g., "Kafka - mTLS"
```

### Data Flow Categories

#### 1. User Traffic Flows

**Web Application Traffic**
```
User Browser → CDN
  Label: "HTTPS (443) - TLS 1.3"

CDN → Load Balancer
  Label: "HTTPS (443) - Internal"

Load Balancer → Web App
  Label: "HTTPS (8443) - OAuth 2.0"
```

**Mobile Application Traffic**
```
Mobile App → API Gateway
  Label: "HTTPS (443) - JWT (Bearer Token)"
  Data: JSON payloads (REST API)

API Gateway → Backend Services
  Label: "gRPC - mTLS"
  Data: Protocol Buffers
```

#### 2. Service-to-Service Communication

**Synchronous (REST)**
```
Service A → Service B
  Label: "HTTPS (8443) - JWT + mTLS"
  Pattern: Request-Response
  Timeout: 5 seconds
  Retry: 3 attempts with exponential backoff
```

**Synchronous (gRPC)**
```
Service A → Service B
  Label: "gRPC (50051) - mTLS"
  Pattern: Request-Response, Streaming
  Data: Protocol Buffers
  Load Balancing: Client-side (round robin)
```

**Asynchronous (Messaging)**
```
Service A → Message Queue → Service B
  Publish: "AMQP (5672) - TLS"
  Consume: "AMQP (5672) - TLS"
  Pattern: Publish-Subscribe
  Message Format: JSON
  Retry: Dead letter queue after 3 failures
```

**Event Streaming**
```
Service A → Kafka Topic → Service B
  Label: "Kafka - SASL_SSL"
  Topic: "order.created"
  Partitions: 10
  Replication: 3
  Format: Avro (Schema Registry)
```

#### 3. Database Access Flows

**Application to Database**
```
Application → Database
  Label: "PostgreSQL (5432) - TLS 1.3 + password"
  Connection Pool: Max 100 connections
  Timeout: 30 seconds
```

**Application to Cache**
```
Application → Redis Cache
  Label: "Redis (6379) - TLS + password"
  Pattern: Cache-aside
  TTL: 1 hour (default)
```

**Database Replication**
```
Primary DB → Read Replica
  Label: "PostgreSQL Streaming Replication"
  Mode: Asynchronous
  Lag: < 100ms (target)
```

#### 4. External Integration Flows

**Third-Party API Calls**
```
Service → Payment Gateway
  Label: "HTTPS (443) - API Key + OAuth 2.0"
  Rate Limit: 100 requests/minute
  Timeout: 10 seconds
  Retry: 3 attempts
  Circuit Breaker: Open after 5 failures
```

**Webhook Callbacks**
```
External Service → API Endpoint
  Label: "HTTPS (443) - HMAC signature"
  Validation: Verify signature + timestamp
  Retry: Exponential backoff (by external service)
```

**File Transfer**
```
Service → SFTP Server
  Label: "SFTP (22) - SSH key auth"
  Encryption: AES-256
  Schedule: Daily at 2 AM
```

#### 5. Monitoring & Logging Flows

**Application Logs**
```
Application → Log Aggregator
  Label: "Syslog over TLS (514)"
  Format: JSON structured logs
  Volume: 10 GB/day
```

**Metrics Collection**
```
Application → Prometheus
  Label: "HTTP (9090) - Pull model"
  Scrape Interval: 15 seconds
  Metrics: Counters, Gauges, Histograms
```

**Distributed Tracing**
```
Application → Tracing Backend (Jaeger)
  Label: "HTTP (14268) - Thrift over HTTP"
  Sampling: 10% of requests
  Retention: 7 days
```

#### 6. Backup & Disaster Recovery Flows

**Database Backup**
```
Database → Backup Storage
  Label: "Encrypted backup stream"
  Frequency: Hourly snapshots
  Encryption: AES-256
  Location: Geo-redundant storage (paired region)
```

**Cross-Region Replication**
```
Primary Region → Secondary Region
  Label: "Geo-replication (async)"
  RPO: 15 minutes
  RTO: 1 hour
  Bandwidth: 1 Gbps dedicated
```

---

## Legend Requirements

### Mandatory Legend Elements

Every architecture diagram must include a comprehensive legend showing:

#### Complete Legend Structure

```
┌─────────────────────────────────────────────────┐
│                    LEGEND                       │
├─────────────────────────────────────────────────┤
│                                                 │
│  Component Types (by color):                    │
│  🟠 Orange: New/Proposed (NashTech scope)      │
│  🔵 Blue: Existing systems (client legacy)     │
│  🟢 Green: External/3rd party services         │
│  🟡 Yellow: Security controls                  │
│  🟣 Purple: Data storage                       │
│  🔴 Red: Critical/high-security components     │
│                                                 │
│  Arrow Types:                                   │
│  ───────▶ Solid Blue: User traffic (HTTPS)    │
│  - - - ▶ Dashed Green: API integrations       │
│  ━━━━━▶ Solid Purple: Database connections    │
│  ······▶ Dotted Orange: Monitoring/logging     │
│  ═══════▶ Solid Red: Critical security flows  │
│  - - - ▶ Dashed Yellow: Admin/management      │
│                                                 │
│  Security Boundaries:                           │
│  ▬▬▬▬▬ Solid (Yellow): Hard boundary (firewall)│
│  ▭▭▭▭▭ Dashed (Yellow): Soft boundary (subnet) │
│  ▬▬▬▬▬ Double (Red): Compliance zone (PCI/HIPAA)│
│  ▭▭▭▭▭ Dotted (Gray): Administrative boundary  │
│                                                 │
│  Infrastructure Zones:                          │
│  🌐 Internet/Edge Zone                         │
│  🛡️ DMZ/Perimeter Zone                         │
│  ⚙️ Application Zone                           │
│  💾 Data Zone                                  │
│  🔧 Management Zone                            │
│  🔗 Integration Zone                           │
│                                                 │
│  Deployment Information:                        │
│  AZ: Availability Zone                          │
│  Multi-AZ: Deployed across 3 zones             │
│  vCPU: Virtual CPU cores                       │
│  GB: Gigabytes of RAM                          │
│  TB: Terabytes of storage                      │
│  IOPS: Input/Output Operations Per Second      │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Technology Icons

Use official technology icons when available:

| Technology | Icon Source |
|------------|------------|
| **AWS Services** | AWS Architecture Icons (official) |
| **Azure Services** | Azure Architecture Icons (official) |
| **Google Cloud** | GCP Architecture Icons (official) |
| **Kubernetes** | CNCF Landscape icons |
| **Databases** | Database vendor official icons |
| **Languages** | Official language logos |

---

## Architecture Notes Panel

### Required Notes Sections

Include an "Architecture Notes" panel in the diagram with:

#### 1. Performance Specifications

```
PERFORMANCE SPECIFICATIONS
─────────────────────────────
Response Time Targets:
• Web Page Load (FCP): < 1.5 seconds
• API Response (p95): < 500 ms
• Search Query: < 2 seconds
• Report Generation: < 30 seconds

Throughput Targets:
• API Requests: 50,000 req/min
• Database Transactions: 10,000 TPS
• Message Processing: 100,000 msg/sec

Concurrent Users:
• Year 1: 1,000 users
• Year 2: 5,000 users
• Year 3: 10,000 users

Data Volume:
• Database: 500 GB → 5 TB (3 years)
• Storage: 2 TB → 20 TB (3 years)
• Daily Ingestion: 10 GB/day
```

#### 2. Security & Compliance

```
SECURITY & COMPLIANCE
─────────────────────────────
Security Level: NashTech Advanced

Compliance Requirements:
• GDPR: EU data residency, encryption
• SOC 2 Type II: Annual audit
• ISO 27001: ISMS certification
• [Industry-specific: PCI DSS, HIPAA, etc.]

Encryption:
• Data at Rest: AES-256 (TDE)
• Data in Transit: TLS 1.3
• Key Management: Azure Key Vault (HSM)

Authentication:
• Method: OAuth 2.0 + OpenID Connect
• Provider: Microsoft Entra ID (Azure AD)
• MFA: Required for admin/privileged access

Network Security:
• All data plane: Private endpoints only
• WAF: OWASP ModSecurity CRS 3.2
• DDoS Protection: Azure DDoS Standard
• Network Segmentation: 6 security zones
```

#### 3. High Availability & DR

```
HIGH AVAILABILITY & DR
─────────────────────────────
SLA Commitment: 99.9% uptime
Allowed Downtime: 8.76 hours/year (43.8 min/month)

Multi-AZ Deployment:
• Application: 3 availability zones
• Database: Multi-AZ with auto-failover
• Load Balancer: Zone-redundant

Auto-Scaling:
• Min Instances: 3 per service
• Max Instances: 20 per service
• Scale-out Trigger: CPU > 70% OR Requests > 1000/sec
• Scale-in Trigger: CPU < 30% for 10 minutes

Disaster Recovery:
• RTO (Recovery Time): 1 hour
• RPO (Recovery Point): 15 minutes
• Backup Frequency: Hourly snapshots
• DR Region: [Paired region]
• DR Testing: Quarterly failover drills
```

#### 4. Cost Estimates

```
COST ESTIMATES (Monthly)
─────────────────────────────
Development Environment: $3,000
• Compute: $1,500
• Database: $800
• Storage: $400
• Networking: $300

Production Environment: $15,000
• Compute (AKS/EKS): $6,000
• Database (Multi-AZ): $4,000
• Storage (Geo-redundant): $2,000
• Load Balancing: $1,000
• Monitoring: $800
• Backup: $700
• Networking: $500

Annual Infrastructure Cost: $216,000

Cost Optimization:
• Reserved Instances: 30% savings
• Auto-scaling: Reduce off-peak costs
• Storage tiering: Hot/Cool/Archive
```

---

## Draw.io XML Format

### Draw.io Best Practices

When creating architecture diagrams in Draw.io:

#### 1. Use Libraries

**Load Architecture Libraries:**
- AWS Architecture 2023
- Azure Architecture 2023
- Google Cloud Platform
- Kubernetes
- Network Diagrams

#### 2. Styling Guidelines

**Component Boxes:**
- Shape: Rectangle with rounded corners (10px radius)
- Border: 3px solid line
- Fill: 20% opacity of category color
- Font: Arial 12pt for labels, Arial 10pt for specs
- Padding: 10px internal padding

**Arrows:**
- Style: Use connector arrows (not lines)
- Width: 2-4px depending on importance
- Arrow head: Standard filled arrow
- Labels: 9pt font, white background with 2px padding

**Colors:**
Use hex values for consistency:
- Orange (New): #FF6B35
- Blue (Existing): #74B9FF
- Green (3rd Party): #00B894
- Yellow (Security): #FDCB6E
- Purple (Data): #A29BFE
- Red (Critical): #E17055

#### 3. Layering

Organize diagram in layers:
1. **Background Layer**: Security zones (shaded regions)
2. **Infrastructure Layer**: Load balancers, firewalls
3. **Application Layer**: Services, microservices
4. **Data Layer**: Databases, caches
5. **Flow Layer**: All arrows and data flows
6. **Labels Layer**: Text labels and annotations

#### 4. Grouping

Group related components:
- Select components
- Right-click → Group
- Name the group (e.g., "User Zone", "Application Zone")

#### 5. Export Settings

**For Presentations (PNG/PDF):**
- Resolution: 300 DPI
- Border: 10px
- Transparent background: No (use white)
- Include grid: No

**For Documentation (SVG):**
- Embed fonts: Yes
- Include links: Yes
- Embed images: Yes

#### 6. Collaboration

**Version Control:**
- Save to GitHub/OneDrive/SharePoint
- Use meaningful filenames: `client-name-architecture-v1.2.drawio`
- Add version notes in diagram description

---

## Quality Checklist

### Before Finalizing Architecture Diagram

#### Content Completeness
- [ ] All components labeled with name, technology, and specifications
- [ ] All data flows labeled with protocol, port, and authentication
- [ ] Security zones clearly defined and shaded
- [ ] Multi-AZ deployment shown (if required)
- [ ] Complete legend included
- [ ] Architecture notes panel included (performance, security, HA/DR, cost)
- [ ] All icons are official/recognizable
- [ ] Version number and date on diagram

#### Technical Accuracy
- [ ] Architecture aligns with stated requirements
- [ ] Component sizing matches expected load
- [ ] Network segmentation follows security best practices
- [ ] Data flows are technically correct
- [ ] Technology versions are current (not EOL)
- [ ] Backup and DR flows shown
- [ ] Monitoring integration shown
- [ ] All services have health checks

#### Security Standards
- [ ] No public data plane access (except edge services)
- [ ] Encryption at rest and in transit specified
- [ ] Authentication mechanisms clearly shown
- [ ] Security boundaries marked (firewalls, NSGs, WAF)
- [ ] Compliance requirements addressed (GDPR, HIPAA, etc.)
- [ ] Secrets management shown (Key Vault, Secrets Manager)
- [ ] Audit logging flows included

#### High Availability
- [ ] Multi-AZ deployment for critical components
- [ ] Load balancers configured
- [ ] Auto-scaling configured (min/max instances)
- [ ] Health checks defined
- [ ] Failover mechanisms shown
- [ ] No single points of failure
- [ ] Database replication shown

#### Clarity and Professionalism
- [ ] Clean, uncluttered layout
- [ ] Consistent component sizing
- [ ] Aligned components (use grid)
- [ ] Readable font sizes (minimum 9pt)
- [ ] Professional color scheme
- [ ] Logical flow (left-to-right or top-to-bottom)
- [ ] Grouped related components
- [ ] White space used effectively

#### Client Specificity
- [ ] Diagram is client-specific (not generic template)
- [ ] Client's existing systems shown
- [ ] Client's technology preferences reflected
- [ ] Client's compliance requirements addressed
- [ ] Client's naming conventions used
- [ ] Client's branding colors (optional)

#### Documentation
- [ ] Diagram title includes client name and date
- [ ] Version control information included
- [ ] Author/architect name included
- [ ] Review status indicated (Draft, Under Review, Approved)
- [ ] Separate detailed view for complex subsystems
- [ ] Accompanying architecture design document references this diagram

---

## Common Mistakes to Avoid

### Mistake 1: Generic Template Diagrams
❌ **Wrong**: Using the same generic "3-tier architecture" template for every client

✅ **Correct**: Create client-specific diagram showing:
- Client's actual services and integrations
- Client's existing systems (blue)
- New proposed services (orange)
- Client-specific requirements (e.g., on-prem AD integration)

### Mistake 2: Missing Component Specifications
❌ **Wrong**: Box labeled "Database" with no details

✅ **Correct**: Detailed specification:
```
Component: Customer Database
Tech: PostgreSQL 15.2
Hosting: Azure Database for PostgreSQL
Tier: Business Critical (99.99% SLA)
Spec: 8 vCores, 32 GB RAM, 1 TB SSD
Replication: Multi-AZ
Backup: Hourly (30-day retention)
```

### Mistake 3: Unlabeled Data Flows
❌ **Wrong**: Arrow with no label

✅ **Correct**: "HTTPS (443) - OAuth 2.0 JWT"

### Mistake 4: No Security Boundaries
❌ **Wrong**: All components in one big box

✅ **Correct**: Clear security zones (Internet, DMZ, Application, Data) with boundaries

### Mistake 5: Ignoring Multi-AZ
❌ **Wrong**: Single instance of everything

✅ **Correct**: Show deployment across 3 availability zones for HA

### Mistake 6: Missing Legend
❌ **Wrong**: Colors and symbols used with no explanation

✅ **Correct**: Comprehensive legend explaining all colors, arrows, and symbols

### Mistake 7: Overcrowded Diagram
❌ **Wrong**: Trying to show everything in one diagram

✅ **Correct**: Create multiple views:
- High-level overview
- Detailed view per subsystem
- Network view
- Security view

---

## Diagram Review Process

### Peer Review Checklist

**Technical Architect Review:**
- [ ] Architecture patterns appropriate
- [ ] Technology choices justified
- [ ] Scalability considerations addressed
- [ ] Performance targets feasible

**Security Architect Review:**
- [ ] Security zones properly defined
- [ ] Encryption standards met
- [ ] Compliance requirements addressed
- [ ] Attack surface minimized

**Cloud Architect Review:**
- [ ] Cloud services used appropriately
- [ ] Cost optimization opportunities identified
- [ ] Multi-region strategy (if applicable)
- [ ] Cloud-native best practices followed

**Client Review:**
- [ ] Meets all stated requirements
- [ ] Integrates with existing systems
- [ ] Budget constraints respected
- [ ] Timeline feasible
- [ ] Risks clearly communicated

---

## Revision History Template

Include revision history in diagram or accompanying document:

```
REVISION HISTORY
────────────────────────────────────────────────────
Version | Date       | Author        | Changes
────────────────────────────────────────────────────
0.1     | 2024-01-10 | J. Smith      | Initial draft
0.2     | 2024-01-15 | J. Smith      | Added security zones
1.0     | 2024-01-20 | J. Smith      | Client review feedback
1.1     | 2024-01-25 | J. Smith      | Added DR architecture
2.0     | 2024-02-01 | J. Smith      | Final - Client approved
────────────────────────────────────────────────────
```

---

## Conclusion

Professional enterprise architecture diagrams are critical for:

✅ **Winning Client Confidence**: Demonstrate deep technical expertise
✅ **Clear Communication**: Enable stakeholders to understand complex systems
✅ **Risk Mitigation**: Surface potential issues early
✅ **Project Foundation**: Provide blueprint for delivery teams
✅ **Compliance**: Document security and regulatory requirements

**Key Principles:**
1. **Client-Specific**: Never use generic templates
2. **Security-First**: Show all security controls explicitly
3. **Detailed**: Include complete component specifications
4. **Professional**: Clean, organized, visually appealing
5. **Comprehensive**: Legend, notes, and proper labeling

**For NashTech TA workflow**, see **[NASHTECH_TA_GUIDELINES.md](./NASHTECH_TA_GUIDELINES.md)**.

**For complete technical proposals**, see **[TECHNICAL_PROPOSAL_GUIDELINES.md](./TECHNICAL_PROPOSAL_GUIDELINES.md)**.

---

**Document Version:** 1.0
**Last Updated:** 2025-11-16
**Maintained By:** NashTech Architecture Team
**Feedback:** [architecture-team@nashtech.com](mailto:architecture-team@nashtech.com)