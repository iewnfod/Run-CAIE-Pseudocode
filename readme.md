\<variable> 可以是一个变量或者一个值
default_value = {'int': 0; 'bool': false; 'float': 0; 'str': ''}

| pseudocode | python |
| ---------- | ------ |
| DECLARE \<variable> : \<type> | \<variable> = default_value[\<type>] |
| IF \<statement> THEN | if \<statement>: |
| ELSE IF \<statement> THEN | elif \<statement>: |
| ELSE | else: |
| ENDIF | |
| \<variable> <- \<statement> | \<variable> = \<statement> |
| FOR \<variable> <- \<variable> TO \<variable> | for \<variable> in range(\<variable>, \<variable>+1) |
| NEXT \<variable> | |
| WHILE \<statement> DO | while \<statement>: |
| \<variable> <- INPUT() | \<variable> = input() |
| OUTPUT \<variable> | print(\<variable>) |
| <> | != |
| LENGTH(\<variable>) | len(\<variable>) |
| // ... | # ... |
| REPEAT | while True |
| UNTIL \<statement> | if \<statement>: break |
| AND | and |
| OR | or |
| NOT | not |
| = | == |
| ^ | ** |
| & | + |
| PROCEDURE | def |
| FUNCTION | def |


类型: INT: 0; BOOL: false; STRING: ''; REAL: 0
需要next+1的语句: IF | FOR | WHILE | REPEAT
需要next-1的语句: ENDIF | NEXT | ENDWHILE | UNTIL
需要current-1的语句: ELSE IF | ELSE

其实cie是不需要declare的，所以我们也可以不写，随地拉变量。
不支持case of(我相信也没什么人会写这个)
部分函数没有转化成python3的书写方式，而是通过定义那些函数达到可以运行的目的。
若要使用二维数组，请使用arr[a][b]而不是arr[a, b]

目前没有报错系统，所以，请尽可能保证代码的正确性。

在读取写入文件的时候请使用绝对路径，以避免一些不必要的错误发生。
若没有正常运行，请在同目录下找到同名的.py文件，手动运行。

# Example

// 1
DECLARE a : INT
a <- 1
OUTPUT(a)

// 2
IF a = 1 THEN
    OUTPUT(a+1)
ELSE IF a = 2 THEN
    OUTPUT(a+2)
ELSE
    OUTPUT a + 3
ENDIF

// 3
IF a = "1" THEN
    OUTPUT "Equal to 1"
ELSE
    OUTPUT "Not equal to 1"
ENDIF

// 3
INPUT a
OUTPUT a

// 4
FUNCTION add10(a)
    OUTPUT a + 10
    RETURN a + 10
ENDFUNCTION

OUTPUT add10(a)

// 5
DECLARE b : STRING
OUTPUT a, b

// 6
FOR i <- 1 TO 10
    OUTPUT i
NEXT i

// 7
OPEN "Desktop/test.txt"
WRITE a
CLOSE "Desktop/test.txt"

// 8
REPEAT
    a <- a + 1
    OUTPUT a
UNTIL a = 100

// 9
WHILE a <> 1000 DO
    a <- a + 1
    OUTPUT a
ENDWHILE
