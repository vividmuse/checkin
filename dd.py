import requests
import sys
import time
import hashlib
import os

sckey = os.environ["PUSH_KEY"]


def httpProxyWithPassRequest(oldarray):
    write = False
    _version = sys.version_info
    is_python3 = (_version[0] == 3)
    timestamp = str(int(time.time()))  # 计算时间戳
    # print(timestamp)
    txt = "pintuan,one-yuan," + timestamp + ",MC0CAQACBQC5FhxRAgMBAAECBF94RXkCAwDlNwIDAM63AgMAp7kCAwC9hwICR5c=,9e94d795b346d65c55b12fee989da49e"
    # print(txt)
    if is_python3:
        txt = txt.encode()
    time_code = hashlib.md5(txt).hexdigest()
    # print(time_code)
    targetUrl = "http://mapi7.dangdang.com/index.php?access-token=&time_code=" + time_code + "&img_size=h&client_version=10.9.2&pageSize=10&union_id=537-101003&timestamp=" + timestamp + "&permanent_id=20201011182108211859309197768661374&a=one-yuan&global_province_id=137&c=pintuan&udid=9e94d795b346d65c55b12fee989da49e&user_client=android&page=1"

    r = requests.get(targetUrl, )
    #print("status Code : " + str(r.status_code))
    if r.status_code == 200:
        #print('返回状态正常,测试判断')
        # print(r.text)
        dict = eval(r.text)
        # print(dict)
        array = dict["productArray"]
        #print(array)
        array1 = []
        #print('读入的数组', oldarray)
        newbook=""
        for product in array:
            #print(product['productId'])
            if product['productId'] not in oldarray:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"发现新书,ID为:" + product['productId'])
                # 发消息给微信
                newbook="发现新书,书名为:" + product['productTitle']+'\r\n\r\n'+newbook
                write = True
                array1.append(product['productId'])
            #print(array1)
            array1 = array1 + oldarray
            #print(array1)
            array1 = list(set(array1))
            #print(array1)
        if write == True:
            webhook_servicejiang(newbook)
            with open('result.txt', 'w', encoding="utf-8-sig") as fp:
                fp.write(str(array1))
                fp.close()
                print("写出数组",array1)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '找到了新书,延时30分钟')
                #oldarray = array1
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '没找到新书,延时30分钟')
        #time.sleep(1800)  # 30min wait


#    print(array1.count('25121755')) #统计个数
#    s=json.loads(r.text.encode())
# print(s)
#    s1=s.get('productArray')
# print('输出',s1)
# 　用个 for 循环就能轻而易举的获取数据

#    for x in s1:
#        #print('遍历list数据：', x)
#        print('取到书名和id',x['productId'],x['productTitle'])  #获取id
#        print(x['productId'])
#        print(qqq.find(x['productId']))
##        if qqq.find(x['productId'])==-1:
##           print('找到一本新上的', x['productId'])
# print('找书结束了')
#    s1 = json.load(s)


def webhook_servicejiang(result):
    webhookurl = "http://sc.ftqq.com/"
    requests.get(url=webhookurl + sckey + ".send?text=有新书了&desp=" + result)


def readfile():
    array = []
    print(os.getcwd())
    print( __file__)
    print(sys.path[0]+'\/result.txt')
    with open('result.txt', 'r', encoding="utf-8-sig") as r:
        t = r.read()
        #print(t)
        array = eval(t)  # 转为数组
        print('读入文件数组', array)
        # print("输出完毕")
        r.close()
    return (array)


if __name__ == '__main__':
    print('开始运行时间:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # array=[]
        # print('main函数下',array)
    #while 1 == 1:
    #    oldarray = readfile()
    #    httpProxyWithPassRequest(oldarray)
    oldarray = readfile()
    httpProxyWithPassRequest(oldarray)
