def merge(meetings):
    sort_meetings = sorted(meetings)
    merge_meetings = [sort_meetings[0]]

    for cur_start, cur_end in sort_meetings[1:]:
        last_start, last_end = merge_meetings[-1]
        if cur_start <= last_end:
            merge_meetings[-1]= (last_start, max(last_end,cur_end))
        else:
            merge_meetings.append((cur_start,cur_end))
    return merge_meetings

meetings = [(0,1),(3,5),(4,8),(10,12),(9,10),(12,14)]
print(merge(meetings))
