# 13-1
# 주어진 문장이 회문인지 찾기
# 큐 & 스택
# 풀이
def palindrome(s):
    qu = []
    st = []
    # 문자열의 알파벳을 각각 큐와 스택에 넣기
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu :
        if qu.pop(0) != st.pop():
            return False

    return True

print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
