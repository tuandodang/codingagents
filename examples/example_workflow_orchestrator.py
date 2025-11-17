"""
Example: Autonomous Workflow Orchestrator

Demonstrates end-to-end autonomous workflow execution.
"""

from autonomous.orchestrator import WorkflowOrchestrator, WorkflowStep

def example_complete_architecture_design():
    """Execute complete architecture design workflow"""
    print("="*60)
    print("Example 1: Complete Architecture Design Workflow")
    print("="*60)
    
    orchestrator = WorkflowOrchestrator()
    
    # Get pre-built template
    workflow = orchestrator.get_template('complete_architecture_design')
    
    if workflow:
        # Execute the workflow
        result = orchestrator.execute_workflow(workflow, auto_continue=True)
        
        # Generate report
        report = orchestrator.generate_report(result)
        print("\n" + report)
        
        # Save results
        orchestrator.save_workflow(result, 'workflow_result.json')
        print("\n✅ Workflow results saved to: workflow_result.json")

def example_security_audit():
    """Execute security audit workflow"""
    print("\n" + "="*60)
    print("Example 2: Security Audit Workflow")
    print("="*60)
    
    orchestrator = WorkflowOrchestrator()
    workflow = orchestrator.get_template('security_audit')
    
    if workflow:
        result = orchestrator.execute_workflow(workflow)
        print(f"\n✅ Security audit completed")
        print(f"   Steps: {len(result.steps)}")
        print(f"   Status: {result.status.value}")

def example_custom_workflow():
    """Create and execute custom workflow"""
    print("\n" + "="*60)
    print("Example 3: Custom Workflow")
    print("="*60)
    
    orchestrator = WorkflowOrchestrator()
    
    # Create custom workflow
    custom_steps = [
        WorkflowStep(
            name="review_code",
            agent="code_reviewer",
            action="review_file",
            inputs={"file_path": "app/main.py", "language": "python"}
        ),
        WorkflowStep(
            name="generate_tests",
            agent="test_generator",
            action="generate_unit_tests",
            inputs={"code": "$review_code"}
        ),
        WorkflowStep(
            name="security_scan",
            agent="security_auditor",
            action="scan_code",
            inputs={"code": "$review_code"}
        )
    ]
    
    workflow = orchestrator.create_workflow(
        name="Code Quality Pipeline",
        description="Review code, generate tests, and scan for security issues",
        steps=custom_steps
    )
    
    result = orchestrator.execute_workflow(workflow)
    
    print(f"\n✅ Custom workflow completed")
    print(f"   Results: {len(result.results)} step outputs")

def main():
    """Run all examples"""
    print("\n🤖 Autonomous Workflow Orchestrator Examples\n")
    
    # List available templates
    orchestrator = WorkflowOrchestrator()
    templates = orchestrator.list_templates()
    print(f"Available templates: {len(templates)}")
    for template in templates:
        print(f"  - {template}")
    print()
    
    # Run examples
    example_complete_architecture_design()
    example_security_audit()
    example_custom_workflow()
    
    print("\n" + "="*60)
    print("✅ All workflow examples completed!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
