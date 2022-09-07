def print_shows(show_list):
    """
    Given a list of shows of format: name, start time, end time
    returns the maximum number of shows someone can attend
    """
    show_list.sort(key = lambda x:x[1] + x[2])
    current_time = 0

    for (show_name, start_time, duration) in show_list:
        end_time = start_time + duration
        if start_time >= current_time:
            current_time = end_time
            print("{} {} {}".format(show_name, start_time, end_time))