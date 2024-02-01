def solution(arr, delete_list):
    ans = []
    for a in arr:
        if a not in delete_list:
            ans.append(a)
    return ans