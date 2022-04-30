nums = []
n = int(input("Enter Number of List Elements: " ))
for i in range(1, n + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    nums.append(value)

smallest = largest = nums[0]

for j in range(1, n):
    if(smallest > nums[j]):
        smallest = nums[j]
        min_position = j
    if(largest < nums[j]):
        largest = nums[j]
        max_position = j

print("The Smallest Element in this List is : ", smallest)
print("The Smallest Element in this List is : ", largest)