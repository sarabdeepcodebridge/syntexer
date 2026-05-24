problems = [
    {
        "id": 1,

        "title": "Two Sum",
        "difficulty": "Easy",
        "topic": "Arrays",
        "python_solution": "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i",
        "java_solution": "public int[] twoSum(int[] nums, int target) {\n    Map<Integer, Integer> seen = new HashMap<>();\n    for (int i = 0; i < nums.length; i++) {\n        int diff = target - nums[i];\n        if (seen.containsKey(diff)) {\n            return new int[]{seen.get(diff), i};\n        }\n        seen.put(nums[i], i);\n    }\n    return new int[]{};\n}",
        "differences": [
            "Python uses a dict, Java uses HashMap",
            "Python enumerate() vs Java for loop with index",
            "Python returns a list, Java returns int[]",

        ],
        "pseudocode": "1. Create empty map\n2. For each number in array:\n3.    Calculate difference = target - current number\n4.    If difference exists in map → return both indexes\n5.    Otherwise store current number and index in map",
"explanation": "Python uses a dictionary to store numbers it has seen. Java uses a HashMap which works the same way but requires explicit type declarations like Map<Integer, Integer>. Both check if the difference exists before storing — the core logic is identical, only the syntax differs.",
    },
    {
        "id": 2,
        "title": "Reverse a String",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def reverse_string(s):\n    return s[::-1]",
        "java_solution": "public String reverseString(String s) {\n    return new StringBuilder(s).reverse().toString();\n}",
        "differences": [
            "Python slicing [::-1] vs Java StringBuilder",
            "Python one line, Java needs method chaining",
            "No type declaration in Python"
        ],
        "pseudocode": "1. Take the string as input\n2. Reverse the order of all characters\n3. Return the reversed string",
        "explanation": "Python has built-in slicing with [::-1] which reads the string backwards in one step. Java doesn't have slicing, so you use StringBuilder which is a special object designed for string manipulation. The .reverse() method does the same job but requires more steps.",

    },
{
        "id": 3,
        "title": "FizzBuzz",
        "difficulty": "Easy",
        "topic": "Loops",
        "python_solution": "def fizzbuzz(n):\n    for i in range(1, n+1):\n        if i % 3 == 0 and i % 5 == 0:\n            print('FizzBuzz')\n        elif i % 3 == 0:\n            print('Fizz')\n        elif i % 5 == 0:\n            print('Buzz')\n        else:\n            print(i)",
        "java_solution": "public void fizzBuzz(int n) {\n    for (int i = 1; i <= n; i++) {\n        if (i % 3 == 0 && i % 5 == 0) {\n            System.out.println(\"FizzBuzz\");\n        } else if (i % 3 == 0) {\n            System.out.println(\"Fizz\");\n        } else if (i % 5 == 0) {\n            System.out.println(\"Buzz\");\n        } else {\n            System.out.println(i);\n        }\n    }\n}",
        "differences": [
            "Python uses 'and', Java uses '&&'",
            "Python print() vs Java System.out.println()",
            "Python range(1, n+1) vs Java for loop with i++"
        ],
        "pseudocode": "1. Loop from 1 to n\n2. If divisible by both 3 and 5 → print FizzBuzz\n3. Else if divisible by 3 → print Fizz\n4. Else if divisible by 5 → print Buzz\n5. Else → print the number",
        "explanation": "The logic is identical in both languages. The key difference is how they handle conditions — Python uses 'and' to combine conditions while Java uses '&&'. Python's print() is simple, Java's System.out.println() is more verbose but does the same thing.",
    },
{
        "id": 4,
        "title": "Palindrome Check",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def is_palindrome(s):\n    return s == s[::-1]",
        "java_solution": "public boolean isPalindrome(String s) {\n    String reversed = new StringBuilder(s).reverse().toString();\n    return s.equals(reversed);\n}",
        "differences": [
            "Python slicing [::-1] vs Java StringBuilder.reverse()",
            "Python == compares strings directly, Java uses .equals()",
            "Python returns in one line, Java needs multiple steps"
        ],
        "pseudocode": "1. Take string as input\n2. Reverse the string\n3. Compare reversed string with original\n4. If they match → return true\n5. Otherwise → return false",
        "explanation": "Python compares strings directly using == which works perfectly. Java cannot use == for string comparison because it compares memory addresses, not content. Java uses .equals() method instead. This is one of the most common Java mistakes for Python developers.",
    },
{
        "id": 5,
        "title": "Find Max in Array",
        "difficulty": "Easy",
        "topic": "Arrays",
        "python_solution": "def find_max(nums):\n    max_val = nums[0]\n    for num in nums:\n        if num > max_val:\n            max_val = num\n    return max_val",
        "java_solution": "public int findMax(int[] nums) {\n    int maxVal = nums[0];\n    for (int num : nums) {\n        if (num > maxVal) {\n            maxVal = num;\n        }\n    }\n    return maxVal;\n}",
        "differences": [
            "Python uses plain variable, Java needs int type declaration",
            "Python for num in nums vs Java enhanced for loop: for (int num : nums)",
            "Python is fewer lines — same logic, less syntax"
        ],
        "pseudocode": "1. Set max to first element\n2. Loop through every number\n3. If current number > max → update max\n4. Return max after loop ends",
        "explanation": "The logic is the same in both — loop through, compare, update max. The difference is Java requires you to declare the type of every variable explicitly with 'int'. Python figures out the type automatically. Java's enhanced for loop 'for (int num : nums)' is equivalent to Python's 'for num in nums'.",
    },
{
        "id": 6,
        "title": "Binary Search",
        "difficulty": "Medium",
        "topic": "Arrays",
        "python_solution": "def binary_search(nums, target):\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
        "java_solution": "public int binarySearch(int[] nums, int target) {\n    int left = 0, right = nums.length - 1;\n    while (left <= right) {\n        int mid = (left + right) / 2;\n        if (nums[mid] == target) {\n            return mid;\n        } else if (nums[mid] < target) {\n            left = mid + 1;\n        } else {\n            right = mid - 1;\n        }\n    }\n    return -1;\n}",
        "differences": [
            "Python uses // for integer division, Java uses /",
            "Python len(nums) vs Java nums.length",
            "Python unpacks two variables in one line: left, right = 0, len(nums)-1"
        ],
        "pseudocode": "1. Set left = 0, right = last index\n2. While left <= right:\n3.    Find middle index\n4.    If middle == target → return index\n5.    If middle < target → search right half\n6.    If middle > target → search left half\n7. Return -1 if not found",
        "explanation": "Binary search cuts the search space in half each time. Both Python and Java implement this identically in logic. The key difference is integer division — Python uses // to force whole numbers, Java's / operator already does integer division when both values are integers. Python also lets you assign two variables in one line which Java cannot do."
    },
{
        "id": 7,
        "title": "Count Vowels",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def count_vowels(s):\n    count = 0\n    for char in s:\n        if char.lower() in 'aeiou':\n            count += 1\n    return count",
        "java_solution": "public int countVowels(String s) {\n    int count = 0;\n    for (char c : s.toCharArray()) {\n        if (\"aeiou\".indexOf(Character.toLowerCase(c)) != -1) {\n            count++;\n        }\n    }\n    return count;\n}",
        "differences": [
            "Python checks 'if char in string' directly, Java uses .indexOf()",
            "Python char.lower() vs Java Character.toLowerCase(c)",
            "Python iterates string directly, Java needs .toCharArray()"
        ],
        "pseudocode": "1. Set count to 0\n2. Loop through each character\n3. Convert to lowercase\n4. If character is a vowel → increment count\n5. Return count",
        "explanation": "Python treats strings like a list — you can loop through characters directly and check membership with 'in'. Java strings are objects and need .toCharArray() to iterate character by character. Checking if a character is a vowel is also more verbose in Java — indexOf() returns -1 if not found, which Python handles more naturally with 'in'."
    },
{
        "id": 8,
        "title": "Fibonacci",
        "difficulty": "Easy",
        "topic": "Math",
        "python_solution": "def fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for i in range(2, n + 1):\n        a, b = b, a + b\n    return b",
        "java_solution": "public int fibonacci(int n) {\n    if (n <= 1) {\n        return n;\n    }\n    int a = 0, b = 1;\n    for (int i = 2; i <= n; i++) {\n        int temp = a;\n        a = b;\n        b = temp + b;\n    }\n    return b;\n}",
        "differences": [
            "Python swaps two variables in one line: a, b = b, a + b",
            "Java needs a temp variable to swap values",
            "Python range(2, n+1) vs Java for loop with i++"
        ],
        "pseudocode": "1. If n is 0 or 1 → return n\n2. Set a = 0, b = 1\n3. Loop from 2 to n:\n4.    Swap: new b = a + b, new a = old b\n5. Return b",
        "explanation": "The logic is identical but Python's variable swapping is much cleaner. In Python you can swap two variables in one line — a, b = b, a + b — without needing a temporary variable. Java requires a temp variable to hold the old value during the swap. This is one of Python's most elegant features that Java simply doesn't have."
    },
]
glossary = [
    {"python": "list", "java": "ArrayList", "example": "[] vs new ArrayList<>()"},
    {"python": "dict", "java": "HashMap", "example": "{} vs new HashMap<>()"},
    {"python": "len()", "java": ".size() / .length", "example": "len(arr) vs arr.length"},
    {"python": "None", "java": "null", "example": "if x is None vs if x == null"},
    {"python": "True / False", "java": "true / false", "example": "Lowercase in Java"},
    {"python": "print()", "java": "System.out.println()", "example": "print('hi') vs System.out.println('hi')"},
    {"python": "and / or", "java": "&& / ||", "example": "if a and b vs if (a && b)"},
    {"python": "def", "java": "public void / int / String", "example": "def fn() vs public void fn()"},
    {"python": "self", "java": "this", "example": "self.name vs this.name"},
    {"python": "elif", "java": "else if", "example": "elif x vs else if (x)"},
]
