# truncate a string

def truncateString(string, num):
    if num >= len(string):
        return string
    elif num <= 3:
        return string[0:num] + "..."
    else:
        return string[0:num-3] + "..."





print(truncateString("A-tisket a tasket A green and yellow basket", 11))
print(truncateString("tommy goes to work.", 3))
print(truncateString("A-tisket a tasket A green and yellow basket",len("A-tisket a tasket A green and yellow basket") + 2))
