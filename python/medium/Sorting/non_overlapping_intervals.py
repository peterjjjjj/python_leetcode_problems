def remove_overlapping_intervals(intervals: list[list[int]]) -> int:
    """
    Given an array of intervals where intervals[i] = [starti, endi].
    Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    So only check for fully contained intervals.


    :param intervals: list[list[int]]
    :return: int
    """

    remove_intervals_count = 0

    #Sort the intervals by the first num in every interval.
    intervals.sort(key=lambda x : x[0])

    for i in range(1, len(intervals)):
        #If the starti of 2 intervals were overlapped.
        if intervals[i][0] <= intervals[i - 1][0]:
            #Increase count.
            remove_intervals_count += 1


if __name__ == '__main__':
    pass

