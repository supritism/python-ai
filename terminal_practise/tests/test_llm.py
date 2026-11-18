# Requirement : Grader implementation that satisfies strict exact matching.
def exact_match(actual, expected):
    return actual == expected


def test_exact_match_identical_strings():
    actual = "Paris"
    expected = "Paris"

    result = exact_match(actual, expected)

    assert result is True

def test_exact_match_different_strings():
    actual = "Paris"
    expected = "London"

    result = exact_match(actual, expected)

    assert result is False

def test_exact_match_rejects_substring():
    actual = "America"
    expected = "North America"

    result = exact_match(actual, expected)

    assert result is False   

def test_exact_match_empty_string():
    actual = ""
    expected = "India"

    result = exact_match(actual, expected)

    assert result is False       

# Python string comparisons using == are case-sensitive.
def test_exact_match_case_mismatch():
    actual = "Paris"
    expected = "paris"

    result = exact_match(actual, expected)

    assert result is False      

# Test whitespace sensitivity
def test_whitespace_sensitivity():
    actual = "Paris "
    expected = "Paris"

    result = exact_match(actual, expected)

    assert result is False          