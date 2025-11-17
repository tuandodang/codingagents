"""
Example: Claude-Powered Agentic System

Demonstrates intelligent, autonomous agent execution.
"""

from autonomous.agentic import AgenticSystem

def example_autonomous_goal_execution():
    """Agent autonomously achieves a goal"""
    print("="*60)
    print("Example 1: Autonomous Goal Execution")
    print("="*60)
    
    agentic = AgenticSystem()
    
    # Give agent a high-level goal
    task = agentic.execute_goal(
        goal="Design a secure e-commerce architecture for 10,000 concurrent users",
        context={
            "budget": "$10,000/month",
            "compliance": ["PCI-DSS", "GDPR"],
            "cloud_provider": "AWS"
        }
    )
    
    print("\n📊 Task Results:")
    print(f"  Goal: {task.goal}")
    print(f"  Status: {task.status.value}")
    print(f"  Steps executed: {len(task.reasoning.actions)}")
    print(f"  Thoughts: {len(task.reasoning.thoughts)}")
    print(f"  Reflections: {len(task.reasoning.reflections)}")

def example_multi_agent_collaboration():
    """Multiple agents collaborate on a goal"""
    print("\n" + "="*60)
    print("Example 2: Multi-Agent Collaboration")
    print("="*60)
    
    agentic = AgenticSystem()
    
    # Agents collaborate
    result = agentic.collaborate(
        agents=[
            'architecture_analyzer',
            'security_auditor',
            'devops_designer',
            'iac_generator'
        ],
        goal="Create production-ready infrastructure with security best practices",
        context={"platform": "Azure", "environment": "production"}
    )
    
    print("\n📊 Collaboration Results:")
    print(f"  Agents: {len(result['agents'])}")
    print(f"  Individual results: {len(result['individual_results'])}")
    print(f"  Combined result: {result['combined_result']}")

def example_learning_from_feedback():
    """Agent learns from human feedback"""
    print("\n" + "="*60)
    print("Example 3: Learning from Feedback")
    print("="*60)
    
    agentic = AgenticSystem()
    
    # Execute task
    task = agentic.execute_goal(
        goal="Generate comprehensive test suite for payment processing module"
    )
    
    # Provide feedback
    agentic.learn_from_feedback(
        task=task,
        feedback="Tests covered main paths but missed edge cases for currency conversion",
        rating=3
    )
    
    # Check memory
    memory = agentic.get_memory_summary()
    print("\n📚 Memory Summary:")
    print(f"  Short-term items: {memory['short_term_items']}")
    print(f"  Long-term keys: {memory['long_term_keys']}")

def example_security_goal():
    """Agent autonomously performs security audit"""
    print("\n" + "="*60)
    print("Example 4: Autonomous Security Audit")
    print("="*60)
    
    agentic = AgenticSystem()
    
    task = agentic.execute_goal(
        goal="Perform comprehensive security audit and generate compliance report",
        context={
            "codebase_path": "/src",
            "standards": ["OWASP Top 10", "SANS Top 25"],
            "compliance": ["SOC 2", "ISO 27001"]
        }
    )
    
    print("\n🔐 Security Audit:")
    print(f"  Observations: {len(task.reasoning.observations)}")
    print(f"  Actions taken: {len(task.reasoning.actions)}")
    print(f"  Reflections: {', '.join(task.reasoning.reflections)}")

def example_testing_goal():
    """Agent autonomously generates test suite"""
    print("\n" + "="*60)
    print("Example 5: Autonomous Test Generation")
    print("="*60)
    
    agentic = AgenticSystem()
    
    task = agentic.execute_goal(
        goal="Generate complete test suite with >90% coverage for user authentication module",
        context={
            "module": "auth",
            "test_types": ["unit", "integration", "e2e", "security"],
            "coverage_target": 90
        }
    )
    
    print("\n🧪 Test Generation:")
    print(f"  Plan steps: {len(task.reasoning.actions)}")
    print(f"  Result keys: {list(task.result.keys()) if task.result else []}")

def example_devops_goal():
    """Agent autonomously sets up DevOps pipeline"""
    print("\n" + "="*60)
    print("Example 6: Autonomous DevOps Setup")
    print("="*60)
    
    agentic = AgenticSystem()
    
    task = agentic.execute_goal(
        goal="Design and implement complete CI/CD pipeline with monitoring and auto-scaling",
        context={
            "platform": "GitHub Actions",
            "deployment_target": "Kubernetes",
            "monitoring": "Prometheus + Grafana"
        }
    )
    
    print("\n🚀 DevOps Pipeline:")
    print(f"  Thoughts: {len(task.reasoning.thoughts)}")
    print(f"  Actions: {task.reasoning.actions}")

def main():
    """Run all examples"""
    print("\n🧠 Claude-Powered Agentic System Examples\n")
    
    example_autonomous_goal_execution()
    example_multi_agent_collaboration()
    example_learning_from_feedback()
    example_security_goal()
    example_testing_goal()
    example_devops_goal()
    
    print("\n" + "="*60)
    print("✅ All agentic examples completed!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
