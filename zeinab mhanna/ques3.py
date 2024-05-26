import json
questions = { }
count = 0
f = open("questions.txt",'r')
questions = json.load(f)
f.close()

name = input("Enter your full name: ")
print("enter t or f")
for ques in questions.keys():
    print( ques)
    ans = input("The answer is ")
    if ans == questions[ques]:
        count = count + 1
        print("Correct ")
    else:
        print ("Wrong")

result={name:count}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()