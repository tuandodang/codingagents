"""Example: Infrastructure as Code Generator"""
from agents.iac_generator import IaCGenerator

def main():
    print("=== Infrastructure as Code Generation Example ===\n")
    
    generator = IaCGenerator()
    
    architecture = {
        "provider": "aws",
        "components": [
            {"type": "vpc", "cidr": "10.0.0.0/16"},
            {"type": "subnet", "cidr": "10.0.1.0/24", "availability_zone": "us-east-1a"},
            {"type": "eks_cluster", "name": "app-cluster", "version": "1.27"},
            {"type": "rds", "engine": "postgresql", "version": "15", "instance_class": "db.t3.medium"},
            {"type": "s3_bucket", "name": "app-storage", "encryption": True}
        ]
    }
    
    # Generate Terraform code
    print("Generating Terraform code...")
    terraform_code = generator.generate_terraform(architecture)
    print("\n" + "="*60)
    print("Terraform Configuration:")
    print("="*60)
    print(terraform_code)
    
    # Generate CloudFormation
    print("\n" + "="*60)
    print("CloudFormation Template:")
    print("="*60)
    cf_template = generator.generate_cloudformation(architecture)
    print(cf_template)

if __name__ == "__main__":
    main()
