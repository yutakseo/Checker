from TEST_DATASET import *
from createArray import visual_array




def evaluation(answer, output):
    #정답데이터의 코너 개수와 좌표
    num_of_corner = 0
    corner_position = []
    #출력데이터의 코너 개수와 좌표
    recognized_output_corner = 0
    output_position = []
    
    #이중배열 반복문 실행
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j] != 0:
                num_of_corner += 1
                corner_position.append([i,j])
                
            if output[i][j] != 0:
                recognized_output_corner += 1
                output_position.append([i,j])
    
    if num_of_corner != recognized_output_corner:
        if num_of_corner > recognized_output_corner:
            return recognized_output_corner/num_of_corner*100
        elif recognized_output_corner > num_of_corner:
            return (num_of_corner-(recognized_output_corner-num_of_corner))/num_of_corner
    else:
        for i in corner_position:
            ㅇㅇㅇ