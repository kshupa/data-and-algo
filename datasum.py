# output a unique pair that sum up to value K

# pair_sum([1, 3, 2, 2], 4)

def pair_sum(lst, total):

    seen = set()
    output = set()

    for i in lst:
        result = total - i
        if result not in seen:
            seen.add(i)
        else:
            output.add((min(result, i), max(result, i)))

    return len(output)




print(pair_sum([1, 3, 2, 2, 7], 8))
