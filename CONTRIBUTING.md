# Contributing to Architecture Design Agents

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

- Check if the bug has already been reported in Issues
- Use the bug report template
- Include detailed steps to reproduce
- Provide example code or diagrams
- Include system information (OS, Python version, etc.)

### Suggesting Enhancements

- Check if the enhancement has been suggested
- Use the feature request template
- Explain the use case clearly
- Provide examples of how it would work
- Consider backward compatibility

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/codingagents.git
cd codingagents

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=agents

# Run specific test file
pytest tests/test_architecture_analyzer.py
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy agents/
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints for function signatures
- Write docstrings for all public functions and classes
- Keep functions focused and small
- Use meaningful variable names

### Example

```python
def generate_diagram(
    nodes: List[Node],
    edges: List[Edge],
    title: str = "Diagram"
) -> str:
    """
    Generate a Mermaid diagram from nodes and edges.

    Args:
        nodes: List of Node objects
        edges: List of Edge objects
        title: Diagram title (default: "Diagram")

    Returns:
        Mermaid diagram code as string
    """
    # Implementation
    pass
```

## Project Structure

```
codingagents/
├── agents/              # Agent implementations
│   ├── architecture-analyzer/
│   ├── diagram-generator/
│   ├── api-designer/
│   └── database-visualizer/
├── skills/              # Reusable skills
├── utils/               # Utility functions
├── examples/            # Example scripts
├── tests/               # Test files
└── docs/                # Documentation
```

## Adding a New Agent

1. Create agent directory in `agents/`
2. Implement `agent.py` with main logic
3. Create `prompt.md` with agent instructions
4. Add tests in `tests/test_agentname.py`
5. Add example in `examples/example_agentname.py`
6. Update main README.md
7. Update GETTING_STARTED.md

### Agent Template

```python
"""
Agent Name

Description of what this agent does.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class AgentInput:
    """Input for the agent"""
    pass


@dataclass
class AgentOutput:
    """Output from the agent"""
    pass


class AgentName:
    """
    Agent description and capabilities.

    Features:
    - Feature 1
    - Feature 2
    - Feature 3
    """

    def __init__(self):
        pass

    def process(self, input: AgentInput) -> AgentOutput:
        """
        Main processing method.

        Args:
            input: Agent input

        Returns:
            Agent output
        """
        pass
```

## Adding Diagram Formats

When adding support for new diagram formats:

1. Add format to appropriate agent
2. Implement generator method
3. Add tests for the format
4. Add examples
5. Update documentation
6. Add to README features list

## Documentation

- Update README.md for user-facing changes
- Update GETTING_STARTED.md for new features
- Add inline code comments for complex logic
- Update agent prompts for capability changes
- Add examples for new features

## Commit Messages

Use clear, descriptive commit messages:

```
Add C4 code diagram support to diagram generator

- Implement generate_c4_code method
- Add tests for code diagram generation
- Update documentation
- Add example usage
```

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Test edge cases
- Include integration tests where applicable

## Questions?

- Open an issue for questions
- Check existing issues and discussions
- Review documentation
- Ask in pull request comments

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow
- Maintain a positive environment

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🎉
