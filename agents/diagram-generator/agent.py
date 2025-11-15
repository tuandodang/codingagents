"""
Diagram Generator Agent

This agent specializes in generating various types of diagrams in multiple formats
including Mermaid, C4, PlantUML, and Draw.io XML.
"""

from typing import List, Dict, Optional, Union
from dataclasses import dataclass
from enum import Enum


class DiagramType(Enum):
    """Supported diagram types"""
    FLOWCHART = "flowchart"
    SEQUENCE = "sequence"
    CLASS = "class"
    ER = "er"
    STATE = "state"
    GANTT = "gantt"
    JOURNEY = "journey"
    C4_CONTEXT = "c4_context"
    C4_CONTAINER = "c4_container"
    C4_COMPONENT = "c4_component"
    C4_CODE = "c4_code"
    COMPONENT = "component"
    DEPLOYMENT = "deployment"


class DiagramFormat(Enum):
    """Supported output formats"""
    MERMAID = "mermaid"
    C4 = "c4"
    PLANTUML = "plantuml"
    DRAWIO = "drawio"


@dataclass
class Node:
    """Represents a node/component in a diagram"""
    id: str
    label: str
    type: str = "default"  # default, database, external, service, etc.
    shape: str = "rectangle"  # rectangle, circle, diamond, cylinder, etc.
    style: Optional[str] = None


@dataclass
class Edge:
    """Represents a connection between nodes"""
    source: str
    target: str
    label: Optional[str] = None
    style: str = "solid"  # solid, dashed, dotted


@dataclass
class DiagramSpec:
    """Specification for diagram generation"""
    title: str
    nodes: List[Node]
    edges: List[Edge]
    diagram_type: DiagramType
    metadata: Optional[Dict] = None


class DiagramGenerator:
    """
    Generates diagrams in multiple formats.

    Supports:
    - Mermaid (all diagram types)
    - C4 Model (Context, Container, Component, Code)
    - PlantUML (all UML diagrams)
    - Draw.io XML format
    """

    def __init__(self):
        self.mermaid_themes = ["default", "forest", "dark", "neutral"]

    def generate(
        self,
        spec: DiagramSpec,
        format: DiagramFormat,
        **kwargs
    ) -> str:
        """
        Generate diagram from specification.

        Args:
            spec: Diagram specification
            format: Output format
            **kwargs: Additional format-specific options

        Returns:
            Diagram code as string
        """
        if format == DiagramFormat.MERMAID:
            return self._generate_mermaid(spec, **kwargs)
        elif format == DiagramFormat.C4:
            return self._generate_c4(spec, **kwargs)
        elif format == DiagramFormat.PLANTUML:
            return self._generate_plantuml(spec, **kwargs)
        elif format == DiagramFormat.DRAWIO:
            return self._generate_drawio(spec, **kwargs)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def generate_mermaid_flowchart(
        self,
        nodes: List[Node],
        edges: List[Edge],
        title: str = "Flowchart",
        direction: str = "TB"
    ) -> str:
        """Generate Mermaid flowchart"""
        diagram = f"graph {direction}\n"
        if title:
            diagram += f"    %% {title}\n\n"

        # Add nodes
        for node in nodes:
            shape_start, shape_end = self._get_mermaid_shape(node.shape)
            diagram += f"    {node.id}{shape_start}{node.label}{shape_end}\n"

        diagram += "\n"

        # Add edges
        for edge in edges:
            arrow = self._get_mermaid_arrow(edge.style)
            label = f"|{edge.label}|" if edge.label else ""
            diagram += f"    {edge.source} {arrow}{label} {edge.target}\n"

        # Add styling
        diagram += self._get_mermaid_styling(nodes)

        return diagram

    def generate_mermaid_sequence(
        self,
        participants: List[str],
        interactions: List[Dict[str, str]],
        title: str = "Sequence Diagram"
    ) -> str:
        """Generate Mermaid sequence diagram"""
        diagram = "sequenceDiagram\n"
        if title:
            diagram += f"    title {title}\n\n"

        # Add participants
        for participant in participants:
            diagram += f"    participant {participant}\n"

        diagram += "\n"

        # Add interactions
        for interaction in interactions:
            source = interaction["from"]
            target = interaction["to"]
            message = interaction["message"]
            style = interaction.get("style", "->")

            if style == "return":
                diagram += f"    {target}-->{source}: {message}\n"
            elif style == "async":
                diagram += f"    {source}->>{target}: {message}\n"
            else:
                diagram += f"    {source}->{target}: {message}\n"

        return diagram

    def generate_mermaid_er(
        self,
        entities: List[Dict],
        relationships: List[Dict],
        title: str = "ER Diagram"
    ) -> str:
        """Generate Mermaid ER diagram"""
        diagram = "erDiagram\n"
        if title:
            diagram += f"    %% {title}\n\n"

        # Add entities with attributes
        for entity in entities:
            name = entity["name"]
            attributes = entity.get("attributes", [])

            diagram += f"    {name} {{\n"
            for attr in attributes:
                attr_type = attr.get("type", "string")
                attr_name = attr["name"]
                key = attr.get("key", "")
                diagram += f"        {attr_type} {attr_name} {key}\n"
            diagram += "    }\n\n"

        # Add relationships
        for rel in relationships:
            entity1 = rel["entity1"]
            entity2 = rel["entity2"]
            cardinality = rel.get("cardinality", "||--o{")
            label = rel.get("label", "")

            diagram += f"    {entity1} {cardinality} {entity2} : {label}\n"

        return diagram

    def generate_c4_context(
        self,
        system_name: str,
        users: List[Dict],
        systems: List[Dict],
        external_systems: List[Dict],
        relationships: List[Dict]
    ) -> str:
        """Generate C4 Context diagram"""
        diagram = "@startuml\n"
        diagram += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml\n\n"
        diagram += "LAYOUT_WITH_LEGEND()\n\n"
        diagram += f"title System Context diagram for {system_name}\n\n"

        # Add users
        for user in users:
            name = user["name"]
            description = user.get("description", "")
            diagram += f'Person({name}, "{name}", "{description}")\n'

        diagram += "\n"

        # Add main system
        for system in systems:
            name = system["name"]
            description = system.get("description", "")
            diagram += f'System({name}, "{name}", "{description}")\n'

        diagram += "\n"

        # Add external systems
        for ext_system in external_systems:
            name = ext_system["name"]
            description = ext_system.get("description", "")
            diagram += f'System_Ext({name}, "{name}", "{description}")\n'

        diagram += "\n"

        # Add relationships
        for rel in relationships:
            source = rel["from"]
            target = rel["to"]
            description = rel.get("description", "Uses")
            technology = rel.get("technology", "")
            diagram += f'Rel({source}, {target}, "{description}", "{technology}")\n'

        diagram += "\n@enduml"
        return diagram

    def generate_c4_container(
        self,
        system_name: str,
        containers: List[Dict],
        databases: List[Dict],
        relationships: List[Dict],
        external_systems: Optional[List[Dict]] = None
    ) -> str:
        """Generate C4 Container diagram"""
        diagram = "@startuml\n"
        diagram += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml\n\n"
        diagram += "LAYOUT_WITH_LEGEND()\n\n"
        diagram += f"title Container diagram for {system_name}\n\n"

        diagram += f'System_Boundary(c1, "{system_name}") {{\n'

        # Add containers
        for container in containers:
            name = container["name"]
            technology = container.get("technology", "")
            description = container.get("description", "")
            diagram += f'    Container({name}, "{name}", "{technology}", "{description}")\n'

        # Add databases
        for db in databases:
            name = db["name"]
            technology = db.get("technology", "Database")
            description = db.get("description", "")
            diagram += f'    ContainerDb({name}, "{name}", "{technology}", "{description}")\n'

        diagram += "}\n\n"

        # Add external systems
        if external_systems:
            for ext in external_systems:
                name = ext["name"]
                description = ext.get("description", "")
                diagram += f'System_Ext({name}, "{name}", "{description}")\n'
            diagram += "\n"

        # Add relationships
        for rel in relationships:
            source = rel["from"]
            target = rel["to"]
            description = rel.get("description", "Uses")
            technology = rel.get("technology", "")
            diagram += f'Rel({source}, {target}, "{description}", "{technology}")\n'

        diagram += "\n@enduml"
        return diagram

    def generate_plantuml_component(
        self,
        components: List[Dict],
        interfaces: List[Dict],
        relationships: List[Dict],
        title: str = "Component Diagram"
    ) -> str:
        """Generate PlantUML component diagram"""
        diagram = "@startuml\n"
        diagram += f"title {title}\n\n"

        # Add components
        for comp in components:
            name = comp["name"]
            comp_type = comp.get("type", "component")
            diagram += f'{comp_type} "{name}" as {name.replace(" ", "_")}\n'

        diagram += "\n"

        # Add interfaces
        for interface in interfaces:
            name = interface["name"]
            diagram += f'interface "{name}" as {name.replace(" ", "_")}\n'

        diagram += "\n"

        # Add relationships
        for rel in relationships:
            source = rel["from"].replace(" ", "_")
            target = rel["to"].replace(" ", "_")
            rel_type = rel.get("type", "-->")
            label = rel.get("label", "")
            diagram += f'{source} {rel_type} {target}'
            if label:
                diagram += f' : {label}'
            diagram += '\n'

        diagram += "\n@enduml"
        return diagram

    def _get_mermaid_shape(self, shape: str) -> tuple:
        """Get Mermaid shape syntax"""
        shapes = {
            "rectangle": ("[", "]"),
            "rounded": ("(", ")"),
            "stadium": ("([", "])"),
            "circle": ("((", "))"),
            "diamond": ("{", "}"),
            "hexagon": ("{{", "}}"),
            "parallelogram": ("[/", "/]"),
            "trapezoid": ("[\\", "\\]"),
            "cylinder": ("[(", ")]"),
            "database": ("[(", ")]")
        }
        return shapes.get(shape, ("[", "]"))

    def _get_mermaid_arrow(self, style: str) -> str:
        """Get Mermaid arrow style"""
        arrows = {
            "solid": "-->",
            "dashed": "-.->",
            "dotted": "-.->",
            "thick": "==>",
            "invisible": "~~~"
        }
        return arrows.get(style, "-->")

    def _get_mermaid_styling(self, nodes: List[Node]) -> str:
        """Generate Mermaid CSS styling"""
        styling = "\n    %% Styling\n"
        styling += "    classDef service fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px\n"
        styling += "    classDef database fill:#50C878,stroke:#2E7D50,color:#fff,stroke-width:2px\n"
        styling += "    classDef external fill:#FF6B6B,stroke:#C44545,color:#fff,stroke-width:2px\n"
        styling += "    classDef cache fill:#FFD93D,stroke:#C7A82E,color:#000,stroke-width:2px\n"

        # Apply classes to nodes
        service_nodes = [n.id for n in nodes if n.type == "service"]
        database_nodes = [n.id for n in nodes if n.type == "database"]
        external_nodes = [n.id for n in nodes if n.type == "external"]
        cache_nodes = [n.id for n in nodes if n.type == "cache"]

        if service_nodes:
            styling += f"    class {','.join(service_nodes)} service\n"
        if database_nodes:
            styling += f"    class {','.join(database_nodes)} database\n"
        if external_nodes:
            styling += f"    class {','.join(external_nodes)} external\n"
        if cache_nodes:
            styling += f"    class {','.join(cache_nodes)} cache\n"

        return styling

    def _generate_mermaid(self, spec: DiagramSpec, **kwargs) -> str:
        """Generate Mermaid diagram from spec"""
        if spec.diagram_type == DiagramType.FLOWCHART:
            direction = kwargs.get("direction", "TB")
            return self.generate_mermaid_flowchart(
                spec.nodes, spec.edges, spec.title, direction
            )
        else:
            # Default to flowchart
            return self.generate_mermaid_flowchart(spec.nodes, spec.edges, spec.title)

    def _generate_c4(self, spec: DiagramSpec, **kwargs) -> str:
        """Generate C4 diagram from spec"""
        # Implementation depends on diagram type
        return self.generate_c4_context(
            spec.title,
            kwargs.get("users", []),
            kwargs.get("systems", []),
            kwargs.get("external_systems", []),
            spec.edges
        )

    def _generate_plantuml(self, spec: DiagramSpec, **kwargs) -> str:
        """Generate PlantUML diagram from spec"""
        components = [{"name": node.label, "type": node.type} for node in spec.nodes]
        relationships = [
            {"from": edge.source, "to": edge.target, "label": edge.label}
            for edge in spec.edges
        ]
        return self.generate_plantuml_component(
            components, [], relationships, spec.title
        )

    def _generate_drawio(self, spec: DiagramSpec, **kwargs) -> str:
        """Generate Draw.io XML from spec"""
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<mxfile host="app.diagrams.net">\n'
        xml += f'  <diagram name="{spec.title}" id="diagram">\n'
        xml += '    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10">\n'
        xml += '      <root>\n'
        xml += '        <mxCell id="0" />\n'
        xml += '        <mxCell id="1" parent="0" />\n'

        # Add nodes
        for i, node in enumerate(spec.nodes):
            x = 100 + (i % 4) * 200
            y = 100 + (i // 4) * 150
            fill_color = self._get_drawio_color(node.type)
            xml += f'        <mxCell id="{node.id}" value="{node.label}" '
            xml += f'style="rounded=1;whiteSpace=wrap;fillColor={fill_color};" '
            xml += 'vertex="1" parent="1">\n'
            xml += f'          <mxGeometry x="{x}" y="{y}" width="120" height="60" as="geometry" />\n'
            xml += '        </mxCell>\n'

        # Add edges
        for i, edge in enumerate(spec.edges):
            xml += f'        <mxCell id="edge_{i}" value="{edge.label or ""}" '
            xml += f'style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" '
            xml += f'source="{edge.source}" target="{edge.target}">\n'
            xml += '          <mxGeometry relative="1" as="geometry" />\n'
            xml += '        </mxCell>\n'

        xml += '      </root>\n'
        xml += '    </mxGraphModel>\n'
        xml += '  </diagram>\n'
        xml += '</mxfile>'
        return xml

    def _get_drawio_color(self, node_type: str) -> str:
        """Get color for draw.io node type"""
        colors = {
            "service": "#dae8fc",
            "database": "#d5e8d4",
            "external": "#f8cecc",
            "cache": "#fff2cc",
            "default": "#e1d5e7"
        }
        return colors.get(node_type, colors["default"])


if __name__ == "__main__":
    # Example usage
    generator = DiagramGenerator()

    # Generate Mermaid flowchart
    nodes = [
        Node("A", "User", "default", "rounded"),
        Node("B", "Web Server", "service"),
        Node("C", "Database", "database", "cylinder"),
    ]
    edges = [
        Edge("A", "B", "HTTP Request"),
        Edge("B", "C", "Query"),
    ]

    flowchart = generator.generate_mermaid_flowchart(
        nodes, edges, "Simple Web App", "LR"
    )
    print(flowchart)
