import pytest
from .Day1 import Solution

a = Solution()


@pytest.mark.parametrize(
    "arr,pieces", [([49, 18, 16], [[16, 18, 49]]), ([1, 3, 5, 7], [[2, 4, 6, 8]])]
)
def test_cannot_form_array(arr, pieces):
    assert not a.canFormArray(arr, pieces)


@pytest.mark.parametrize(
    "arr,pieces",
    [
        ([], []),
        ([85], [[85]]),
        ([15, 88], [[88], [15]]),
        ([91, 4, 64, 78], [[78], [4, 64], [91]]),
    ],
)
def test_can_form_array(arr, pieces):
    assert a.canFormArray(arr, pieces)
