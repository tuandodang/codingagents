"""
Example: Using Architecture Analyzer Agent

This example demonstrates how to use the Architecture Analyzer agent
to analyze a codebase and generate architecture diagrams.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.architecture_analyzer.agent import ArchitectureAnalyzer
import json


def main():
    print("=" * 80)
    print("Architecture Analyzer Agent Example")
    print("=" * 80)
    print()

    # Initialize the analyzer
    analyzer = ArchitectureAnalyzer()

    # Example 1: Analyze current directory
    print("Example 1: Analyzing current directory")
    print("-" * 80)

    result = analyzer.analyze_codebase(
        path=".",
        diagram_format="mermaid",
        depth="moderate"
    )

    print("\n📊 Analysis Results:")
    print(f"Architecture Pattern: {result['analysis']['architecture_pattern']}")
    print(f"Number of Components: {len(result['analysis']['components'])}")

    print("\n🏗️ Technology Stack:")
    for category, technologies in result['analysis']['technology_stack'].items():
        if technologies:
            print(f"  {category.title()}: {', '.join(technologies)}")

    print("\n📋 Recommendations:")
    for i, rec in enumerate(result['analysis']['recommendations'], 1):
        print(f"  {i}. {rec}")

    print("\n📈 Mermaid Diagram:")
    print("-" * 80)
    print(result['diagram'])
    print("-" * 80)

    # Example 2: Generate C4 diagram
    print("\n\nExample 2: Generating C4 Container Diagram")
    print("-" * 80)

    result_c4 = analyzer.analyze_codebase(
        path=".",
        diagram_format="c4",
        depth="moderate"
    )

    print("\n📈 C4 Diagram:")
    print("-" * 80)
    print(result_c4['diagram'])
    print("-" * 80)

    # Save results
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/architecture_analysis.json", "w") as f:
        json.dump(result, indent=2, default=str, fp=f)

    with open(f"{output_dir}/architecture_diagram.mmd", "w") as f:
        f.write(result['diagram'])

    with open(f"{output_dir}/architecture_c4.puml", "w") as f:
        f.write(result_c4['diagram'])

    print(f"\n✅ Results saved to {output_dir}/")


if __name__ == "__main__":
    main()
