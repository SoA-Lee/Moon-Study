pageNumber = int(input())
number= [0 for i in range(10)]
count = 1
while pageNumber != 0:
    while pageNumber % 10 != 9: #일의 자리가 9가 아닐 경우
        for i in str(pageNumber):
            number[int(i)] += count
        pageNumber -= 1
    if pageNumber< 10: #페이지수가 10보다 작을 경우는 0제외 1씩 증가
        for i in range(pageNumber + 1):
            number[i] += count
        number[0] -= count
        break
    else:
        for i in range(10): 
            number[i] += (pageNumber // 10 + 1) * count
            #예를 들어 23페이지라면 3개씩 증가, 십의자릿수로 결정
    number[0] -= count
    count *= 10 #자릿수 만큼 곱해주기
    pageNumber //= 10
for i in number:
    print(i, end=' ')
