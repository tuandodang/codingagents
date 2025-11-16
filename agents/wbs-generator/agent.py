"""
WBS (Work Breakdown Structure) Generator Agent

Generates work breakdown structures for project planning, estimation, and presale activities.
Supports creating hierarchical task breakdowns, effort estimation, resource planning, and timeline generation.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union
from enum import Enum
import json


class TaskType(Enum):
    """Types of tasks in WBS"""
    PHASE = "phase"
    DELIVERABLE = "deliverable"
    WORK_PACKAGE = "work_package"
    TASK = "task"
    SUBTASK = "subtask"
    MILESTONE = "milestone"


class TaskStatus(Enum):
    """Task status"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"


class ResourceType(Enum):
    """Resource types"""
    DEVELOPER = "developer"
    ARCHITECT = "architect"
    QA_ENGINEER = "qa_engineer"
    DEVOPS_ENGINEER = "devops_engineer"
    DESIGNER = "designer"
    PROJECT_MANAGER = "project_manager"
    BUSINESS_ANALYST = "business_analyst"
    TECHNICAL_WRITER = "technical_writer"


class EstimationUnit(Enum):
    """Estimation units"""
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"
    STORY_POINTS = "story_points"


@dataclass
class Resource:
    """Represents a project resource"""
    name: str
    type: ResourceType
    hourly_rate: Optional[float] = None
    availability: float = 1.0  # 0.0 to 1.0 (percentage)
    skills: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "type": self.type.value,
            "hourly_rate": self.hourly_rate,
            "availability": self.availability,
            "skills": self.skills
        }


@dataclass
class Estimation:
    """Represents effort estimation"""
    optimistic: float
    likely: float
    pessimistic: float
    unit: EstimationUnit = EstimationUnit.HOURS

    @property
    def pert_estimate(self) -> float:
        """Calculate PERT estimate: (O + 4M + P) / 6"""
        return (self.optimistic + 4 * self.likely + self.pessimistic) / 6

    @property
    def standard_deviation(self) -> float:
        """Calculate standard deviation: (P - O) / 6"""
        return (self.pessimistic - self.optimistic) / 6

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "optimistic": self.optimistic,
            "likely": self.likely,
            "pessimistic": self.pessimistic,
            "pert_estimate": round(self.pert_estimate, 2),
            "standard_deviation": round(self.standard_deviation, 2),
            "unit": self.unit.value
        }


@dataclass
class Task:
    """Represents a task in the WBS"""
    id: str
    name: str
    type: TaskType
    description: Optional[str] = None
    parent_id: Optional[str] = None
    children: List['Task'] = field(default_factory=list)
    estimation: Optional[Estimation] = None
    dependencies: List[str] = field(default_factory=list)
    assigned_resources: List[Resource] = field(default_factory=list)
    status: TaskStatus = TaskStatus.NOT_STARTED
    deliverables: List[str] = field(default_factory=list)
    acceptance_criteria: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    completion_percentage: float = 0.0

    def add_child(self, child: 'Task') -> None:
        """Add a child task"""
        child.parent_id = self.id
        self.children.append(child)

    def total_effort(self) -> float:
        """Calculate total effort including children"""
        effort = self.estimation.pert_estimate if self.estimation else 0
        for child in self.children:
            effort += child.total_effort()
        return effort

    def total_cost(self) -> float:
        """Calculate total cost based on assigned resources"""
        if not self.estimation or not self.assigned_resources:
            return 0.0

        cost = 0.0
        effort_hours = self.estimation.pert_estimate

        # Convert to hours if needed
        if self.estimation.unit == EstimationUnit.DAYS:
            effort_hours *= 8
        elif self.estimation.unit == EstimationUnit.WEEKS:
            effort_hours *= 40

        for resource in self.assigned_resources:
            if resource.hourly_rate:
                cost += effort_hours * resource.hourly_rate * resource.availability

        # Add children costs
        for child in self.children:
            cost += child.total_cost()

        return cost

    def to_dict(self, include_children: bool = True) -> Dict:
        """Convert to dictionary"""
        data = {
            "id": self.id,
            "name": self.name,
            "type": self.type.value,
            "description": self.description,
            "parent_id": self.parent_id,
            "status": self.status.value,
            "completion_percentage": self.completion_percentage,
            "deliverables": self.deliverables,
            "acceptance_criteria": self.acceptance_criteria,
            "risks": self.risks,
            "assumptions": self.assumptions,
            "dependencies": self.dependencies,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

        if self.estimation:
            data["estimation"] = self.estimation.to_dict()
            data["total_effort"] = round(self.total_effort(), 2)
            data["total_cost"] = round(self.total_cost(), 2)

        if self.assigned_resources:
            data["assigned_resources"] = [r.to_dict() for r in self.assigned_resources]

        if include_children and self.children:
            data["children"] = [child.to_dict() for child in self.children]

        return data


@dataclass
class WBSProject:
    """Represents a complete WBS project"""
    name: str
    description: str
    root_tasks: List[Task] = field(default_factory=list)
    resources: List[Resource] = field(default_factory=list)
    budget: Optional[float] = None
    timeline_weeks: Optional[int] = None
    risks: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)

    def add_root_task(self, task: Task) -> None:
        """Add a root-level task"""
        self.root_tasks.append(task)

    def total_effort(self) -> float:
        """Calculate total project effort"""
        return sum(task.total_effort() for task in self.root_tasks)

    def total_cost(self) -> float:
        """Calculate total project cost"""
        return sum(task.total_cost() for task in self.root_tasks)

    def find_task(self, task_id: str, tasks: Optional[List[Task]] = None) -> Optional[Task]:
        """Find a task by ID recursively"""
        if tasks is None:
            tasks = self.root_tasks

        for task in tasks:
            if task.id == task_id:
                return task
            found = self.find_task(task_id, task.children)
            if found:
                return found
        return None

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "description": self.description,
            "root_tasks": [task.to_dict() for task in self.root_tasks],
            "resources": [resource.to_dict() for resource in self.resources],
            "budget": self.budget,
            "timeline_weeks": self.timeline_weeks,
            "total_effort": round(self.total_effort(), 2),
            "total_cost": round(self.total_cost(), 2),
            "risks": self.risks,
            "assumptions": self.assumptions,
            "constraints": self.constraints
        }


class WBSGenerator:
    """
    WBS (Work Breakdown Structure) Generator

    Generates work breakdown structures for project planning, estimation, and presale activities.

    Features:
    - Hierarchical task breakdown
    - Effort estimation (PERT method)
    - Resource allocation and costing
    - Timeline generation
    - Multiple output formats (Mermaid Gantt, JSON, Markdown)
    - Presale proposal generation
    - Risk and assumption tracking
    """

    def __init__(self):
        """Initialize WBS Generator"""
        pass

    def create_project(
        self,
        name: str,
        description: str,
        budget: Optional[float] = None,
        timeline_weeks: Optional[int] = None
    ) -> WBSProject:
        """
        Create a new WBS project.

        Args:
            name: Project name
            description: Project description
            budget: Project budget (optional)
            timeline_weeks: Project timeline in weeks (optional)

        Returns:
            WBSProject instance
        """
        return WBSProject(
            name=name,
            description=description,
            budget=budget,
            timeline_weeks=timeline_weeks
        )

    def generate_mermaid_gantt(self, project: WBSProject) -> str:
        """
        Generate Mermaid Gantt chart from WBS.

        Args:
            project: WBS project

        Returns:
            Mermaid Gantt diagram code
        """
        lines = [
            "gantt",
            f"    title {project.name}",
            "    dateFormat YYYY-MM-DD",
            ""
        ]

        def add_task_to_gantt(task: Task, section_name: Optional[str] = None):
            """Recursively add tasks to Gantt chart"""
            if task.type == TaskType.PHASE:
                lines.append(f"    section {task.name}")
                for child in task.children:
                    add_task_to_gantt(child, task.name)
            else:
                task_line = f"    {task.name}"

                # Add status
                if task.status == TaskStatus.COMPLETED:
                    task_line += " :done"
                elif task.status == TaskStatus.IN_PROGRESS:
                    task_line += " :active"
                else:
                    task_line += " :"

                # Add ID
                task_line += f" {task.id}"

                # Add dependencies
                if task.dependencies:
                    task_line += f", after {' '.join(task.dependencies)}"

                # Add duration
                if task.estimation:
                    duration = int(task.estimation.pert_estimate)
                    unit = task.estimation.unit.value
                    if unit == "hours":
                        duration = max(1, duration // 8)  # Convert to days
                    elif unit == "weeks":
                        duration = duration * 5
                    task_line += f", {duration}d"

                lines.append(task_line)

                # Add children
                for child in task.children:
                    add_task_to_gantt(child, section_name)

        for task in project.root_tasks:
            add_task_to_gantt(task)

        return "\n".join(lines)

    def generate_wbs_tree_mermaid(self, project: WBSProject) -> str:
        """
        Generate Mermaid tree diagram showing WBS hierarchy.

        Args:
            project: WBS project

        Returns:
            Mermaid tree diagram code
        """
        lines = [
            "graph TD",
            f'    ROOT["{project.name}"]',
            ""
        ]

        def add_task_to_tree(task: Task, parent_id: str = "ROOT"):
            """Recursively add tasks to tree diagram"""
            # Create node
            node_id = task.id.replace("-", "_").replace(".", "_")

            # Format label with effort
            label = task.name
            if task.estimation:
                effort = round(task.estimation.pert_estimate, 1)
                label += f"<br/>{effort} {task.estimation.unit.value}"

            lines.append(f'    {node_id}["{label}"]')
            lines.append(f"    {parent_id} --> {node_id}")

            # Add children
            for child in task.children:
                add_task_to_tree(child, node_id)

        for task in project.root_tasks:
            add_task_to_tree(task)

        return "\n".join(lines)

    def generate_markdown_wbs(self, project: WBSProject) -> str:
        """
        Generate Markdown WBS document.

        Args:
            project: WBS project

        Returns:
            Markdown document
        """
        lines = [
            f"# Work Breakdown Structure: {project.name}",
            "",
            f"**Description:** {project.description}",
            "",
        ]

        # Project summary
        lines.extend([
            "## Project Summary",
            "",
            f"- **Total Effort:** {round(project.total_effort(), 2)} hours",
            f"- **Estimated Cost:** ${round(project.total_cost(), 2):,.2f}",
        ])

        if project.budget:
            lines.append(f"- **Budget:** ${project.budget:,.2f}")
            variance = project.budget - project.total_cost()
            lines.append(f"- **Budget Variance:** ${variance:,.2f} ({'under' if variance > 0 else 'over'} budget)")

        if project.timeline_weeks:
            lines.append(f"- **Timeline:** {project.timeline_weeks} weeks")

        lines.extend(["", "---", ""])

        # Risks
        if project.risks:
            lines.extend([
                "## Project Risks",
                "",
            ])
            for risk in project.risks:
                lines.append(f"- {risk}")
            lines.extend(["", "---", ""])

        # Assumptions
        if project.assumptions:
            lines.extend([
                "## Assumptions",
                "",
            ])
            for assumption in project.assumptions:
                lines.append(f"- {assumption}")
            lines.extend(["", "---", ""])

        # Resources
        if project.resources:
            lines.extend([
                "## Resources",
                "",
                "| Resource | Type | Rate | Availability |",
                "|----------|------|------|--------------|",
            ])
            for resource in project.resources:
                rate = f"${resource.hourly_rate}/hr" if resource.hourly_rate else "N/A"
                avail = f"{resource.availability * 100}%"
                lines.append(f"| {resource.name} | {resource.type.value} | {rate} | {avail} |")
            lines.extend(["", "---", ""])

        # Work breakdown
        lines.extend([
            "## Work Breakdown",
            ""
        ])

        def add_task_to_markdown(task: Task, level: int = 2):
            """Recursively add tasks to markdown"""
            indent = "#" * level

            # Task header
            lines.append(f"{indent} {task.name}")
            lines.append("")

            # Task details
            if task.description:
                lines.append(f"**Description:** {task.description}")
                lines.append("")

            lines.append(f"- **ID:** {task.id}")
            lines.append(f"- **Type:** {task.type.value}")
            lines.append(f"- **Status:** {task.status.value}")

            if task.estimation:
                est = task.estimation
                lines.append(f"- **Effort Estimate:**")
                lines.append(f"  - Optimistic: {est.optimistic} {est.unit.value}")
                lines.append(f"  - Likely: {est.likely} {est.unit.value}")
                lines.append(f"  - Pessimistic: {est.pessimistic} {est.unit.value}")
                lines.append(f"  - **PERT Estimate: {round(est.pert_estimate, 2)} {est.unit.value}**")

            if task.assigned_resources:
                lines.append(f"- **Assigned Resources:** {', '.join(r.name for r in task.assigned_resources)}")

            if task.dependencies:
                lines.append(f"- **Dependencies:** {', '.join(task.dependencies)}")

            if task.deliverables:
                lines.append(f"- **Deliverables:**")
                for deliverable in task.deliverables:
                    lines.append(f"  - {deliverable}")

            if task.acceptance_criteria:
                lines.append(f"- **Acceptance Criteria:**")
                for criterion in task.acceptance_criteria:
                    lines.append(f"  - {criterion}")

            if task.risks:
                lines.append(f"- **Risks:**")
                for risk in task.risks:
                    lines.append(f"  - {risk}")

            total_effort = round(task.total_effort(), 2)
            if total_effort > 0:
                lines.append(f"- **Total Effort (including children):** {total_effort} hours")

            total_cost = round(task.total_cost(), 2)
            if total_cost > 0:
                lines.append(f"- **Total Cost (including children):** ${total_cost:,.2f}")

            lines.append("")

            # Children
            for child in task.children:
                add_task_to_markdown(child, level + 1)

        for task in project.root_tasks:
            add_task_to_markdown(task)

        return "\n".join(lines)

    def generate_json_wbs(self, project: WBSProject) -> str:
        """
        Generate JSON representation of WBS.

        Args:
            project: WBS project

        Returns:
            JSON string
        """
        return json.dumps(project.to_dict(), indent=2)

    def generate_presale_proposal(self, project: WBSProject) -> str:
        """
        Generate presale proposal document.

        Args:
            project: WBS project

        Returns:
            Markdown proposal document
        """
        lines = [
            f"# Project Proposal: {project.name}",
            "",
            "## Executive Summary",
            "",
            f"{project.description}",
            "",
            "## Project Overview",
            "",
        ]

        # Key metrics
        total_effort = round(project.total_effort(), 2)
        total_cost = round(project.total_cost(), 2)

        lines.extend([
            "### Key Metrics",
            "",
            f"- **Total Effort:** {total_effort} hours ({round(total_effort / 8, 1)} days)",
            f"- **Estimated Cost:** ${total_cost:,.2f}",
        ])

        if project.budget:
            lines.append(f"- **Client Budget:** ${project.budget:,.2f}")

        if project.timeline_weeks:
            lines.append(f"- **Estimated Timeline:** {project.timeline_weeks} weeks")

        lines.extend(["", "---", ""])

        # Scope
        lines.extend([
            "## Project Scope",
            "",
            "### Deliverables",
            "",
        ])

        # Collect all deliverables
        def collect_deliverables(tasks: List[Task]) -> List[str]:
            deliverables = []
            for task in tasks:
                deliverables.extend(task.deliverables)
                deliverables.extend(collect_deliverables(task.children))
            return deliverables

        all_deliverables = collect_deliverables(project.root_tasks)
        for i, deliverable in enumerate(all_deliverables, 1):
            lines.append(f"{i}. {deliverable}")

        lines.extend(["", "---", ""])

        # Timeline
        lines.extend([
            "## Timeline & Milestones",
            "",
        ])

        # List phases and milestones
        for task in project.root_tasks:
            if task.type == TaskType.PHASE:
                effort = round(task.total_effort(), 2)
                lines.append(f"### {task.name}")
                lines.append(f"- **Effort:** {effort} hours ({round(effort / 8 / 5, 1)} weeks)")
                if task.description:
                    lines.append(f"- **Description:** {task.description}")
                lines.append("")

        lines.extend(["---", ""])

        # Team structure
        if project.resources:
            lines.extend([
                "## Team Structure",
                "",
                "| Role | Resource | Rate | Allocation |",
                "|------|----------|------|------------|",
            ])
            for resource in project.resources:
                rate = f"${resource.hourly_rate}/hr" if resource.hourly_rate else "TBD"
                allocation = f"{resource.availability * 100}%"
                lines.append(f"| {resource.type.value} | {resource.name} | {rate} | {allocation} |")
            lines.extend(["", "---", ""])

        # Cost breakdown
        lines.extend([
            "## Cost Breakdown",
            "",
            "| Phase | Effort (hrs) | Cost |",
            "|-------|--------------|------|",
        ])

        for task in project.root_tasks:
            effort = round(task.total_effort(), 2)
            cost = round(task.total_cost(), 2)
            lines.append(f"| {task.name} | {effort} | ${cost:,.2f} |")

        lines.append(f"| **Total** | **{total_effort}** | **${total_cost:,.2f}** |")
        lines.extend(["", "---", ""])

        # Risks
        if project.risks:
            lines.extend([
                "## Risks & Mitigation",
                "",
            ])
            for i, risk in enumerate(project.risks, 1):
                lines.append(f"{i}. {risk}")
            lines.extend(["", "---", ""])

        # Assumptions
        if project.assumptions:
            lines.extend([
                "## Assumptions",
                "",
            ])
            for i, assumption in enumerate(project.assumptions, 1):
                lines.append(f"{i}. {assumption}")
            lines.extend(["", "---", ""])

        # Constraints
        if project.constraints:
            lines.extend([
                "## Constraints",
                "",
            ])
            for i, constraint in enumerate(project.constraints, 1):
                lines.append(f"{i}. {constraint}")
            lines.extend(["", "---", ""])

        # Next steps
        lines.extend([
            "## Next Steps",
            "",
            "1. Review and approve proposal",
            "2. Sign contract and initiate project",
            "3. Kickoff meeting and requirements gathering",
            "4. Begin execution according to timeline",
            "",
            "---",
            "",
            "## Contact",
            "",
            "For questions or clarifications, please contact the project team.",
            ""
        ])

        return "\n".join(lines)

    def generate_effort_summary(self, project: WBSProject) -> str:
        """
        Generate effort summary by resource type.

        Args:
            project: WBS project

        Returns:
            Markdown summary
        """
        # Collect effort by resource type
        effort_by_type: Dict[ResourceType, float] = {}
        cost_by_type: Dict[ResourceType, float] = {}

        def collect_effort(tasks: List[Task]):
            for task in tasks:
                if task.assigned_resources and task.estimation:
                    effort = task.estimation.pert_estimate
                    for resource in task.assigned_resources:
                        if resource.type not in effort_by_type:
                            effort_by_type[resource.type] = 0
                            cost_by_type[resource.type] = 0

                        effort_by_type[resource.type] += effort
                        if resource.hourly_rate:
                            cost_by_type[resource.type] += effort * resource.hourly_rate

                collect_effort(task.children)

        collect_effort(project.root_tasks)

        # Generate summary
        lines = [
            "# Effort Summary by Resource Type",
            "",
            f"**Project:** {project.name}",
            "",
            "| Resource Type | Total Effort (hrs) | Total Cost |",
            "|---------------|-------------------|------------|",
        ]

        total_effort = 0
        total_cost = 0

        for resource_type, effort in sorted(effort_by_type.items(), key=lambda x: x[1], reverse=True):
            cost = cost_by_type[resource_type]
            total_effort += effort
            total_cost += cost
            lines.append(f"| {resource_type.value} | {round(effort, 2)} | ${round(cost, 2):,.2f} |")

        lines.append(f"| **Total** | **{round(total_effort, 2)}** | **${round(total_cost, 2):,.2f}** |")

        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    # Create WBS Generator
    generator = WBSGenerator()

    # Create project
    project = generator.create_project(
        name="E-Commerce Platform Development",
        description="Build a scalable e-commerce platform with microservices architecture",
        budget=500000,
        timeline_weeks=24
    )

    # Add resources
    project.resources = [
        Resource("John Smith", ResourceType.ARCHITECT, 150.0, 0.5),
        Resource("Jane Doe", ResourceType.DEVELOPER, 100.0, 1.0),
        Resource("Bob Wilson", ResourceType.DEVELOPER, 100.0, 1.0),
        Resource("Alice Brown", ResourceType.QA_ENGINEER, 80.0, 1.0),
        Resource("Charlie Davis", ResourceType.DEVOPS_ENGINEER, 120.0, 0.5),
    ]

    # Add project-level risks and assumptions
    project.risks = [
        "Third-party API availability and performance",
        "Team member availability during holidays",
        "Scope creep from stakeholder requests"
    ]

    project.assumptions = [
        "Client provides requirements within 1 week",
        "Infrastructure provisioning takes max 1 week",
        "No major technology changes during development"
    ]

    # Create WBS structure
    phase1 = Task(
        id="1",
        name="Planning & Analysis",
        type=TaskType.PHASE,
        description="Project planning and requirements analysis"
    )

    # Add tasks to phase 1
    phase1.add_child(Task(
        id="1.1",
        name="Requirements Gathering",
        type=TaskType.WORK_PACKAGE,
        description="Gather and document functional and non-functional requirements",
        estimation=Estimation(40, 60, 80, EstimationUnit.HOURS),
        deliverables=["Requirements Document", "Use Case Diagrams"],
        assigned_resources=[project.resources[0]]
    ))

    phase1.add_child(Task(
        id="1.2",
        name="Architecture Design",
        type=TaskType.WORK_PACKAGE,
        description="Design system architecture and component interactions",
        estimation=Estimation(60, 80, 120, EstimationUnit.HOURS),
        deliverables=["Architecture Document", "C4 Diagrams"],
        dependencies=["1.1"],
        assigned_resources=[project.resources[0]]
    ))

    project.add_root_task(phase1)

    # Generate outputs
    print("=== Mermaid Gantt Chart ===")
    print(generator.generate_mermaid_gantt(project))

    print("\n=== WBS Tree Diagram ===")
    print(generator.generate_wbs_tree_mermaid(project))

    print("\n=== Presale Proposal ===")
    print(generator.generate_presale_proposal(project))
