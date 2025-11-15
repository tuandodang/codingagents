"""
Architecture Analyzer Agent

This agent analyzes codebases to understand their architecture and generates
appropriate architecture diagrams in various formats.
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict


@dataclass
class Component:
    """Represents a component in the architecture"""
    name: str
    type: str  # service, module, layer, database, external
    description: str
    technologies: List[str]
    dependencies: List[str]
    path: Optional[str] = None


@dataclass
class ArchitectureAnalysis:
    """Results of architecture analysis"""
    components: List[Component]
    architecture_pattern: str  # MVC, microservices, layered, etc.
    technology_stack: Dict[str, List[str]]
    data_flow: List[Dict[str, str]]
    external_dependencies: List[str]
    recommendations: List[str]


class ArchitectureAnalyzer:
    """
    Analyzes codebases and generates architecture diagrams.

    This agent can:
    1. Scan directory structure to identify components
    2. Analyze code to detect patterns and dependencies
    3. Identify technology stack
    4. Generate architecture diagrams in multiple formats
    5. Provide architecture recommendations
    """

    def __init__(self):
        self.supported_formats = ["mermaid", "c4", "plantuml", "drawio"]
        self.framework_indicators = {
            "react": ["package.json", "jsx", "tsx"],
            "vue": ["package.json", ".vue"],
            "angular": ["angular.json", ".component.ts"],
            "django": ["manage.py", "settings.py", "wsgi.py"],
            "flask": ["app.py", "flask"],
            "fastapi": ["main.py", "fastapi"],
            "spring": ["pom.xml", "application.properties"],
            "express": ["package.json", "express"],
            "nextjs": ["next.config.js"],
            "nestjs": ["nest-cli.json"]
        }

    def analyze_codebase(
        self,
        path: str,
        diagram_format: str = "mermaid",
        depth: str = "moderate"
    ) -> Dict:
        """
        Analyze a codebase and generate architecture diagram.

        Args:
            path: Path to codebase
            diagram_format: Output format (mermaid, c4, plantuml, drawio)
            depth: Analysis depth (quick, moderate, deep)

        Returns:
            Dict containing analysis results and diagram
        """
        if diagram_format not in self.supported_formats:
            raise ValueError(f"Unsupported format. Use one of: {self.supported_formats}")

        # Perform analysis
        analysis = self._analyze_structure(path, depth)

        # Generate diagram based on format
        diagram = self._generate_diagram(analysis, diagram_format)

        return {
            "analysis": asdict(analysis),
            "diagram": diagram,
            "format": diagram_format
        }

    def _analyze_structure(self, path: str, depth: str) -> ArchitectureAnalysis:
        """Analyze the codebase structure"""
        components = []
        tech_stack = {
            "frontend": [],
            "backend": [],
            "database": [],
            "infrastructure": [],
            "other": []
        }

        # Detect project type and components
        project_path = Path(path)

        # Check for common project structures
        if (project_path / "package.json").exists():
            tech_stack["frontend"].append("JavaScript/Node.js")
            components.append(Component(
                name="Frontend",
                type="module",
                description="Frontend application",
                technologies=["JavaScript"],
                dependencies=[]
            ))

        if (project_path / "requirements.txt").exists() or (project_path / "pyproject.toml").exists():
            tech_stack["backend"].append("Python")
            components.append(Component(
                name="Backend",
                type="service",
                description="Backend service",
                technologies=["Python"],
                dependencies=[]
            ))

        if (project_path / "pom.xml").exists() or (project_path / "build.gradle").exists():
            tech_stack["backend"].append("Java")
            components.append(Component(
                name="Backend",
                type="service",
                description="Backend service",
                technologies=["Java"],
                dependencies=[]
            ))

        # Detect architecture pattern
        pattern = self._detect_architecture_pattern(project_path)

        return ArchitectureAnalysis(
            components=components,
            architecture_pattern=pattern,
            technology_stack=tech_stack,
            data_flow=[],
            external_dependencies=[],
            recommendations=self._generate_recommendations(components, pattern)
        )

    def _detect_architecture_pattern(self, path: Path) -> str:
        """Detect the architecture pattern used"""
        # Check for microservices
        if (path / "docker-compose.yml").exists() or list(path.glob("**/Dockerfile")):
            return "Microservices"

        # Check for MVC
        if (path / "models").exists() and (path / "views").exists() and (path / "controllers").exists():
            return "MVC"

        # Check for layered
        if (path / "domain").exists() or (path / "application").exists() or (path / "infrastructure").exists():
            return "Layered/Clean Architecture"

        return "Monolithic"

    def _generate_recommendations(self, components: List[Component], pattern: str) -> List[str]:
        """Generate architecture recommendations"""
        recommendations = []

        if pattern == "Monolithic" and len(components) > 5:
            recommendations.append(
                "Consider migrating to microservices for better scalability"
            )

        recommendations.append(
            "Implement API gateway for better security and routing"
        )
        recommendations.append(
            "Add caching layer (Redis/Memcached) for improved performance"
        )
        recommendations.append(
            "Consider implementing event-driven architecture for async operations"
        )

        return recommendations

    def _generate_diagram(self, analysis: ArchitectureAnalysis, format: str) -> str:
        """Generate diagram in specified format"""
        if format == "mermaid":
            return self._generate_mermaid(analysis)
        elif format == "c4":
            return self._generate_c4(analysis)
        elif format == "plantuml":
            return self._generate_plantuml(analysis)
        elif format == "drawio":
            return self._generate_drawio(analysis)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _generate_mermaid(self, analysis: ArchitectureAnalysis) -> str:
        """Generate Mermaid diagram"""
        diagram = "graph TB\n"
        diagram += "    %% Architecture Diagram\n\n"

        # Add components
        for i, component in enumerate(analysis.components):
            node_id = f"comp{i}"
            diagram += f"    {node_id}[{component.name}]\n"

        # Add relationships
        if len(analysis.components) > 1:
            diagram += "\n    %% Relationships\n"
            for i in range(len(analysis.components) - 1):
                diagram += f"    comp{i} --> comp{i+1}\n"

        # Add styling
        diagram += "\n    %% Styling\n"
        diagram += "    classDef service fill:#4A90E2,stroke:#2E5C8A,color:#fff\n"
        diagram += "    classDef database fill:#50C878,stroke:#2E7D50,color:#fff\n"
        diagram += "    classDef external fill:#FF6B6B,stroke:#C44545,color:#fff\n"

        return diagram

    def _generate_c4(self, analysis: ArchitectureAnalysis) -> str:
        """Generate C4 model diagram (as PlantUML)"""
        diagram = "@startuml\n"
        diagram += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml\n\n"
        diagram += f"LAYOUT_WITH_LEGEND()\n\n"
        diagram += f"title Container Diagram - {analysis.architecture_pattern}\n\n"

        # Add containers
        for component in analysis.components:
            tech = ", ".join(component.technologies) if component.technologies else "Technology"
            diagram += f'Container({component.name.replace(" ", "_")}, "{component.name}", "{tech}", "{component.description}")\n'

        # Add relationships
        if len(analysis.components) > 1:
            diagram += "\n"
            for i in range(len(analysis.components) - 1):
                comp1 = analysis.components[i].name.replace(" ", "_")
                comp2 = analysis.components[i+1].name.replace(" ", "_")
                diagram += f'Rel({comp1}, {comp2}, "Uses")\n'

        diagram += "@enduml"
        return diagram

    def _generate_plantuml(self, analysis: ArchitectureAnalysis) -> str:
        """Generate PlantUML component diagram"""
        diagram = "@startuml\n"
        diagram += f"title {analysis.architecture_pattern} Architecture\n\n"

        # Add components
        for component in analysis.components:
            comp_type = "component" if component.type == "module" else "database" if component.type == "database" else "node"
            diagram += f'{comp_type} "{component.name}" as {component.name.replace(" ", "_")}\n'

        # Add relationships
        if len(analysis.components) > 1:
            diagram += "\n"
            for i in range(len(analysis.components) - 1):
                comp1 = analysis.components[i].name.replace(" ", "_")
                comp2 = analysis.components[i+1].name.replace(" ", "_")
                diagram += f'{comp1} --> {comp2}\n'

        diagram += "@enduml"
        return diagram

    def _generate_drawio(self, analysis: ArchitectureAnalysis) -> str:
        """Generate draw.io XML format"""
        # Basic draw.io XML structure
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<mxfile host="app.diagrams.net" modified="2024-01-01T00:00:00.000Z" agent="Architecture Analyzer" version="21.1.0">\n'
        xml += '  <diagram name="Architecture" id="architecture">\n'
        xml += '    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">\n'
        xml += '      <root>\n'
        xml += '        <mxCell id="0" />\n'
        xml += '        <mxCell id="1" parent="0" />\n'

        # Add components as cells
        y_pos = 100
        for i, component in enumerate(analysis.components):
            cell_id = f"component_{i}"
            x_pos = 100 + (i * 200)
            xml += f'        <mxCell id="{cell_id}" value="{component.name}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">\n'
            xml += f'          <mxGeometry x="{x_pos}" y="{y_pos}" width="120" height="60" as="geometry" />\n'
            xml += '        </mxCell>\n'

        # Add connections
        for i in range(len(analysis.components) - 1):
            edge_id = f"edge_{i}"
            source = f"component_{i}"
            target = f"component_{i+1}"
            xml += f'        <mxCell id="{edge_id}" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="{source}" target="{target}">\n'
            xml += '          <mxGeometry relative="1" as="geometry" />\n'
            xml += '        </mxCell>\n'

        xml += '      </root>\n'
        xml += '    </mxGraphModel>\n'
        xml += '  </diagram>\n'
        xml += '</mxfile>'

        return xml


if __name__ == "__main__":
    # Example usage
    analyzer = ArchitectureAnalyzer()
    result = analyzer.analyze_codebase(
        path=".",
        diagram_format="mermaid",
        depth="moderate"
    )
    print(json.dumps(result, indent=2, default=str))
