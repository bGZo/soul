alias:: code/pseido, 伪代码
-
- 用词描述解决何种问题, 不包含具体实现
  - ```
    Extract the next word from the line (good)
    set word to get next token (poor)
    Append the file extension to the name (good)
    name = name + extension (poor)
    FOR all the characters in the name (good)
    FOR character = first to last (ok)
    ```
- 描述分解到单层循环或决策的地步
  - ```
    [X] Search the list and find the customer with highest balance
    ```
- 伪码因人而异, 没有详尽的符号, 因为供人阅读(!=机器)
- Specific Structured Programming Constructs
  collapsed:: true
  特定结构化编程组件(6) -- 逻辑/算法控制流
  - SEQUENCE
    - a linear progression where one task is performed sequentially after another
    - Several keywords
      - Input: READ, OBTAIN, GET
      - Output: PRINT, DISPLAY, SHOW
      - Compute: COMPUTE, CALCULATE, DETERMINE
      - Initialize: SET, INIT
      - Add one: INCREMENT, BUMP
    - ```
      Brush teeth
      Wash face
      Comb hair
      Smile in mirror
      ```
  - WHILE
    collapsed:: true
    - a loop (repetition) with a simple conditional test at its beginning.
    - ```
      WHILE employee.type NOT EQUAL manager AND personCount < numEmployees
        INCREMENT personCount
        CALL employeeList.getPerson with personCount RETURNING employee
      ENDWHILE
      ```
  - IF-THEN-ELSE
    collapsed:: true
    - a decision (selection) in which a choice is made between two alternative courses of action.
    - ```
      IF HoursWorked > NormalMax THEN
        Display overtime message
      ELSE
        Display regular time message
      ENDIF
      ```
  - (flow of control)
    ---
    (need more)
  - REPEAT-UNTIL
    - a loop with a simple conditional test at the bottom
  - FOR
    collapsed:: true
    - a "counting" loop
    - ```
      FOR each month of the year (good)
      FOR month = 1 to 12 (ok)
      FOR each employee in the list (good)
      FOR empno = 1 to listsize (ok)
      ```
  - CASE
    collapsed:: true
    - a multiway branch (decision) based on the value of an expression. CASE is a generalization of IF-THEN-ELSE.
    - ```
      CASE  Title  OF
        Mr      : Print "Mister"
        Mrs     : Print "Missus"
        Miss    : Print "Miss"
        Ms      : Print "Mizz"
        Dr      : Print "Doctor"
      ENDCASE
      ```
- NESTED **CONSTRUCTS**
  collapsed:: true
  嵌套结构
  - 组件可以彼此嵌套, 使用缩进(indented)区隔
  - ```
    SET total to zero
    REPEAT
      READ Temperature
      IF Temperature > Freezing THEN
          INCREMENT total
      END IF
    UNTIL Temperature < zero
    Print total
    ```
- INVOKING SUBPROCEDURES
  collapsed:: true
  调用子过程
  - ```
    CALL AvgAge with StudentAges
    CALL Swap with CurrentItem and TargetItem
    CALL Account.debit with CheckAmount
    CALL getBalance RETURNING aBalance
    CALL SquareRoot with orbitHeight RETURNING nominalOrbit
    ```
- EXCEPETION HANDLING
  collapsed:: true
  - ```
    BEGIN
      statements
    EXCEPTION
      WHEN exception type
          statements to handle exception
        WHEN another exception type
            statements to handle exception
    END
    ```
- ## Refs
  - [学会写伪代码 - fengMisaka](https://www.cnblogs.com/linuxAndMcu/p/11242905.html)
  - [Pseudocode Standard](https://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html)