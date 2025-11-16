"""Example: DevOps Pipeline Designer"""
from agents.devops_designer import DevOpsDesigner

def main():
    print("=== DevOps Pipeline Design Example ===\n")
    
    designer = DevOpsDesigner()
    
    requirements = {
        "project_type": "web_application",
        "language": "python",
        "framework": "django",
        "deployment_target": "kubernetes",
        "environments": ["dev", "staging", "prod"]
    }
    
    pipeline = designer.design_pipeline(requirements)
    
    print(f"Pipeline: {pipeline.name}")
    print(f"Stages: {len(pipeline.stages)}")
    for stage in pipeline.stages:
        print(f"\n  - {stage.name}")
        for step in stage.steps:
            print(f"    * {step}")
    
    # Generate GitHub Actions workflow
    print("\n" + "="*60)
    print("GitHub Actions Workflow:")
    print("="*60)
    workflow = designer.generate_github_actions(pipeline)
    print(workflow)

if __name__ == "__main__":
    main()
