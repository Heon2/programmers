from collections import defaultdict


def solution(genres, plays):
    answer = []
    dict_genres = defaultdict(int)
    for i in range(len(genres)):
        dict_genres[genres[i]] += plays[i]  # {"classic":1450, "pop":3100}
    # [["pop",3100],["classic",1450]]
    list_genres = sorted(dict_genres.items(), key=lambda x: -x[1])

    li = []  # 많이 재생된 장르순으로 저장
    for i in list_genres:
        li.append(i[0])  # li = ["pop","classic"]

    dict_plays = defaultdict(list)
    for idx, plays in enumerate(plays):
        # dict_plays = {"classic":[[500,0],[150,2],[800,3]],"pop":[[600,1],[2500,4]]}
        dict_plays[genres[idx]].append((plays, idx))

    for i in li:  # li = ["pop","classic"]
        # dict_plays[0]=[[600,1],[2500,4]], dict_plays[1] = [[150,2],[500,0],[800,3]]
        dict_plays[i].sort(key=lambda x: (x[0], -x[1]))
        # pop()은 마지막 원소를 가져오므로 위와같이 정렬한다
        count = 0
        while dict_plays[i] and count < 2:  # 장르당 최대 2개까지만 저장
            p, idx = dict_plays[i].pop()
            answer.append(idx)
            count += 1
    return answer
