
from project import validate_difficulty, search_by_topic,format_problem_string

def test_validate_difficulty():
    assert validate_difficulty("Easy") is True
    assert validate_difficulty("Medium") is True
    assert validate_difficulty("Hard") is True
    assert validate_difficulty("Impossible") is False

def test_search_by_topic():
    result = search_by_topic("Arrays")
    assert isinstance(result, list)

def test_format_problem_string():
    sample_row = (1, "Two Sum", "LeetCode", "Arrays", "Easy", "2026-07-01")
    expected_output = "[Easy] Two Sum on LeetCode (Arrays) - Solved: 2026-07-01"
    assert format_problem_string(sample_row) == expected_output