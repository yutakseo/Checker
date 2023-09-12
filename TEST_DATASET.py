#사각형
test_data1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#ㄴ자형
test_data2 =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#ㄷ자형
test_data3 =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
              [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
              [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
              [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
              [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
              [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#한 쪽 모서리가 깎인 사각형
test_data4 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


rectangle = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]
             ]

stair = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [1,1,1,1,0,0,0,0,0,0],
             [1,1,1,1,0,0,0,0,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]
             ]


truncated = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [1,1,1,1,1,0,0,0,0,0],
             [1,1,1,1,1,1,0,0,0,0],
             [1,1,1,1,1,1,1,0,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [1,1,1,1,1,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]
             ] 


#정답 데이터
source = [[1,0,0],
          [1,0,0],
          [1,1,1]]

#출력 데이터
compare = [[1,0,0],
           [0,0,0],   
           [0,0,1]]