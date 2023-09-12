import math
from TEST_DATASET import *
from createArray import visual_array

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def evaluation(answer, output):
    #정답데이터의 코너 개수와 좌표
    corner_position = []
    #출력데이터의 코너 개수와 좌표
    output_position = []
    
    #이중배열 반복문 실행
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j] != 0:
                corner_position.append([i,j])
            if output[i][j] != 0:
                output_position.append([i,j])
    
    #정답데이터의 코너 개수와 출력데이터의 코너 개수가 다를 경우의 평가
    if len(corner_position) != len(output_position):
        if len(corner_position) > len(output_position):
            return len(output_position)/len(corner_position)*100
        elif len(output_position) > len(corner_position):
            return (len(corner_position)-(len(output_position)-len(corner_position)))/len(corner_position)
    #두 데이터의 개수가 같을 때
    else:
        closest_pair = None
        min_distance = float('inf')  # 초기 최소 거리를 무한대로 설정

        for point1 in corner_position:
            for point2 in output_position:
                distance = calculate_distance(point1, point2)
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = {point1, point2}
        print(closest_pair)

evaluation(test_data_mini, test_data_mini_compare)