def rotate(nums: list, k: int) -> list:
    k = k % len(nums)
    reverse_list = nums[::-1]
    reverse_list[:k] = reverse_list[:k][::-1]
    reverse_list[k:] = reverse_list[k:][::-1]
    return reverse_list
