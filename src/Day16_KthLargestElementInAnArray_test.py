import pytest
from .Day16_KthLargestElementInAnArray import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        
    ],
)
def test_get_maximum_generated(nums, k, expected):
    assert s.findKthLargest(nums, k) == expected