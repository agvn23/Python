### Meetings ###

# Meetings challange to see if any meetings overlap

# overlap False
# no-overlap True

# 1 solution   using IF to check start and end time (nested loops) O(n^)
[[0,30], [15,20], [5,10]]
#[[0,30], [35,45], [40,60]]
def can_attend_meetings(intervals):            # using verbs good practice ie. is_admin = True /has_permission = False
    # for i in range(len(intervals)):
    #     for j in range(i + 1, len(intervals)):
    #         interval_1_start = intervals[i][0]
    #         interval_1_end = intervals[i][1]
    #         interval_2_start = intervals[j][0]
    #         interval_2_end = intervals[j][1]

    #         if (
    #             interval_1_start >= interval_2_start 
    #             and interval_1_start < interval_2_end 
    #             or interval_2_start >= interval_1_start 
    #             and interval_2_start < interval_1_end 
    #         ):
    #             return False
    # return True
    for i in range (0, len(intervals)):        # defind first index [0]
        for j in range(i + 1, len(intervals)): # defind second index [15] 
            if (intervals[i][0] >= intervals[j][0]) and (intervals[i][0] < intervals[j][1]) or (intervals[j][0] >= intervals[i][0]) and (intervals[j][0] < intervals[i][1]): # compare
                return False   

    return True             
print(can_attend_meetings([[0,30], [15,20], [5,10]]))



# 2 solutions    using SORT to sort start time
# sort list      [[0,30], [5,10],[15,20]]

def can_attend_meetings_2(intervals):
    intervals.sort()                             # Variation of QUICK SORT O(n log n)
# loop compare   only compares 1 at a time no need for nested
    for i in range(0, len(intervals)-1):         # O(n) (fast) but BiG O keeps the dominante O(n log n) (less fast) 
# i = [0,30] i+1 = [5,10] [i][1] = 30 [i+1][0] = 5
        if intervals[i][1] > intervals[i+1][0]:                             
            return False    
    return True       
#print(can_attend_meetings_2([[0,30], [5, 10], [15, 20]]))
print(can_attend_meetings_2([[7, 10], [2, 4]]))  