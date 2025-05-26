""" 
unicode 文本排序

排序前设置区域生效

1. 区域设置全局生效，因此不建议在库中调用 setlocale 函数。应用程序或框架应该在启动进程时设定区域，而且此后不要再修改。
2. 操作系统必须支持你设定的区域，否则 setlocale 函数会抛出 locale.Error: unsupported locale setting 异常。
3. 你必须知道如何拼写区域名称。
4. 操作系统制造商必须正确实现你设定的区域。我在 Ubuntu 19.10 中成功了，但是在 macOS 10.14 中失败了。在 macOS 中，
   setlocale(LC_COLLATE, 'pt_BR.UTF-8') 调用返回字符串 'pt_BR.UTF-8'，没有报错。但是，sorted(fruits,
   key=locale.strxfrm) 的结果与 sorted(fruits) 一样，也是错的。我在 macOS 中也试过 fr_FR、es_ES 和 de_DE 等区域，locale.strxfrm 均未生效。
"""
import locale

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

# 变音字对排序有影响，['acerola', 'atemoia', 'açaí', 'caju', 'cajá']
print(sorted(fruits))

# 得到正确的结果， sorted 之前设置正确的区域
my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(my_locale)

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits, key=locale.strxfrm))

