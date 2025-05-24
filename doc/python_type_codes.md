# Python 类型码概览

Python 中"类型码"主要用于处理底层的二进制数据表示，常见于 `array` 模块和 `struct` 模块（以及间接通过 `memoryview.cast()`）。这些类型码是字符，通常代表了 C 语言中的数据类型。

## 1. `array` 模块的类型码

当你创建一个 `array.array` 对象时，需要指定一个类型码，它决定了数组中所有元素的类型和大小。

| 类型码 | C 类型             | Python 类型 | 最小字节数 | 备注                                   |
| :----- | :----------------- | :---------- | :--------- | :------------------------------------- |
| `'b'`  | signed char        | int         | 1          |                                        |
| `'B'`  | unsigned char      | int         | 1          |                                        |
| `'u'`  | Py_UNICODE         | Unicode char| 2          | Unicode 字符 (Python 3.x 中不常用)     |
| `'h'`  | signed short       | int         | 2          |                                        |
| `'H'`  | unsigned short     | int         | 2          |                                        |
| `'i'`  | signed int         | int         | 2          | (通常 4 字节)                          |
| `'I'`  | unsigned int       | int         | 2          | (通常 4 字节)                          |
| `'l'`  | signed long        | int         | 4          |                                        |
| `'L'`  | unsigned long      | int         | 4          |                                        |
| `'q'`  | signed long long   | int         | 8          | (如果平台支持)                         |
| `'Q'`  | unsigned long long | int         | 8          | (如果平台支持)                         |
| `'f'`  | float              | float       | 4          | 单精度浮点数                           |
| `'d'`  | double             | float       | 8          | 双精度浮点数                           |

**注意**:
*   实际的字节数可能因平台（操作系统和 CPU 架构）而异。
*   `array` 模块的类型码集合相对固定且有限。

## 2. `struct` 模块的格式字符

`struct` 模块用于在 Python 值和表示为 Python `bytes` 对象的 C 结构之间进行转换。它使用一套格式字符来定义数据的打包和解包方式。

| 格式 | C 类型             | Python 类型     | 标准尺寸 (字节) | 备注                                     |
| :--- | :----------------- | :-------------- | :-------------- | :--------------------------------------- |
| `x`  | pad byte           | no value        |                 | 填充字节                                 |
| `c`  | char               | bytes of length 1 | 1               |                                          |
| `b`  | signed char        | int             | 1               |                                          |
| `B`  | unsigned char      | int             | 1               |                                          |
| `?`  | _Bool              | bool            | 1               | (C99)                                    |
| `h`  | short              | int             | 2               |                                          |
| `H`  | unsigned short     | int             | 2               |                                          |
| `i`  | int                | int             | 4               |                                          |
| `I`  | unsigned int       | int             | 4               |                                          |
| `l`  | long               | int             | 4               |                                          |
| `L`  | unsigned long      | int             | 4               |                                          |
| `q`  | long long          | int             | 8               |                                          |
| `Q`  | unsigned long long | int             | 8               |                                          |
| `n`  | ssize_t            | int             | (平台相关)    | 指针大小的整数                           |
| `N`  | size_t             | int             | (平台相关)    | 指针大小的无符号整数                     |
| `e`  | (see notes)        | float           | 2               | 半精度浮点数 (IEEE 754)                  |
| `f`  | float              | float           | 4               | 单精度浮点数 (IEEE 754)                  |
| `d`  | double             | float           | 8               | 双精度浮点数 (IEEE 754)                  |
| `s`  | char[]             | bytes           |                 | 字符串 (前面可以带数字表示长度)        |
| `p`  | char[]             | bytes           |                 | Pascal 字符串 (第一个字节是长度)         |
| `P`  | void \*            | int             | (平台相关)    | 指针 (通常转换为整数)                    |

**`struct` 模块格式字符的额外特性:**

*   **字节序 (Endianness):** 格式字符串的第一个字符可以指定字节序：
    *   `@`: 本机字节序、大小和对齐方式 (默认)。
    *   `=`: 本机字节序，标准大小，无对齐。
    *   `<`: 小端字节序，标准大小，无对齐。
    *   `>`: 大端字节序，标准大小，无对齐。
    *   `!`: 网络字节序 (大端)，标准大小，无对齐。
*   **重复计数**: 可在格式字符前加数字表示重复，如 `'4h'` 表示 4 个 short。
*   **对齐**: `@` 会考虑对齐，其他标准模式通常不考虑。

**`memoryview.cast()` 与 `struct` 格式:**
`memoryview.cast(format, shape)` 中的 `format` 参数直接使用了 `struct` 模块的格式语法，这使得 `cast` 操作非常灵活。

## 总结

类型码提供了一种标准化的方式来描述和操作二进制数据：
*   在 `array.array` 上下文中，指的是 `array` 模块定义的字符。
*   在 `struct` 模块或 `memoryview.cast()` 上下文中，指的是 `struct` 模块的格式字符，功能更丰富。 