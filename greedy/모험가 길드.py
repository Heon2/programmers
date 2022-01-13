num = int(input())  # 5
people = ('').join(sorted(input().split()))  # 2 3 1 2 2 => 12223
count = 0  # 만들어진 그룹의 수
group = 0  # 한 그룹안에 모험가의 수
counted_people = 0  # 그룹을 이룬 사람의 수
for i in people:    # 1 2 2 2 3
    if(int(i) > (num-counted_people)):
        break
    else:
        group += 1
        if(int(i) == group):
            counted_people += group
            group = 0
            count += 1

print(count)
