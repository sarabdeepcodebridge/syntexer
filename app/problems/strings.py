strings = [
    {
        "id": 11,
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
        "explanation": "Python has built-in slicing with [::-1] which reads the string backwards in one step. Java doesn't have slicing, so you use StringBuilder which is a special object designed for string manipulation."
    },
    {
        "id": 12,
        "title": "Palindrome Check",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def is_palindrome(s):\n    return s == s[::-1]",
        "java_solution": "public boolean isPalindrome(String s) {\n    String reversed = new StringBuilder(s).reverse().toString();\n    return s.equals(reversed);\n}",
        "differences": [
            "Python == compares strings directly, Java uses .equals()",
            "Python slicing [::-1] vs Java StringBuilder.reverse()",
            "Python one line, Java needs multiple steps"
        ],
        "pseudocode": "1. Take string as input\n2. Reverse the string\n3. Compare reversed with original\n4. If they match → return true",
        "explanation": "The most common Java mistake for Python developers is using == for string comparison. In Java, == compares memory addresses not content. Always use .equals() in Java for string comparison."
    },
    {
        "id": 13,
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
        "explanation": "Python treats strings like a list — you can loop through characters directly. Java strings are objects and need .toCharArray() to iterate. Python's 'in' operator is much more readable than Java's indexOf() != -1."
    },
    {
        "id": 14,
        "title": "Valid Anagram",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def is_anagram(s, t):\n    return sorted(s) == sorted(t)",
        "java_solution": "public boolean isAnagram(String s, String t) {\n    char[] sArr = s.toCharArray();\n    char[] tArr = t.toCharArray();\n    Arrays.sort(sArr);\n    Arrays.sort(tArr);\n    return Arrays.equals(sArr, tArr);\n}",
        "differences": [
            "Python sorted() works on strings directly, Java needs toCharArray()",
            "Python == compares sorted strings, Java needs Arrays.equals()",
            "Python is one line, Java needs 5 lines"
        ],
        "pseudocode": "1. Sort both strings\n2. Compare sorted versions\n3. If equal → anagram",
        "explanation": "Python's sorted() function works directly on strings and returns a sorted list. Java can't sort strings directly — you must convert to a char array first. This is a pattern you'll see repeatedly: Python treats strings as sequences, Java treats them as objects."
    },
    {
        "id": 15,
        "title": "First Non-Repeating Character",
        "difficulty": "Medium",
        "topic": "Strings",
        "python_solution": "def first_unique_char(s):\n    count = {}\n    for char in s:\n        count[char] = count.get(char, 0) + 1\n    for i, char in enumerate(s):\n        if count[char] == 1:\n            return i\n    return -1",
        "java_solution": "public int firstUniqChar(String s) {\n    Map<Character, Integer> count = new HashMap<>();\n    for (char c : s.toCharArray())\n        count.put(c, count.getOrDefault(c, 0) + 1);\n    for (int i = 0; i < s.length(); i++)\n        if (count.get(s.charAt(i)) == 1) return i;\n    return -1;\n}",
        "differences": [
            "Python dict.get(key, default) vs Java map.getOrDefault()",
            "Python enumerate() vs Java manual index",
            "Python s[i] vs Java s.charAt(i)"
        ],
        "pseudocode": "1. Count frequency of each character\n2. Loop through string again\n3. Return index of first character with count 1\n4. Return -1 if none found",
        "explanation": "Both use a hash map to count frequencies. Python's dict.get(key, 0) and Java's getOrDefault() do the same thing — get value or return default. Python's enumerate() is cleaner than Java's manual index tracking."
    },
    {
        "id": 16,
        "title": "Longest Common Prefix",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def longest_common_prefix(strs):\n    if not strs:\n        return ''\n    prefix = strs[0]\n    for s in strs[1:]:\n        while not s.startswith(prefix):\n            prefix = prefix[:-1]\n            if not prefix:\n                return ''\n    return prefix",
        "java_solution": "public String longestCommonPrefix(String[] strs) {\n    if (strs.length == 0) return \"\";\n    String prefix = strs[0];\n    for (int i = 1; i < strs.length; i++) {\n        while (!strs[i].startsWith(prefix)) {\n            prefix = prefix.substring(0, prefix.length() - 1);\n            if (prefix.isEmpty()) return \"\";\n        }\n    }\n    return prefix;\n}",
        "differences": [
            "Python prefix[:-1] slicing vs Java prefix.substring()",
            "Python 'not strs' vs Java strs.length == 0",
            "Python 'not prefix' vs Java prefix.isEmpty()"
        ],
        "pseudocode": "1. Start with first string as prefix\n2. For each other string:\n3.    Shrink prefix until it matches start\n4. Return prefix",
        "explanation": "Python's slicing prefix[:-1] removes the last character cleanly. Java needs substring(0, length-1) for the same effect. Python's truthiness checks (not prefix) are more concise than Java's explicit isEmpty() calls."
    },
    {
        "id": 17,
        "title": "Count and Say",
        "difficulty": "Medium",
        "topic": "Strings",
        "python_solution": "def count_and_say(n):\n    result = '1'\n    for _ in range(n - 1):\n        new_result = ''\n        i = 0\n        while i < len(result):\n            count = 1\n            while i + count < len(result) and result[i] == result[i + count]:\n                count += 1\n            new_result += str(count) + result[i]\n            i += count\n        result = new_result\n    return result",
        "java_solution": "public String countAndSay(int n) {\n    String result = \"1\";\n    for (int i = 1; i < n; i++) {\n        StringBuilder sb = new StringBuilder();\n        int j = 0;\n        while (j < result.length()) {\n            int count = 1;\n            while (j + count < result.length() && result.charAt(j) == result.charAt(j + count))\n                count++;\n            sb.append(count).append(result.charAt(j));\n            j += count;\n        }\n        result = sb.toString();\n    }\n    return result;\n}",
        "differences": [
            "Python string concatenation += vs Java StringBuilder.append()",
            "Python result[i] vs Java result.charAt(i)",
            "Java StringBuilder is more efficient for repeated concatenation"
        ],
        "pseudocode": "1. Start with '1'\n2. For each iteration:\n3.    Count consecutive identical digits\n4.    Append count + digit to new string\n5. Return final string",
        "explanation": "Python string concatenation with += works but is less efficient than Java's StringBuilder for large strings. StringBuilder is Java's recommended approach for building strings in loops. The core algorithm is identical in both languages."
    },
    {
        "id": 18,
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "topic": "Strings",
        "python_solution": "def is_valid(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
        "java_solution": "public boolean isValid(String s) {\n    Stack<Character> stack = new Stack<>();\n    for (char c : s.toCharArray()) {\n        if (c == '(' || c == '{' || c == '[') stack.push(c);\n        else {\n            if (stack.isEmpty()) return false;\n            char top = stack.pop();\n            if (c == ')' && top != '(' || c == '}' && top != '{' || c == ']' && top != '[') return false;\n        }\n    }\n    return stack.isEmpty();\n}",
        "differences": [
            "Python uses dict for mapping, Java uses explicit comparisons",
            "Python 'not stack' vs Java stack.isEmpty()",
            "Java needs Stack<Character> type declaration"
        ],
        "pseudocode": "1. Create empty stack\n2. For each character:\n3.    If opening bracket → push to stack\n4.    If closing bracket → check if matches top of stack\n5. Return true if stack is empty",
        "explanation": "Python's dictionary mapping is much cleaner than Java's explicit comparisons. Python's 'not stack' truthiness check is elegant — an empty list is falsy. Java needs explicit isEmpty() calls. The stack-based algorithm is the same in both."
    },
    {
        "id": 19,
        "title": "Longest Substring Without Repeating",
        "difficulty": "Medium",
        "topic": "Strings",
        "python_solution": "def length_of_longest_substring(s):\n    char_index = {}\n    max_len = 0\n    left = 0\n    for right, char in enumerate(s):\n        if char in char_index and char_index[char] >= left:\n            left = char_index[char] + 1\n        char_index[char] = right\n        max_len = max(max_len, right - left + 1)\n    return max_len",
        "java_solution": "public int lengthOfLongestSubstring(String s) {\n    Map<Character, Integer> charIndex = new HashMap<>();\n    int maxLen = 0, left = 0;\n    for (int right = 0; right < s.length(); right++) {\n        char c = s.charAt(right);\n        if (charIndex.containsKey(c) && charIndex.get(c) >= left)\n            left = charIndex.get(c) + 1;\n        charIndex.put(c, right);\n        maxLen = Math.max(maxLen, right - left + 1);\n    }\n    return maxLen;\n}",
        "differences": [
            "Python enumerate() vs Java manual index",
            "Python 'char in dict' vs Java map.containsKey()",
            "Python max() vs Java Math.max()"
        ],
        "pseudocode": "1. Use sliding window with left and right pointers\n2. Track last seen index of each character\n3. If character repeated, move left pointer\n4. Update max length at each step",
        "explanation": "The sliding window technique is identical in both languages. Python's enumerate() gives both index and value cleanly. Java's Map requires containsKey() and get() separately. Python's dict membership check with 'in' is more readable."
    },
    {
        "id": 20,
        "title": "String to Integer (atoi)",
        "difficulty": "Medium",
        "topic": "Strings",
        "python_solution": "def my_atoi(s):\n    s = s.strip()\n    if not s:\n        return 0\n    sign = -1 if s[0] == '-' else 1\n    if s[0] in ('+', '-'):\n        s = s[1:]\n    result = 0\n    for char in s:\n        if not char.isdigit():\n            break\n        result = result * 10 + int(char)\n    return max(-2**31, min(sign * result, 2**31 - 1))",
        "java_solution": "public int myAtoi(String s) {\n    s = s.trim();\n    if (s.isEmpty()) return 0;\n    int sign = 1, i = 0;\n    if (s.charAt(0) == '-') { sign = -1; i++; }\n    else if (s.charAt(0) == '+') i++;\n    long result = 0;\n    while (i < s.length() && Character.isDigit(s.charAt(i))) {\n        result = result * 10 + (s.charAt(i++) - '0');\n        if (result * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;\n        if (result * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;\n    }\n    return (int)(result * sign);\n}",
        "differences": [
            "Python handles overflow with min/max, Java checks during loop",
            "Python int(char) converts char, Java uses char - '0'",
            "Python 2**31 vs Java Integer.MAX_VALUE"
        ],
        "pseudocode": "1. Strip whitespace\n2. Handle sign\n3. Convert digits one by one\n4. Handle overflow\n5. Return result with sign",
        "explanation": "Python handles integer overflow naturally — Python integers can be arbitrarily large. Java uses long to avoid overflow during computation then clamps to int range. The char-to-digit conversion differs: Python uses int(), Java subtracts '0' (ASCII trick)."
    },
]
