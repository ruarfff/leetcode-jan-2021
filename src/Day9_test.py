import pytest
from .Day9 import Solution

s = Solution()


@pytest.mark.parametrize(
    "beginWord,endWord,wordList,expected",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),        
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
        ("count", "court", ["mount", "point"], 0),
    ],
)
def test_length_of_longest_substring(beginWord, endWord, wordList, expected):
    assert s.ladderLength(beginWord, endWord, wordList) == expected