""" 
编码解码器
"""

# 不同的编码器对同一字符串的编码结果不同
# latin_1 iso-8859-1 是单字节编码，所以对多字节字符会进行拆分
# utf_8 是多字节编码，所以对多字节字符不会进行拆分
# utf_16 是多字节编码，所以对多字节字符不会进行拆分
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

# 使用 codecs 模块
import codecs






