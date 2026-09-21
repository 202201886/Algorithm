print("점수를 입력하세요: ")
score = int(input())  
#모든 input은 문자열로 들어오기 때문에 int()를 이용해 형 변환

if score >= 90 :
     print("Grade: A")
elif score >= 80 and score < 90 :
     print("Grade: B") 
elif score >= 70 and score < 80 :
     print("Grade: C")
elif score >= 60 and score < 70 :
     print("Grade: D")
else :
     print("Grade: F")