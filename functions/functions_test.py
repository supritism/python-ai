# Q1 : args / kwargs
## Write a function call_llm that:
# - Takes prompt as a required argument
# - Takes model with a default of "gpt-4"
# - Takes **kwargs for any extra config like temperature, max_tokens
# - Inside the function, build and return a config dict with:
    # "prompt" — the prompt passed in
    # "model" — the model passed in
    # "temperature" — from kwargs, default to 0.7 if not passed
    # "max_tokens" — from kwargs, default to 512 if not passed

def call_llm(prompt: str, model="gpt-4", **configs) -> dict:
    return {
        "prompt": prompt,
        "model": model,
        "temperature": configs.get("temperature", 0.7),
        "max_tokens": configs.get("max_tokens", 512)
    }

# Call 1 — only prompt
print(call_llm("What is AI?"))

# Call 2 — prompt and model
print(call_llm("What is AI?", model="claude-3"))

# Call 3 — all options
print(call_llm("What is AI?", model="claude-3", temperature=0.2, max_tokens=1024))

# -------------------------------------------------------- #
## Q2: return values

# You are writing an eval scoring function. Write a function 'score_response' that:
# Takes response: dict as input
# Uses a guard clause — if response is empty return {"error": "empty response", "passed": False} immediately
# Otherwise extracts "score" safely — default to 0 if missing
# Returns a dict with:
    # "id" — from response, default "unknown"
    # "score" — the score
    # "passed" — True if score >= 0.8
    # "grade" — "A" if score >= 0.9, "B" if >= 0.8, "F" otherwise


def score_response(response: dict) -> dict:
    
    # guard clause
    if not response:
        return {"error": "empty response", "passed": False}
    
    score = response.get("score", 0)

    return {
        "id" : response.get("id"),
        "score" : score,
        "passed" : score >= 0.8,
        "grade" : "A" if score >=0.9 else "B" if score >= 0.8 else "F"
    }

print ("----------------------------")
print(score_response({})) # {'error': 'empty response', 'passed': False}
print(score_response({"id": "case_1", "score": 0.91})) # {'id': 'case_1', 'score': 0.91, 'passed': True, 'grade': 'A'}
print(score_response({"id": "case_2", "score": 0.55})) # {'id': 'case_2', 'score': 0.55, 'passed': False, 'grade': 'F'}

# -------------------------------------------------------- #
## Q3 : try/except

# You are writing a safe JSONL loader for your eval pipeline. Write a function 'load_eval_cases' that:
# Takes 'filepath: str' as input
# Opens and reads the JSONL file line by line
# Wraps everything in proper error handling:
    # If file is not found — return {"error": "file not found", "cases": []}
    # If any line has invalid JSON — skip that line, print which line failed, continue loading the rest
    # Uses 'finally' to print "file load attempt complete" — always, no matter what
# Returns {"total": len(cases), "cases": cases} on success

def load_eval_cases(filepath: str) -> dict:
    cases = []

    try:                                            
        with open(filepath, "r") as f:
            for i, row in enumerate(f, start=1): # enumerate(f, start=1) gives 2 things per iteration — i : line number + row : content. start=1 makes the counter match real file line numbers so error messages point you to the exact line to fix.
                try:                               
                    case = json.loads(row.strip())
                    cases.append(case)
                except json.JSONDecodeError:
                    print(f"Skipping line {i} — invalid JSON: {row.strip()}")

        return {"total": len(cases), "cases": cases}

    except FileNotFoundError:
        return {"error": f"file not found: {filepath}", "cases": []}

    finally:
        print("file load attempt complete")         # always runs

print ("**************************")
print(load_eval_cases("eval_cases.jsonl"))     # valid file
load_eval_cases("missing.jsonl")        # file doesn't exist