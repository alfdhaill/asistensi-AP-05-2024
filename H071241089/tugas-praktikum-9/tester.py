import time
from secretcode import SecretCode
from codebreaker import CodeBreaker


class Tester:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0

    def test_break_code(self, initial_code, expected_result):
        try:
            secret_code = SecretCode(initial_code)
            code_breaker = CodeBreaker(secret_code)
            # TODO: Something is missing here
            result = code_breaker.break_code()

            self.tests_run += 1
            if result == expected_result:
                self.tests_passed += 1
                time.sleep(1)
                print(f"Test {self.tests_run}: Passed")
            else:
                time.sleep(1)
                print(f"Test {self.tests_run}: Failed (Result: {result}, Expected: {expected_result})")
        except Exception as e:
            self.tests_run += 1
            time.sleep(1)
            print(f"Test {self.tests_run}: Failed (Error: {e})")

    def final_results(self):
        print(f"Total Tests Run: {self.tests_run}")
        print(f"Total Tests Passed: {self.tests_passed}")