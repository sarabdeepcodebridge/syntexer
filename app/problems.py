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

    }
]
