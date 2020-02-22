n=int(input())
score=list(map(int,input().split(" ")))
high_score=score[0];low_score=score[0];
high=0;low=0
for i in score:
    if i>high_score:
        high_score=i;
        high+=1
    if i<low_score:
        low_score=i;low+=1;
print(high,low)
