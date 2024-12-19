import random


def check_notes(left_limit, right_limit, notes_list, target):
    prev_note = notes_list[0]
    for cur_note in notes_list[1:]:
        check_result = check_note(cur_note, prev_note, target)
        if check_result:
            if cur_note > prev_note:
                if ((cur_note + prev_note) // 2) <= target:
                    left_limit = max(left_limit, (cur_note + prev_note) // 2)
                else:
                    right_limit = min(right_limit, (cur_note + prev_note) // 2)
            else:
                right_limit = min(right_limit, (cur_note + prev_note) // 2)
        else:
            if cur_note < prev_note:
                left_limit = max(left_limit, (cur_note + prev_note) // 2)
            else:
                right_limit = min(right_limit, (cur_note + prev_note) // 2)
        prev_note = cur_note
    return left_limit, right_limit


def check_note(cur, prev, target):
    if abs(target - cur) < abs(target - prev):
        return "closer"
    return None


L = 30
R = 4000
N = 10
target = 2500
notes_range = (L, R)
notes_list = [random.randint(L, R) for _ in range(N)]
print("Notes:", notes_list)
print("Note in range:", check_notes(L, R, notes_list, target), 'Hz')
