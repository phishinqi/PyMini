import urllib.request
import os



print("讀取URL中......")
result = []
with open('main_url.txt', 'r') as f:
    for line in f:
        result.append(list(line.strip('\n').split(',')))
url_number = len(result)
print("OK!")
print("URL列表：", result)
print("--------------------")


#打印網頁至trackers.txt
file_path = os.getcwd()
print("當前文件路徑：", file_path)
path = file_path + '\\trackers.txt'
print("正在輸出trackers至trackers.txt")
if os.path.exists(path):
    print("文件存在！正在刪除原始内容......")
    with open("./trackers.txt", 'r+') as files:
        files.truncate(0)
    print("OK!")
    print("--------------------")
else:
    print("文件不存在！正在創建中......")
    os.mkdir(path)
    print("OK!")
    print("--------------------")

#file = open('./trackers.txt', 'w')
#file.write(html)



#打開網頁
#print("正在嘗試獲取trackers......")
trackers_list = []
for url_line in open("main_url.txt"):
    print(url_line)
    try:
        #html = urllib.request.urlopen(url_line).read().decode()
        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        req = urllib.request.Request(url=url_line,headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        trackers_list.append(html)
        #print(trackers_list)
        with open('./trackers.txt', 'a') as f:
            f.writelines(html)
            print("OK!")
    except:
        continue
#print(html)



