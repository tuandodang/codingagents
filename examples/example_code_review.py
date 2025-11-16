"""
Example: Code Review Agent

Demonstrates automated code review for quality, security, and performance.
"""

from agents.code_reviewer import CodeReviewer, IssueSeverity

# Sample code to review
sample_code = """
def login(username, password):
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query)
    return result

def get_user_posts(user_ids):
    # N+1 query problem
    posts = []
    for user_id in user_ids:
        user_posts = db.query(f"SELECT * FROM posts WHERE user_id={user_id}")
        posts.extend(user_posts)
    return posts
"""

def main():
    print("=== Code Review Example ===\n")
    
    # Initialize reviewer
    reviewer = CodeReviewer()
    
    # Review the code
    review = reviewer.review_file(
        file_path="app/auth.py",
        code=sample_code,
        language="python"
    )
    
    # Display results
    print(f"Quality Score: {review.quality_score}/100")
    print(f"Total Issues: {review.total_issues}\n")
    
    # Show issues by severity
    critical = sum(1 for i in review.issues if i.severity == IssueSeverity.CRITICAL)
    high = sum(1 for i in review.issues if i.severity == IssueSeverity.HIGH)
    
    print(f"Critical: {critical}")
    print(f"High: {high}")
    print(f"\nTop Recommendations:")
    for rec in review.recommendations:
        print(f"  - {rec}")
    
    # Generate markdown report
    print("\n" + "="*60)
    report = reviewer.generate_report(review, format="markdown")
    print(report)

if __name__ == "__main__":
    main()
