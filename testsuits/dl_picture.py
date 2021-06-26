# _*_ coding: utf-8 _*_
import urllib
import re
import requests
from time import ctime
from multiprocessing import Pool

def picture():
    url_begin = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=狗&pn=1&gsm=0x1&ct=&ic=0&lm=-1&width=0&height=0'
    r = requests.get(url_begin).text
    pic_urls = re.findall('"objURL":"(.*?)",', r,re.S)
    print (pic_urls[0])
# threads = []
# t1 = threading.Thread(target=picture)
# threads.append(t1)
# t2 = threading.Thread(target=picture_1)
# threads.append(t2)
if __name__ == '__main__':
    picture()
#     # #启动线程
#     # for t in threads:
#     #     t.start()
#     # print "all over %s" % ctime()
#     pool = Pool()
#     file_name = 'https://goss2.vcg.com/editorial/vcg/400/new/VCG111173861438.jpg'
#     pool.map(picture,file_name)
#     pool.close()
#     pool.join()
#     print "all over %s" % ctime()