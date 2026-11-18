
# Environment Variables 
- An environment variable is a named value stored in a process's environment that programs can read while running.
    - Example in Terminal execute: 
        - ``export EVALKIT_MODEL="mock-llm"``
        - ``echo "$EVALKIT_MODEL"``
        - ``python3 -c 'import os; print(os.getenv("EVALKIT_MODEL"))'``
        - ``unset EVALKIT_MODEL`` - Removes/Resets the environment value

    ## Environment Variables vs. Virtual Environments
    - [Q] Does deactivating a Python virtual environment also delete environment variables you exported in Terminal?
    - [A] No. The environment variable is exported in your current shell session, not stored inside your Python virtual environment. Activating or deactivating a venv changes which Python interpreter and packages you use. It does not normally remove unrelated environment variables you exported.

    ## Lifetime of an Environment variable
    - When we execute - export EVALKIT_MODE="debug" , the variable becomes available to your current shell and the processes it launches. But opening a separate Terminal window normally starts a new shell that does not inherit variables you exported only in the previous window.

    ## Understanding .env files
    - It's an ordinary text file that stores environment-style configuration values for our Project.

    Example : 
        EVALKIT_MODEL=mock-llm
        EVALKIT_MODE=debug
        EVALKIT_API_KEY=demo-key-12345  

    - There are important distinction : 
        - Creating a .env file does not automatically make those variables available to Python. Your application needs to load them explicitly, using a library such as 'python-dotenv' or another configuration mechanism.

        - Also, a .env file is not encrypted. Real secrets must be protected from accidental sharing.

   - Important Note : File names starting with '.' like .venv or .env or .gitignore are hidden from the default 'ls' listing on macOS. Use : ``ls -a`` to see hidden entries

        ### Install python-dotenv
        - Python's built-in os.getenv() can read environment variables, but it does not automatically read a .env file.
        - We'll use a library called ``python-dotenv`` to load the file. 
            - Run : ``python3 -m pip install python-dotenv``
            - Then open a new file : ``nano config_practice.py`` and add below then save and exit (Ctrl+O and Ctrl+X):

            ```
            import os
            from dotenv import load_dotenv

            # Load variables from the .env file
            load_dotenv()

            model = os.getenv("EVALKIT_MODEL")
            mode = os.getenv("EVALKIT_MODE")
            api_key = os.getenv("EVALKIT_API_KEY")

            print("Model:", model)
            print("Mode:", mode)
            print("API key configured:", bool(api_key))
            ```

            - Then execute your script : ``python3 config_practice.py``

            ### Environment Variable Precedence: `export` vs. `.env`

            **Default precedence:** When using `python-dotenv` with `load_dotenv()`, an existing exported shell environment variable takes priority over the value in `.env`.

            **Example:**
                `.env` file:
                ```
                EVALKIT_MODEL=mock-llm
                ```

                Terminal:
                ```
                export EVALKIT_MODEL="candidate-v2"
                python3 config_practice.py
                ```

                Python: config_practice.py
                ```
                from dotenv import load_dotenv
                import os

                load_dotenv()
                print(os.getenv("EVALKIT_MODEL"))
                ```

            **Output:** `candidate-v2`

            **Why?** `load_dotenv()` uses `override=False` by default. It does not replace an environment variable that is already set.

            **After `unset`:**
            ```
            unset EVALKIT_MODEL
            python3 config_practice.py
            ```

            **Output:** `mock-llm` 
            — Python now loads the value from `.env`.

            **Can we reverse the precedence?**
            Yes. Using: `load_dotenv(override=True)` which makes values defined in `.env` override existing environment variables with the same names in the running Python process.

            **Why is this useful in AI Evaluation Engineering?**

            It allows us to run the same evaluation code against different models or configurations without modifying code or the default `.env` file. This is useful for local testing, model comparisons, and CI/CD pipelines.

            **Remember:**
            `export` wins by default → `load_dotenv(override=False)`
            `.env` wins when explicitly configured → `load_dotenv(override=True)`