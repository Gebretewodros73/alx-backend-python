# Unittests and Integration Tests

This directory contains Python scripts for testing various functions and classes using the unittest framework. Each task focuses on different aspects of unit testing and integration testing.

## Tasks

### Task 0: Parameterize a Unit Test
- **File**: `test_utils.py`
- **Instructions**:
  - Familiarize yourself with the `utils.access_nested_map` function and understand its purpose.
  - Write a unit test for `utils.access_nested_map` that checks if it returns the expected result for different inputs.
  - Use `@parameterized.expand` to test the function with specific inputs.

### Task 1: Parameterize a Unit Test (Exception)
- **File**: `test_utils.py`
- **Instructions**:
  - Implement a unit test to check if `utils.access_nested_map` raises a `KeyError` for specific inputs.
  - Use `@parameterized.expand` to test the function with different inputs that should raise a `KeyError`.

### Task 2: Mock HTTP Calls
- **File**: `test_utils.py`
- **Instructions**:
  - Familiarize yourself with the `utils.get_json` function.
  - Write a unit test for `utils.get_json` that mocks the HTTP calls using `unittest.mock.patch`.
  - Make sure it returns the expected result for different test cases.

### Task 3: Parameterize and Patch
- **File**: `test_utils.py`
- **Instructions**:
  - Read about memoization and understand the `utils.memoize` decorator.
  - Write a unit test to verify that memoization is working correctly using `unittest.mock.patch`.

### Task 4: Parameterize and Patch as Decorators
- **File**: `test_client.py`
- **Instructions**:
  - Familiarize yourself with the `client.GithubOrgClient` class.
  - Write a unit test for `GithubOrgClient.org` that uses `@patch` as a decorator to mock external HTTP calls.
  - Use `@parameterized.expand` to test the function with different organization names.

### Task 5: Mocking a Property
- **File**: `test_client.py`
- **Instructions**:
  - Implement a unit test to mock a property (`GithubOrgClient._public_repos_url`) using `unittest.mock.patch`.
  - Verify that the result of `_public_repos_url` is as expected based on the mocked payload.

### Task 6: More Patching
- **File**: `test_client.py`
- **Instructions**:
  - Write a unit test for `GithubOrgClient.public_repos` that uses `@patch` to mock `get_json`.
  - Verify that the list of repos is as expected from the chosen payload.

### Task 7: Parameterize
- **File**: `test_client.py`
- **Instructions**:
  - Write a unit test for `GithubOrgClient.has_license` that is parameterized with different inputs and expected return values.

### Task 8: Integration Test (Fixtures)
- **File**: `test_client.py`
- **Instructions**:
  - Implement an integration test for `GithubOrgClient.public_repos` using fixtures from `fixtures.py`.
  - Mock external requests using `requests.get` and parametrize the test with different fixtures.

### Task 9: Integration Tests (Advanced)
- **File**: `test_client.py`
- **Instructions**:
  - Implement integration tests for `GithubOrgClient.public_repos` with specific arguments.
  - Verify that the method returns the expected results based on the provided fixtures.

## Repository Information

- **GitHub Repository**: alx-backend-python
- **Directory**: 0x03-Unittests_and_integration_tests
