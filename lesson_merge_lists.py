import random


def merge(nums1, nums2):
    merged_list = [0] * (len(nums1) + len(nums2))
    first_1 = first_2 = 0
    inf = max(nums1[-1], nums2[-1]) + 1
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1) + len(nums2) - 2):
        if nums1[first_1] <= nums2[first_2]:
            merged_list[k] = nums1[first_1]
            first_1 += 1
        else:
            merged_list[k] = nums2[first_2]
            first_2 += 1
    nums1.pop()
    nums2.pop()
    return merged_list


def merge2(nums1, nums2):
    merged_list = []
    first_1 = first_2 = 0
    for k in range(len(nums1) + len(nums2)):
        if first_1 <= len(nums1) and first_2 == len(nums2) or nums1[first_1] <= nums2[first_2]:
            merged_list.append(nums1[first_1])
            first_1 += 1
        else:
            merged_list.append(nums2[first_2])
            first_2 += 1
    return merged_list


nums1 = [1, 2, 4, 6, 11]
nums2 = [1, 2, 3, 3, 4, 6]

print("nums1:", nums1)
print("nums2:", nums2)
print("Best_com:", merge(nums1, nums2))
print("Best_com:", merge2(nums1, nums2))
# print("Note in range:", check_notes(L, R, notes_list, target), 'Hz')
