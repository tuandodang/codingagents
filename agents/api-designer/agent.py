"""
API Design Agent

This agent helps design and document APIs with specifications and diagrams.
Supports REST, GraphQL, gRPC, and generates OpenAPI/Swagger specs.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum
import json


class APIType(Enum):
    """Supported API types"""
    REST = "rest"
    GRAPHQL = "graphql"
    GRPC = "grpc"
    WEBSOCKET = "websocket"


class HTTPMethod(Enum):
    """HTTP methods"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


@dataclass
class APIEndpoint:
    """Represents a single API endpoint"""
    path: str
    method: HTTPMethod
    summary: str
    description: str
    request_body: Optional[Dict] = None
    response: Optional[Dict] = None
    parameters: List[Dict] = field(default_factory=list)
    authentication: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class APISpecification:
    """Complete API specification"""
    name: str
    version: str
    description: str
    base_url: str
    api_type: APIType
    endpoints: List[APIEndpoint]
    authentication_schemes: List[Dict] = field(default_factory=list)
    servers: List[Dict] = field(default_factory=list)


class APIDesigner:
    """
    API Design Agent that helps design and document APIs.

    Features:
    - Generate OpenAPI/Swagger specifications
    - Create API sequence diagrams
    - Design RESTful endpoints
    - Generate GraphQL schemas
    - Create gRPC service definitions
    - Provide API best practices and recommendations
    """

    def __init__(self):
        self.openapi_version = "3.0.0"

    def design_rest_api(
        self,
        name: str,
        resources: List[str],
        version: str = "1.0.0",
        include_crud: bool = True
    ) -> APISpecification:
        """
        Design a RESTful API based on resources.

        Args:
            name: API name
            resources: List of resource names (e.g., ['users', 'products', 'orders'])
            version: API version
            include_crud: Whether to include full CRUD operations

        Returns:
            APISpecification object
        """
        endpoints = []

        for resource in resources:
            resource_lower = resource.lower()
            resource_singular = resource_lower.rstrip('s')

            if include_crud:
                # GET all
                endpoints.append(APIEndpoint(
                    path=f"/{resource_lower}",
                    method=HTTPMethod.GET,
                    summary=f"List all {resource_lower}",
                    description=f"Retrieve a list of {resource_lower}",
                    parameters=[
                        {"name": "page", "in": "query", "type": "integer"},
                        {"name": "limit", "in": "query", "type": "integer"},
                        {"name": "sort", "in": "query", "type": "string"}
                    ],
                    response={"type": "array", "items": resource_singular},
                    tags=[resource]
                ))

                # GET by ID
                endpoints.append(APIEndpoint(
                    path=f"/{resource_lower}/{{id}}",
                    method=HTTPMethod.GET,
                    summary=f"Get {resource_singular} by ID",
                    description=f"Retrieve a single {resource_singular}",
                    parameters=[
                        {"name": "id", "in": "path", "required": True, "type": "string"}
                    ],
                    response={"type": "object", "schema": resource_singular},
                    authentication="Bearer",
                    tags=[resource]
                ))

                # POST
                endpoints.append(APIEndpoint(
                    path=f"/{resource_lower}",
                    method=HTTPMethod.POST,
                    summary=f"Create {resource_singular}",
                    description=f"Create a new {resource_singular}",
                    request_body={"type": "object", "schema": f"{resource_singular}Create"},
                    response={"type": "object", "schema": resource_singular},
                    authentication="Bearer",
                    tags=[resource]
                ))

                # PUT
                endpoints.append(APIEndpoint(
                    path=f"/{resource_lower}/{{id}}",
                    method=HTTPMethod.PUT,
                    summary=f"Update {resource_singular}",
                    description=f"Update an existing {resource_singular}",
                    parameters=[
                        {"name": "id", "in": "path", "required": True, "type": "string"}
                    ],
                    request_body={"type": "object", "schema": f"{resource_singular}Update"},
                    response={"type": "object", "schema": resource_singular},
                    authentication="Bearer",
                    tags=[resource]
                ))

                # DELETE
                endpoints.append(APIEndpoint(
                    path=f"/{resource_lower}/{{id}}",
                    method=HTTPMethod.DELETE,
                    summary=f"Delete {resource_singular}",
                    description=f"Delete a {resource_singular}",
                    parameters=[
                        {"name": "id", "in": "path", "required": True, "type": "string"}
                    ],
                    response={"type": "object", "properties": {"message": "string"}},
                    authentication="Bearer",
                    tags=[resource]
                ))

        return APISpecification(
            name=name,
            version=version,
            description=f"{name} API",
            base_url="https://api.example.com/v1",
            api_type=APIType.REST,
            endpoints=endpoints,
            authentication_schemes=[
                {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
            ]
        )

    def generate_openapi_spec(self, api_spec: APISpecification) -> Dict:
        """Generate OpenAPI 3.0 specification"""
        spec = {
            "openapi": self.openapi_version,
            "info": {
                "title": api_spec.name,
                "version": api_spec.version,
                "description": api_spec.description
            },
            "servers": api_spec.servers or [
                {"url": api_spec.base_url}
            ],
            "paths": {},
            "components": {
                "securitySchemes": {},
                "schemas": {}
            }
        }

        # Add authentication schemes
        for auth in api_spec.authentication_schemes:
            scheme_name = auth.get("name", "bearerAuth")
            spec["components"]["securitySchemes"][scheme_name] = {
                "type": auth["type"],
                "scheme": auth.get("scheme", "bearer"),
                "bearerFormat": auth.get("bearerFormat", "JWT")
            }

        # Add endpoints
        for endpoint in api_spec.endpoints:
            path = endpoint.path
            method = endpoint.method.value.lower()

            if path not in spec["paths"]:
                spec["paths"][path] = {}

            operation = {
                "summary": endpoint.summary,
                "description": endpoint.description,
                "tags": endpoint.tags,
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": endpoint.response or {}
                            }
                        }
                    }
                }
            }

            # Add parameters
            if endpoint.parameters:
                operation["parameters"] = endpoint.parameters

            # Add request body
            if endpoint.request_body:
                operation["requestBody"] = {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": endpoint.request_body
                        }
                    }
                }

            # Add security
            if endpoint.authentication:
                operation["security"] = [{"bearerAuth": []}]

            spec["paths"][path][method] = operation

        return spec

    def generate_sequence_diagram(
        self,
        endpoint: APIEndpoint,
        include_auth: bool = True
    ) -> str:
        """Generate Mermaid sequence diagram for API endpoint"""
        diagram = "sequenceDiagram\n"
        diagram += "    autonumber\n"
        diagram += "    actor Client\n"
        diagram += "    participant Gateway as API Gateway\n"

        if include_auth and endpoint.authentication:
            diagram += "    participant Auth as Auth Service\n"

        diagram += f"    participant API as {endpoint.tags[0] if endpoint.tags else 'API'} Service\n"
        diagram += "    participant DB as Database\n\n"

        # Request flow
        diagram += f"    Client->>Gateway: {endpoint.method.value} {endpoint.path}\n"

        if include_auth and endpoint.authentication:
            diagram += "    Gateway->>Auth: Validate Token\n"
            diagram += "    Auth-->>Gateway: Token Valid\n\n"

        diagram += "    Gateway->>API: Forward Request\n"

        # Database operations based on method
        if endpoint.method == HTTPMethod.GET:
            diagram += "    API->>DB: SELECT Query\n"
            diagram += "    DB-->>API: Return Data\n"
        elif endpoint.method == HTTPMethod.POST:
            diagram += "    API->>API: Validate Data\n"
            diagram += "    API->>DB: INSERT Query\n"
            diagram += "    DB-->>API: Confirm Insert\n"
        elif endpoint.method in [HTTPMethod.PUT, HTTPMethod.PATCH]:
            diagram += "    API->>DB: SELECT (check exists)\n"
            diagram += "    DB-->>API: Record Found\n"
            diagram += "    API->>DB: UPDATE Query\n"
            diagram += "    DB-->>API: Confirm Update\n"
        elif endpoint.method == HTTPMethod.DELETE:
            diagram += "    API->>DB: DELETE Query\n"
            diagram += "    DB-->>API: Confirm Delete\n"

        # Response flow
        diagram += "\n    API-->>Gateway: Response\n"
        diagram += "    Gateway-->>Client: 200 OK\n"

        return diagram

    def generate_graphql_schema(
        self,
        types: List[Dict],
        queries: List[Dict],
        mutations: List[Dict]
    ) -> str:
        """Generate GraphQL schema"""
        schema = "# GraphQL Schema\n\n"

        # Add types
        for type_def in types:
            schema += f"type {type_def['name']} {{\n"
            for field in type_def.get('fields', []):
                field_type = field['type']
                nullable = "" if field.get('required', True) else ""
                schema += f"  {field['name']}: {field_type}{'!' if field.get('required') else ''}\n"
            schema += "}\n\n"

        # Add Query type
        if queries:
            schema += "type Query {\n"
            for query in queries:
                args = ", ".join([f"{arg['name']}: {arg['type']}" for arg in query.get('args', [])])
                schema += f"  {query['name']}({args}): {query['returns']}\n"
            schema += "}\n\n"

        # Add Mutation type
        if mutations:
            schema += "type Mutation {\n"
            for mutation in mutations:
                args = ", ".join([f"{arg['name']}: {arg['type']}" for arg in mutation.get('args', [])])
                schema += f"  {mutation['name']}({args}): {mutation['returns']}\n"
            schema += "}\n"

        return schema

    def generate_recommendations(self, api_spec: APISpecification) -> List[str]:
        """Generate API design recommendations"""
        recommendations = []

        recommendations.append("✓ Use versioning in URL (e.g., /v1/) or headers")
        recommendations.append("✓ Implement rate limiting to prevent abuse")
        recommendations.append("✓ Use HTTPS for all endpoints")
        recommendations.append("✓ Implement proper error handling with consistent error responses")
        recommendations.append("✓ Use pagination for list endpoints (limit, offset or cursor-based)")
        recommendations.append("✓ Implement request validation and sanitization")
        recommendations.append("✓ Use proper HTTP status codes (200, 201, 400, 401, 404, 500, etc.)")
        recommendations.append("✓ Add API documentation (Swagger/OpenAPI, Postman collections)")
        recommendations.append("✓ Implement logging and monitoring")
        recommendations.append("✓ Use API Gateway for cross-cutting concerns (auth, rate limiting, logging)")
        recommendations.append("✓ Consider implementing HATEOAS for better API discoverability")
        recommendations.append("✓ Use ETags for caching and optimistic concurrency control")

        return recommendations


if __name__ == "__main__":
    # Example usage
    designer = APIDesigner()

    # Design REST API
    api_spec = designer.design_rest_api(
        name="E-commerce API",
        resources=["Users", "Products", "Orders"],
        version="1.0.0"
    )

    # Generate OpenAPI spec
    openapi = designer.generate_openapi_spec(api_spec)
    print(json.dumps(openapi, indent=2))

    # Generate sequence diagram for first endpoint
    if api_spec.endpoints:
        sequence = designer.generate_sequence_diagram(api_spec.endpoints[0])
        print("\n" + sequence)
