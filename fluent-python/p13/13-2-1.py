""" 
__getitem__ 实现的协议, 可以按索引获取项
"""
class Vowels: 
    def __getitem__(self, index): 
        return 'AEIOU'[index]

vowels = Vowels()
print(vowels[0])
print(vowels[-1])

for c in vowels: 
    print(c)

print('E' in vowels)
print('Z' in vowels)