#3 solutions, sorting, heap, bucket

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

if __name__ == '__main__':
    print(sorting([1,1,1,2,2,0,0,0,0,0,3], 2))