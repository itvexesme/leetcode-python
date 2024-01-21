from solution import (
    Solution
)

def run_solution(s: str) -> int:
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    return result

def test_1():
    result = run_solution("abcabcbb")
    expected = 3
    assert result == expected
    
def test_2():
    result = run_solution("bbbbb")
    expected = 1
    assert result == expected
    
def test_3():
    result = run_solution("pwwkew")
    expected = 3
    assert result == expected
    
def test_4():
    result = run_solution("a")
    expected = 1
    assert result == expected