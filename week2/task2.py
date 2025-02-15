
def number_sum(arr):
    return sum(arr)
def print_numbers(arr):
    return [i for i in arr if i%2==0]

def largest_number(arr):
    return max(arr)
arr=[i for i in range(1,21)]
ans=number_sum(arr)
ans2=print_numbers(arr)
ans3=largest_number(arr)
print(ans)
print(ans2)
print(ans3)