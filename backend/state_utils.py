def stats_change(state,stat_name,deltapoint):
    newpoint = state["national_stats"][stat_name] + deltapoint
    if newpoint > 1000:
        newpoint = 1000
    elif newpoint < 0:
        newpoint = 0
    else:
        pass
    state["national_stats"][stat_name] = newpoint