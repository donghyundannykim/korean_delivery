# db_uploader.py
import codecs
from os import listdir
from os.path import isfile, join
import sys
"""

정부기관에서 나온 csv는 종종 인코딩 문제가나서
utf-8를 cp949로 변환
이미 바뀌어져있으면 try를 안함
에러날경우 에러메세지가 뜸
아래 블로그를 보고 참조함 
https://m.blog.naver.com/PostView.naver?blogId=pino93&logNo=222472773459&categoryNo=169&proxyReferer= 
"""
def utf8_to_others (f):
    #encodings = ['cp949', 'utf8', 'utf16', 'euc-kr']
    encodings = ['cp949', 'utf8', 'utf16', 'euc-kr']

    print('----- [%s] -----' % f)
    for enc in encodings:
        try:
            s = open(f, mode = 'r', encoding = enc).read()
            open(f, mode='w', encoding='cp949').write(s)
        except Exception as ex:
            print('encoding failed : %s, message : %s' %(enc, ex))
        else:
            print('encoding successful : %s' %(enc))
            break
"""file encoding list"""

def file_encoding_lst(dirPath):
    for f in listdir(dirPath):  # 경로지정
        path = join(dirPath, f)
        if isfile(path) and '.csv' in f :    # 파일여부
            utf8_to_others(path)
            
if __name__ == "__main__":
    dirPath = "/Users/donghyunkim/Library/CloudStorage/GoogleDrive-dannykim0195@gmail.com/My Drive/korean_delivery" #path 
    file_encoding_lst(dirPath)
