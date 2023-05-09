def show_performance(*secs) -> None:
    """顯示時間(單位：秒)差異。
    """
    durations = {'list_plus_list': secs[1] - secs[0],
                'addition_assignment': secs[2] - secs[1],
                'list_append': secs[3] - secs[2]}

    for method, secs in durations.items():
        print(f'{method = :24}{secs = }')

    # find minimum value in dict
    min_secs = min(durations.values())
    max_secs = max(durations.values())
    # get keys with minimal value using list comprehension
    fastest_method = [method for method in durations if durations[method] == min_secs]
    slowest_method = [method for method in durations if durations[method] == max_secs]
    print(f'fastest: {fastest_method[0]:24}slowest: {slowest_method[0]:24}')


LOOPS = 50_000