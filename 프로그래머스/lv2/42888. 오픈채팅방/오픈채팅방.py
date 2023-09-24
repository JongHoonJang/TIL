def solution(record):
    answer = []
    res = []
    user_name = {}
    for data_list in record:
        data = list(data_list.split())
        if data[0] == 'Enter':
            user_name[data[1]] = data[2]
            res.append((data[1],'in'))
        elif data[0] == 'Leave':
            res.append((data[1],'out'))
        elif data[0] == 'Change':
            user_name[data[1]] = data[2]
            
    for user, do in res:
        if do == 'in':
            answer.append(f'{user_name[user]}님이 들어왔습니다.')
        elif do == 'out':
            answer.append(f'{user_name[user]}님이 나갔습니다.')
    
    return answer