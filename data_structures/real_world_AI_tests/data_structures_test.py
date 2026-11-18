# 6 questions, each one tests multiple DS concepts together exactly like real AI engineering work.

## Q1 — Dicts + Safe parsing
#  You receive this raw JSON string back from an LLM API. Write code to:
#  [a] Safely parse it into a dict
#  [b] Extract "finish_reason" safely — default to "unknown" if missing
#  [c] Extract the nested "total_tokens" safely — default to 0 if missing

import json
raw = '{"model": "gpt-4", "finish_reason": "stop", "usage": {"input_tokens": 120, "total_tokens": 205}}'

#[a] Safely parse it into a dict
api_response = json.loads(raw)
print(api_response) # o/p - {'model': 'gpt-4', 'finish_reason': 'stop', 'usage': {'input_tokens': 120, 'total_tokens': 205}}

#[b] Extract "finish_reason" safely — default to "unknown" if missing
print(f"Finish reason is : {api_response.get("finish_reason", "unknown")}") # Finish reason is : stop

#[c] Extract the nested "total_tokens" safely — default to 0 if missing
print(f"Value of total tokens is: {api_response.get("usage", {}).get("total_tokens", 0)}") # Value of total tokens is: 205

# ----------------------------------------------------------------------------------------------------------
## Q2 — Lists + Comprehension
#  You have a list of eval results. In one line each, write:
#  [a] A list of all case IDs where the model passed
#  [b] A list of scores converted to percentages as strings — e.g. 0.9 → "90%"
#  [c] A list that labels every result as "pass" or "fail" — no filtering, every case appears

results = [
    {"id": "case_1", "model": "gpt-4",   "score": 0.92, "passed": True},
    {"id": "case_2", "model": "claude-3", "score": 0.55, "passed": False},
    {"id": "case_3", "model": "gpt-4",   "score": 0.87, "passed": True},
    {"id": "case_4", "model": "claude-3", "score": 0.40, "passed": False},
    {"id": "case_5", "model": "gpt-4",   "score": 0.91, "passed": True},
]

# [a] A list of all case IDs where the model passed
passed_IDs = [row["id"] for row in results if row["passed"]]
print(f"All case IDs where the model passed : {passed_IDs}") # All case IDs where the model passed : ['case_1', 'case_3', 'case_5']

# [b] A list of scores converted to percentages as strings — e.g. 0.9 → "90%"
scores = [f"{row["score"] * 100:.0f}%" for row in results]
print(f"A list of scores converted to percentages as string: {scores}") # A list of scores converted to percentages as string: ['92%', '55%', '87%', '40%', '91%']

# [c] A list that labels every result as "pass" or "fail" — no filtering, every case appears
case_label = ["pass" if row["passed"] else "fail" for row in results]
print(f"Case label: {case_label}") # Case label: ['pass', 'fail', 'pass', 'fail', 'pass']

# ----------------------------------------------------------------------------------------------------------
## Q3 — Sets
# You ran two eval versions of the same model. Using set operations answer all four questions — one line each:
v1_passed = {"case_1", "case_2", "case_3", "case_5"}
v2_passed = {"case_1", "case_3", "case_4", "case_5"}

# [a] Which cases passed in both versions?
print(v1_passed & v2_passed) # {'case_3', 'case_1', 'case_5'}

# [b] Which cases passed in either version?
print(v1_passed | v2_passed) # {'case_2', 'case_1', 'case_5', 'case_4', 'case_3'}

# [c] Which cases regressed — passed v1 but failed v2?
print(v1_passed - v2_passed) # {'case_2'}

# [d] Which cases changed status in either direction between v1 and v2?
print(v1_passed ^ v2_passed) # {'case_4', 'case_2'}

# ----------------------------------------------------------------------------------------------------------
## Q4 — Tuples
# You are building an eval benchmarking system. Answer all three below questions

response = {"case_id": "case_1", "model": "gpt-4", "score": 0.91, "temperature": 0.7}

# Expected after unpacking:
# case_id → "case_1"
# score   → 0.91
# passed  → True

# [a] Write a function : 'score_case(response: dict) -> tuple' that returns (case_id, score, passed) — pass threshold is 0.8
def score_case(response: dict) -> tuple:
    case_id = response.get("case_id", None)
    score = response.get("score", 0)
    passed = score >= 0.8
    return case_id, score, passed

# [b] Call the function and unpack the result into three variables
response_id, response_score, response_passed = score_case(response)
print(response_id)
print(response_score)
print(response_passed)

# [c] Store benchmark results in a dict using (model, temperature) as the key
benchmark = {}

model = response["model"]
temperature = response["temperature"]

benchmark[(model,temperature)] = response["score"]
print(benchmark)

# ----------------------------------------------------------------------------------------------------------
## Q5 — JSONL + Comprehension combined
# You have 'benchmark_results.jsonl' on disk. 

# Write code to:
# [a] Read the file into a list called 'cases' using a list comprehension

with open("benchmark_results.jsonl", "r") as f:
    cases = [json.loads(row.strip()) for row in f] #list comprehension

print(cases)

# [b] Using a dict comprehension, build a dict mapping each id to its score
dict_cases = {row["id"]:row["score"] for row in cases}

print(dict_cases) # {'case_1': 0.92, 'case_2': 0.55, 'case_3': 0.87, 'case_4': 0.4}

# [c] Using a list comprehension, get the id of every failed case
failed_case = [row["id"] for row in cases if not row["passed"]]

# ----------------------------------------------------------------------------------------------------------
## Q6 — Everything combined
# You are building a mini eval pipeline from scratch. Write complete code that:
    # [a] Reads eval cases from 'eval_cases.jsonl'
cases = []
with open("eval_cases.jsonl", "r") as f:
    for row in f:
        case = json.loads(row.strip())
        cases.append(case)

print(cases) # [{'id': 'case_1', 'score': 0.92}, {'id': 'case_2', 'score': 0.55}, {'id': 'case_3', 'score': 0.87}, {'id': 'case_4', 'score': 0.4}, {'id': 'case_5', 'score': 0.91}]
    
    # [b] For each case — mark it passed if score >= 0.8
for row in cases:
    if row["score"] >= 0.8:
        row["status"] = "Passed"
    else:
        row["status"] = "Failed"

print(cases) # [{'id': 'case_1', 'score': 0.92, 'status': 'Passed'}, {'id': 'case_2', 'score': 0.55, 'status': 'Failed'}, {'id': 'case_3', 'score': 0.87, 'status': 'Passed'}, {'id': 'case_4', 'score': 0.4, 'status': 'Failed'}, {'id': 'case_5', 'score': 0.91, 'status': 'Passed'}]            

    # [c] Saves results to eval_output.jsonl
with open("eval_output.jsonl", "w") as f:
    for case in cases:
        f.write(json.dumps(case) + "\n")

    # [d] Uses a SET to find which case IDs failed
failed_cases = set()

for case in cases:
    if case["status"] == "Failed":
        failed_cases.add(case["id"])

print(failed_cases) # {'case_4', 'case_2'}

    # [e] Prints a summary: total cases, passed count, failed count, and failed case IDs
passed_count = len(cases) - len(failed_cases)
print(f"Total cases: {len(cases)}, Passed count: {passed_count}, Failed count: {len(failed_cases)}, Failed case IDS: {failed_cases}") # Total cases: 5, Passed count: 3, Failed count: 2, Failed case IDS: {'case_4', 'case_2'}