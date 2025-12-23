#Hash, pointer

class Intersection:
    def __init__(self, arr1: list[int], arr2: list[int]):
        #Longer arr goes to 1
        if len(arr1) < len(arr2):
            self.arr1 = arr1
            self.arr2 = arr2
        else:
            self.arr1 = arr2
            self.arr2 = arr1

    def hash(self) -> list[int]:
        nums1 = {}
        for num in self.arr1:
            nums1[num] = nums1.get(num, 0) + 1

        duplicates = []

        for num in self.arr2:
            if num in nums1:
                if nums1[num] > 0:
                    nums1[num] -= 1
                    duplicates.append(num)

        return duplicates

    def pointer(self) -> list[int]:
        arr1 = sorted(self.arr1)
        arr2 = sorted(self.arr2)
        i = 0
        j = 0
        duplicates = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                duplicates.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] > arr2[j]:
                j += 1
            elif arr2[j] > arr1[i]:
                i += 1

        return duplicates


if __name__ == "__main__":
    testcase = Intersection(arr1=[1,2,3,4,5], arr2=[1,2,6,5])
    print(testcase.hash())
    print(testcase.pointer())

