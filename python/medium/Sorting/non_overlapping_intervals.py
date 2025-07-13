def remove_overlapping_intervals(intervals: list[list[int]]) -> int:
    """
    Given an array of intervals where intervals[i] = [starti, endi].
    Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


    :param intervals: list[list[int]]
    :return: int
    """

    remove_intervals_count = 0

    #Sort the intervals by the end i in every interval.
    intervals.sort(key=lambda x : x[1])

    #Keep track of the last interval's end time.
    previous_end = intervals[0][1]

    i = 1
    while i < len(intervals):
        #The end time is sorted, if start time of current is less than previous.
        #Means there is an overlap in those 2 intervals.
        if intervals[i][0] < previous_end:
            remove_intervals_count += 1
        else:
            previous_end = intervals[i][1]

        i += 1

    return remove_intervals_count


if __name__ == '__main__':
    print(remove_overlapping_intervals([[1,100],[11,22],[1,11],[2,12]]))

