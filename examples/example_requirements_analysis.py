"""
Example: Using Requirements Analyzer Agent

This example demonstrates how to use the Requirements Analyzer agent
to extract and analyze requirements from multiple document formats.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.requirements_analyzer.agent import (
    RequirementsAnalyzer,
    Requirement,
    RequirementType,
    RequirementPriority,
    RequirementStatus
)


def create_sample_requirements():
    """Create sample requirements for demonstration"""
    requirements = [
        Requirement(
            id="FR-001",
            title="User Registration",
            description="The system shall allow users to register with email and password",
            type=RequirementType.FUNCTIONAL,
            priority=RequirementPriority.HIGH,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "Email validation is performed",
                "Password must be at least 8 characters",
                "Confirmation email is sent",
                "User profile is created"
            ],
            stakeholder="Product Owner"
        ),
        Requirement(
            id="FR-002",
            title="Product Search",
            description="The system shall provide product search functionality with filters",
            type=RequirementType.FUNCTIONAL,
            priority=RequirementPriority.HIGH,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "Search by product name",
                "Filter by category",
                "Filter by price range",
                "Sort by relevance, price, rating"
            ],
            dependencies=["FR-003"],
            stakeholder="Product Owner"
        ),
        Requirement(
            id="FR-003",
            title="Product Catalog",
            description="The system shall maintain a catalog of products with details",
            type=RequirementType.FUNCTIONAL,
            priority=RequirementPriority.HIGH,
            status=RequirementStatus.IMPLEMENTED,
            acceptance_criteria=[
                "Product name, description, price",
                "Product images (multiple)",
                "Stock quantity",
                "Category assignment"
            ],
            stakeholder="Product Owner"
        ),
        Requirement(
            id="NFR-001",
            title="Response Time",
            description="The system shall respond to user requests within 2 seconds under normal load",
            type=RequirementType.PERFORMANCE,
            priority=RequirementPriority.HIGH,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "95th percentile < 2 seconds",
                "Support 1000 concurrent users",
                "API response time < 500ms",
                "Database query optimization"
            ],
            stakeholder="Technical Lead"
        ),
        Requirement(
            id="NFR-002",
            title="System Availability",
            description="The system shall maintain 99.9% uptime",
            type=RequirementType.PERFORMANCE,
            priority=RequirementPriority.CRITICAL,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "Maximum 43 minutes downtime per month",
                "Automated health checks",
                "Failover mechanisms",
                "Disaster recovery plan"
            ],
            stakeholder="Operations Manager"
        ),
        Requirement(
            id="SEC-001",
            title="Data Encryption",
            description="The system shall encrypt all sensitive data at rest and in transit",
            type=RequirementType.SECURITY,
            priority=RequirementPriority.CRITICAL,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "AES-256 encryption for data at rest",
                "TLS 1.3 for data in transit",
                "Encrypted database connections",
                "Secure key management"
            ],
            stakeholder="Security Officer"
        ),
        Requirement(
            id="SEC-002",
            title="Authentication & Authorization",
            description="The system shall implement secure authentication and role-based access control",
            type=RequirementType.SECURITY,
            priority=RequirementPriority.CRITICAL,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "JWT-based authentication",
                "Role-based permissions",
                "Session timeout after 30 minutes",
                "Account lockout after 5 failed attempts"
            ],
            dependencies=["FR-001"],
            stakeholder="Security Officer"
        ),
        Requirement(
            id="BUS-001",
            title="Order Validation",
            description="The system shall validate orders before processing payment",
            type=RequirementType.BUSINESS,
            priority=RequirementPriority.HIGH,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "Check product availability",
                "Validate shipping address",
                "Verify payment details",
                "Calculate total with taxes"
            ],
            stakeholder="Business Analyst"
        ),
        Requirement(
            id="COMP-001",
            title="GDPR Compliance",
            description="The system shall comply with GDPR regulations for data privacy",
            type=RequirementType.COMPLIANCE,
            priority=RequirementPriority.CRITICAL,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "User consent for data collection",
                "Right to data deletion",
                "Data export functionality",
                "Privacy policy acknowledgment"
            ],
            stakeholder="Legal Team"
        ),
        Requirement(
            id="USE-001",
            title="Mobile Responsive Design",
            description="The system shall provide responsive design for mobile devices",
            type=RequirementType.USABILITY,
            priority=RequirementPriority.MEDIUM,
            status=RequirementStatus.APPROVED,
            acceptance_criteria=[
                "Support iOS and Android browsers",
                "Responsive layout (320px - 2560px)",
                "Touch-friendly UI elements",
                "Fast mobile page load (< 3s)"
            ],
            stakeholder="UX Designer"
        )
    ]
    return requirements


def main():
    print("=" * 80)
    print("Requirements Analyzer Agent Examples")
    print("=" * 80)
    print()

    analyzer = RequirementsAnalyzer()

    # Example 1: Analyze sample requirements
    print("Example 1: Analyzing Sample Requirements")
    print("-" * 80)

    # Create sample requirements
    sample_reqs = create_sample_requirements()

    # Create analysis manually for demonstration
    from agents.requirements_analyzer.agent import RequirementAnalysis, RequirementCategory

    categories = {}
    for req_type in RequirementType:
        reqs = [r for r in sample_reqs if r.type == req_type]
        if reqs:
            categories[req_type.value] = RequirementCategory(
                category=req_type.value,
                requirements=reqs
            )

    summary = {
        'total': len(sample_reqs),
        'by_type': {rt.value: len([r for r in sample_reqs if r.type == rt]) for rt in RequirementType},
        'by_priority': {rp.value: len([r for r in sample_reqs if r.priority == rp]) for rp in RequirementPriority},
    }

    stakeholders = set(r.stakeholder for r in sample_reqs if r.stakeholder)

    analysis = RequirementAnalysis(
        requirements=sample_reqs,
        categories=categories,
        total_count=len(sample_reqs),
        summary=summary,
        sources=["sample_requirements"],
        stakeholders=stakeholders,
        recommendations=analyzer._generate_recommendations(sample_reqs)
    )

    print(f"\n📊 Analysis Summary:")
    print(f"Total Requirements: {analysis.total_count}")
    print(f"Stakeholders: {', '.join(analysis.stakeholders)}")

    print("\n📋 Requirements by Type:")
    for req_type, count in analysis.summary['by_type'].items():
        if count > 0:
            print(f"  {req_type.replace('_', ' ').title()}: {count}")

    print("\n🎯 Requirements by Priority:")
    for priority, count in analysis.summary['by_priority'].items():
        if count > 0:
            print(f"  {priority.title()}: {count}")

    # Example 2: Generate Use Case Diagram
    print("\n\nExample 2: Use Case Diagram")
    print("-" * 80)

    use_case_diagram = analyzer.generate_use_case_diagram(analysis)
    print(use_case_diagram)

    # Example 3: Generate Traceability Matrix
    print("\n\nExample 3: Traceability Matrix")
    print("-" * 80)

    traceability = analyzer.generate_traceability_matrix(analysis)
    print(traceability)

    # Example 4: Generate Full Report
    print("\n\nExample 4: Full Requirements Report")
    print("-" * 80)

    report = analyzer.generate_requirement_report(analysis)
    print(report[:2000], "...\n[Report truncated for display]")

    # Example 5: Demonstrate Text File Parsing
    print("\n\nExample 5: Parsing Text File")
    print("-" * 80)

    # Create a sample text file
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)

    sample_text = """# E-commerce Platform Requirements

## Functional Requirements

1. The system shall allow users to browse products by category
2. The system must provide a shopping cart functionality
3. Users shall be able to checkout and complete purchases
4. The system will send order confirmation emails

## Non-Functional Requirements

### Performance
- The system shall load pages within 2 seconds
- API responses must be under 500ms
- The system should support 1000 concurrent users

### Security
- All data must be encrypted using AES-256
- User passwords shall be hashed using bcrypt
- The system must implement rate limiting

### Usability
- The interface should be mobile-responsive
- The system must support multiple languages
- Accessibility compliance with WCAG 2.1 AA
"""

    sample_file = f"{output_dir}/sample_requirements.txt"
    with open(sample_file, 'w') as f:
        f.write(sample_text)

    print(f"Created sample file: {sample_file}")

    # Parse the text file
    text_reqs = analyzer._parse_text(sample_file)
    print(f"\n📄 Extracted {len(text_reqs)} requirements from text file:")
    for req in text_reqs[:3]:
        print(f"\n  {req.id}: {req.title}")
        print(f"  Type: {req.type.value}, Priority: {req.priority.value}")

    # Save all outputs
    with open(f"{output_dir}/use_case_diagram.puml", "w") as f:
        f.write(use_case_diagram)

    with open(f"{output_dir}/traceability_matrix.md", "w") as f:
        f.write(traceability)

    with open(f"{output_dir}/requirements_report.md", "w") as f:
        f.write(report)

    print(f"\n✅ All outputs saved to {output_dir}/")

    # Example 6: Show recommendations
    print("\n\nExample 6: Recommendations")
    print("-" * 80)

    if analysis.recommendations:
        print("\n💡 Analysis Recommendations:")
        for i, rec in enumerate(analysis.recommendations, 1):
            print(f"  {i}. {rec}")
    else:
        print("No specific recommendations - requirements look good!")

    # Example 7: Requirement Dependencies
    print("\n\nExample 7: Requirement Dependencies")
    print("-" * 80)

    print("\n🔗 Requirements with Dependencies:")
    for req in analysis.requirements:
        if req.dependencies:
            print(f"\n  {req.id}: {req.title}")
            print(f"  Depends on: {', '.join(req.dependencies)}")


if __name__ == "__main__":
    main()
