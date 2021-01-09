from typing import List, Dict
import collections


def visitWordNode(
    queue,
    visited: Dict[str, int],
    otherVisited: Dict[str, int],
    wordLength: int,
    combos: Dict[str, List[str]],
):
    word, level = queue.popleft()
    for i in range(wordLength):
        testWord = word[:i] + "*" + word[i + 1 :]
        if testWord in combos:
            for w in combos[testWord]:
                if w in otherVisited:
                    return level + otherVisited[w]
                if w not in visited:
                    visited[w] = level + 1
                    queue.append((w, level + 1))
    return 0


def preProcessNeighbors(wordList: List[str], wordLength: int):
    combos = {}
    for word in wordList:
        for i in range(wordLength):
            testWord = word[:i] + "*" + word[i + 1 :]
            if testWord not in combos:
                combos[testWord] = []
            combos[testWord].append(word)
    return combos


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wl = len(beginWord)
        combos = preProcessNeighbors(wordList, wl)

        qBegin = collections.deque([(beginWord, 1)])
        qEnd = collections.deque([(endWord, 1)])

        visitedBegin = {beginWord: 1}
        visitedEnd = {endWord: 1}
        ladderLength = 0

        while qBegin and qEnd:
            ladderLength = visitWordNode(qBegin, visitedBegin, visitedEnd, wl, combos)
            if ladderLength > 0:
                return ladderLength
            ladderLength = visitWordNode(qEnd, visitedEnd, visitedBegin, wl, combos)
            if ladderLength > 0:
                return ladderLength

        return 0
