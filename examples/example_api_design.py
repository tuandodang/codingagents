"""
Example: Using API Designer Agent

This example demonstrates how to use the API Designer agent
to design and document APIs.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.api_designer.agent import APIDesigner
import json


def main():
    print("=" * 80)
    print("API Designer Agent Examples")
    print("=" * 80)
    print()

    designer = APIDesigner()

    # Example 1: Design REST API for E-commerce
    print("Example 1: E-commerce REST API Design")
    print("-" * 80)

    api_spec = designer.design_rest_api(
        name="E-commerce API",
        resources=["Users", "Products", "Orders", "Categories"],
        version="1.0.0",
        include_crud=True
    )

    print(f"\n✅ Created API: {api_spec.name} v{api_spec.version}")
    print(f"📝 Total Endpoints: {len(api_spec.endpoints)}")
    print(f"🔗 Base URL: {api_spec.base_url}")

    print("\n📋 Endpoints:")
    for endpoint in api_spec.endpoints[:5]:  # Show first 5
        print(f"  {endpoint.method.value:8} {endpoint.path:30} - {endpoint.summary}")
    print(f"  ... and {len(api_spec.endpoints) - 5} more endpoints")

    # Example 2: Generate OpenAPI Specification
    print("\n\nExample 2: OpenAPI Specification")
    print("-" * 80)

    openapi_spec = designer.generate_openapi_spec(api_spec)

    print("\n📄 OpenAPI Specification (YAML format):\n")
    print(json.dumps(openapi_spec, indent=2))

    # Example 3: Generate Sequence Diagram
    print("\n\nExample 3: API Sequence Diagram")
    print("-" * 80)

    # Get a POST endpoint for the diagram
    post_endpoint = next((e for e in api_spec.endpoints if e.method.value == "POST"), None)

    if post_endpoint:
        sequence_diagram = designer.generate_sequence_diagram(
            post_endpoint,
            include_auth=True
        )

        print(f"\n🔄 Sequence Diagram for: {post_endpoint.method.value} {post_endpoint.path}")
        print()
        print(sequence_diagram)

    # Example 4: GraphQL Schema
    print("\n\nExample 4: GraphQL Schema Design")
    print("-" * 80)

    types = [
        {
            "name": "User",
            "fields": [
                {"name": "id", "type": "ID", "required": True},
                {"name": "email", "type": "String", "required": True},
                {"name": "name", "type": "String", "required": True},
                {"name": "orders", "type": "[Order!]", "required": True}
            ]
        },
        {
            "name": "Product",
            "fields": [
                {"name": "id", "type": "ID", "required": True},
                {"name": "name", "type": "String", "required": True},
                {"name": "price", "type": "Float", "required": True},
                {"name": "stock", "type": "Int", "required": True}
            ]
        },
        {
            "name": "Order",
            "fields": [
                {"name": "id", "type": "ID", "required": True},
                {"name": "user", "type": "User", "required": True},
                {"name": "total", "type": "Float", "required": True},
                {"name": "status", "type": "OrderStatus", "required": True}
            ]
        }
    ]

    queries = [
        {
            "name": "user",
            "args": [{"name": "id", "type": "ID!"}],
            "returns": "User"
        },
        {
            "name": "products",
            "args": [
                {"name": "page", "type": "Int"},
                {"name": "limit", "type": "Int"}
            ],
            "returns": "[Product!]!"
        }
    ]

    mutations = [
        {
            "name": "createUser",
            "args": [{"name": "input", "type": "CreateUserInput!"}],
            "returns": "User!"
        },
        {
            "name": "createOrder",
            "args": [{"name": "input", "type": "CreateOrderInput!"}],
            "returns": "Order!"
        }
    ]

    graphql_schema = designer.generate_graphql_schema(types, queries, mutations)

    print("\n📜 GraphQL Schema:\n")
    print(graphql_schema)

    # Example 5: Best Practices & Recommendations
    print("\n\nExample 5: API Best Practices")
    print("-" * 80)

    recommendations = designer.generate_recommendations(api_spec)

    print("\n💡 Recommendations:")
    for rec in recommendations:
        print(f"  {rec}")

    # Save results
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/api_openapi_spec.json", "w") as f:
        json.dump(openapi_spec, f, indent=2)

    if post_endpoint:
        with open(f"{output_dir}/api_sequence_diagram.mmd", "w") as f:
            f.write(sequence_diagram)

    with open(f"{output_dir}/api_graphql_schema.graphql", "w") as f:
        f.write(graphql_schema)

    print(f"\n✅ API specifications saved to {output_dir}/")


if __name__ == "__main__":
    main()
