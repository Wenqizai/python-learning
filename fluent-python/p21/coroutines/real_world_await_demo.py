"""
真实场景演示：网络请求中的 await 重要性
"""
import asyncio
import time
from unittest import result

async def fetch_data_without_await(url: str):
    """模拟网络请求 - 错误方式（无 await）"""
    print(f"开始请求 {url}")
    # 模拟网络延迟
    result = asyncio.sleep(2)  # 没有 await！
    print(f"完成请求 {url}")
    return f"数据来自 {result}"

async def fetch_data_with_await(url: str):
    """模拟网络请求 - 正确方式（有 await）"""
    print(f"开始请求 {url}")
    # 模拟网络延迟
    result = await asyncio.sleep(2)  # 有 await！
    print(f"完成请求 {url}")
    return f"数据来自 {result}"

async def main():
    print("=== 场景1：错误方式 - 数据获取失败 ===")
    start_time = time.time()
    
    # 尝试获取多个数据源
    data1 = await fetch_data_without_await("API1")
    data2 = await fetch_data_without_await("API2")
    
    end_time = time.time()
    print(f"获取的数据: {data1}, {data2}")
    print(f"耗时: {end_time - start_time:.2f} 秒")
    print("问题：数据没有真正获取到，因为网络请求没有等待！")
    print()
    
    print("=== 场景2：正确方式 - 数据获取成功 ===")
    start_time = time.time()
    
    # 正确获取数据
    data1 = await fetch_data_with_await("API1")
    data2 = await fetch_data_with_await("API2")
    
    end_time = time.time()
    print(f"获取的数据: {data1}, {data2}")
    print(f"耗时: {end_time - start_time:.2f} 秒")
    print("正确：数据真正获取到了！")
    print()
    
    print("=== 场景3：并发获取 - 效率最高 ===")
    start_time = time.time()
    
    # 并发获取数据
    results = await asyncio.gather(
        fetch_data_with_await("API1"),
        fetch_data_with_await("API2"),
        fetch_data_with_await("API3")
    )
    
    end_time = time.time()
    print(f"获取的数据: {results}")
    print(f"耗时: {end_time - start_time:.2f} 秒")
    print("最佳：并发获取，效率最高！")

if __name__ == "__main__":
    asyncio.run(main())
