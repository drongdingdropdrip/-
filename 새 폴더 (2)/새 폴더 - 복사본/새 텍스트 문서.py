list = ["바", "보", "멍", "청", "이"]
balls = []
balls.append({
    "pos_x" : 50, #공의 x좌표
    "pos_y" : 50, #공의 y좌표
    "ball_img_idx" : 0, #공에 이미지 인덱스
    "to_x" : 3,#x이동방향 -3이면 왼쪽 3이면 오른쪽
    "to_y" : -6 #y축 이동뱡향 
    #y 최초속도
})

for a, b in enumerate(balls):
    ball_x = b[0]
    print(ball_x)
# listst = [190,48,194,1857,2754,1873,5482]
# listst.sort()
# print(listst)