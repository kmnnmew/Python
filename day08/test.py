# # # 완주하지 못한 선수
# # def solution(participant, completion):
# #     answer = ''
# #     participant.sort()
# #     completion.sort()
# #     print(participant)
# #     print(completion)
# #     for i in range(len(participant)):
# #         if i > len(completion)-1:
# #             completion.append(None)
# #         if participant[i] != completion[i]:
# #             answer = participant[i]
# #             break
# #     return answer

# # print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# # 전화번호 목록
# def solution(phone_book):
#     answer = True
#     h = {}
#     for i in phone_book:
#         h[i] = 1
#     for i in phone_book:
#         temp = ""
#         for j in i[:-1]:
#             temp+=j
#             if temp in h:
#                 answer = False
#     return answer

# 신규 아이디 추천
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    id = ''
    for i in new_id: 
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            id += i
    while '..' in id:
        id = id.replace('..', '.')
    if id and id[0] == '.':
        listid = list(id)
        del listid[0]
        id = "".join(listid)
    if id and id[-1] == '.':
        listid = list(id)
        del listid[-1]
        id = "".join(listid)
    if len(id) == 0:
        id = 'a'
    if len(id) >= 16:
        id = id[:15]
    if id[0] == '.':
        listid = list(id)
        del listid[0]
        id = "".join(listid)
    if id[-1] == '.':
        listid = list(id)
        del listid[-1]
        id = "".join(listid)
    while len(id) < 3:
        listid = list(id)
        listid.append(listid[-1])
        id = "".join(listid)
    return id

print(solution("=.="))