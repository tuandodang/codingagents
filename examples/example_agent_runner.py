"""
Example: Background Agent Runner

Demonstrates scheduled and event-driven agent execution.
"""

from autonomous.runner import AgentRunner, TriggerType
import time

def example_scheduled_jobs():
    """Schedule jobs to run at intervals"""
    print("="*60)
    print("Example 1: Scheduled Jobs")
    print("="*60 + "\n")
    
    runner = AgentRunner()
    
    # Schedule daily security scan
    runner.schedule_job(
        name="daily_security_scan",
        agent="security_auditor",
        action="scan_vulnerabilities",
        trigger_type=TriggerType.SCHEDULE,
        interval_seconds=86400,  # 24 hours
        parameters={"scan_depth": "deep"}
    )
    
    # Schedule hourly code quality check
    runner.schedule_job(
        name="hourly_code_quality",
        agent="code_reviewer",
        action="review_codebase",
        trigger_type=TriggerType.SCHEDULE,
        interval_seconds=3600,  # 1 hour
        parameters={"path": "/src"}
    )
    
    # Schedule weekly performance tests
    runner.schedule_job(
        name="weekly_performance_tests",
        agent="test_generator",
        action="run_performance_tests",
        trigger_type=TriggerType.SCHEDULE,
        interval_seconds=604800,  # 7 days
        parameters={"load": "high"}
    )
    
    # Start the runner
    runner.start(num_workers=2)
    
    # Let it run for demonstration
    print("\n⏳ Running for 10 seconds...\n")
    time.sleep(10)
    
    # Stop the runner
    runner.stop()
    
    # Show job statuses
    print("\nJob Statuses:")
    for job in runner.list_jobs():
        status = runner.get_job_status(job.name)
        print(f"  - {status['name']}: {status['run_count']} runs")

def example_continuous_monitoring():
    """Continuous monitoring jobs"""
    print("\n" + "="*60)
    print("Example 2: Continuous Monitoring")
    print("="*60 + "\n")
    
    runner = AgentRunner()
    
    # Continuous infrastructure monitoring
    runner.schedule_job(
        name="infrastructure_monitor",
        agent="devops_designer",
        action="monitor_health",
        trigger_type=TriggerType.CONTINUOUS,
        parameters={"check_interval": 5}
    )
    
    # Continuous security monitoring
    runner.schedule_job(
        name="security_monitor",
        agent="security_auditor",
        action="monitor_threats",
        trigger_type=TriggerType.CONTINUOUS,
        parameters={"alert_threshold": "medium"}
    )
    
    runner.start(num_workers=2)
    
    print("\n⏳ Monitoring for 5 seconds...\n")
    time.sleep(5)
    
    runner.stop()

def example_manual_triggers():
    """Manual job triggering"""
    print("\n" + "="*60)
    print("Example 3: Manual Job Triggering")
    print("="*60 + "\n")
    
    runner = AgentRunner()
    
    # Create manual jobs
    runner.schedule_job(
        name="manual_code_review",
        agent="code_reviewer",
        action="review_pr",
        trigger_type=TriggerType.MANUAL,
        parameters={"pr_number": 123}
    )
    
    runner.schedule_job(
        name="manual_security_audit",
        agent="security_auditor",
        action="full_audit",
        trigger_type=TriggerType.MANUAL
    )
    
    runner.start(num_workers=2)
    
    # Manually trigger jobs
    print("Manually triggering jobs...\n")
    runner.trigger_job("manual_code_review")
    runner.trigger_job("manual_security_audit")
    
    time.sleep(5)
    
    runner.stop()

def example_job_management():
    """Demonstrate job enable/disable"""
    print("\n" + "="*60)
    print("Example 4: Job Management")
    print("="*60 + "\n")
    
    runner = AgentRunner()
    
    # Create jobs
    runner.schedule_job(
        name="test_job_1",
        agent="test_generator",
        action="test",
        trigger_type=TriggerType.SCHEDULE,
        interval_seconds=60
    )
    
    runner.schedule_job(
        name="test_job_2",
        agent="code_reviewer",
        action="review",
        trigger_type=TriggerType.SCHEDULE,
        interval_seconds=60
    )
    
    # Disable a job
    runner.disable_job("test_job_1")
    
    # Enable it again
    runner.enable_job("test_job_1")
    
    # List all jobs
    print("All jobs:")
    for job in runner.list_jobs():
        print(f"  - {job.name} (enabled: {job.enabled})")

def main():
    """Run all examples"""
    print("\n⏰ Background Agent Runner Examples\n")
    
    example_scheduled_jobs()
    example_continuous_monitoring()
    example_manual_triggers()
    example_job_management()
    
    print("\n" + "="*60)
    print("✅ All runner examples completed!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
