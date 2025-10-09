#Create a dictionary/map of months with their corresponding numbers. Use function for lookups and cover for errors.

#initial version, uses try+except to cover KeyError
def num_to_month(n):
    try:
        months = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec"
        }
        return months[n]
    except KeyError:
        return "Invalid"
    
#improved version using .get() as the lookup function. allows return of a default value of "Invalid"
def num_to_month(n):
        months = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec"
        }
        return months.get(n, "Invalid")

assert num_to_month(1) == "Jan"
assert num_to_month(12) == "Dec"
assert num_to_month(13) == "Invalid"