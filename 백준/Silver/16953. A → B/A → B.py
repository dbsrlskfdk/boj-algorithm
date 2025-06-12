from collections import defaultdict

A, B = map(int, input().split())
calc_nums = defaultdict(int)


def solution(prev, try_num):
    if prev > B:
        return

    if prev in calc_nums:
        calc_nums[prev] = min(try_num, calc_nums[prev])
    else:
        calc_nums[prev] = try_num

    solution(prev * 2, try_num + 1)
    solution(int(str(prev) + "1"), try_num + 1)


if __name__ == "__main__":
    calc_nums[A] = 0
    solution(A, 0)

    if B in calc_nums:
        print(calc_nums[B] + 1)
    else:
        print(-1)
