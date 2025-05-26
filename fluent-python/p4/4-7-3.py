""" 
unicode 的规范化：极端情况下的规范化， 去掉变音符
"""

import unicodedata
import string

def shave_marks(txt):
    """ 
    去掉变音符
    """
    norm_txt = unicodedata.normalize('NFD', txt) # 把所有字符分解成基字符和组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c)) # 过滤掉组合记号
    return unicodedata.normalize('NFC', shaved) # 重新组合成标准形式


order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order))

Greek = 'Zέφupoς, Zéfiro'
print(shave_marks(Greek))


def shave_marks_latin(txt):
    """ 
    去掉拉丁字符串中的变音符
    """
    norm_txt = unicodedata.normalize('NFD', txt) # 把所有字符分解成基字符和组合记号
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue # 如果 c 是组合记号且 latin_base 为 True, 则跳过, 忽略拉丁基字符的变音符
        preserve.append(c)
        if not unicodedata.combining(c): # 如果 c 不是组合记号
            latin_base = c.isalpha()
    shaved = ''.join(preserve)
    return unicodedata.normalize('NFC', shaved)


print("--------------------------------")

single_map = str.maketrans("""‚ƒ„†ˆ‹›‘’“”•–—˜›""",  
                            """'f"*^<>>>''""---~>""")

multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    """ 
    把cp1252 转换为 ASCII 字符或字符序列
    """
    return txt.translate(multi_map)

def asciize(txt):
    """ 
    把文本转换为 ASCII 字符或字符序列
    """
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)










