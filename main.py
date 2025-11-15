#!/usr/bin/env python3
"""
Main Orchestrator for Architecture Design Agents

This script provides a CLI interface to interact with all architecture design agents.
"""

import argparse
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.architecture_analyzer.agent import ArchitectureAnalyzer
from agents.diagram_generator.agent import DiagramGenerator, Node, Edge
from agents.api_designer.agent import APIDesigner
from agents.database_visualizer.agent import DatabaseVisualizer
from agents.requirements_analyzer.agent import RequirementsAnalyzer


def architecture_command(args):
    """Run architecture analysis"""
    print(f"🔍 Analyzing architecture at: {args.path}")

    analyzer = ArchitectureAnalyzer()
    result = analyzer.analyze_codebase(
        path=args.path,
        diagram_format=args.format,
        depth=args.depth
    )

    print(f"\n📊 Architecture Pattern: {result['analysis']['architecture_pattern']}")
    print(f"📦 Components: {len(result['analysis']['components'])}")

    if args.output:
        with open(args.output, 'w') as f:
            f.write(result['diagram'])
        print(f"\n✅ Diagram saved to: {args.output}")
    else:
        print("\n" + "=" * 80)
        print(result['diagram'])
        print("=" * 80)


def api_command(args):
    """Run API design"""
    print(f"🔧 Designing API: {args.name}")

    designer = APIDesigner()

    if args.resources:
        resources = [r.strip() for r in args.resources.split(',')]

        api_spec = designer.design_rest_api(
            name=args.name,
            resources=resources,
            version=args.version,
            include_crud=True
        )

        print(f"\n✅ Created {len(api_spec.endpoints)} endpoints")

        if args.format == 'openapi':
            import json
            openapi = designer.generate_openapi_spec(api_spec)

            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(openapi, f, indent=2)
                print(f"📄 OpenAPI spec saved to: {args.output}")
            else:
                print("\n" + json.dumps(openapi, indent=2))


def database_command(args):
    """Run database visualization"""
    print("🗄️  Generating database diagram")

    visualizer = DatabaseVisualizer()
    schema = visualizer.create_example_schema()

    diagram = visualizer.generate_er_diagram(schema, format=args.format)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(diagram)
        print(f"✅ Diagram saved to: {args.output}")
    else:
        print("\n" + "=" * 80)
        print(diagram)
        print("=" * 80)


def diagram_command(args):
    """Generate custom diagram"""
    print(f"📈 Generating {args.type} diagram")

    generator = DiagramGenerator()

    if args.type == 'flowchart':
        # Example flowchart
        nodes = [
            Node("start", "Start", "default", "rounded"),
            Node("process", "Process Data", "service"),
            Node("decision", "Valid?", "default", "diamond"),
            Node("success", "Success", "service", "rounded"),
            Node("error", "Error", "external", "rounded"),
        ]
        edges = [
            Edge("start", "process"),
            Edge("process", "decision"),
            Edge("decision", "success", "Yes"),
            Edge("decision", "error", "No"),
        ]

        diagram = generator.generate_mermaid_flowchart(
            nodes, edges,
            title=args.title or "Flowchart",
            direction="TB"
        )

        if args.output:
            with open(args.output, 'w') as f:
                f.write(diagram)
            print(f"✅ Diagram saved to: {args.output}")
        else:
            print("\n" + diagram)


def requirements_command(args):
    """Analyze requirements from documents"""
    print(f"📋 Analyzing requirements from {len(args.files)} file(s)")

    analyzer = RequirementsAnalyzer()

    # Analyze documents
    analysis = analyzer.analyze_documents(
        file_paths=args.files,
        auto_categorize=True
    )

    # Display summary
    print(f"\n📊 Requirements Summary:")
    print(f"Total Requirements: {analysis.total_count}")
    print(f"Sources: {', '.join(analysis.sources)}")

    print("\n📋 By Type:")
    for req_type, count in analysis.summary['by_type'].items():
        if count > 0:
            print(f"  {req_type.replace('_', ' ').title()}: {count}")

    print("\n🎯 By Priority:")
    for priority, count in analysis.summary['by_priority'].items():
        if count > 0:
            print(f"  {priority.title()}: {count}")

    # Generate output based on format
    if args.format == 'report':
        output_content = analyzer.generate_requirement_report(analysis)
    elif args.format == 'matrix':
        output_content = analyzer.generate_traceability_matrix(analysis)
    elif args.format == 'usecase':
        output_content = analyzer.generate_use_case_diagram(analysis)
    else:
        output_content = analyzer.generate_requirement_report(analysis)

    # Save or display
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_content)
        print(f"\n✅ Output saved to: {args.output}")
    else:
        print("\n" + "=" * 80)
        print(output_content[:1000] + "\n...\n[Output truncated]")
        print("=" * 80)

    # Show recommendations
    if analysis.recommendations:
        print("\n💡 Recommendations:")
        for i, rec in enumerate(analysis.recommendations, 1):
            print(f"  {i}. {rec}")


def main():
    parser = argparse.ArgumentParser(
        description="Architecture Design Agents - AI-powered architecture design and diagramming",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze architecture
  python main.py architecture --path ./myproject --format mermaid

  # Design API
  python main.py api --name "My API" --resources "Users,Products,Orders"

  # Generate database diagram
  python main.py database --format mermaid --output schema.mmd

  # Generate custom diagram
  python main.py diagram --type flowchart --title "My Process"

  # Analyze requirements
  python main.py requirements --files requirements.txt requirements.xlsx --format report
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Architecture command
    arch_parser = subparsers.add_parser('architecture', help='Analyze architecture')
    arch_parser.add_argument('--path', default='.', help='Path to analyze')
    arch_parser.add_argument('--format', choices=['mermaid', 'c4', 'plantuml', 'drawio'],
                           default='mermaid', help='Diagram format')
    arch_parser.add_argument('--depth', choices=['quick', 'moderate', 'deep'],
                           default='moderate', help='Analysis depth')
    arch_parser.add_argument('--output', help='Output file path')

    # API command
    api_parser = subparsers.add_parser('api', help='Design API')
    api_parser.add_argument('--name', required=True, help='API name')
    api_parser.add_argument('--resources', help='Comma-separated resources')
    api_parser.add_argument('--version', default='1.0.0', help='API version')
    api_parser.add_argument('--format', choices=['openapi', 'graphql'],
                          default='openapi', help='API spec format')
    api_parser.add_argument('--output', help='Output file path')

    # Database command
    db_parser = subparsers.add_parser('database', help='Visualize database')
    db_parser.add_argument('--format', choices=['mermaid', 'plantuml', 'dbml'],
                          default='mermaid', help='Diagram format')
    db_parser.add_argument('--output', help='Output file path')

    # Diagram command
    diag_parser = subparsers.add_parser('diagram', help='Generate diagram')
    diag_parser.add_argument('--type', choices=['flowchart', 'sequence', 'er'],
                            default='flowchart', help='Diagram type')
    diag_parser.add_argument('--title', help='Diagram title')
    diag_parser.add_argument('--output', help='Output file path')

    # Requirements command
    req_parser = subparsers.add_parser('requirements', help='Analyze requirements')
    req_parser.add_argument('--files', nargs='+', required=True,
                           help='Requirement document files (DOCX, XLSX, PDF, TXT, MD, JSON)')
    req_parser.add_argument('--format', choices=['report', 'matrix', 'usecase'],
                           default='report', help='Output format')
    req_parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Route to appropriate command
    if args.command == 'architecture':
        architecture_command(args)
    elif args.command == 'api':
        api_command(args)
    elif args.command == 'database':
        database_command(args)
    elif args.command == 'diagram':
        diagram_command(args)
    elif args.command == 'requirements':
        requirements_command(args)


if __name__ == '__main__':
    main()
