# languages = ['c/c++', 'java', 'c#', 'python', 'javascript']

# uri = '/Users/boblee/Desktop/제로베이스 강의자료/python.txt/'

# with open(uri + 'languages.txt', 'a') as f:
#     # f.write(item)
#     # f.write('\n')
#     f.writelines(item + '\n' for item in languages)
#
# with open(uri + 'languages.txt', 'r') as f:
#     print(f.read())

uri = '/Users/boblee/Desktop/제로베이스 강의자료/python.txt/'

scoreDic = {'kor': 85, 'eng': 90, 'mat': 92, 'sci': 79, 'his': 82}
scoreList = [85, 90, 92, 79, 82]
# for key in scoreDic.keys():
#     with open(uri + 'scoreDic.txt', 'a') as f:
#         f.write(key + '\t:' + str(scoreDic[key]) + '\n')

with open(uri + 'scores.txt', 'a') as f:
    print(scoreList, file=f)




