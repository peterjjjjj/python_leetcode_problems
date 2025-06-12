from enum import unique
import random


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

def top_k_elements_quickselect(nums, k):
    frequency = dict()
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    unique_num = list(frequency.keys())

    def partition(elements, frequencies, low, high):
        """"
        i: iterator of left part
        j: iterator of nums
        pivot: index of pivot
        """
        pivot_index = random.randint(low, high)
        pivot_frequency = frequencies[elements[pivot_index]]

        elements[pivot_index], elements[high] = elements[high], elements[pivot_index]
        i = low - 1

        for j in range(low, high):
            if frequencies[elements[j]] > pivot_frequency:
                i += 1
                elements[i], elements[j] = elements[j], elements[i]

        #swap the pivot to it's correct position
        elements[i + 1], elements[high] = elements[high], elements[i + 1]


        return i + 1

    def select(elements, frequencies, low, high, k):

        if low == high:
            return elements[low]

        pivot_index = partition(elements, frequencies, low, high)

        if pivot_index == k - 1:
            return elements[pivot_index]

        elif pivot_index < k - 1:

            return select(elements, frequencies, pivot_index + 1, high, k)
        else:
            return select(elements, frequencies, low, pivot_index - 1, k)

    kth_most_frequent_element = select(unique_num, frequency, 0, len(unique_num) - 1, k)

    top_k_elements = []
    count = 0
    kth_most_frequent_frequency = frequency[kth_most_frequent_element]

    for element in unique_num:
        if frequency[element] >= kth_most_frequent_frequency and count < k:
            top_k_elements.append(element)
            count += 1

    return top_k_elements[:k]


if __name__ == '__main__':
    print(top_k_elements_sorting( [1,1,1,2,2,3,], 2))
    print(top_k_elements_quickselect( [1,1,1,2,2,3,], 3))
