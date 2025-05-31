# inventory_item.py
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class InventoryItem:
    # 实例属性 (会被包含在 __init__, __repr__ 等)
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    # 类属性 - 方式1: 直接赋值 (没有被 dataclass 当作字段)
    # 注意：如果这里也用了类型注解如 tax_rate: float = 0.05，
    # dataclass 默认会把它当作一个有默认值的实例字段。
    # 所以，对于不想成为实例字段的类属性，要么不用类型注解，要么用 ClassVar。
    _internal_category_code = "GEN_ITEM" # 通常用于内部，不希望外部直接依赖

    # 类属性 - 方式2: 使用 ClassVar (推荐，更明确)
    # 这个属性不会成为 __init__ 的参数，也不会出现在默认的 repr 中
    tax_rate: ClassVar[float] = 0.05
    supported_currencies: ClassVar[list[str]] = ["USD", "EUR"] # 注意可变类属性的共享特性

    # 这是一个实例属性，但它不会在 __init__ 中初始化，
    # 它的值在 __post_init__ 中基于其他实例属性计算。
    total_value: float = field(init=False)

    def __post_init__(self):
        self.total_value = self.unit_price * self.quantity_on_hand

    def get_price_with_tax(self) -> float:
        return self.unit_price * (1 + InventoryItem.tax_rate) # 访问类属性

# 示例用法
if __name__ == "__main__":
    item1 = InventoryItem("Laptop", 1200.00, 5)
    item2 = InventoryItem("Mouse", 25.00, 20)

    print("--- 实例属性 ---")
    print(f"{item1.name}: Price={item1.unit_price}, Qty={item1.quantity_on_hand}, Total Value={item1.total_value}")
    print(f"{item2.name}: Price={item2.unit_price}, Qty={item2.quantity_on_hand}, Total Value={item2.total_value}")

    print("\n--- 类属性访问 (通过类名) ---")
    print(f"Tax Rate: {InventoryItem.tax_rate}")
    print(f"Supported Currencies: {InventoryItem.supported_currencies}")
    print(f"Internal Category Code: {InventoryItem._internal_category_code}")


    print("\n--- 类属性访问 (通过实例名) ---")
    print(f"Item 1 Tax Rate: {item1.tax_rate}") # 实际访问的是 InventoryItem.tax_rate
    print(f"Item 1 Currencies: {item1.supported_currencies}")

    print("\n--- 修改类属性 ---")
    InventoryItem.tax_rate = 0.07 # 修改会影响所有实例未来的计算（如果它们通过类访问）
    print(f"New Tax Rate: {InventoryItem.tax_rate}")
    print(f"Item 1 Price with new tax: {item1.get_price_with_tax()}") # item1 的计算会使用新的税率
    print(f"Item 2 Price with new tax: {item2.get_price_with_tax()}")

    print("\n--- 注意可变类属性的共享 ---")
    item1.supported_currencies.append("JPY") # 这修改了类本身的列表
    print(f"Item 1 Currencies: {item1.supported_currencies}")
    print(f"Item 2 Currencies: {item2.supported_currencies}") # item2 也会看到变化
    print(f"InventoryItem Currencies: {InventoryItem.supported_currencies}")

    print("\n--- 尝试在实例上“覆盖”类属性 ---")
    item1.tax_rate = 0.10 # 这在 item1 上创建了一个名为 tax_rate 的新 *实例* 属性
                         # InventoryItem.tax_rate 仍然是 0.07
    print(f"Item 1 (instance) Tax Rate: {item1.tax_rate}") # 输出 0.10
    print(f"Item 2 Tax Rate (from class): {item2.tax_rate}") # 输出 0.07 (因为 item2 没有自己的 tax_rate 实例属性)
    print(f"InventoryItem Class Tax Rate: {InventoryItem.tax_rate}") # 输出 0.07

    # item1.get_price_with_tax() 仍然会使用 InventoryItem.tax_rate，因为方法内部是这样写的。
    # 如果想让它使用实例上的 tax_rate (如果存在)，方法需要修改为 self.tax_rate
    print(f"Item 1 Price with tax (method uses class tax_rate): {item1.get_price_with_tax()}")