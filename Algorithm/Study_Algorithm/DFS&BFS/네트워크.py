def dfs(n, computer, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computer[com][connect] == 1:
            if visited[connect] == False:
                dfs(n, computer, connect, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for num in range(n):
        if visited[num] == False:
            dfs(n, computers, num, visited)
            answer += 1
    return answer

a = [[1,1,0],[1,1,0],[0,0,1]]
b = 3
print(solution(b, a))