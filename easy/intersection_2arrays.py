def intersection_hashing(nums1, nums2):
    count = dict()
    intersection = []
    for num in nums1:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    for num in nums2:
        if num in count:
            if count[num]:
                count[num] -= 1
                intersection.append(num)

    return intersection

def intersection_sorting(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    intersection = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersection.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1

    return intersection

def intersection_uhmmmidk(nums1, nums2):
    #won't return duplicated intersection
    set1 = set(nums1)
    set2 = set(nums2)
    intersection = set1 & set2
    return list(intersection)