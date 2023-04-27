arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds(arr):
    odd_sum = 0
    for item in arr:
        if item % 2 != 0:
            odd_sum += item
    return odd_sum

print(sum_odds(arr))