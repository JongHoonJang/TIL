# def solution(phone_book):
#     answer = True
#     d = 0
#     i = 1
#     phone_book.sort(key=lambda x : x[0])
#     for phone in phone_book:
#         if len(phone) < 19:
#             k = 0
#             for book in phone_book:
#                 if phone[0] == book[0] and phone != book:
#                     k = 1
#                     if phone == book[:len(phone)]:
#                         answer = False
#                         d = 1
#                         break
#                 if k:
#                     if phone[0] != book[0]:
#                         break
#         if d:
#             break
#     return answer
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True