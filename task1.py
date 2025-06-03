import random
from timeit import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def generate_numbers(n): return [random.randint(0, 10000000) for _ in range(n)]

def test_sort(lst):
    t1 = timeit(lambda: insertion_sort(lst.copy()), number=1)
    t2 = timeit(lambda: merge_sort(lst.copy()), number=1)
    t3 = timeit(lambda: sorted(lst.copy()), number=1)
    print(f"For {len(lst)} values, insertion_sort: {t1:.6f} s")
    print(f"For {len(lst)} values, merge_sort    : {t2:.6f} s")
    print(f"For {len(lst)} values, timsort : {t3:.6f} s")

def main():
    sl = generate_numbers(100)
    ml = generate_numbers(1000)
    ll = generate_numbers(10000)

    for lst in [sl, ml, ll]:
        test_sort(lst)

    print("=== Conclusion ===")
    print("insertion_sort only suitable for very small data sets or training")
    print("merge_sort effective for medium to large lists, has stable performance O(n log n).")
    print("The best option is the timsort` function, because it is optimized and faster than all the others.")


if __name__ == "__main__":
    main()



