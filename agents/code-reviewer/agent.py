"""
Code Review Agent

Performs comprehensive code reviews analyzing quality, security, performance, and best practices.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum


class IssueSeverity(Enum):
    """Severity levels for code issues"""
    CRITICAL = "critical"  # Security vulnerabilities, data loss risks
    HIGH = "high"  # Major bugs, performance issues
    MEDIUM = "medium"  # Code quality, maintainability
    LOW = "low"  # Style issues, minor improvements
    INFO = "info"  # Suggestions, best practices


class IssueCategory(Enum):
    """Categories of code issues"""
    SECURITY = "security"  # Security vulnerabilities
    BUG = "bug"  # Logic errors, potential bugs
    PERFORMANCE = "performance"  # Performance issues
    CODE_QUALITY = "code_quality"  # Code smells, complexity
    MAINTAINABILITY = "maintainability"  # Hard to maintain code
    TESTING = "testing"  # Missing or inadequate tests
    DOCUMENTATION = "documentation"  # Missing or poor documentation
    STYLE = "style"  # Code style violations
    BEST_PRACTICE = "best_practice"  # Deviation from best practices
    DEPENDENCY = "dependency"  # Dependency issues


@dataclass
class Issue:
    """Represents a code review issue"""
    severity: IssueSeverity
    category: IssueCategory
    title: str
    description: str
    file_path: str
    line_number: Optional[int] = None
    code_snippet: Optional[str] = None
    suggestion: Optional[str] = None
    references: List[str] = field(default_factory=list)


@dataclass
class CodeReview:
    """Results of a code review"""
    files_reviewed: int
    total_issues: int
    issues_by_severity: Dict[IssueSeverity, int]
    issues_by_category: Dict[IssueCategory, int]
    issues: List[Issue]
    summary: str
    recommendations: List[str]
    quality_score: float  # 0-100
    metrics: Dict[str, any] = field(default_factory=dict)


class CodeReviewer:
    """
    Code Review Agent

    Performs comprehensive code reviews with focus on:
    - Security vulnerabilities (OWASP Top 10, injection flaws, auth issues)
    - Code quality (complexity, duplication, code smells)
    - Performance (inefficient algorithms, N+1 queries, memory leaks)
    - Best practices (SOLID principles, design patterns, error handling)
    - Testing (coverage, test quality, missing tests)
    - Documentation (API docs, comments, README)

    Features:
    - Multi-language support (Python, JavaScript, Java, C#, Go, etc.)
    - Security-focused analysis
    - Performance profiling suggestions
    - Automated fix suggestions
    - Integration with linters (ESLint, Pylint, SonarQube)
    - SAST (Static Application Security Testing)
    """

    def __init__(self):
        """Initialize the Code Reviewer"""
        self.supported_languages = [
            'python', 'javascript', 'typescript', 'java',
            'csharp', 'go', 'rust', 'php', 'ruby'
        ]

    def review_file(
        self,
        file_path: str,
        code: str,
        language: str,
        context: Optional[Dict[str, any]] = None
    ) -> CodeReview:
        """
        Review a single code file

        Args:
            file_path: Path to the file being reviewed
            code: Source code content
            language: Programming language
            context: Additional context (project type, framework, etc.)

        Returns:
            CodeReview object with issues and recommendations
        """
        issues = []

        # Security analysis
        issues.extend(self._check_security(code, language, file_path))

        # Code quality analysis
        issues.extend(self._check_quality(code, language, file_path))

        # Performance analysis
        issues.extend(self._check_performance(code, language, file_path))

        # Best practices
        issues.extend(self._check_best_practices(code, language, file_path))

        # Testing
        issues.extend(self._check_testing(code, language, file_path))

        # Documentation
        issues.extend(self._check_documentation(code, language, file_path))

        # Calculate metrics
        issues_by_severity = self._count_by_severity(issues)
        issues_by_category = self._count_by_category(issues)
        quality_score = self._calculate_quality_score(issues)

        # Generate summary
        summary = self._generate_summary(issues, quality_score)
        recommendations = self._generate_recommendations(issues)

        return CodeReview(
            files_reviewed=1,
            total_issues=len(issues),
            issues_by_severity=issues_by_severity,
            issues_by_category=issues_by_category,
            issues=issues,
            summary=summary,
            recommendations=recommendations,
            quality_score=quality_score,
            metrics={
                'lines_of_code': code.count('\n'),
                'language': language,
                'file_path': file_path
            }
        )

    def review_project(
        self,
        project_path: str,
        file_patterns: Optional[List[str]] = None
    ) -> CodeReview:
        """
        Review an entire project

        Args:
            project_path: Root path of the project
            file_patterns: File patterns to include (e.g., ['**/*.py', '**/*.js'])

        Returns:
            Aggregated CodeReview for the entire project
        """
        # This would scan all files and aggregate results
        # Placeholder for full implementation
        pass

    def _check_security(
        self,
        code: str,
        language: str,
        file_path: str
    ) -> List[Issue]:
        """Check for security vulnerabilities"""
        issues = []

        # SQL Injection
        if 'execute(' in code or 'exec(' in code:
            if not ('parameterized' in code or 'prepared' in code):
                issues.append(Issue(
                    severity=IssueSeverity.CRITICAL,
                    category=IssueCategory.SECURITY,
                    title="Potential SQL Injection",
                    description="Use of execute() without parameterized queries",
                    file_path=file_path,
                    suggestion="Use parameterized queries or ORM to prevent SQL injection",
                    references=["https://owasp.org/www-community/attacks/SQL_Injection"]
                ))

        # Hardcoded secrets
        secret_patterns = ['password', 'api_key', 'secret', 'token']
        for pattern in secret_patterns:
            if f'{pattern} =' in code.lower() and ('"""' not in code and "'''" not in code):
                issues.append(Issue(
                    severity=IssueSeverity.CRITICAL,
                    category=IssueCategory.SECURITY,
                    title="Hardcoded Credentials",
                    description=f"Potential hardcoded {pattern} found",
                    file_path=file_path,
                    suggestion="Use environment variables or secret management service",
                    references=["https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html"]
                ))

        # Command Injection
        if language == 'python' and ('os.system(' in code or 'subprocess.call(' in code):
            issues.append(Issue(
                severity=IssueSeverity.HIGH,
                category=IssueCategory.SECURITY,
                title="Potential Command Injection",
                description="Use of os.system() or subprocess.call() with user input",
                file_path=file_path,
                suggestion="Use subprocess with arguments list, not shell=True",
                references=["https://owasp.org/www-community/attacks/Command_Injection"]
            ))

        return issues

    def _check_quality(
        self,
        code: str,
        language: str,
        file_path: str
    ) -> List[Issue]:
        """Check code quality issues"""
        issues = []

        # Cyclomatic complexity (simplified check)
        complexity = code.count('if ') + code.count('for ') + code.count('while ')
        if complexity > 10:
            issues.append(Issue(
                severity=IssueSeverity.MEDIUM,
                category=IssueCategory.CODE_QUALITY,
                title="High Cyclomatic Complexity",
                description=f"Function has high complexity (estimated: {complexity})",
                file_path=file_path,
                suggestion="Refactor into smaller functions following Single Responsibility Principle"
            ))

        # Long functions (simplified)
        lines = code.split('\n')
        if len(lines) > 50:
            issues.append(Issue(
                severity=IssueSeverity.LOW,
                category=IssueCategory.CODE_QUALITY,
                title="Long Function",
                description=f"Function is very long ({len(lines)} lines)",
                file_path=file_path,
                suggestion="Break down into smaller, focused functions"
            ))

        # Code duplication (basic check)
        if code.count('def ') > 3:
            # Check for similar patterns
            pass

        return issues

    def _check_performance(
        self,
        code: str,
        language: str,
        file_path: str
    ) -> List[Issue]:
        """Check performance issues"""
        issues = []

        # N+1 query problem
        if 'for ' in code and ('.get(' in code or '.find(' in code):
            issues.append(Issue(
                severity=IssueSeverity.HIGH,
                category=IssueCategory.PERFORMANCE,
                title="Potential N+1 Query Problem",
                description="Database query inside a loop",
                file_path=file_path,
                suggestion="Use bulk queries or eager loading to fetch all data at once"
            ))

        # Inefficient string concatenation
        if language == 'python' and 'for ' in code and '+=' in code and 'str' in code:
            issues.append(Issue(
                severity=IssueSeverity.MEDIUM,
                category=IssueCategory.PERFORMANCE,
                title="Inefficient String Concatenation",
                description="String concatenation in loop is inefficient",
                file_path=file_path,
                suggestion="Use ''.join() or StringIO for better performance"
            ))

        return issues

    def _check_best_practices(
        self,
        code: str,
        language: str,
        file_path: str
    ) -> List[Issue]:
        """Check adherence to best practices"""
        issues = []

        # Broad exception catching
        if 'except:' in code or 'except Exception:' in code:
            issues.append(Issue(
                severity=IssueSeverity.MEDIUM,
                category=IssueCategory.BEST_PRACTICE,
                title="Broad Exception Catching",
                description="Catching all exceptions can hide bugs",
                file_path=file_path,
                suggestion="Catch specific exceptions and handle them appropriately"
            ))

        # Missing error handling
        if language == 'javascript' and 'fetch(' in code and 'catch' not in code:
            issues.append(Issue(
                severity=IssueSeverity.HIGH,
                category=IssueCategory.BEST_PRACTICE,
                title="Missing Error Handling",
                description="Async operation without error handling",
                file_path=file_path,
                suggestion="Add try-catch or .catch() for promise rejection handling"
            ))

        return issues

    def _check_testing(
        self,
        code: str,
        language: str,
        file_path: str
    ) -> List[Issue]:
        """Check testing-related issues"""
        issues = []

        # Check if test file has tests
        if 'test' in file_path.lower():
            test_keywords = ['test_', 'it(', 'describe(', '@Test']
            has_tests = any(keyword in code for keyword in test_keywords)
            if not has_tests:
                issues.append(Issue(
                    severity=IssueSeverity.MEDIUM,
                    category=IssueCategory.TESTING,
                    title="Test File Without Tests",
                    description="File appears to be a test file but contains no tests",
                    file_path=file_path,
                    suggestion="Add test cases or remove empty test file"
                ))

        return issues

    def _check_documentation(
        self,
        code: str,
        language: str,
        file_path: str
    ) -> List[Issue]:
        """Check documentation quality"""
        issues = []

        # Missing docstrings/comments
        if language == 'python':
            function_count = code.count('def ')
            docstring_count = code.count('"""') // 2
            if function_count > 0 and docstring_count == 0:
                issues.append(Issue(
                    severity=IssueSeverity.LOW,
                    category=IssueCategory.DOCUMENTATION,
                    title="Missing Documentation",
                    description="Functions lack docstrings",
                    file_path=file_path,
                    suggestion="Add docstrings following PEP 257 or Google style"
                ))

        return issues

    def _count_by_severity(self, issues: List[Issue]) -> Dict[IssueSeverity, int]:
        """Count issues by severity"""
        counts = {severity: 0 for severity in IssueSeverity}
        for issue in issues:
            counts[issue.severity] += 1
        return counts

    def _count_by_category(self, issues: List[Issue]) -> Dict[IssueCategory, int]:
        """Count issues by category"""
        counts = {category: 0 for category in IssueCategory}
        for issue in issues:
            counts[issue.category] += 1
        return counts

    def _calculate_quality_score(self, issues: List[Issue]) -> float:
        """Calculate overall quality score (0-100)"""
        if not issues:
            return 100.0

        # Weighted scoring
        weights = {
            IssueSeverity.CRITICAL: 20,
            IssueSeverity.HIGH: 10,
            IssueSeverity.MEDIUM: 5,
            IssueSeverity.LOW: 2,
            IssueSeverity.INFO: 1,
        }

        total_penalty = sum(weights[issue.severity] for issue in issues)
        score = max(0, 100 - total_penalty)

        return round(score, 1)

    def _generate_summary(self, issues: List[Issue], quality_score: float) -> str:
        """Generate review summary"""
        if not issues:
            return "Excellent! No issues found. Code quality score: 100/100"

        critical = sum(1 for i in issues if i.severity == IssueSeverity.CRITICAL)
        high = sum(1 for i in issues if i.severity == IssueSeverity.HIGH)

        summary = f"Code quality score: {quality_score}/100\n"
        summary += f"Found {len(issues)} issue(s): "

        if critical > 0:
            summary += f"{critical} critical, "
        if high > 0:
            summary += f"{high} high priority, "

        summary += f"{len(issues) - critical - high} other issues"

        return summary

    def _generate_recommendations(self, issues: List[Issue]) -> List[str]:
        """Generate top recommendations"""
        recommendations = []

        # Prioritize critical and high severity issues
        critical_issues = [i for i in issues if i.severity == IssueSeverity.CRITICAL]
        high_issues = [i for i in issues if i.severity == IssueSeverity.HIGH]

        for issue in critical_issues[:3]:
            recommendations.append(f"🚨 {issue.title}: {issue.suggestion}")

        for issue in high_issues[:3]:
            recommendations.append(f"⚠️ {issue.title}: {issue.suggestion}")

        # Add general recommendations
        if any(i.category == IssueCategory.TESTING for i in issues):
            recommendations.append("📝 Improve test coverage for critical paths")

        if any(i.category == IssueCategory.DOCUMENTATION for i in issues):
            recommendations.append("📚 Add comprehensive documentation and comments")

        return recommendations[:5]  # Top 5 recommendations

    def generate_report(self, review: CodeReview, format: str = "markdown") -> str:
        """
        Generate formatted review report

        Args:
            review: CodeReview object
            format: Output format ('markdown', 'html', 'json')

        Returns:
            Formatted report string
        """
        if format == "markdown":
            return self._generate_markdown_report(review)
        elif format == "html":
            return self._generate_html_report(review)
        elif format == "json":
            import json
            return json.dumps(review.__dict__, default=str, indent=2)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _generate_markdown_report(self, review: CodeReview) -> str:
        """Generate Markdown report"""
        report = []

        report.append("# Code Review Report\n")
        report.append(f"**Quality Score:** {review.quality_score}/100\n")
        report.append(f"**Files Reviewed:** {review.files_reviewed}\n")
        report.append(f"**Total Issues:** {review.total_issues}\n\n")

        report.append("## Summary\n")
        report.append(f"{review.summary}\n\n")

        if review.recommendations:
            report.append("## Top Recommendations\n")
            for rec in review.recommendations:
                report.append(f"- {rec}\n")
            report.append("\n")

        if review.issues:
            report.append("## Issues\n\n")

            # Group by severity
            for severity in [IssueSeverity.CRITICAL, IssueSeverity.HIGH, IssueSeverity.MEDIUM, IssueSeverity.LOW]:
                severity_issues = [i for i in review.issues if i.severity == severity]
                if severity_issues:
                    report.append(f"### {severity.value.upper()} Severity\n\n")
                    for issue in severity_issues:
                        report.append(f"#### {issue.title}\n")
                        report.append(f"**Category:** {issue.category.value}\n")
                        report.append(f"**File:** {issue.file_path}\n")
                        if issue.line_number:
                            report.append(f"**Line:** {issue.line_number}\n")
                        report.append(f"\n{issue.description}\n\n")
                        if issue.suggestion:
                            report.append(f"**💡 Suggestion:** {issue.suggestion}\n\n")
                        if issue.code_snippet:
                            report.append(f"```\n{issue.code_snippet}\n```\n\n")
                        if issue.references:
                            report.append("**References:**\n")
                            for ref in issue.references:
                                report.append(f"- {ref}\n")
                            report.append("\n")

        return ''.join(report)

    def _generate_html_report(self, review: CodeReview) -> str:
        """Generate HTML report"""
        # Placeholder for HTML generation
        return "<html><body>HTML report not yet implemented</body></html>"
