print('---------------------')
# 1.r 以只读模式打开文件，文件的指针将会放在文件的开头
# 2.w 以只写模式打开文件，如果文件不存你在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
# 3.a 以追加模式打开文件你，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
# 4.b 以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb 或者wb
# 5.+ 以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
print('----------------------')
# 1.read([size]) 从文件中读取size个字节或者字符的内容返回，若省略[size],则读取到文件末尾，记一次读取文件所有内容
# 2.readlie() 从文本文件中读取一行内容
# 3.readlines() 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表中返回
# 4.write(str) 将字符串str内容写入文件
# 5.writelines(s_list) 将字符串列表s_list写入文本文件，不添加换行符
# 6.seek(offset[,whence]) 将文件指针移到新的位置,offset表示相对于whence的位置，offset：为正往结束方向移动,是负往开始方向移动whence不同的值不同的含义:
#     0:从文件头开始计算(默认)
#     1:从当前位置开始计算
#     2:从文件尾开始计算
# 7.tell() 返回文件指针的当前位置
# 8.flush() 把缓冲区的内容写入文件，但不关闭文件
# 9.close() 把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关的资源
file=open('test.txt','r')
print(file.readlines())
file.close()

file2=open('test2.txt','w')
file2.write("helloworld")
file2.close()

file3=open('QQ.png','rb')
file4=open('pu.png','wb')#其实是一个空文件；pu.png是创建的生成的文件名
file4.write(file3.read())#将QQ.png复制到pu.png
file3.close()
file4.close()

file2=open('test2.txt','w')
file2.write("hello")
file2.flush()
file2.write("python")
file2.close()