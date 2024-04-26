arr=input("enter the list of numbers separated by space:").split()
arr=[int(x) for x in arr]

target=int(input("enter the target value to search:"))

found=False
for i in range(len(arr)):
    if arr[i]==target:
        print(f"Target {target} found at Index {i}.")
        found=True
        break
    
if not found:
    print(f"Target{target} not found in the array.")