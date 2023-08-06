def solution(players, callings):
    # for call in callings:
    #     k = players.index(call)
    #     players.insert(k - 1,players.pop(k))
    #     players[k - 1], players[k] = players[k], players[k - 1]
    # 선수: 위치
    p_idx_dict = {player: i for i, player in enumerate(players)}
    # 위치: 선수
    idx_p_dict = {i: player for i, player in enumerate(players)}
    for call in callings:
        cur_idx = p_idx_dict[call]  # 현재 선수의 위치
        pre_idx = cur_idx-1         # 현재 선수보다 앞에 있는 선수 등수
        cur_player = call
        pre_player = idx_p_dict[pre_idx]    # *

        p_idx_dict[cur_player] = pre_idx    # 현재 선수는 앞에 선수 등수가 되고
        p_idx_dict[pre_player] = cur_idx    # 앞에 선수는 뒷 등수가 되고 
        
        idx_p_dict[pre_idx] = cur_player    # 등수별 선수 표 업데이트 * 때문에
        idx_p_dict[cur_idx] = pre_player

    return list(idx_p_dict.values())