"""Example: Test Case Generator"""
from agents.test_generator import TestGenerator, TestType

def main():
    print("=== Test Generation Example ===\n")
    
    generator = TestGenerator()
    
    # Generate unit tests for a function
    code = """
    def calculate_discount(price, discount_percent):
        if price < 0 or discount_percent < 0 or discount_percent > 100:
            raise ValueError("Invalid input")
        return price * (1 - discount_percent / 100)
    """
    
    test_suite = generator.generate_unit_tests(code, language="python")
    
    print(f"Generated {len(test_suite.test_cases)} test cases")
    for test in test_suite.test_cases:
        print(f"\n- {test.name}")
        print(f"  Expected: {test.expected_result}")

if __name__ == "__main__":
    main()
