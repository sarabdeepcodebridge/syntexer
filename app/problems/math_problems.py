math_problems = [
    {
        "id": 31,
        "title": "Fibonacci",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for i in range(2, n + 1):\n        a, b = b, a + b\n    return b",
        "java_solution": "public int fibonacci(int n) {\n    if (n <= 1) return n;\n    int a = 0, b = 1;\n    for (int i = 2; i <= n; i++) {\n        int temp = a;\n        a = b;\n        b = temp + b;\n    }\n    return b;\n}",
        "differences": [
            "Python swaps variables in one line: a, b = b, a + b",
            "Java needs a temp variable to swap values",
            "Python range(2, n+1) vs Java for loop with i++"
        ],
        "pseudocode": "1. If n is 0 or 1 → return n\n2. Set a = 0, b = 1\n3. Loop from 2 to n:\n4.    Swap: new b = a + b, new a = old b\n5. Return b",
        "explanation": "Python's simultaneous variable assignment (a, b = b, a+b) is elegant and avoids the need for a temp variable. Java requires storing the old value before overwriting. This single-line swap is one of Python's most celebrated features."
    },
    {
        "id": 32,
        "title": "Is Prime",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True",
        "java_solution": "public boolean isPrime(int n) {\n    if (n < 2) return false;\n    for (int i = 2; i <= Math.sqrt(n); i++) {\n        if (n % i == 0) return false;\n    }\n    return true;\n}",
        "differences": [
            "Python int(n**0.5) vs Java (int)Math.sqrt(n)",
            "Python True/False vs Java true/false",
            "Python ** operator vs Java Math.sqrt()"
        ],
        "pseudocode": "1. If n < 2 → not prime\n2. Check divisibility from 2 to sqrt(n)\n3. If any divisor found → not prime\n4. Otherwise → prime",
        "explanation": "Square root optimization is identical in both. Python's ** operator computes powers directly. Java uses Math.sqrt() from the Math library. The boolean return values look the same but differ in capitalization — True vs true."
    },
    {
        "id": 33,
        "title": "Greatest Common Divisor",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a",
        "java_solution": "public int gcd(int a, int b) {\n    while (b != 0) {\n        int temp = a % b;\n        a = b;\n        b = temp;\n    }\n    return a;\n}",
        "differences": [
            "Python 'while b' uses truthiness (0 is falsy), Java needs b != 0",
            "Python simultaneous assignment vs Java temp variable",
            "Python is 3 lines, Java needs 6"
        ],
        "pseudocode": "1. While b is not 0:\n2.    Store a % b as new b\n3.    Old b becomes new a\n4. Return a",
        "explanation": "Python's truthiness makes 'while b' work — 0 evaluates to False. Java can't do this, needing explicit b != 0. The simultaneous assignment in Python again avoids the temp variable that Java requires. Euclid's algorithm is elegant in Python."
    },
    {
        "id": 34,
        "title": "Power Function",
        "difficulty": "Medium",
        "topic": "Math",
        "python_solution": "def my_pow(x, n):\n    if n < 0:\n        x, n = 1/x, -n\n    result = 1\n    while n:\n        if n % 2 == 1:\n            result *= x\n        x *= x\n        n //= 2\n    return result",
        "java_solution": "public double myPow(double x, int n) {\n    if (n < 0) { x = 1 / x; n = -n; }\n    double result = 1;\n    while (n != 0) {\n        if (n % 2 == 1) result *= x;\n        x *= x;\n        n /= 2;\n    }\n    return result;\n}",
        "differences": [
            "Python simultaneous assignment for negative n",
            "Python 'while n' vs Java 'while (n != 0)'",
            "Java needs double type declaration"
        ],
        "pseudocode": "1. Handle negative exponent\n2. Use fast exponentiation (binary method)\n3. If bit set → multiply result\n4. Square x, halve n each iteration",
        "explanation": "Fast exponentiation (binary exponentiation) halves the work each iteration. Python's 'while n' works because 0 is falsy. Java needs explicit != 0. Both achieve O(log n) time complexity with identical logic."
    },
    {
        "id": 35,
        "title": "Reverse Integer",
        "difficulty": "Medium",
        "topic": "Math",
        "python_solution": "def reverse_integer(x):\n    sign = -1 if x < 0 else 1\n    x = abs(x)\n    reversed_x = int(str(x)[::-1])\n    result = sign * reversed_x\n    if result < -2**31 or result > 2**31 - 1:\n        return 0\n    return result",
        "java_solution": "public int reverse(int x) {\n    long result = 0;\n    while (x != 0) {\n        result = result * 10 + x % 10;\n        x /= 10;\n    }\n    if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) return 0;\n    return (int) result;\n}",
        "differences": [
            "Python converts to string and slices, Java uses math",
            "Python 2**31 vs Java Integer.MAX_VALUE",
            "Java uses long to handle overflow during computation"
        ],
        "pseudocode": "1. Extract sign\n2. Reverse digits\n3. Check for overflow\n4. Return result with sign",
        "explanation": "Python's string conversion and slicing makes reversal trivial. Java takes the mathematical approach which is more efficient. Python's arbitrary precision integers mean overflow isn't a concern during computation — Java uses long as a safety buffer."
    },
    {
        "id": 36,
        "title": "Count Primes",
        "difficulty": "Medium",
        "topic": "Math",
        "python_solution": "def count_primes(n):\n    if n < 2:\n        return 0\n    sieve = [True] * n\n    sieve[0] = sieve[1] = False\n    for i in range(2, int(n**0.5) + 1):\n        if sieve[i]:\n            for j in range(i*i, n, i):\n                sieve[j] = False\n    return sum(sieve)",
        "java_solution": "public int countPrimes(int n) {\n    if (n < 2) return 0;\n    boolean[] sieve = new boolean[n];\n    Arrays.fill(sieve, true);\n    sieve[0] = sieve[1] = false;\n    for (int i = 2; i * i < n; i++) {\n        if (sieve[i]) {\n            for (int j = i * i; j < n; j += i) sieve[j] = false;\n        }\n    }\n    int count = 0;\n    for (boolean b : sieve) if (b) count++;\n    return count;\n}",
        "differences": [
            "Python [True] * n creates array, Java needs Arrays.fill()",
            "Python sum(sieve) counts Trues, Java needs explicit loop",
            "Python range(i*i, n, i) vs Java for loop with j += i"
        ],
        "pseudocode": "1. Create boolean array of size n\n2. Mark 0 and 1 as not prime\n3. For each prime found, mark its multiples\n4. Count remaining trues",
        "explanation": "Sieve of Eratosthenes. Python's list multiplication [True]*n and sum() function make it very concise. Java needs Arrays.fill() and an explicit counting loop. Python's range() with step parameter (range(i*i, n, i)) is cleaner than Java's j+=i pattern."
    },
    {
        "id": 37,
        "title": "Integer to Roman",
        "difficulty": "Medium",
        "topic": "Math",
        "python_solution": "def int_to_roman(num):\n    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]\n    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']\n    result = ''\n    for i, v in enumerate(vals):\n        while num >= v:\n            result += syms[i]\n            num -= v\n    return result",
        "java_solution": "public String intToRoman(int num) {\n    int[] vals = {1000,900,500,400,100,90,50,40,10,9,5,4,1};\n    String[] syms = {\"M\",\"CM\",\"D\",\"CD\",\"C\",\"XC\",\"L\",\"XL\",\"X\",\"IX\",\"V\",\"IV\",\"I\"};\n    StringBuilder result = new StringBuilder();\n    for (int i = 0; i < vals.length; i++) {\n        while (num >= vals[i]) {\n            result.append(syms[i]);\n            num -= vals[i];\n        }\n    }\n    return result.toString();\n}",
        "differences": [
            "Python enumerate() vs Java manual index",
            "Python string += vs Java StringBuilder.append()",
            "Python list literals vs Java array literals with {}"
        ],
        "pseudocode": "1. Define value-symbol pairs in order\n2. For each value, while num >= value:\n3.    Append symbol, subtract value\n4. Return result string",
        "explanation": "The greedy algorithm is identical. Python's enumerate() avoids manual index tracking. Python's string concatenation with += works fine here. Java uses StringBuilder for efficiency — repeated string concatenation in Java creates many intermediate objects."
    },
    {
        "id": 38,
        "title": "Pascal's Triangle",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def generate_pascals(num_rows):\n    triangle = []\n    for i in range(num_rows):\n        row = [1] * (i + 1)\n        for j in range(1, i):\n            row[j] = triangle[i-1][j-1] + triangle[i-1][j]\n        triangle.append(row)\n    return triangle",
        "java_solution": "public List<List<Integer>> generate(int numRows) {\n    List<List<Integer>> triangle = new ArrayList<>();\n    for (int i = 0; i < numRows; i++) {\n        List<Integer> row = new ArrayList<>(Collections.nCopies(i + 1, 1));\n        for (int j = 1; j < i; j++) {\n            row.set(j, triangle.get(i-1).get(j-1) + triangle.get(i-1).get(j));\n        }\n        triangle.add(row);\n    }\n    return triangle;\n}",
        "differences": [
            "Python [1] * (i+1) vs Java Collections.nCopies()",
            "Python row[j] = vs Java row.set(j, value)",
            "Java's generic types List<List<Integer>> vs Python's simple list"
        ],
        "pseudocode": "1. For each row i:\n2.    Create row of 1s with size i+1\n3.    Fill middle values from previous row\n4.    Add row to triangle",
        "explanation": "Python's list multiplication [1]*(i+1) is much cleaner than Java's Collections.nCopies(). Java's List requires set() to modify elements, Python uses direct index assignment. Java's generic type system adds verbosity that Python completely avoids."
    },
    {
        "id": 39,
        "title": "Sqrt (Integer)",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def my_sqrt(x):\n    if x < 2:\n        return x\n    left, right = 1, x // 2\n    while left <= right:\n        mid = (left + right) // 2\n        if mid * mid == x:\n            return mid\n        elif mid * mid < x:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return right",
        "java_solution": "public int mySqrt(int x) {\n    if (x < 2) return x;\n    int left = 1, right = x / 2;\n    while (left <= right) {\n        int mid = (left + right) / 2;\n        if ((long)mid * mid == x) return mid;\n        else if ((long)mid * mid < x) left = mid + 1;\n        else right = mid - 1;\n    }\n    return right;\n}",
        "differences": [
            "Java casts to (long) to prevent integer overflow in multiplication",
            "Python // for integer division vs Java /",
            "Python handles large integers natively, Java needs long cast"
        ],
        "pseudocode": "1. Binary search between 1 and x/2\n2. If mid*mid == x → found exact sqrt\n3. If mid*mid < x → search right half\n4. If mid*mid > x → search left half\n5. Return right (floor of sqrt)",
        "explanation": "Binary search for square root. Java needs (long) cast because mid*mid can overflow int range. Python handles arbitrarily large integers natively — no overflow ever. This is a real advantage of Python's integer type."
    },
    {
        "id": 40,
        "title": "Roman to Integer",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def roman_to_int(s):\n    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}\n    result = 0\n    for i in range(len(s)):\n        if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:\n            result -= values[s[i]]\n        else:\n            result += values[s[i]]\n    return result",
        "java_solution": "public int romanToInt(String s) {\n    Map<Character, Integer> values = new HashMap<>();\n    values.put('I',1); values.put('V',5); values.put('X',10);\n    values.put('L',50); values.put('C',100); values.put('D',500); values.put('M',1000);\n    int result = 0;\n    for (int i = 0; i < s.length(); i++) {\n        if (i + 1 < s.length() && values.get(s.charAt(i)) < values.get(s.charAt(i+1)))\n            result -= values.get(s.charAt(i));\n        else\n            result += values.get(s.charAt(i));\n    }\n    return result;\n}",
        "differences": [
            "Python dict literal {} vs Java HashMap with multiple put() calls",
            "Python s[i] vs Java s.charAt(i)",
            "Python dict initialization is far more concise"
        ],
        "pseudocode": "1. Map each Roman symbol to its value\n2. For each character:\n3.    If next char is larger → subtract current\n4.    Otherwise → add current\n5. Return total",
        "explanation": "Python's dictionary literal initialization is dramatically cleaner than Java's HashMap which requires a separate put() call for each entry. Python's s[i] character access vs Java's s.charAt(i) is another readability difference. The algorithm is identical."
    },
]
