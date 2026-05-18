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
]
