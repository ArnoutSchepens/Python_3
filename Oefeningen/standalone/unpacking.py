def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)


nums1 = (1, 2, 3, 4, 5)
nums2 = (6, 7, 8, 9, 10)
sum_all_values(*nums1, *nums2)
