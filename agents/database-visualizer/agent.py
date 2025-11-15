"""
Database Schema Visualizer Agent

This agent creates ER diagrams and database schema visualizations from
database schemas, SQL files, or ORM models.
"""

from typing import List, Dict, Optional, Set
from dataclasses import dataclass, field
from enum import Enum


class FieldType(Enum):
    """Database field types"""
    INTEGER = "int"
    BIGINT = "bigint"
    STRING = "string"
    TEXT = "text"
    BOOLEAN = "boolean"
    DECIMAL = "decimal"
    FLOAT = "float"
    DATE = "date"
    DATETIME = "datetime"
    TIMESTAMP = "timestamp"
    JSON = "json"
    UUID = "uuid"
    BINARY = "binary"


class RelationType(Enum):
    """Database relationship types"""
    ONE_TO_ONE = "one_to_one"
    ONE_TO_MANY = "one_to_many"
    MANY_TO_ONE = "many_to_one"
    MANY_TO_MANY = "many_to_many"


class Cardinality(Enum):
    """ER diagram cardinality notation"""
    ZERO_OR_ONE = "|o--o|"      # 0..1 to 0..1
    ONE_ONLY = "||--||"           # 1 to 1
    ZERO_OR_MORE = "}o--o{"      # 0..* to 0..*
    ONE_OR_MORE = "}|--|{"        # 1..* to 1..*
    MANY_TO_ONE = "}o--||"        # many to 1
    ONE_TO_MANY = "||--o{"        # 1 to many


@dataclass
class Field:
    """Represents a database field/column"""
    name: str
    type: FieldType
    nullable: bool = True
    primary_key: bool = False
    unique: bool = False
    foreign_key: Optional[str] = None
    default: Optional[str] = None
    auto_increment: bool = False
    indexed: bool = False


@dataclass
class Table:
    """Represents a database table"""
    name: str
    fields: List[Field]
    description: Optional[str] = None
    indexes: List[Dict] = field(default_factory=list)
    constraints: List[Dict] = field(default_factory=list)


@dataclass
class Relationship:
    """Represents a relationship between tables"""
    from_table: str
    to_table: str
    relation_type: RelationType
    from_field: str
    to_field: str
    cardinality: Cardinality
    label: Optional[str] = None


@dataclass
class DatabaseSchema:
    """Complete database schema"""
    name: str
    tables: List[Table]
    relationships: List[Relationship]
    description: Optional[str] = None


class DatabaseVisualizer:
    """
    Database Schema Visualizer Agent.

    Features:
    - Generate ER diagrams from database schemas
    - Parse SQL DDL statements
    - Visualize ORM models
    - Create database documentation
    - Identify relationships and constraints
    - Generate migration plans
    """

    def __init__(self):
        self.supported_formats = ["mermaid", "plantuml", "dbml"]

    def generate_er_diagram(
        self,
        schema: DatabaseSchema,
        format: str = "mermaid"
    ) -> str:
        """
        Generate ER diagram from database schema.

        Args:
            schema: Database schema object
            format: Output format (mermaid, plantuml, dbml)

        Returns:
            ER diagram code
        """
        if format == "mermaid":
            return self._generate_mermaid_er(schema)
        elif format == "plantuml":
            return self._generate_plantuml_er(schema)
        elif format == "dbml":
            return self._generate_dbml(schema)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _generate_mermaid_er(self, schema: DatabaseSchema) -> str:
        """Generate Mermaid ER diagram"""
        diagram = "erDiagram\n"

        if schema.description:
            diagram += f"    %% {schema.description}\n\n"

        # Add tables with fields
        for table in schema.tables:
            diagram += f"    {table.name} {{\n"

            for field in table.fields:
                field_type = field.type.value
                field_name = field.name

                # Add key indicators
                key_indicator = ""
                if field.primary_key:
                    key_indicator = "PK"
                elif field.foreign_key:
                    key_indicator = "FK"
                elif field.unique:
                    key_indicator = "UK"

                # Add not null indicator
                nullable = "" if field.nullable else "NOT NULL"

                diagram += f"        {field_type} {field_name} {key_indicator} {nullable}\n"

            diagram += "    }\n\n"

        # Add relationships
        for rel in schema.relationships:
            cardinality = rel.cardinality.value
            label = rel.label or f"{rel.from_field} -> {rel.to_field}"
            diagram += f"    {rel.from_table} {cardinality} {rel.to_table} : {label}\n"

        return diagram

    def _generate_plantuml_er(self, schema: DatabaseSchema) -> str:
        """Generate PlantUML ER diagram"""
        diagram = "@startuml\n"

        if schema.description:
            diagram += f"title {schema.description}\n\n"

        diagram += "' Entity Definitions\n"

        # Add entities
        for table in schema.tables:
            diagram += f"entity {table.name} {{\n"

            # Primary key section
            pk_fields = [f for f in table.fields if f.primary_key]
            if pk_fields:
                for field in pk_fields:
                    diagram += f"  * {field.name} : {field.type.value}\n"
                diagram += "  --\n"

            # Other fields
            other_fields = [f for f in table.fields if not f.primary_key]
            for field in other_fields:
                prefix = "*" if not field.nullable else ""
                fk_indicator = " <<FK>>" if field.foreign_key else ""
                diagram += f"  {prefix} {field.name} : {field.type.value}{fk_indicator}\n"

            diagram += "}\n\n"

        # Add relationships
        diagram += "' Relationships\n"
        for rel in schema.relationships:
            # Convert to PlantUML notation
            if rel.relation_type == RelationType.ONE_TO_ONE:
                notation = "||--||"
            elif rel.relation_type == RelationType.ONE_TO_MANY:
                notation = "||--o{"
            elif rel.relation_type == RelationType.MANY_TO_ONE:
                notation = "}o--||"
            elif rel.relation_type == RelationType.MANY_TO_MANY:
                notation = "}o--o{"
            else:
                notation = "--"

            label = rel.label or ""
            diagram += f"{rel.from_table} {notation} {rel.to_table} : {label}\n"

        diagram += "\n@enduml"
        return diagram

    def _generate_dbml(self, schema: DatabaseSchema) -> str:
        """Generate DBML (Database Markup Language)"""
        dbml = f"// Database: {schema.name}\n"
        if schema.description:
            dbml += f"// {schema.description}\n"
        dbml += "\n"

        # Add tables
        for table in schema.tables:
            dbml += f"Table {table.name} {{\n"

            for field in table.fields:
                field_def = f"  {field.name} {field.type.value}"

                # Add constraints
                constraints = []
                if field.primary_key:
                    constraints.append("pk")
                if not field.nullable:
                    constraints.append("not null")
                if field.unique:
                    constraints.append("unique")
                if field.auto_increment:
                    constraints.append("increment")
                if field.default:
                    constraints.append(f"default: {field.default}")

                if constraints:
                    field_def += f" [{', '.join(constraints)}]"

                dbml += field_def + "\n"

            dbml += "}\n\n"

        # Add relationships
        for rel in schema.relationships:
            from_ref = f"{rel.from_table}.{rel.from_field}"
            to_ref = f"{rel.to_table}.{rel.to_field}"

            if rel.relation_type == RelationType.ONE_TO_ONE:
                dbml += f"Ref: {from_ref} - {to_ref}\n"
            elif rel.relation_type == RelationType.ONE_TO_MANY:
                dbml += f"Ref: {from_ref} < {to_ref}\n"
            elif rel.relation_type == RelationType.MANY_TO_ONE:
                dbml += f"Ref: {from_ref} > {to_ref}\n"
            elif rel.relation_type == RelationType.MANY_TO_MANY:
                dbml += f"Ref: {from_ref} <> {to_ref}\n"

        return dbml

    def parse_sql_schema(self, sql_ddl: str) -> DatabaseSchema:
        """
        Parse SQL DDL statements to extract schema.
        (Simplified implementation - would need full SQL parser for production)
        """
        # This is a simplified example
        # In production, you'd use a proper SQL parser
        tables = []
        # Parsing logic would go here
        return DatabaseSchema(
            name="Parsed Schema",
            tables=tables,
            relationships=[]
        )

    def generate_schema_documentation(self, schema: DatabaseSchema) -> str:
        """Generate markdown documentation for database schema"""
        doc = f"# {schema.name} - Database Schema Documentation\n\n"

        if schema.description:
            doc += f"{schema.description}\n\n"

        doc += "## Tables\n\n"

        for table in schema.tables:
            doc += f"### {table.name}\n\n"

            if table.description:
                doc += f"{table.description}\n\n"

            doc += "| Column | Type | Constraints | Description |\n"
            doc += "|--------|------|-------------|-------------|\n"

            for field in table.fields:
                constraints = []
                if field.primary_key:
                    constraints.append("PRIMARY KEY")
                if not field.nullable:
                    constraints.append("NOT NULL")
                if field.unique:
                    constraints.append("UNIQUE")
                if field.foreign_key:
                    constraints.append(f"FK → {field.foreign_key}")
                if field.auto_increment:
                    constraints.append("AUTO_INCREMENT")
                if field.default:
                    constraints.append(f"DEFAULT {field.default}")

                constraint_str = ", ".join(constraints) if constraints else "-"

                doc += f"| {field.name} | {field.type.value} | {constraint_str} | - |\n"

            doc += "\n"

            # Add indexes
            if table.indexes:
                doc += "**Indexes:**\n"
                for idx in table.indexes:
                    doc += f"- {idx}\n"
                doc += "\n"

        # Add relationships section
        if schema.relationships:
            doc += "## Relationships\n\n"
            doc += "| From | To | Type | Description |\n"
            doc += "|------|-----|------|-------------|\n"

            for rel in schema.relationships:
                from_ref = f"{rel.from_table}.{rel.from_field}"
                to_ref = f"{rel.to_table}.{rel.to_field}"
                rel_type = rel.relation_type.value.replace("_", " ").title()
                label = rel.label or "-"

                doc += f"| {from_ref} | {to_ref} | {rel_type} | {label} |\n"

        return doc

    def create_example_schema(self) -> DatabaseSchema:
        """Create an example e-commerce database schema"""
        users_table = Table(
            name="users",
            description="User accounts",
            fields=[
                Field("id", FieldType.UUID, primary_key=True, nullable=False),
                Field("email", FieldType.STRING, unique=True, nullable=False),
                Field("password_hash", FieldType.STRING, nullable=False),
                Field("name", FieldType.STRING, nullable=False),
                Field("created_at", FieldType.TIMESTAMP, nullable=False),
                Field("updated_at", FieldType.TIMESTAMP, nullable=False)
            ]
        )

        products_table = Table(
            name="products",
            description="Product catalog",
            fields=[
                Field("id", FieldType.UUID, primary_key=True, nullable=False),
                Field("name", FieldType.STRING, nullable=False),
                Field("description", FieldType.TEXT),
                Field("price", FieldType.DECIMAL, nullable=False),
                Field("stock", FieldType.INTEGER, nullable=False, default="0"),
                Field("category_id", FieldType.UUID, foreign_key="categories.id"),
                Field("created_at", FieldType.TIMESTAMP, nullable=False)
            ]
        )

        orders_table = Table(
            name="orders",
            description="Customer orders",
            fields=[
                Field("id", FieldType.UUID, primary_key=True, nullable=False),
                Field("user_id", FieldType.UUID, foreign_key="users.id", nullable=False),
                Field("total", FieldType.DECIMAL, nullable=False),
                Field("status", FieldType.STRING, nullable=False),
                Field("created_at", FieldType.TIMESTAMP, nullable=False),
                Field("updated_at", FieldType.TIMESTAMP, nullable=False)
            ]
        )

        order_items_table = Table(
            name="order_items",
            description="Items in orders",
            fields=[
                Field("id", FieldType.UUID, primary_key=True, nullable=False),
                Field("order_id", FieldType.UUID, foreign_key="orders.id", nullable=False),
                Field("product_id", FieldType.UUID, foreign_key="products.id", nullable=False),
                Field("quantity", FieldType.INTEGER, nullable=False),
                Field("price", FieldType.DECIMAL, nullable=False)
            ]
        )

        categories_table = Table(
            name="categories",
            description="Product categories",
            fields=[
                Field("id", FieldType.UUID, primary_key=True, nullable=False),
                Field("name", FieldType.STRING, nullable=False),
                Field("slug", FieldType.STRING, unique=True, nullable=False),
                Field("parent_id", FieldType.UUID, foreign_key="categories.id")
            ]
        )

        relationships = [
            Relationship("users", "orders", RelationType.ONE_TO_MANY,
                        "id", "user_id", Cardinality.ONE_TO_MANY, "places"),
            Relationship("orders", "order_items", RelationType.ONE_TO_MANY,
                        "id", "order_id", Cardinality.ONE_TO_MANY, "contains"),
            Relationship("products", "order_items", RelationType.ONE_TO_MANY,
                        "id", "product_id", Cardinality.ONE_TO_MANY, "ordered_in"),
            Relationship("categories", "products", RelationType.ONE_TO_MANY,
                        "id", "category_id", Cardinality.ONE_TO_MANY, "has"),
            Relationship("categories", "categories", RelationType.ONE_TO_MANY,
                        "id", "parent_id", Cardinality.ONE_TO_MANY, "parent_of")
        ]

        return DatabaseSchema(
            name="E-commerce Database",
            description="Schema for e-commerce platform",
            tables=[users_table, products_table, orders_table, order_items_table, categories_table],
            relationships=relationships
        )


if __name__ == "__main__":
    # Example usage
    visualizer = DatabaseVisualizer()

    # Create example schema
    schema = visualizer.create_example_schema()

    # Generate Mermaid ER diagram
    mermaid_er = visualizer.generate_er_diagram(schema, format="mermaid")
    print("=== Mermaid ER Diagram ===")
    print(mermaid_er)

    print("\n=== PlantUML ER Diagram ===")
    plantuml_er = visualizer.generate_er_diagram(schema, format="plantuml")
    print(plantuml_er)

    print("\n=== Documentation ===")
    docs = visualizer.generate_schema_documentation(schema)
    print(docs)
