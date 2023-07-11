


#Problem:
#There is a flight of n stairs
#A person can walk 1, 2, or 3 stairs at a time
#How many possible ways are there for this person to walk up the flight of stairs


def iterat_dp(total_steps):
    steps = [0] * (total_steps+1)
    steps[0] = 1
    for i in range(1, total_steps+1):
        steps[i] = steps[i-1] + \
                   (steps[i-2] if i>=2 else 0) + \
                   (steps[i-3] if i>=3 else 0)
    return steps[total_steps]




def recur_dp(total_steps):
    duplicates = [None]*(total_steps+1)
    duplicates[0] = 1
    def recur_helper(current_total):
        if current_total < 0:
            return 0

        if duplicates[current_total] != None:
            return duplicates[current_total]

        duplicates[current_total] = recur_helper(current_total-1) + recur_helper(current_total-2) +recur_helper(current_total-3)
        return duplicates[current_total]

    return recur_helper(total_steps)



