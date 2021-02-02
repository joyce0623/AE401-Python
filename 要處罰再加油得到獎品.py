math_score= int(input("請輸入數學成績"))
eng_score=input("請輸入數學成績")
eng_score= int(eng_score)
if(math_score>=90 and eng_score>=90):
 print('得到獎品')
elif(math_score<60 and eng_score<60):
 print('要處罰')
elif(math_score<60 or eng_score<60):
 print('再加油')
else:
    print('pass')
