from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    processes = deque(i for i in range(len(priorities)))
    
    while True:
        max_priority = max(priorities)
        if priorities[0] == max_priority:
            priorities.popleft()
            if processes[0] == location:
                answer += 1
                break
            else:
              processes.popleft()
              answer += 1
        else:
            priorities.append(priorities.popleft())
            processes.append(processes.popleft())

    return answer
