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
