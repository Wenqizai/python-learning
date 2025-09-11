""" 
重载 max 函数

解决问题：TypeError: '>' not supported between instances of 'int' and
'NoneType'
"""

# 创建一个唯一的标记对象，用于检测是否提供了 default 参数
MISSING = object()

# 定义空序列时的错误消息常量
EMPTY_MSG = 'max() arg is an empty sequence'


def max(first, *args, key=None, default=MISSING):
    """
    重载的 max 函数，处理包含 None 值的序列
    
    参数:
        first: 第一个参数。如果只有位置参数，这是可迭代对象；如果有多参数，这是第一个比较值
        *args: 可变位置参数。如果提供，则与 first 一起作为多个值比较
        key: 可选的函数参数，用于从每个元素中提取比较键
        default: 可选参数，当序列为空时返回的默认值
    
    返回:
        序列中的最大值
    """
    
    # 判断是否提供了多个位置参数 (max(a, b, c) 模式)
    if args:
        # 如果有 *args，说明是多个值比较模式
        # 将第一个值和其余值组合成要比较的序列
        series = args
        candidate = first  # 候选最大值设为第一个参数
    else:
        # 如果没有 *args，说明是单参数可迭代对象模式 (max([a, b, c]) 模式)
        # 将 first 转换为迭代器
        series = iter(first)
        try: 
            # 尝试获取迭代器的第一个元素作为候选最大值
            candidate = next(series)
        except StopIteration:
            # 如果迭代器为空（空序列），检查是否提供了默认值
            if default is not MISSING:
                return default
            # 如果没有提供默认值，抛出 ValueError
            raise ValueError(EMPTY_MSG) from None
    
    # 判断是否使用了 key 函数进行键值比较
    if key is None:
        # 没有 key 函数时，直接比较元素值
        for current in series:  # 遍历剩余的元素
            if candidate < current:  # 如果找到更大的值
                candidate = current  # 更新候选最大值
    else:
        # 使用 key 函数时，先提取候选值的键
        candidate_key = key(candidate)
        for current in series:  # 遍历剩余的元素
            current_key = key(current)  # 提取当前元素的键
            if candidate_key < current_key:  # 比较键值
                candidate = current  # 更新候选最大值
                candidate_key = current_key  # 更新候选键值
    return candidate



