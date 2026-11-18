
# pytest
- pytest is a Python testing framework used to write, discover, execute and report automated tests.
- In AI Evaluation Engineering, pytest helps test our evaluation code, such as exact-match graders, dataset loaders, scoring logic, and evaluation pipelines.

    ## Installation and verification
    - python3 -m pip install pytest : Install pytest in the currently selected Python environment.
    - python3 -m pytest --version : Check the installed pytest version.

    **Why -m ?** - It tells Python to execute a module using the selected Python interpreter.

    ## Common pytest commands
    - python3 -m pytest :  Discover and run tests
    - python3 -m pytest -v : Run tests with verbose output
    - python3 -m pytest -q : Run tests with concise output
    - python3 -m pytest tests/test_llm.py : Run tests from one file
    - python3 -m pytest tests/test_llm.py -v : Run one file with detailed results
    - python3 -m pytest -k exact_match : Run tests with exact_match in their names
    - python3 -m pytest -x : Stop after the first failure

    ## How to run a specific test within a test file using pytest
    - Syntax : python3 -m pytest path/to/test_file.py::test_function_name -v

    ## Key points :
    - Test files commonly start with test_, e.g., test_llm.py
    - Test functions should start with test_
    - assert verifies expected behavior
    - PASSED = Test succeeded
    - FAILED = Assertion failed or test encountered an error