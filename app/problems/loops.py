loops = [
    {
        "id": 21,
        "title": "FizzBuzz",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def fizzbuzz(n):\n    for i in range(1, n+1):\n        if i % 3 == 0 and i % 5 == 0:\n            print('FizzBuzz')\n        elif i % 3 == 0:\n            print('Fizz')\n        elif i % 5 == 0:\n            print('Buzz')\n        else:\n            print(i)",
        "java_solution": "public void fizzBuzz(int n) {\n    for (int i = 1; i <= n; i++) {\n        if (i % 3 == 0 && i % 5 == 0) System.out.println(\"FizzBuzz\");\n        else if (i % 3 == 0) System.out.println(\"Fizz\");\n        else if (i % 5 == 0) System.out.println(\"Buzz\");\n        else System.out.println(i);\n    }\n}",
        "differences": [
            "Python uses 'and', Java uses '&&'",
            "Python print() vs Java System.out.println()",
            "Python range(1, n+1) vs Java for loop with i++"
        ],
        "pseudocode": "1. Loop from 1 to n\n2. If divisible by both 3 and 5 → FizzBuzz\n3. Else if divisible by 3 → Fizz\n4. Else if divisible by 5 → Buzz\n5. Else → print number",
        "explanation": "The logic is identical in both languages. Python uses 'and' to combine conditions while Java uses '&&'. Python's print() is simple, Java's System.out.println() is more verbose but does the same thing."
    },
    {
        "id": 22,
        "title": "Sum of Digits",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def sum_of_digits(n):\n    total = 0\n    while n > 0:\n        total += n % 10\n        n //= 10\n    return total",
        "java_solution": "public int sumOfDigits(int n) {\n    int total = 0;\n    while (n > 0) {\n        total += n % 10;\n        n /= 10;\n    }\n    return total;\n}",
        "differences": [
            "Python //= for integer division assignment, Java uses /=",
            "Java needs int type declaration",
            "Logic is nearly identical"
        ],
        "pseudocode": "1. While n > 0:\n2.    Add last digit (n % 10) to total\n3.    Remove last digit (n // 10)\n4. Return total",
        "explanation": "One of the closest-looking Python-Java pairs. Python uses //= for integer division assignment, Java uses /= which does integer division automatically for int types. The algorithm is identical."
    },
    {
        "id": 23,
        "title": "Power of Two",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def is_power_of_two(n):\n    if n <= 0:\n        return False\n    while n % 2 == 0:\n        n //= 2\n    return n == 1",
        "java_solution": "public boolean isPowerOfTwo(int n) {\n    if (n <= 0) return false;\n    while (n % 2 == 0) n /= 2;\n    return n == 1;\n}",
        "differences": [
            "Python returns True/False, Java returns true/false (lowercase)",
            "Python //= vs Java /=",
            "Logic is identical"
        ],
        "pseudocode": "1. If n <= 0 → return false\n2. While n is divisible by 2 → divide by 2\n3. If n == 1 → it was a power of 2",
        "explanation": "Boolean values are capitalized in Python (True/False) but lowercase in Java (true/false). This is one of the most common syntax mistakes when switching between them. The algorithm itself is identical."
    },
    {
        "id": 24,
        "title": "Print Multiplication Table",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def multiplication_table(n):\n    for i in range(1, n+1):\n        for j in range(1, n+1):\n            print(f'{i*j:4}', end='')\n        print()",
        "java_solution": "public void multiplicationTable(int n) {\n    for (int i = 1; i <= n; i++) {\n        for (int j = 1; j <= n; j++) {\n            System.out.printf(\"%4d\", i * j);\n        }\n        System.out.println();\n    }\n}",
        "differences": [
            "Python f-string formatting vs Java printf",
            "Python print(end='') to suppress newline, Java uses printf",
            "Python print() with no args prints newline, Java System.out.println()"
        ],
        "pseudocode": "1. For each row i from 1 to n:\n2.    For each column j from 1 to n:\n3.        Print i*j with formatting\n4.    Print newline",
        "explanation": "Nested loops work identically. The formatting differs significantly — Python's f-strings with format spec {:4} vs Java's printf with %4d. Python's print(end='') suppresses the newline, while Java's printf doesn't add one by default."
    },
    {
        "id": 25,
        "title": "Number of Steps to Zero",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def number_of_steps(num):\n    steps = 0\n    while num > 0:\n        if num % 2 == 0:\n            num //= 2\n        else:\n            num -= 1\n        steps += 1\n    return steps",
        "java_solution": "public int numberOfSteps(int num) {\n    int steps = 0;\n    while (num > 0) {\n        if (num % 2 == 0) num /= 2;\n        else num -= 1;\n        steps++;\n    }\n    return steps;\n}",
        "differences": [
            "Python steps += 1 vs Java steps++",
            "Python //= vs Java /=",
            "Logic is identical"
        ],
        "pseudocode": "1. While num > 0:\n2.    If even → divide by 2\n3.    If odd → subtract 1\n4.    Increment steps\n5. Return steps",
        "explanation": "Another case where Python and Java are nearly identical. The increment operator ++ doesn't exist in Python — you must use += 1. Java's ++ is a common shorthand that Python simply chose not to include."
    },
    {
        "id": 26,
        "title": "Reverse Digits of Number",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def reverse_digits(n):\n    sign = -1 if n < 0 else 1\n    n = abs(n)\n    reversed_num = 0\n    while n > 0:\n        reversed_num = reversed_num * 10 + n % 10\n        n //= 10\n    return sign * reversed_num",
        "java_solution": "public int reverseDigits(int n) {\n    int sign = n < 0 ? -1 : 1;\n    n = Math.abs(n);\n    long reversed = 0;\n    while (n > 0) {\n        reversed = reversed * 10 + n % 10;\n        n /= 10;\n    }\n    return (int)(sign * reversed);\n}",
        "differences": [
            "Python ternary: x if condition else y vs Java: condition ? x : y",
            "Python abs() vs Java Math.abs()",
            "Java uses long to avoid overflow, Python handles big ints natively"
        ],
        "pseudocode": "1. Save sign, work with absolute value\n2. While n > 0:\n3.    Extract last digit\n4.    Build reversed number\n5. Return sign * reversed",
        "explanation": "Python's ternary operator reads naturally: 'value if condition else other'. Java's ternary uses ? and : which is more compact but less readable for beginners. Python handles arbitrarily large integers natively — Java needs long to avoid overflow."
    },
    {
        "id": 27,
        "title": "Happy Number",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def is_happy(n):\n    seen = set()\n    while n != 1:\n        if n in seen:\n            return False\n        seen.add(n)\n        n = sum(int(d)**2 for d in str(n))\n    return True",
        "java_solution": "public boolean isHappy(int n) {\n    Set<Integer> seen = new HashSet<>();\n    while (n != 1) {\n        if (seen.contains(n)) return false;\n        seen.add(n);\n        int sum = 0;\n        while (n > 0) { int d = n % 10; sum += d * d; n /= 10; }\n        n = sum;\n    }\n    return true;\n}",
        "differences": [
            "Python sum(int(d)**2 for d in str(n)) is one elegant line",
            "Java needs a nested loop to sum digit squares",
            "Python converts number to string to iterate digits, Java uses math"
        ],
        "pseudocode": "1. Track seen numbers in a set\n2. While n != 1:\n3.    If n seen before → not happy (cycle)\n4.    Calculate sum of squared digits\n5. Return true if reached 1",
        "explanation": "Python's generator expression sum(int(d)**2 for d in str(n)) is one of the language's most powerful features — converting a number to a string to iterate its digits. Java takes the mathematical approach with a nested while loop. Both work but Python's is far more concise."
    },
    {
        "id": 28,
        "title": "Climbing Stairs",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def climb_stairs(n):\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n+1):\n        a, b = b, a + b\n    return b",
        "java_solution": "public int climbStairs(int n) {\n    if (n <= 2) return n;\n    int a = 1, b = 2;\n    for (int i = 3; i <= n; i++) {\n        int temp = a + b;\n        a = b;\n        b = temp;\n    }\n    return b;\n}",
        "differences": [
            "Python swaps in one line: a, b = b, a + b",
            "Java needs temp variable for swap",
            "Python _ as throwaway loop variable"
        ],
        "pseudocode": "1. Base case: n <= 2 → return n\n2. Start with a=1, b=2\n3. Each step: new b = a + b, new a = old b\n4. Return b",
        "explanation": "This is essentially Fibonacci. Python's simultaneous assignment (a, b = b, a+b) is one of its most elegant features — both sides evaluate before any assignment happens. Java needs a temp variable for the same effect. Python's _ convention signals an unused loop variable."
    },
    {
        "id": 29,
        "title": "Print Prime Numbers",
        "difficulty": "Medium",
        "topic": "Loops",
        "python_solution": "def print_primes(n):\n    for num in range(2, n+1):\n        is_prime = True\n        for i in range(2, int(num**0.5) + 1):\n            if num % i == 0:\n                is_prime = False\n                break\n        if is_prime:\n            print(num)",
        "java_solution": "public void printPrimes(int n) {\n    for (int num = 2; num <= n; num++) {\n        boolean isPrime = true;\n        for (int i = 2; i <= Math.sqrt(num); i++) {\n            if (num % i == 0) { isPrime = false; break; }\n        }\n        if (isPrime) System.out.println(num);\n    }\n}",
        "differences": [
            "Python int(num**0.5) vs Java Math.sqrt(num)",
            "Python boolean True/False vs Java true/false",
            "Python ** for power vs Java Math.pow() or direct multiplication"
        ],
        "pseudocode": "1. For each number from 2 to n:\n2.    Check if divisible by any number up to sqrt\n3.    If not divisible → it's prime, print it",
        "explanation": "The prime checking algorithm is identical. Python uses ** for exponentiation (num**0.5 = square root), Java uses Math.sqrt(). Python's boolean literals are capitalized, Java's are lowercase — a small but common source of errors."
    },
    {
        "id": 30,
        "title": "Flatten Nested List",
        "difficulty": "Medium",
        "topic": "Loops",
        "python_solution": "def flatten(nested):\n    result = []\n    for item in nested:\n        if isinstance(item, list):\n            result.extend(flatten(item))\n        else:\n            result.append(item)\n    return result",
        "java_solution": "public List<Integer> flatten(List<Object> nested) {\n    List<Integer> result = new ArrayList<>();\n    for (Object item : nested) {\n        if (item instanceof List) {\n            result.addAll(flatten((List<Object>) item));\n        } else {\n            result.add((Integer) item);\n        }\n    }\n    return result;\n}",
        "differences": [
            "Python isinstance() vs Java instanceof",
            "Python result.extend() vs Java result.addAll()",
            "Java needs explicit casting (Integer) item"
        ],
        "pseudocode": "1. For each item in list:\n2.    If item is a list → recursively flatten\n3.    Otherwise → add to result\n4. Return flattened result",
        "explanation": "Python's dynamic typing makes this much cleaner — no casting needed. Java's instanceof works like isinstance() but requires explicit casting when you use the object. Python's extend() and Java's addAll() both merge lists."
    },
]
