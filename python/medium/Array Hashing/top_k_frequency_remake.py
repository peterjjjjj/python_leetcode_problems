#3 solutions, sorting, heap, bucket
import collections, heapq


def sorting(nums: list[int], k: int) -> list[int]:
    frequency_map = {}

    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    frequency_list = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)

    result = []
    for i in range(k):
        result.append(frequency_list[i][0])

    return result


def heap(nums: list[int], k: int) -> list[int]:
    """
    Heap is a tree structure, accessing smallest : O(1), Insert O(log K(K is the height of the tree)), space: O(K)
    """

    counts = collections.Counter(nums)

    results = heapq.nlargest(k, counts.keys(), key=lambda x: counts[x])

    return results


if __name__ == '__main__':
    print(sorting([1,1,1,2,2,0,0,0,0,0,3], 2))
    print(heap([1,1,1,2,2,0,0,0,0,0,0,4], 2))