import requests
import os

path_dir = './test_img/' #가져올 파일들이 있는 directory path
url = 'http://127.0.0.1:3000/media/capture'


# 파일 이름 추출
filename_list = os.listdir(path_dir) # path에 존재하는 파일 목록가져오기 str배열

print(filename_list) # debug log
filename_list.remove('.DS_Store') # default로 저장되는 .DS_Store를 삭제해준다.

file_list = []

'''
reqeusts.post(url, files = )에서 files 파라미터에는
files = [('file', open('report.xls', 'rb')), ('file', open('report2.xls', 'rb'))]
형식이 들어가야 한다.
list안에 'file', 실제 file 로 이루어진 tuple.
참고: https://stackoverflow.com/questions/43266317/upload-a-file-to-nodejs-using-python-request

'''
# 파일 불러오기
for each in filename_list:
    file_obj = []
    file_obj.append('file')
    file_obj.append(open(path_dir+each, 'rb'))
    file = tuple(file_obj)
    file_list.append(file)

print(file_list)


res = requests.post(url, files = file_list)
print(res)

# #test
# res = requests.get('http://127.0.0.1:3000/users')
# print(res)