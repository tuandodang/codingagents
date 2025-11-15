"""
Example: Using Database Visualizer Agent

This example demonstrates how to use the Database Visualizer agent
to create ER diagrams and database documentation.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.database_visualizer.agent import DatabaseVisualizer


def main():
    print("=" * 80)
    print("Database Visualizer Agent Examples")
    print("=" * 80)
    print()

    visualizer = DatabaseVisualizer()

    # Create example e-commerce schema
    schema = visualizer.create_example_schema()

    print(f"📊 Database: {schema.name}")
    print(f"📝 Description: {schema.description}")
    print(f"📋 Tables: {len(schema.tables)}")
    print(f"🔗 Relationships: {len(schema.relationships)}")
    print()

    # Example 1: Mermaid ER Diagram
    print("\nExample 1: Mermaid ER Diagram")
    print("-" * 80)

    mermaid_er = visualizer.generate_er_diagram(schema, format="mermaid")
    print(mermaid_er)
    print()

    # Example 2: PlantUML ER Diagram
    print("\nExample 2: PlantUML ER Diagram")
    print("-" * 80)

    plantuml_er = visualizer.generate_er_diagram(schema, format="plantuml")
    print(plantuml_er)
    print()

    # Example 3: DBML
    print("\nExample 3: DBML (Database Markup Language)")
    print("-" * 80)

    dbml = visualizer.generate_er_diagram(schema, format="dbml")
    print(dbml)
    print()

    # Example 4: Schema Documentation
    print("\nExample 4: Database Schema Documentation")
    print("-" * 80)

    documentation = visualizer.generate_schema_documentation(schema)
    print(documentation)

    # Save all outputs
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/database_er_mermaid.mmd", "w") as f:
        f.write(mermaid_er)

    with open(f"{output_dir}/database_er_plantuml.puml", "w") as f:
        f.write(plantuml_er)

    with open(f"{output_dir}/database_schema.dbml", "w") as f:
        f.write(dbml)

    with open(f"{output_dir}/database_documentation.md", "w") as f:
        f.write(documentation)

    print(f"\n✅ Database diagrams and documentation saved to {output_dir}/")


if __name__ == "__main__":
    main()
