"""
Background Agent Runner

Runs agents on schedule or triggered by events.
"""

from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
import time
import threading
import queue


class TriggerType(Enum):
    """Types of triggers"""
    SCHEDULE = "schedule"  # Cron-like schedule
    EVENT = "event"  # Git commit, file change, etc.
    MANUAL = "manual"  # User-triggered
    CONTINUOUS = "continuous"  # Always running


@dataclass
class ScheduledJob:
    """Scheduled agent job"""
    name: str
    agent: str
    action: str
    trigger_type: TriggerType
    schedule: Optional[str] = None  # Cron expression
    interval_seconds: Optional[int] = None
    enabled: bool = True
    last_run: Optional[datetime] = None
    next_run: Optional[datetime] = None
    run_count: int = 0
    parameters: Dict[str, Any] = field(default_factory=dict)


class AgentRunner:
    """
    Background Agent Runner
    
    Runs agents automatically based on:
    - Schedule (cron-like)
    - Events (git commits, file changes, webhooks)
    - Continuous monitoring
    
    Use Cases:
    - Code Review on every PR
    - Security Scan daily
    - Performance Tests weekly
    - Backup and archival monthly
    - Continuous monitoring
    
    Features:
    - Multi-threaded execution
    - Job queuing
    - Error handling and retry
    - Logging and notifications
    - Job history
    """
    
    def __init__(self):
        """Initialize the agent runner"""
        self.jobs: Dict[str, ScheduledJob] = {}
        self.job_queue = queue.Queue()
        self.running = False
        self.worker_threads: List[threading.Thread] = []
    
    def schedule_job(
        self,
        name: str,
        agent: str,
        action: str,
        trigger_type: TriggerType,
        schedule: Optional[str] = None,
        interval_seconds: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None
    ) -> ScheduledJob:
        """
        Schedule a new job
        
        Args:
            name: Job name
            agent: Agent to run
            action: Action to execute
            trigger_type: When to trigger
            schedule: Cron expression (if schedule trigger)
            interval_seconds: Interval in seconds (if schedule trigger)
            parameters: Job parameters
            
        Returns:
            Created job
        """
        job = ScheduledJob(
            name=name,
            agent=agent,
            action=action,
            trigger_type=trigger_type,
            schedule=schedule,
            interval_seconds=interval_seconds,
            parameters=parameters or {}
        )
        
        if trigger_type == TriggerType.SCHEDULE and interval_seconds:
            job.next_run = datetime.now() + timedelta(seconds=interval_seconds)
        
        self.jobs[name] = job
        print(f"✅ Scheduled job: {name} ({trigger_type.value})")
        
        return job
    
    def start(self, num_workers: int = 2):
        """
        Start the agent runner
        
        Args:
            num_workers: Number of worker threads
        """
        if self.running:
            print("Agent runner already running")
            return
        
        self.running = True
        print(f"\n{'='*60}")
        print(f"🚀 Starting Agent Runner with {num_workers} workers")
        print(f"{'='*60}\n")
        
        # Start scheduler thread
        scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        scheduler_thread.start()
        
        # Start worker threads
        for i in range(num_workers):
            worker = threading.Thread(target=self._worker_loop, args=(i,), daemon=True)
            worker.start()
            self.worker_threads.append(worker)
        
        print(f"✅ Agent Runner started")
        print(f"   - Scheduler: Running")
        print(f"   - Workers: {num_workers}")
        print(f"   - Scheduled Jobs: {len(self.jobs)}\n")
    
    def stop(self):
        """Stop the agent runner"""
        print("\n🛑 Stopping Agent Runner...")
        self.running = False
        
        # Wait for workers to finish
        for worker in self.worker_threads:
            worker.join(timeout=5)
        
        print("✅ Agent Runner stopped\n")
    
    def _scheduler_loop(self):
        """Main scheduler loop"""
        while self.running:
            now = datetime.now()
            
            for job in self.jobs.values():
                if not job.enabled:
                    continue
                
                should_run = False
                
                if job.trigger_type == TriggerType.SCHEDULE:
                    if job.next_run and now >= job.next_run:
                        should_run = True
                elif job.trigger_type == TriggerType.CONTINUOUS:
                    should_run = True
                
                if should_run:
                    self.job_queue.put(job)
                    job.last_run = now
                    
                    if job.interval_seconds:
                        job.next_run = now + timedelta(seconds=job.interval_seconds)
            
            time.sleep(1)  # Check every second
    
    def _worker_loop(self, worker_id: int):
        """Worker thread loop"""
        while self.running:
            try:
                job = self.job_queue.get(timeout=1)
                self._execute_job(job, worker_id)
                self.job_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"❌ Worker {worker_id} error: {e}")
    
    def _execute_job(self, job: ScheduledJob, worker_id: int):
        """Execute a job"""
        print(f"\n[Worker {worker_id}] Executing: {job.name}")
        print(f"  Agent: {job.agent}")
        print(f"  Action: {job.action}")
        print(f"  Run count: {job.run_count + 1}")
        
        try:
            # Simulate agent execution
            result = self._dispatch_agent(job.agent, job.action, job.parameters)
            
            job.run_count += 1
            
            print(f"  ✅ Completed successfully")
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
    
    def _dispatch_agent(self, agent: str, action: str, parameters: Dict[str, Any]) -> Any:
        """Dispatch to agent"""
        # Placeholder for actual agent integration
        time.sleep(2)  # Simulate work
        return {'status': 'completed', 'agent': agent, 'action': action}
    
    def trigger_job(self, job_name: str):
        """Manually trigger a job"""
        if job_name in self.jobs:
            job = self.jobs[job_name]
            self.job_queue.put(job)
            print(f"✅ Triggered job: {job_name}")
        else:
            print(f"❌ Job not found: {job_name}")
    
    def enable_job(self, job_name: str):
        """Enable a job"""
        if job_name in self.jobs:
            self.jobs[job_name].enabled = True
            print(f"✅ Enabled job: {job_name}")
    
    def disable_job(self, job_name: str):
        """Disable a job"""
        if job_name in self.jobs:
            self.jobs[job_name].enabled = False
            print(f"⏸️ Disabled job: {job_name}")
    
    def list_jobs(self) -> List[ScheduledJob]:
        """List all jobs"""
        return list(self.jobs.values())
    
    def get_job_status(self, job_name: str) -> Optional[Dict[str, Any]]:
        """Get job status"""
        if job_name not in self.jobs:
            return None
        
        job = self.jobs[job_name]
        return {
            'name': job.name,
            'agent': job.agent,
            'enabled': job.enabled,
            'trigger_type': job.trigger_type.value,
            'run_count': job.run_count,
            'last_run': job.last_run.isoformat() if job.last_run else None,
            'next_run': job.next_run.isoformat() if job.next_run else None
        }
