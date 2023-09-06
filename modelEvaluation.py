from TEST_DATASET import *
from createArray import visual_array

def evaluation(answer, output):
    total_cell = 0
    true_cell = 0
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j] == output[i][j]:
                true_cell += 1
            total_cell += 1
    
    average = true_cell / total_cell * 100
    print("유사도 : ",round(average,2))
    return average

'''
print("유사도 : ",round(evaluation(test_data_mini, test_data_mini_compare),2))
visual_array("true",test_data_mini)
visual_array('model' ,test_data_mini_compare)
'''