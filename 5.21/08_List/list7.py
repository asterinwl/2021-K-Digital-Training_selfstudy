#리스트 일치 검사

list1=[1,2,3]
list2=[1,2,3]
print(list1==list2)
print(list1!=list2)
print(list1>list2)

#2차원 리스트
list3=[[1,2,3],[4,5,6],[7,8,9]]
print(list3)
# [1 2 3]
# [4 5 6]
# [7 8 9]   방법으로 출력해보기
for i in list3 :
    print(i)
# 1 2 3
# 4 5 6
# 7 8 9   방법으로 출력해보기
for i in list3 :
    for j in i :
        print(j,end=" ")
    print()
for i in list3 :
    print(*i)

print(list3[1][1])  #list[1]=2  2*2=4 list[4]=5
print(len(list3))

# 2차원 리스트 연습문제
# 10명의 학생의 국어,영어,수학 점수가 2차원 리스트 형식으로 저장된 경우
# 각 학생별 세 과목의 총점과 평균 점수를 계산하여 과목점수와 함께 출력하는 코드 작성
#
# [30,85,70]
# [88,72,92]
# [100,100,90]
# [90,60,50]
# ...
#
# 출력
# [90,85,70],245,81.7

students = [[90, 85, 70], [88, 72, 92], [100, 100, 90], [90, 60, 50]]
for student in students :
    total = 0
    for score in student :
        total += score
    average = total / len(student)

    print('{}, {}, {:.1f}'.format(student, total, average))

print(round(70.5555,1))  #반올림하는 결과를 나타냄.