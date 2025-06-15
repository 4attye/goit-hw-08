import heapq


def merge_k_lists(lists):

    # Ініціалізуємо купу
    heap = []

    # Додаємо перші елементи кожного списку у купу (значення, індекс списку, індекс елемента)
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))

    # Результуючий список
    merged = []

    # Поки купа не пуста
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        merged.append(val)

        # Якщо в тому ж списку ще є елементи, додаємо наступний
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return merged

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)