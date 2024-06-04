from datetime import datetime


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start < x < end
    else:
        return start < x or x < end


def check_for_intersection(
    _interval1: tuple[datetime, datetime], _interval2: tuple[datetime, datetime]
) -> bool:
    interval1 = (_interval1[0].timestamp(), _interval1[1].timestamp())
    interval2 = (_interval2[0].timestamp(), _interval2[1].timestamp())

    if interval1[0] < interval2[1] and interval2[0] < interval1[1]:
        return True

    # interval1 in interval2
    if interval1[0] >= interval2[0] and interval1[1] <= interval2[1]:
        return True

    return False
