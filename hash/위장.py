clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    dict = {}
    for name,kind in clothes:   #[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
        if(kind in dict):       
            dict[kind] += 1
        else:
            dict[kind] = 1      
    #dict = {"headgear":2, "eyewear":1}

    total = 1           #계속 곱해야하므로 0이 아닌 1로 설정
    for i in dict.values():
        total *= i+1        #입지않는 경우를 생각해서 1더해준다,   3x2
        
    return total - 1        #아무것도 입지않은경우 1을 빼준다

print(solution(clothes))