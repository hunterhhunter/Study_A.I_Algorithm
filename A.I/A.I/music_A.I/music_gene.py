gok #\\음악 정보
make_music_best_score #\\작곡 최고점수
make_music_i #\\작곡 i
make_music_j #\\작곡 j
best_score #\\최고 점수
pos_make_music #\\작곡 가능
output #\\출력
study_i #\\학습 i
study_j #\\학습 j
score_now #\\현재 점수(누적)
al_satisfy #\\ai만족도
code #\\코드
error #\\에러
i
l
j
weight = []
sprite_masage=[]
data_fail = []
data_music = []
hidden_layers =[]
output_layers = []
scores = []
best_weight = []
input_layers = []
name = []
sound = []
state = []
temp = []

def clear_input_layers(code):
    input_layers = []
    study_i = 0
    for _ in len(code):
        study_i += 1
        if code[study_i] == 1:
            input_layers.append(1)
            input_layers.append(0)
            input_layers.append(0)
            input_layers.append(0)
        elif code[study_i] == 2:
            input_layers.append(0)
            input_layers.append(1)
            input_layers.append(0)
            input_layers.append(0)
        elif code[study_i] == 3:
            input_layers.append(0)
            input_layers.append(0)
            input_layers.append(1)
            input_layers.append(0)
        elif code[study_i] == 4:
            input_layers.append(0)
            input_layers.append(0)
            input_layers.append(0)
            input_layers.append(1)
    return input_layers

def perceptron(hidden_layer, bool): #히든래이어는 함수 내에서 사용하는 것
    hidden_layers = []
    for _ in range(len(hidden_layers)):
        hidden_layers.append(0)
    output_layers = []
    output_layers.append(0)
    output_layers.append(0)

    if bool == False:
        l = 0
        i = 0
        for _ in range(len(input_layers)):
            i += 1
            j = 0
            for _ in range(len(hidden_layer)):
                l += 1
                j += 1
                hidden_layers[j] = input_layers[i] + input_layers[j] * weight[l]
        i = 0
        l = 0
        for _ in range(len(hidden_layer)):
            i += 1
            j = 0
            for _ in range(len(output_layers)):
                l += 1
                j += 1
                output_layers[j] = output_layers[i] + hidden_layers[j] * weight[l]
    else:
        i = 0
        l = 0
        for _ in range(len(input_layers)):
            i += 1
            j = 0
            for _ in range(len(hidden_layer)):
                l += 1
                j += 1
                hidden_layers[j] = input_layers[i] + input_layers[j] * best_weight[l]
        i = 0
        l = 0
        for _ in range(len(hidden_layer)):
            i += 1
            j = 0
            for _ in range(len(output_layers)):
                l += 1
                j += 1
                output_layers[j] = output_layers[i] + hidden_layers * best_weight[l]
    output = output_layers[1] - output_layers[2]
    return output

def change_best_score():
    best_score = score_cow
    i = 0
    best_weight = []
    for _ in range(len(weight)):
        i += 1
        best_weight.append(weight[i])

def test():
    score_now = 0
    study_i = 0
    for _ in range(len(data_music)):
        study_i += 1
        clear_input_layers(data_music[study_i])
        perceptron(200, False)
        score_now += output
        if score_now < best_score:
            return 0
    study_i = 0
    score_now = 0
    for _ in range(len(data_fail)):
        study_i += 1
        clear_input_layers(data_fail[study_i])
        perceptron(200, False)
        score_now = 0 - output
        if score_now < best_score:
            change_best_score()