import requests
from PIL import Image
import pytesseract
from fnmatch import fnmatch
url = 'https://bjjj.jtgl.beijing.gov.cn/suishoupai/ssp_platform/org/queryOrgList'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22178596a43dc89c-0bdbe56d4bb9ba-5771031-1327104-178596a43dd48c%22%7D; _va_id=cff654cd544806cd.1617098059.4.1623992124.1623991997.; Admin-Phone=17600352198; sidebarStatus=1; Admin-Token=CCD9386892BEABC8CBEB7484E4B1458F'
}
date = {
    'appId' : '100100006211',
    'nonce' : '2956241832556415',
    'pageNo' : '1',
    'pageSize':'10',
    'timestamp':'1625190606432',
    'token':'CCD9386892BEABC8CBEB7484E4B1458F',
    'sign':'CEDEBFF69DE08038C536C8427EF3ED3D'
}
response = requests.post(url,headers, date)

print(response.json())


