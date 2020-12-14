d1,v1,d2,v2,p=map(int,input().strip().split())
sum_=0
ans=0

while(sum_<p):
    ans+=1
    if ans>d1 or ans==d1:
        sum_+=v1
    if ans>d2 or ans==d2:
        sum_+=v2
    # print(sum_)
    
    # print(day)
    
print(ans)