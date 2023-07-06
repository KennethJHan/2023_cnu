def make_sum(num: int) -> int:
    """1 부터 입력된 num 까지의 숫자를 더하여 반환하는 함수

    Args:
        num (int): 1부터 num 까지 더할 수

    Returns:
        int: 1부터 num 까지 더한 결과 값을 반환

    Examples:
    >>> make_sum(10)
    55
    """
    result: int = 0
    for i in range(1, num+1, 1):
        result += i
    return result

result = make_sum(10)
print(result) # 55
