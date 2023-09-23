#n을 입력받고, n 이하의 소수 중 3k-1(k는 1이상의 자연수) 꼴인 수를 포함하는 리스트를 만들고 출력하세요. ( 리스트는 작은 수 부터 오름차순으로 정렬되어 있어야 합니다. )
#예를 들어, n = 10 인 경우 2,5가 리스트에 차례로 들어 있어야 합니다.

n = int(input())
prime_and_3k_1 = []

print(prime_and_3k_1)

#소수인지 아닌지 판별
#for x in range(2, 17)
#    if a % x =! 0: #나머지 0이 아니어야 한다.
#        pass #아직까지 소수
#    else:
#        prime = False #나머지가 0이면 소수가 아니다
#        break

for num in range(2, n+1):
    prime = True
    for x in range(2, num):
        if num%x ==0:
            prime = False
            break

    if (prime == True) and (num %3 == 2):
        prime_and_3k_1.append(num)
print(prime_and_3k_1)