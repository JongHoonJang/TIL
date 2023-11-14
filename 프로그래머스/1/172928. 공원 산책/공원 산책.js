function solution(park, routes) {
    var answer = [];
    const x_len = park[0].length;
    const y_len = park.length;
    for (let i = 0; i < y_len; i++){
        for (let j = 0; j < x_len; j++){
            if (park[i][j] === 'S') {
                answer.push(i);
                answer.push(j);
                break;
            };
        };
    };
    const op = {'N': [-1, 0], 'S': [1, 0],'W': [0, -1],'E': [0, 1]}
    for (let i = 0; i < routes.length; i++){
        const o = op[routes[i][0]];
        const c = Number(routes[i][2]);
        let t = 0
        if (0 <= answer[0] + o[0] * c && answer[0] + o[0] * c < y_len && 0 <= answer[1] + o[1] * c && answer[1] + o[1] * c < x_len){
            for (let k = 1; k < c + 1; k++){
                if (park[answer[0] + o[0] * k][answer[1] + o[1] * k] === 'O' || park[answer[0] + o[0] * k][answer[1] + o[1] * k] === 'S'){
                    t++
                };
            };  
            if (t === c){
                answer[0] = answer[0] + o[0] * c
                answer[1] = answer[1] + o[1] * c
            };
        };
    };
    return answer;
}