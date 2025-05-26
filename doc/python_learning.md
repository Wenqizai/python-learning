# 字符

## 字符编码/解码

**Python2**

1. Python：字符 unicode（字符引号前加u，u'好'），二进制 str（注意这里不是 string，字符串）

2. 编码 encode：从字符编码成二进制	unicode -> str

​	解码 decode：从二进制解码成字符	str -> unicode

3. 编码方式：utf-8, utf-16, assci, gdk
4. Python2 默认使用的编码方式是 assci，并不支持中文，Python3 统一的编码方式是 unicode。

Python2 编码：https://mp.weixin.qq.com/s/LQrPmp2HMlw5C7izJIUHNQ

**Python3**

1. Python：字符 str（表示所有的文本字符，包括 unicode），二进制 bytes（字符引号前加 b，b'好'）

2. 编码 encode：从字符编码成二进制	str -> bytes

​	解码 decode：从二进制解码成字符	bytes -> str

Python3 编码：https://mp.weixin.qq.com/s/RSCI3kil6KvyQjA7ZXsg2w