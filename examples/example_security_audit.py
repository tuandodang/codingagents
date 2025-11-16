"""Example: Security Auditor"""
from agents.security_auditor import SecurityAuditor

def main():
    print("=== Security Audit Example ===\n")
    
    auditor = SecurityAuditor()
    
    # Architecture security audit
    print("Auditing architecture for security vulnerabilities...")
    
    # Code security audit (SAST)
    code = """
    password = "hardcoded_password"
    api_key = "sk-1234567890"
    """
    
    audit = auditor.audit_code(code, language="python")
    
    print(f"Security Score: {audit.security_score}/100")
    print(f"Vulnerabilities: {len(audit.vulnerabilities)}")
    
    for vuln in audit.vulnerabilities:
        print(f"\n[{vuln.severity.value.upper()}] {vuln.title}")
        print(f"  Remediation: {vuln.remediation}")

if __name__ == "__main__":
    main()
