list1 = [2, 3, 4, 5, 23, 45, 78]  # sorted list
key = int(input("Enter the key you want to search: "))

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if key == arr[mid]:
            print(f"Key found at {mid} index")
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Key not found")

binary_search(list1, key)
