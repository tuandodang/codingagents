"""
Example: WBS (Work Breakdown Structure) Generation

This example demonstrates how to use the WBS Generator agent to create
comprehensive work breakdown structures for project planning and presale proposals.
"""

from agents.wbs_generator import (
    WBSGenerator,
    Task,
    Resource,
    Estimation,
    TaskType,
    TaskStatus,
    ResourceType,
    EstimationUnit
)


def example_simple_wbs():
    """Example 1: Create a simple WBS for a web application"""
    print("=" * 80)
    print("Example 1: Simple Web Application WBS")
    print("=" * 80)

    generator = WBSGenerator()

    # Create project
    project = generator.create_project(
        name="Customer Portal Development",
        description="Build a customer self-service portal with authentication, dashboards, and reporting",
        budget=150000,
        timeline_weeks=12
    )

    # Define resources
    project.resources = [
        Resource("Sarah Johnson", ResourceType.ARCHITECT, 150.0, 0.5, ["Architecture", "Cloud"]),
        Resource("Mike Chen", ResourceType.DEVELOPER, 110.0, 1.0, ["React", "Node.js"]),
        Resource("Lisa Martinez", ResourceType.DEVELOPER, 100.0, 1.0, ["React", "Python"]),
        Resource("Tom Wilson", ResourceType.QA_ENGINEER, 85.0, 1.0, ["Testing", "Automation"]),
        Resource("Emily Brown", ResourceType.DEVOPS_ENGINEER, 120.0, 0.5, ["AWS", "CI/CD"]),
    ]

    # Phase 1: Planning
    phase1 = Task(
        id="1",
        name="Planning & Design",
        type=TaskType.PHASE,
        description="Project planning and technical design",
        status=TaskStatus.COMPLETED
    )

    phase1.add_child(Task(
        id="1.1",
        name="Requirements Analysis",
        type=TaskType.TASK,
        description="Gather and document requirements",
        estimation=Estimation(30, 40, 50, EstimationUnit.HOURS),
        assigned_resources=[project.resources[0]],
        deliverables=["Requirements Document", "User Stories"],
        status=TaskStatus.COMPLETED
    ))

    phase1.add_child(Task(
        id="1.2",
        name="Architecture Design",
        type=TaskType.TASK,
        description="Design system architecture",
        estimation=Estimation(40, 60, 80, EstimationUnit.HOURS),
        assigned_resources=[project.resources[0]],
        dependencies=["1.1"],
        deliverables=["Architecture Diagram", "Technology Stack Document"],
        status=TaskStatus.COMPLETED
    ))

    project.add_root_task(phase1)

    # Phase 2: Development
    phase2 = Task(
        id="2",
        name="Development",
        type=TaskType.PHASE,
        description="Frontend and backend development",
        status=TaskStatus.IN_PROGRESS
    )

    phase2.add_child(Task(
        id="2.1",
        name="Backend API Development",
        type=TaskType.WORK_PACKAGE,
        description="Develop RESTful APIs",
        estimation=Estimation(120, 160, 200, EstimationUnit.HOURS),
        assigned_resources=[project.resources[1]],
        dependencies=["1.2"],
        deliverables=["API Endpoints", "API Documentation"],
        status=TaskStatus.IN_PROGRESS
    ))

    phase2.add_child(Task(
        id="2.2",
        name="Frontend Development",
        type=TaskType.WORK_PACKAGE,
        description="Build React frontend",
        estimation=Estimation(150, 200, 250, EstimationUnit.HOURS),
        assigned_resources=[project.resources[2]],
        dependencies=["1.2"],
        deliverables=["React Application", "UI Components"],
        status=TaskStatus.NOT_STARTED
    ))

    project.add_root_task(phase2)

    # Phase 3: Testing
    phase3 = Task(
        id="3",
        name="Testing & QA",
        type=TaskType.PHASE,
        description="Quality assurance and testing",
        status=TaskStatus.NOT_STARTED
    )

    phase3.add_child(Task(
        id="3.1",
        name="Integration Testing",
        type=TaskType.TASK,
        estimation=Estimation(40, 60, 80, EstimationUnit.HOURS),
        assigned_resources=[project.resources[3]],
        dependencies=["2.1", "2.2"],
        deliverables=["Test Cases", "Test Report"]
    ))

    project.add_root_task(phase3)

    # Add project-level details
    project.risks = [
        "Third-party API availability",
        "Resource availability during holidays",
        "Scope changes from stakeholders"
    ]
    project.assumptions = [
        "Requirements stable after week 2",
        "Infrastructure ready in week 1",
        "No major technology changes"
    ]

    # Generate outputs
    print("\n--- WBS Tree Diagram (Mermaid) ---")
    print(generator.generate_wbs_tree_mermaid(project))

    print("\n--- Gantt Chart (Mermaid) ---")
    print(generator.generate_mermaid_gantt(project))

    print("\n--- Effort Summary ---")
    print(generator.generate_effort_summary(project))

    print("\n--- Project Summary ---")
    print(f"Total Effort: {project.total_effort()} hours")
    print(f"Total Cost: ${project.total_cost():,.2f}")
    print(f"Budget: ${project.budget:,.2f}")
    print(f"Variance: ${project.budget - project.total_cost():,.2f}")


def example_ecommerce_presale():
    """Example 2: E-commerce platform presale proposal"""
    print("\n" + "=" * 80)
    print("Example 2: E-Commerce Platform Presale Proposal")
    print("=" * 80)

    generator = WBSGenerator()

    # Create project
    project = generator.create_project(
        name="E-Commerce Platform Development",
        description="Build a scalable e-commerce platform with microservices architecture, "
                    "supporting web and mobile channels with advanced features like "
                    "personalization, real-time inventory, and integrated payments",
        budget=500000,
        timeline_weeks=24
    )

    # Define team
    project.resources = [
        Resource("Senior Architect", ResourceType.ARCHITECT, 180.0, 0.5),
        Resource("Tech Lead", ResourceType.DEVELOPER, 140.0, 1.0),
        Resource("Senior Developer 1", ResourceType.DEVELOPER, 120.0, 1.0),
        Resource("Senior Developer 2", ResourceType.DEVELOPER, 120.0, 1.0),
        Resource("Developer 1", ResourceType.DEVELOPER, 100.0, 1.0),
        Resource("Developer 2", ResourceType.DEVELOPER, 100.0, 1.0),
        Resource("QA Lead", ResourceType.QA_ENGINEER, 100.0, 1.0),
        Resource("QA Engineer", ResourceType.QA_ENGINEER, 80.0, 1.0),
        Resource("DevOps Engineer", ResourceType.DEVOPS_ENGINEER, 130.0, 0.75),
        Resource("UI/UX Designer", ResourceType.DESIGNER, 110.0, 0.5),
    ]

    # Phase 1: Discovery & Planning
    phase1 = Task(
        id="1",
        name="Discovery & Planning",
        type=TaskType.PHASE,
        description="Requirements gathering, architecture design, and project planning"
    )

    phase1.add_child(Task(
        id="1.1",
        name="Business Requirements",
        type=TaskType.TASK,
        estimation=Estimation(60, 80, 100, EstimationUnit.HOURS),
        assigned_resources=[project.resources[0], project.resources[1]],
        deliverables=[
            "Business Requirements Document",
            "User Personas",
            "User Journey Maps"
        ],
        acceptance_criteria=[
            "All stakeholders have reviewed and approved",
            "Success criteria defined",
            "KPIs identified"
        ]
    ))

    phase1.add_child(Task(
        id="1.2",
        name="Architecture Design",
        type=TaskType.TASK,
        estimation=Estimation(80, 120, 160, EstimationUnit.HOURS),
        assigned_resources=[project.resources[0], project.resources[1]],
        dependencies=["1.1"],
        deliverables=[
            "Architecture Design Document",
            "C4 Diagrams (Context, Container, Component)",
            "Technology Stack Selection",
            "Deployment Architecture"
        ],
        acceptance_criteria=[
            "Scalability targets defined (100K concurrent users)",
            "Security architecture approved",
            "Technology choices justified"
        ]
    ))

    phase1.add_child(Task(
        id="1.3",
        name="UI/UX Design",
        type=TaskType.TASK,
        estimation=Estimation(100, 140, 180, EstimationUnit.HOURS),
        assigned_resources=[project.resources[9]],
        dependencies=["1.1"],
        deliverables=[
            "Wireframes",
            "High-fidelity Mockups",
            "Design System",
            "Prototype"
        ]
    ))

    project.add_root_task(phase1)

    # Phase 2: Backend Development
    phase2 = Task(
        id="2",
        name="Backend Microservices Development",
        type=TaskType.PHASE,
        description="Develop core backend microservices"
    )

    backend_services = [
        ("User Service", "2.1", 160, 200, 240, ["User registration/login", "Profile management", "OAuth integration"]),
        ("Product Catalog Service", "2.2", 180, 240, 300, ["Product CRUD", "Category management", "Search & filters"]),
        ("Inventory Service", "2.3", 120, 160, 200, ["Stock management", "Real-time updates", "Warehouse integration"]),
        ("Shopping Cart Service", "2.4", 100, 140, 180, ["Cart operations", "Session management", "Persistence"]),
        ("Order Service", "2.5", 200, 260, 320, ["Order processing", "Order status tracking", "History"]),
        ("Payment Service", "2.6", 140, 180, 220, ["Payment gateway integration", "PCI compliance", "Refunds"]),
        ("Notification Service", "2.7", 80, 120, 160, ["Email notifications", "SMS integration", "Templates"]),
    ]

    for service_name, task_id, opt, likely, pess, deliverables in backend_services:
        phase2.add_child(Task(
            id=task_id,
            name=service_name,
            type=TaskType.WORK_PACKAGE,
            estimation=Estimation(opt, likely, pess, EstimationUnit.HOURS),
            assigned_resources=[project.resources[2], project.resources[4]],
            dependencies=["1.2"],
            deliverables=deliverables + ["API Documentation", "Unit Tests"],
            acceptance_criteria=[
                "API endpoints implemented",
                "Code coverage > 80%",
                "Performance tests passed"
            ]
        ))

    project.add_root_task(phase2)

    # Phase 3: Frontend Development
    phase3 = Task(
        id="3",
        name="Frontend Development",
        type=TaskType.PHASE,
        description="Web and mobile application development"
    )

    phase3.add_child(Task(
        id="3.1",
        name="Web Application (React)",
        type=TaskType.WORK_PACKAGE,
        estimation=Estimation(300, 400, 500, EstimationUnit.HOURS),
        assigned_resources=[project.resources[3], project.resources[5]],
        dependencies=["1.3", "2.2"],
        deliverables=[
            "React Application",
            "Component Library",
            "Responsive Design",
            "State Management"
        ]
    ))

    phase3.add_child(Task(
        id="3.2",
        name="Mobile App (React Native)",
        type=TaskType.WORK_PACKAGE,
        estimation=Estimation(250, 340, 430, EstimationUnit.HOURS),
        assigned_resources=[project.resources[4], project.resources[5]],
        dependencies=["1.3", "2.2"],
        deliverables=[
            "iOS App",
            "Android App",
            "Shared Components",
            "Mobile-specific Features"
        ]
    ))

    project.add_root_task(phase3)

    # Phase 4: Integration & Testing
    phase4 = Task(
        id="4",
        name="Integration & Testing",
        type=TaskType.PHASE,
        description="System integration and comprehensive testing"
    )

    testing_tasks = [
        ("Integration Testing", "4.1", 120, 160, 200, ["2.7", "3.1", "3.2"]),
        ("Performance Testing", "4.2", 80, 100, 120, ["2.7", "3.1"]),
        ("Security Testing", "4.3", 60, 80, 100, ["2.6"]),
        ("User Acceptance Testing", "4.4", 80, 120, 160, ["3.1", "3.2"]),
    ]

    for task_name, task_id, opt, likely, pess, deps in testing_tasks:
        phase4.add_child(Task(
            id=task_id,
            name=task_name,
            type=TaskType.TASK,
            estimation=Estimation(opt, likely, pess, EstimationUnit.HOURS),
            assigned_resources=[project.resources[6], project.resources[7]],
            dependencies=deps,
            deliverables=["Test Plan", "Test Cases", "Test Report", "Bug Reports"]
        ))

    project.add_root_task(phase4)

    # Phase 5: Deployment & Launch
    phase5 = Task(
        id="5",
        name="Deployment & Launch",
        type=TaskType.PHASE,
        description="Production deployment and go-live"
    )

    phase5.add_child(Task(
        id="5.1",
        name="Infrastructure Setup",
        type=TaskType.TASK,
        estimation=Estimation(60, 80, 100, EstimationUnit.HOURS),
        assigned_resources=[project.resources[8]],
        dependencies=["1.2"],
        deliverables=[
            "Kubernetes Cluster",
            "Database Setup",
            "CDN Configuration",
            "Monitoring Setup"
        ]
    ))

    phase5.add_child(Task(
        id="5.2",
        name="CI/CD Pipeline",
        type=TaskType.TASK,
        estimation=Estimation(40, 60, 80, EstimationUnit.HOURS),
        assigned_resources=[project.resources[8]],
        dependencies=["5.1"],
        deliverables=[
            "Build Pipeline",
            "Deployment Pipeline",
            "Automated Testing Integration"
        ]
    ))

    phase5.add_child(Task(
        id="5.3",
        name="Production Deployment",
        type=TaskType.TASK,
        estimation=Estimation(30, 40, 50, EstimationUnit.HOURS),
        assigned_resources=[project.resources[8], project.resources[1]],
        dependencies=["4.4", "5.2"],
        deliverables=[
            "Production Deployment",
            "Smoke Tests",
            "Monitoring Dashboards"
        ]
    ))

    project.add_root_task(phase5)

    # Add project details
    project.risks = [
        "Payment gateway integration complexity",
        "Third-party API dependencies",
        "Scalability challenges with initial traffic",
        "Mobile app store approval delays",
        "Data migration from legacy system"
    ]

    project.assumptions = [
        "Client provides requirements and feedback within 48 hours",
        "AWS infrastructure provisioning takes max 1 week",
        "Payment gateway API access provided by client",
        "No major scope changes after design approval",
        "Client team available for UAT"
    ]

    project.constraints = [
        "Must launch before Q4 shopping season",
        "PCI-DSS compliance required for payments",
        "GDPR compliance for EU customers",
        "Mobile apps must support iOS 14+ and Android 10+"
    ]

    # Generate presale proposal
    print("\n--- PRESALE PROPOSAL ---")
    proposal = generator.generate_presale_proposal(project)
    print(proposal)

    print("\n--- GANTT CHART ---")
    print(generator.generate_mermaid_gantt(project))

    print("\n--- WBS MARKDOWN ---")
    wbs_doc = generator.generate_markdown_wbs(project)
    # Save to file
    with open("ecommerce_wbs.md", "w") as f:
        f.write(wbs_doc)
    print("WBS documentation saved to: ecommerce_wbs.md")


def example_resource_utilization():
    """Example 3: Resource utilization analysis"""
    print("\n" + "=" * 80)
    print("Example 3: Resource Utilization Analysis")
    print("=" * 80)

    generator = WBSGenerator()

    project = generator.create_project(
        name="Mobile Banking App",
        description="iOS and Android banking application",
        timeline_weeks=16
    )

    # Define resources
    project.resources = [
        Resource("Alex Smith", ResourceType.DEVELOPER, 110.0, 1.0, ["iOS", "Swift"]),
        Resource("Jamie Lee", ResourceType.DEVELOPER, 110.0, 1.0, ["Android", "Kotlin"]),
        Resource("Taylor Johnson", ResourceType.DEVELOPER, 120.0, 0.5, ["Backend", "Node.js"]),
        Resource("Morgan Davis", ResourceType.QA_ENGINEER, 85.0, 1.0, ["Mobile Testing"]),
        Resource("Casey Wilson", ResourceType.DESIGNER, 100.0, 0.5, ["UI/UX"]),
    ]

    # Create tasks with specific resource assignments
    task1 = Task(
        id="1",
        name="iOS Development",
        type=TaskType.PHASE,
        estimation=Estimation(280, 350, 420, EstimationUnit.HOURS),
        assigned_resources=[project.resources[0]]
    )

    task2 = Task(
        id="2",
        name="Android Development",
        type=TaskType.PHASE,
        estimation=Estimation(280, 350, 420, EstimationUnit.HOURS),
        assigned_resources=[project.resources[1]]
    )

    task3 = Task(
        id="3",
        name="Backend API",
        type=TaskType.PHASE,
        estimation=Estimation(160, 200, 240, EstimationUnit.HOURS),
        assigned_resources=[project.resources[2]]
    )

    task4 = Task(
        id="4",
        name="Testing",
        type=TaskType.PHASE,
        estimation=Estimation(120, 160, 200, EstimationUnit.HOURS),
        assigned_resources=[project.resources[3]]
    )

    task5 = Task(
        id="5",
        name="Design",
        type=TaskType.PHASE,
        estimation=Estimation(80, 100, 120, EstimationUnit.HOURS),
        assigned_resources=[project.resources[4]]
    )

    project.add_root_task(task1)
    project.add_root_task(task2)
    project.add_root_task(task3)
    project.add_root_task(task4)
    project.add_root_task(task5)

    # Generate effort summary
    print(generator.generate_effort_summary(project))

    print(f"\nTotal Project Cost: ${project.total_cost():,.2f}")
    print(f"Total Project Effort: {project.total_effort():,.2f} hours")
    print(f"Timeline: {project.timeline_weeks} weeks")


def example_json_export():
    """Example 4: JSON export for integration"""
    print("\n" + "=" * 80)
    print("Example 4: JSON Export")
    print("=" * 80)

    generator = WBSGenerator()

    project = generator.create_project(
        name="API Gateway Migration",
        description="Migrate legacy API gateway to modern cloud-native solution"
    )

    # Create simple structure
    task = Task(
        id="1",
        name="Assessment & Planning",
        type=TaskType.PHASE,
        estimation=Estimation(40, 60, 80, EstimationUnit.HOURS)
    )

    project.add_root_task(task)

    # Generate JSON
    json_output = generator.generate_json_wbs(project)
    print(json_output)

    # Save to file
    with open("wbs_export.json", "w") as f:
        f.write(json_output)
    print("\nJSON exported to: wbs_export.json")


if __name__ == "__main__":
    # Run examples
    example_simple_wbs()
    example_ecommerce_presale()
    example_resource_utilization()
    example_json_export()

    print("\n" + "=" * 80)
    print("Examples completed!")
    print("=" * 80)
