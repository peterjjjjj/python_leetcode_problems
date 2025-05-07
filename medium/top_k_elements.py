def top_k_elements_sorting(nums, k):
    queue = dict()
    for num in nums:
        if num not in queue.keys():
            queue[num] = 1
        else:
            queue[num] += 1

    sorted_queue = sorted(queue.items(), key=lambda x: x[1], reverse=True)

    elements = []
    for num,freq in sorted_queue[:k]:
        elements.append(num)

    return elements

if __name__ == '__main__':
    print(top_k_elements_sorting([1, 1, 1, 2, 2, 3, 4, 5, 5], 3))
