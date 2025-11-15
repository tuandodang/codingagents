"""
Example: Using Diagram Generator Agent

This example demonstrates how to use the Diagram Generator agent
to create various types of diagrams.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.diagram_generator.agent import (
    DiagramGenerator,
    Node,
    Edge,
    DiagramSpec,
    DiagramType,
    DiagramFormat
)


def main():
    print("=" * 80)
    print("Diagram Generator Agent Examples")
    print("=" * 80)
    print()

    generator = DiagramGenerator()

    # Example 1: Microservices Architecture Flowchart
    print("Example 1: Microservices Architecture")
    print("-" * 80)

    nodes = [
        Node("web", "Web App", "service", "rounded"),
        Node("mobile", "Mobile App", "service", "rounded"),
        Node("gateway", "API Gateway", "service"),
        Node("auth", "Auth Service", "service"),
        Node("users", "Users Service", "service"),
        Node("products", "Products Service", "service"),
        Node("orders", "Orders Service", "service"),
        Node("db_users", "Users DB", "database", "cylinder"),
        Node("db_products", "Products DB", "database", "cylinder"),
        Node("db_orders", "Orders DB", "database", "cylinder"),
        Node("cache", "Redis", "cache", "cylinder"),
        Node("payment", "Payment Gateway", "external", "rounded"),
        Node("email", "Email Service", "external", "rounded"),
    ]

    edges = [
        Edge("web", "gateway", "HTTPS"),
        Edge("mobile", "gateway", "HTTPS"),
        Edge("gateway", "auth", "Authenticate"),
        Edge("gateway", "users", ""),
        Edge("gateway", "products", ""),
        Edge("gateway", "orders", ""),
        Edge("users", "db_users", "Query"),
        Edge("products", "db_products", "Query"),
        Edge("orders", "db_orders", "Query"),
        Edge("users", "cache", "Cache"),
        Edge("products", "cache", "Cache"),
        Edge("orders", "payment", "Process Payment", "dashed"),
        Edge("orders", "email", "Send Email", "dashed"),
    ]

    flowchart = generator.generate_mermaid_flowchart(
        nodes, edges,
        title="Microservices E-commerce Platform",
        direction="TB"
    )

    print(flowchart)
    print()

    # Example 2: API Sequence Diagram
    print("\nExample 2: API Sequence Diagram")
    print("-" * 80)

    participants = ["Client", "Gateway", "Auth", "OrderService", "Database", "PaymentGateway"]
    interactions = [
        {"from": "Client", "to": "Gateway", "message": "POST /orders", "style": "->"},
        {"from": "Gateway", "to": "Auth", "message": "Validate Token", "style": "->"},
        {"from": "Auth", "to": "Gateway", "message": "Token Valid", "style": "return"},
        {"from": "Gateway", "to": "OrderService", "message": "Create Order", "style": "->"},
        {"from": "OrderService", "to": "Database", "message": "Save Order", "style": "->"},
        {"from": "Database", "to": "OrderService", "message": "Order Saved", "style": "return"},
        {"from": "OrderService", "to": "PaymentGateway", "message": "Process Payment", "style": "->"},
        {"from": "PaymentGateway", "to": "OrderService", "message": "Payment Confirmed", "style": "return"},
        {"from": "OrderService", "to": "Gateway", "message": "Order Created", "style": "return"},
        {"from": "Gateway", "to": "Client", "message": "201 Created", "style": "return"},
    ]

    sequence = generator.generate_mermaid_sequence(
        participants, interactions,
        title="Order Creation Flow"
    )

    print(sequence)
    print()

    # Example 3: ER Diagram
    print("\nExample 3: Database ER Diagram")
    print("-" * 80)

    entities = [
        {
            "name": "User",
            "attributes": [
                {"name": "id", "type": "uuid", "key": "PK"},
                {"name": "email", "type": "string", "key": "UK"},
                {"name": "name", "type": "string"},
                {"name": "created_at", "type": "timestamp"}
            ]
        },
        {
            "name": "Order",
            "attributes": [
                {"name": "id", "type": "uuid", "key": "PK"},
                {"name": "user_id", "type": "uuid", "key": "FK"},
                {"name": "total", "type": "decimal"},
                {"name": "status", "type": "string"}
            ]
        },
        {
            "name": "Product",
            "attributes": [
                {"name": "id", "type": "uuid", "key": "PK"},
                {"name": "name", "type": "string"},
                {"name": "price", "type": "decimal"},
                {"name": "stock", "type": "int"}
            ]
        }
    ]

    relationships = [
        {"entity1": "User", "entity2": "Order", "cardinality": "||--o{", "label": "places"},
        {"entity1": "Order", "entity2": "Product", "cardinality": "}o--o{", "label": "contains"}
    ]

    er_diagram = generator.generate_mermaid_er(
        entities, relationships,
        title="E-commerce Database"
    )

    print(er_diagram)
    print()

    # Example 4: C4 Context Diagram
    print("\nExample 4: C4 Context Diagram")
    print("-" * 80)

    c4_context = generator.generate_c4_context(
        system_name="E-commerce Platform",
        users=[
            {"name": "Customer", "description": "Online shopper"},
            {"name": "Admin", "description": "Platform administrator"}
        ],
        systems=[
            {"name": "EcommercePlatform", "description": "Online shopping platform"}
        ],
        external_systems=[
            {"name": "PaymentGateway", "description": "Stripe payment processing"},
            {"name": "EmailService", "description": "SendGrid email service"},
            {"name": "ShippingProvider", "description": "FedEx shipping"}
        ],
        relationships=[
            {"from": "Customer", "to": "EcommercePlatform", "description": "Uses", "technology": "HTTPS"},
            {"from": "Admin", "to": "EcommercePlatform", "description": "Manages", "technology": "HTTPS"},
            {"from": "EcommercePlatform", "to": "PaymentGateway", "description": "Processes payments", "technology": "REST API"},
            {"from": "EcommercePlatform", "to": "EmailService", "description": "Sends emails", "technology": "SMTP"},
            {"from": "EcommercePlatform", "to": "ShippingProvider", "description": "Ships orders", "technology": "REST API"}
        ]
    )

    print(c4_context)
    print()

    # Save all diagrams
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/microservices_flowchart.mmd", "w") as f:
        f.write(flowchart)

    with open(f"{output_dir}/api_sequence.mmd", "w") as f:
        f.write(sequence)

    with open(f"{output_dir}/er_diagram.mmd", "w") as f:
        f.write(er_diagram)

    with open(f"{output_dir}/c4_context.puml", "w") as f:
        f.write(c4_context)

    print(f"\n✅ All diagrams saved to {output_dir}/")


if __name__ == "__main__":
    main()
