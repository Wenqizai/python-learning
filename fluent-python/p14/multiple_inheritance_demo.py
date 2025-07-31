#!/usr/bin/env python3
"""
Python 多重继承演示程序
展示各种多重继承的使用场景和最佳实践

本程序通过8个不同的示例，全面展示Python多重继承的各种用法：
1. 基本多重继承 - 展示如何从多个父类继承功能
2. 钻石问题 - 演示MRO如何解决方法调用冲突
3. 混入类模式 - 展示如何设计可复用的功能模块
4. 抽象基类结合多重继承 - 规范接口的同时提供灵活性
5. 复杂混入类 - 实际应用中的高级技巧
6. 协作式继承 - 正确使用super()的方法
7. Protocol的现代方法 - Python 3.8+的新特性
8. 反面示例 - 应该避免的错误做法
"""

from abc import ABC, abstractmethod
from collections import UserDict, Counter
from typing import Protocol


# ==================== 1. 基本多重继承示例 ====================
print("=" * 60)
print("1. 基本多重继承示例")
print("=" * 60)
print("""
说明：这个示例展示了多重继承的基本用法。
- Animal类提供基础的动物属性和行为
- Flyable和Swimmable是功能性接口，提供特定能力
- Duck类通过多重继承获得了所有父类的功能
- 继承顺序很重要：Duck(Animal, Flyable, Swimmable)
- MRO决定了方法查找的顺序
""")

class Animal:
    """基础动物类，提供名称和基本行为"""
    def __init__(self, name):
        self.name = name
        print(f"  Animal.__init__: 创建动物 {name}")
    
    def speak(self):
        print(f"  {self.name} makes a sound")

class Flyable:
    """飞行能力混入类"""
    def fly(self):
        print(f"  {self.name} is flying high in the sky!")

class Swimmable:
    """游泳能力混入类"""
    def swim(self):
        print(f"  {self.name} is swimming gracefully in water!")

class Duck(Animal, Flyable, Swimmable):
    """鸭子类：继承动物基础功能，同时具备飞行和游泳能力"""
    def __init__(self, name):
        print(f"Duck.__init__: 开始创建鸭子 {name}")
        super().__init__(name)  # 调用Animal的__init__
        print(f"Duck.__init__: 鸭子 {name} 创建完成")
    
    def speak(self):
        """重写父类方法，提供鸭子特有的叫声"""
        print(f"  {self.name} says quack! quack!")

# 演示基本多重继承
print("创建Duck实例：")
duck = Duck("Donald")

print("\n调用各种方法：")
duck.speak()    # 调用重写的方法
duck.fly()      # 从Flyable继承
duck.swim()     # 从Swimmable继承

print(f"\nDuck的方法解析顺序(MRO):")
for i, cls in enumerate(Duck.__mro__):
    print(f"  {i+1}. {cls}")

print("\n解释：")
print("- MRO决定了方法查找顺序：Duck -> Animal -> Flyable -> Swimmable -> object")
print("- 当调用duck.speak()时，首先在Duck中找到，所以执行Duck.speak()")
print("- 当调用duck.fly()时，Duck中没有，按MRO顺序在Flyable中找到")
print("- super()会按照MRO顺序调用下一个类的方法")
print()


# ==================== 2. 钻石问题演示 ====================
print("=" * 60)
print("2. 钻石问题演示 (Diamond Problem)")
print("=" * 60)
print("""
说明：钻石问题是多重继承中的经典问题
继承结构：
    Base
   /    \\
 Left    Right
   \\    /
   Diamond

问题：如果Left和Right都重写了Base的方法，Diamond应该调用哪个？
解决：Python使用C3线性化算法确定MRO，确保每个类只被调用一次
""")

class Base:
    """基础类，所有类的共同祖先"""
    def __init__(self):
        print("  Base.__init__: 基础类初始化")
    
    def method(self):
        print("  Base.method: 基础实现")

class Left(Base):
    """左分支类"""
    def __init__(self):
        print("  Left.__init__: 左分支初始化")
        super().__init__()  # 注意：这里调用的不一定是Base.__init__
    
    def method(self):
        print("  Left.method: 左分支实现")
        super().method()  # 按MRO调用下一个类的方法

class Right(Base):
    """右分支类"""
    def __init__(self):
        print("  Right.__init__: 右分支初始化")
        super().__init__()
    
    def method(self):
        print("  Right.method: 右分支实现")
        super().method()

class Diamond(Left, Right):
    """钻石类：同时继承Left和Right"""
    def __init__(self):
        print("  Diamond.__init__: 钻石类初始化")
        super().__init__()
    
    def method(self):
        print("  Diamond.method: 钻石类实现")
        super().method()

# 演示钻石问题的解决
print("创建 Diamond 实例 (观察初始化顺序):")
diamond = Diamond()

print("\n调用 method (观察方法调用顺序):")
diamond.method()

print(f"\nDiamond 的 MRO (方法解析顺序):")
for i, cls in enumerate(Diamond.__mro__):
    print(f"  {i+1}. {cls}")

print("\n关键理解：")
print("- 虽然Base被Left和Right都继承，但Base.__init__只会被调用一次")
print("- MRO确保了线性化：Diamond -> Left -> Right -> Base -> object")
print("- super()不是调用父类，而是调用MRO中的下一个类")
print("- 这就是为什么Left.super().__init__()调用的是Right.__init__，而不是Base.__init__")
print("- C3线性化算法保证了方法调用的一致性和唯一性")
print()


# ==================== 3. 混入类 (Mixin) 示例 ====================
print("=" * 60)
print("3. 混入类 (Mixin) 示例")
print("=" * 60)
print("""
说明：混入类是多重继承的最佳实践模式
特点：
- 混入类提供特定功能，但不能单独实例化
- 混入类应该放在继承列表的左侧
- 混入类通过super()与其他类协作
- 每个混入类只负责一个特定的功能领域

本例展示了三个实用的混入类：
1. LoggerMixin - 提供日志功能
2. TimestampMixin - 提供时间戳功能  
3. ValidationMixin - 提供数据验证功能
""")

class LoggerMixin:
    """日志混入类 - 为任何类添加日志功能"""
    def log(self, message):
        class_name = self.__class__.__name__
        print(f"  [{class_name}] {message}")

class TimestampMixin:
    """时间戳混入类 - 为任何类添加创建时间跟踪"""
    def __init__(self, *args, **kwargs):
        # 重要：混入类必须调用super().__init__()以支持协作式继承
        super().__init__(*args, **kwargs)
        import datetime
        self.created_at = datetime.datetime.now()
        if hasattr(self, 'log'):  # 如果有日志功能，即 log 方法，就记录
            self.log("Timestamp initialized")
    
    def get_age(self):
        """获取对象存在的时间（秒）"""
        import datetime
        age = datetime.datetime.now() - self.created_at
        return age.total_seconds()

class ValidationMixin:
    """验证混入类 - 为任何类添加数据验证功能"""
    def validate(self, data):
        """验证数据不能为空"""
        if not data:
            raise ValueError("Data cannot be empty")
        if hasattr(self, 'log'):  # 如果有日志功能, 即 log 方法，就记录
            self.log("Data validation passed")
        return True

class User(LoggerMixin, TimestampMixin, ValidationMixin):
    """用户类：组合了日志、时间戳和验证功能"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # 调用super().__init__()会按MRO顺序初始化所有混入类
        super().__init__()
        self.log(f"User {name} created with email {email}")
    
    def update_email(self, new_email):
        """更新邮箱地址，包含验证和日志记录"""
        self.validate(new_email)  # 使用ValidationMixin的功能
        old_email = self.email
        self.email = new_email
        self.log(f"Email updated from {old_email} to {new_email}")  # 使用LoggerMixin的功能

# 演示混入类的使用
print("创建User实例（观察混入类的协作）：")
user = User("Alice", "alice@example.com")

print("\n使用混入类提供的功能：")
user.update_email("alice.new@example.com")
print(f"  用户存在时间: {user.get_age():.4f} 秒")

print(f"\nUser类的MRO：")
for i, cls in enumerate(User.__mro__):
    print(f"  {i+1}. {cls}")

print("\n混入类设计要点：")
print("- LoggerMixin在最左侧，优先级最高")
print("- 每个混入类都使用super().__init__()支持协作")
print("- 混入类之间可以相互配合（如ValidationMixin调用LoggerMixin的log方法）")
print("- User类只需要关注自己的核心业务逻辑")
print()


# ==================== 4. 抽象基类 + 多重继承 ====================
print("=" * 60)
print("4. 抽象基类 + 多重继承 - 规范接口与灵活扩展")
print("=" * 60)
print("""
说明：抽象基类(ABC)与多重继承的结合使用
目标：既要规范接口，又要提供灵活的功能扩展

设计模式：
1. Shape作为抽象基类，定义必须实现的接口
2. ColorMixin和BorderMixin作为功能混入类
3. Rectangle继承抽象基类并混入功能类

优势：
- 强制子类实现核心方法（area, perimeter）
- 通过混入类提供可选功能（颜色、边框）
- 功能模块化，可以任意组合
- 符合开闭原则：对扩展开放，对修改封闭
""")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class ColorMixin:
    def __init__(self, color="black", *args, **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

class BorderMixin:
    def __init__(self, border_width=1, *args, **kwargs):
        self.border_width = border_width
        super().__init__(*args, **kwargs)
    
    def get_border_info(self):
        return f"Border width: {self.border_width}"

class Rectangle(ColorMixin, BorderMixin, Shape):
    def __init__(self, width, height, **kwargs):
        self.width = width
        self.height = height
        super().__init__(**kwargs)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height}, {self.color}, {self.get_border_info()})"

# 演示抽象基类 + 混入的组合使用
print("创建Rectangle实例（组合抽象基类和混入类）：")
rect = Rectangle(10, 5, color="red", border_width=2)
print(f"  创建的对象: {rect}")
print(f"  面积: {rect.area()}")
print(f"  周长: {rect.perimeter()}")
print(f"  颜色: {rect.get_color()}")
print(f"  边框信息: {rect.get_border_info()}")

print(f"\nRectangle的MRO：")
for i, cls in enumerate(Rectangle.__mro__):
    print(f"  {i+1}. {cls}")

print("\n设计要点：")
print("- Shape(ABC)确保Rectangle必须实现area()和perimeter()方法")
print("- ColorMixin和BorderMixin可以独立使用，提供额外功能")
print("- 混入类使用**kwargs支持参数传递")
print("- 这种设计既保证了接口规范，又提供了灵活的功能扩展")

# 演示不同的组合方式
print("\n演示其他组合方式：")
class Circle(ColorMixin, Shape):
    def __init__(self, radius, **kwargs):
        self.radius = radius
        super().__init__(**kwargs)
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(3, color="blue")
print(f"  圆形: 半径={circle.radius}, 颜色={circle.get_color()}, 面积={circle.area():.2f}")
print()


# ==================== 5. 复杂的混入类示例 ====================
print("=" * 60)
print("5. 复杂的混入类示例 - 大小写不敏感字典")
print("=" * 60)
print("""
说明：这是一个实际应用中的高级混入类示例
目标：创建大小写不敏感的字典和计数器

设计思路：
1. 创建UpperCaseMixin混入类，重写字典的关键方法
2. 将所有键转换为大写进行存储和查找
3. 可以与任何映射类型（dict、UserDict、Counter等）组合使用
4. 展示了混入类如何修改现有类的行为

技术要点：
- 混入类必须使用super()调用下一个类的方法
- 混入类应该在继承列表的左侧（优先级高）
- 通过重写特殊方法(__setitem__, __getitem__等)改变行为
""")

# 首先定义辅助函数

def _upper(key):
    """将键转换为大写，如果不是字符串则返回原值"""
    try:
        return key.upper()
    except AttributeError:
        return key

class UpperCaseMixin:
    """大小写不敏感的混入类"""
    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))

class UpperDict(UpperCaseMixin, UserDict):
    """大小写不敏感的字典"""
    pass

class UpperCounter(UpperCaseMixin, Counter):
    """大小写不敏感的计数器"""
    pass

# 演示大小写不敏感的数据结构
print("UpperDict 演示:")
ud = UpperDict([('name', 'Alice'), ('AGE', 30)])
ud['City'] = 'New York'
print(f"ud['name']: {ud['name']}")
print(f"ud['NAME']: {ud['NAME']}")
print(f"'city' in ud: {'city' in ud}")
print(f"ud.get('age'): {ud.get('age')}")

print("\nUpperCounter 演示:")
uc = UpperCounter(['apple', 'APPLE', 'Apple', 'banana', 'BANANA'])
print(f"Counter: {dict(uc)}")
print()


# ==================== 6. 协作式继承示例 ====================
print("=" * 60)
print("6. 协作式继承示例 - 正确使用super()和**kwargs")
print("=" * 60)
print("""
说明：协作式继承是多重继承中最重要的概念之一
问题：在多重继承中，如何确保所有父类的__init__方法都被正确调用？

解决方案：
1. 所有类都使用super().__init__()而不是直接调用父类
2. 使用**kwargs传递参数，让每个类提取自己需要的参数
3. 确保参数传递链不会中断

本例展示了错误做法和正确做法的对比：
""")

print("错误示例（会导致参数传递问题）：")
print("class BadA(Root):")
print("    def __init__(self, value, a_param=None):")
print("        super().__init__(value)  # 不接受其他参数")
print("")
print("正确示例（支持参数协作）：")

class Root:
    def __init__(self, value):
        self.value = value
        print(f"Root.__init__({value})")

class A(Root):
    def __init__(self, value, a_param=None, **kwargs):
        print(f"A.__init__({value}, a_param={a_param})")
        super().__init__(value, **kwargs)
        self.a_param = a_param

class B(Root):
    def __init__(self, value, b_param=None, **kwargs):
        print(f"B.__init__({value}, b_param={b_param})")
        super().__init__(value, **kwargs)
        self.b_param = b_param

class C(A, B):
    def __init__(self, value, a_param=None, b_param=None, c_param=None):
        print(f"C.__init__({value}, a_param={a_param}, b_param={b_param}, c_param={c_param})")
        super().__init__(value, a_param=a_param, b_param=b_param)
        self.c_param = c_param

# 演示协作式继承
print("创建 C 实例:")
c = C(42, a_param="A", b_param="B", c_param="C")
print(f"C MRO: {C.__mro__}")
print()


# ==================== 7. 使用 Protocol 的现代方法 ====================
print("=" * 60)
print("7. 使用 Protocol 的现代方法 - 结构化子类型")
print("=" * 60)
print("""
说明：Protocol是Python 3.8+引入的新特性，提供了结构化子类型(structural subtyping)
也称为"鸭子类型"的正式化版本

对比传统多重继承：
传统方式：class Circle(Drawable, Movable)  # 继承关系
Protocol方式：只要实现了相应方法就符合协议  # 结构关系

优势：
- 无需显式继承，只需实现相应方法
- 更灵活，避免了继承层次的复杂性
- 更好的类型检查支持
- 符合"组合优于继承"的设计原则

适用场景：
- 定义接口规范但不想强制继承
- 第三方库的对象需要符合某种协议
- 避免多重继承的复杂性
""")

class Drawable(Protocol):
    def draw(self) -> None: ...

class Movable(Protocol):
    def move(self, x: int, y: int) -> None: ...

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.x = 0
        self.y = 0
    
    def draw(self):
        print(f"Drawing circle with radius {self.radius} at ({self.x}, {self.y})")
    
    def move(self, x: int, y: int):
        self.x = x
        self.y = y
        print(f"Moved circle to ({self.x}, {self.y})")

def process_drawable_movable(obj: Drawable) -> None:
    """处理既可绘制又可移动的对象"""
    obj.draw()
    if hasattr(obj, 'move'):
        obj.move(10, 20)

# 演示 Protocol 的使用
print("演示Protocol的结构化子类型：")
circle = Circle(5)
print("  Circle类没有继承任何Protocol，但实现了相应方法")
process_drawable_movable(circle)

print("\n创建另一个符合协议的类：")
class Square:
    def __init__(self, size):
        self.size = size
        self.x = 0
        self.y = 0
    
    def draw(self):
        print(f"  Drawing square with size {self.size} at ({self.x}, {self.y})")
    
    def move(self, x: int, y: int):
        self.x = x
        self.y = y
        print(f"  Moved square to ({self.x}, {self.y})")

square = Square(4)
print("  Square类也没有继承Protocol，但同样符合协议")
process_drawable_movable(square)

print("\nProtocol的关键优势：")
print("- 无需修改现有类的继承关系")
print("- 第三方库的类可以自然地符合我们的协议")
print("- 类型检查器可以验证协议的实现")
print("- 避免了多重继承可能带来的复杂性")
print()


# ==================== 8. 反面示例：应该避免的做法 ====================
print("=" * 60)
print("8. 反面示例：应该避免的做法")
print("=" * 60)
print("""
说明：多重继承虽然强大，但容易被误用
以下是一些常见的错误做法和应该避免的陷阱：
""")

# 错误示例1：过深的继承层次
print("❌ 错误示例1：过深的继承层次")
class TooDeep1: 
    def method1(self): pass

class TooDeep2: 
    def method2(self): pass

class TooDeep3(TooDeep1, TooDeep2): 
    def method3(self): pass

class TooDeep4(TooDeep3): 
    def method4(self): pass

class TooDeep5(TooDeep4): 
    def method5(self): pass  # 继承层次过深，难以维护

print(f"  TooDeep5 的 MRO 长度: {len(TooDeep5.__mro__)}")
print("  问题：继承层次过深，难以理解和维护")

# 错误示例2：混入类单独使用
print("\n❌ 错误示例2：混入类设计不当")
class BadMixin:
    def mixin_method(self):
        # 这个方法依赖于其他类的属性，但没有检查
        return self.value * 2  # 假设 self.value 存在，但可能不存在

print("  问题：BadMixin依赖于self.value，但没有确保这个属性存在")
print("  不要这样做：BadMixin()  # 会出错，因为没有 value 属性")

# 错误示例3：不使用super()
print("\n❌ 错误示例3：不正确使用super()")
class BadParent1:
    def __init__(self):
        print("  BadParent1.__init__")
        self.value1 = 1

class BadParent2:
    def __init__(self):
        print("  BadParent2.__init__")
        self.value2 = 2

class BadChild(BadParent1, BadParent2):
    def __init__(self):
        # 错误：直接调用父类，破坏MRO
        BadParent1.__init__(self)  # 这样BadParent2.__init__不会被调用
        print("  BadChild.__init__")

print("  演示错误的super()使用：")
bad_child = BadChild()
print(f"  bad_child有value1: {hasattr(bad_child, 'value1')}")
print(f"  bad_child有value2: {hasattr(bad_child, 'value2')}")  # False!
print("  问题：BadParent2.__init__没有被调用")

# 错误示例4：混入类顺序错误
print("\n❌ 错误示例4：混入类顺序错误")
class CoreClass:
    def method(self):
        return "core"

class ImportantMixin:
    def method(self):
        return "important " + super().method()

class LessImportantMixin:
    def method(self):
        return "less important " + super().method()

# 错误的顺序
class WrongOrder(CoreClass, ImportantMixin, LessImportantMixin):
    pass

# 正确的顺序  
class RightOrder(ImportantMixin, LessImportantMixin, CoreClass):
    pass

print("  错误顺序的结果:", WrongOrder().method())
print("  正确顺序的结果:", RightOrder().method())
print("  问题：混入类应该在基类左侧，重要的混入类应该在最左侧")

print("\n✅ 多重继承的最佳实践总结：")
print("1. 保持继承层次简单（通常不超过3-4层）")
print("2. 混入类应该设计为不能单独实例化")
print("3. 总是使用super()而不是直接调用父类")
print("4. 混入类放在继承列表左侧，重要的在最左")
print("5. 使用抽象基类定义接口规范")
print("6. 考虑使用组合、装饰器或Protocol替代复杂的多重继承")
print("7. 优先考虑代码的可读性和可维护性")
print()


# ==================== 总结 ====================
print("=" * 50)
print("总结")
print("=" * 50)
print("Python 多重继承的关键点：")
print("1. 理解 MRO (方法解析顺序)")
print("2. 正确使用 super() 进行协作式继承")
print("3. 混入类应该设计为不能单独实例化")
print("4. 避免过深的继承层次")
print("5. 考虑使用组合、装饰器或 Protocol 作为替代方案")
print("6. 在复杂项目中优先考虑代码的可读性和可维护性")