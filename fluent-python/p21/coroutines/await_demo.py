"""
演示 await 的重要性：对比有无 await 的区别
"""
import asyncio
import time

async def say_hello_without_await(name: str):
    """不使用 await 的版本"""
    print(f"开始处理 {name}")
    asyncio.sleep(1)  # 没有 await！
    print(f"完成处理 {name}")
    return f"Hello, {name}!"

async def say_hello_with_await(name: str):
    """使用 await 的版本"""
    print(f"开始处理 {name}")
    await asyncio.sleep(1)  # 有 await！
    print(f"完成处理 {name}")
    return f"Hello, {name}!"

async def main():
    """主协程函数"""
    print("=== 测试1：不使用 await ===")
    start_time = time.time()
    
    # 串行执行（不使用 await）
    result1 = await say_hello_without_await("Alice")
    result2 = await say_hello_without_await("Bob")
    
    end_time = time.time()
    print(f"结果: {result1}, {result2}")
    print(f"总耗时: {end_time - start_time:.2f} 秒")
    print()
    
    print("=== 测试2：使用 await ===")
    start_time = time.time()
    
    # 串行执行（使用 await）
    result1 = await say_hello_with_await("Alice")
    result2 = await say_hello_with_await("Bob")
    
    end_time = time.time()
    print(f"结果: {result1}, {result2}")
    print(f"总耗时: {end_time - start_time:.2f} 秒")
    print()
    
    print("=== 测试3：并发执行（使用 await）===")
    start_time = time.time()
    
    # 并发执行
    results = await asyncio.gather(
        say_hello_with_await("Charlie"),
        say_hello_with_await("David")
    )
    
    end_time = time.time()
    print(f"结果: {results}")
    print(f"总耗时: {end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())
