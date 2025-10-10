def dayIndex(s):
    days = {
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6,
        "sun": 7
    }
    return days.get(s.lower(), 0)

def dayIndex(s):
    days = {
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6,
        "sun": 7
    }
    return days.get(s.lower()[:3], 0)
