def solution(numbers, hand):
    positions = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2),
                 7:(2, 0), 8:(2, 1), 9:(2, 2), "*":(3, 0), 0:(3, 1), "#":(3, 2)
                }
    left_idx = (3, 0)
    right_idx = (3, 2)
    answer = ''
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left_idx = positions[n]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right_idx = positions[n]
        elif n == 0 or n == 2 or n == 5 or n == 8 :
            a, left_idx, right_idx = find_hand(positions[n], left_idx, right_idx, hand)
            answer += a
            
    return answer

def find_hand(n_idx, left_idx, right_idx, hand):
    left_diff = abs(n_idx[0] - left_idx[0]) + abs(n_idx[1] - left_idx[1])
    right_diff = abs(n_idx[0] - right_idx[0]) + abs(n_idx[1] - right_idx[1])
    
    if left_diff < right_diff:
        left_idx = n_idx
        return 'L', left_idx, right_idx
    elif left_diff > right_diff:
        right_idx = n_idx
        return 'R', left_idx, right_idx
    else:
        if hand == 'right':
            right_idx = n_idx
            return 'R', left_idx, right_idx
        else:
            left_idx = n_idx
            return 'L', left_idx, right_idx

    