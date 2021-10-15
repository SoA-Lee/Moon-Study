N=int(input())
setting=[]
row=0 #행
col=0 #열
cnt_w=0
cnt_h=0

for i in range(N):
    setting.append(input())
for i in setting:
    for j in i:
        if j=='.':
            row+=1
        else:
            if row>=2:
                cnt_w+=1
            row=0
    if row>1:
        cnt_w+=1
    row=0
for i in range(N):
    for j in range(N):
        if setting[j][i] == '.':
            col += 1
        else:
            if col > 1:
                cnt_h += 1
            col = 0
    if col>1:
        cnt_h += 1
    col = 0
print(cnt_w, cnt_h) 
