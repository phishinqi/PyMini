print("正在准备去重中...")
def remove_duplicates():
    f_read=open(r'./trackers.txt','r')     #将需要去除重复值的txt文本重命名text.txt
    f_write=open(r'./output_trackers.txt','w')  #去除重复值之后，生成新的txt文本 --“去除重复值后的文本.txt”
    data=set()
    for a in [a.strip('\n') for a in list(f_read)]:
        if a not in data:
            f_write.write(a+'\n')
            data.add(a)
    f_read.close()
    f_write.close()
remove_duplicates()
print("OK!")