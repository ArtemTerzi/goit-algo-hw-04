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

def merge_k_lists(lists):
    if not lists:
        return []
    
    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged = merge(lists[i], lists[i + 1])
                merged_lists.append(merged)
            else:
                merged_lists.append(lists[i])
        
        lists = merged_lists 
    
    return lists[0]

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()