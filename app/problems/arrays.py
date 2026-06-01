arrays = [
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
            "Python returns a list, Java returns int[]"
        ],
        "pseudocode": "1. Create empty map\n2. For each number in array:\n3.    Calculate difference = target - current number\n4.    If difference exists in map → return both indexes\n5.    Otherwise store current number and index in map",
        "explanation": "Python uses a dictionary to store numbers it has seen. Java uses a HashMap which works the same way but requires explicit type declarations. Both check if the difference exists before storing — the core logic is identical, only the syntax differs."
    },
    {
        "id": 2,
        "title": "Find Max in Array",
        "difficulty": "Easy",
        "topic": "Arrays",
        "python_solution": "def find_max(nums):\n    max_val = nums[0]\n    for num in nums:\n        if num > max_val:\n            max_val = num\n    return max_val",
        "java_solution": "public int findMax(int[] nums) {\n    int maxVal = nums[0];\n    for (int num : nums) {\n        if (num > maxVal) {\n            maxVal = num;\n        }\n    }\n    return maxVal;\n}",
        "differences": [
            "Python uses plain variable, Java needs int type declaration",
            "Python for num in nums vs Java enhanced for loop",
            "Python is fewer lines — same logic, less syntax"
        ],
        "pseudocode": "1. Set max to first element\n2. Loop through every number\n3. If current number > max → update max\n4. Return max after loop ends",
        "explanation": "The logic is the same in both. The difference is Java requires explicit type declarations. Python figures out the type automatically. Java's enhanced for loop is equivalent to Python's for-in loop."
    },
    {
        "id": 3,
        "title": "Binary Search",
        "difficulty": "Medium",
        "topic": "Arrays",
        "python_solution": "def binary_search(nums, target):\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
        "java_solution": "public int binarySearch(int[] nums, int target) {\n    int left = 0, right = nums.length - 1;\n    while (left <= right) {\n        int mid = (left + right) / 2;\n        if (nums[mid] == target) return mid;\n        else if (nums[mid] < target) left = mid + 1;\n        else right = mid - 1;\n    }\n    return -1;\n}",
        "differences": [
            "Python uses // for integer division, Java uses /",
            "Python len(nums) vs Java nums.length",
            "Python unpacks two variables in one line"
        ],
        "pseudocode": "1. Set left = 0, right = last index\n2. While left <= right:\n3.    Find middle index\n4.    If middle == target → return index\n5.    If middle < target → search right half\n6.    If middle > target → search left half\n7. Return -1 if not found",
        "explanation": "Binary search cuts the search space in half each time. The key difference is integer division — Python uses // to force whole numbers, Java's / already does integer division for integers."
    },
    {
        "id": 4,
        "title": "Rotate Array",
        "difficulty": "Medium",
        "topic": "Arrays",
        "python_solution": "def rotate(nums, k):\n    k = k % len(nums)\n    nums[:] = nums[-k:] + nums[:-k]",
        "java_solution": "public void rotate(int[] nums, int k) {\n    k = k % nums.length;\n    reverse(nums, 0, nums.length - 1);\n    reverse(nums, 0, k - 1);\n    reverse(nums, k, nums.length - 1);\n}\nprivate void reverse(int[] nums, int l, int r) {\n    while (l < r) {\n        int temp = nums[l];\n        nums[l++] = nums[r];\n        nums[r--] = temp;\n    }\n}",
        "differences": [
            "Python uses slicing to rotate in one line",
            "Java needs a helper reverse() method",
            "Python modifies list in place with nums[:]"
        ],
        "pseudocode": "1. Normalize k = k % length\n2. Reverse entire array\n3. Reverse first k elements\n4. Reverse remaining elements",
        "explanation": "Python's slicing makes array rotation elegant — one line does it all. Java lacks slicing so uses the classic three-reverse algorithm. Both are O(n) time but Java requires significantly more code."
    },
    {
        "id": 5,
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "topic": "Arrays",
        "python_solution": "def contains_duplicate(nums):\n    return len(nums) != len(set(nums))",
        "java_solution": "public boolean containsDuplicate(int[] nums) {\n    Set<Integer> seen = new HashSet<>();\n    for (int num : nums) {\n        if (!seen.add(num)) return true;\n    }\n    return false;\n}",
        "differences": [
            "Python converts to set in one line, Java builds a HashSet manually",
            "Python uses len() comparison, Java uses Set.add() return value",
            "Python solution is one line, Java needs a loop"
        ],
        "pseudocode": "1. Create empty set\n2. For each number:\n3.    If number already in set → return true\n4.    Add number to set\n5. Return false",
        "explanation": "Python's set conversion is one of its most powerful features — converting a list to a set removes duplicates, so if the lengths differ, there were duplicates. Java's HashSet.add() returns false if the element already exists, which is used as the duplicate check."
    },
    {
        "id": 6,
        "title": "Move Zeroes",
        "difficulty": "Easy",
        "topic": "Arrays",
        "python_solution": "def move_zeroes(nums):\n    pos = 0\n    for num in nums:\n        if num != 0:\n            nums[pos] = num\n            pos += 1\n    while pos < len(nums):\n        nums[pos] = 0\n        pos += 1",
        "java_solution": "public void moveZeroes(int[] nums) {\n    int pos = 0;\n    for (int num : nums) {\n        if (num != 0) nums[pos++] = num;\n    }\n    while (pos < nums.length) nums[pos++] = 0;\n}",
        "differences": [
            "Python pos += 1 vs Java pos++ (post-increment)",
            "Python len(nums) vs Java nums.length",
            "Logic is identical, syntax differences only"
        ],
        "pseudocode": "1. Track position pointer at 0\n2. Copy all non-zero elements forward\n3. Fill remaining positions with zeros",
        "explanation": "This is a classic two-pointer pattern. Both languages implement it identically in logic. The main difference is Java's post-increment operator ++ which Python doesn't have — Python uses += 1 instead."
    },
    {
        "id": 7,
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "topic": "Arrays",
        "python_solution": "def product_except_self(nums):\n    n = len(nums)\n    result = [1] * n\n    left = 1\n    for i in range(n):\n        result[i] = left\n        left *= nums[i]\n    right = 1\n    for i in range(n - 1, -1, -1):\n        result[i] *= right\n        right *= nums[i]\n    return result",
        "java_solution": "public int[] productExceptSelf(int[] nums) {\n    int n = nums.length;\n    int[] result = new int[n];\n    Arrays.fill(result, 1);\n    int left = 1;\n    for (int i = 0; i < n; i++) {\n        result[i] = left;\n        left *= nums[i];\n    }\n    int right = 1;\n    for (int i = n - 1; i >= 0; i--) {\n        result[i] *= right;\n        right *= nums[i];\n    }\n    return result;\n}",
        "differences": [
            "Python [1] * n creates array, Java needs Arrays.fill()",
            "Python range(n-1, -1, -1) for reverse, Java uses i--",
            "Java needs explicit array size: new int[n]"
        ],
        "pseudocode": "1. Create result array of 1s\n2. Left pass: multiply all elements to the left\n3. Right pass: multiply all elements to the right\n4. Return result",
        "explanation": "This elegant O(n) solution uses two passes. Python's list multiplication [1]*n is a concise way to create an array of ones. Java needs Arrays.fill() for the same effect. The algorithm itself is identical."
    },
    {
        "id": 8,
        "title": "Maximum Subarray",
        "difficulty": "Medium",
        "topic": "Arrays",
        "python_solution": "def max_subarray(nums):\n    max_sum = nums[0]\n    current = nums[0]\n    for num in nums[1:]:\n        current = max(num, current + num)\n        max_sum = max(max_sum, current)\n    return max_sum",
        "java_solution": "public int maxSubArray(int[] nums) {\n    int maxSum = nums[0], current = nums[0];\n    for (int i = 1; i < nums.length; i++) {\n        current = Math.max(nums[i], current + nums[i]);\n        maxSum = Math.max(maxSum, current);\n    }\n    return maxSum;\n}",
        "differences": [
            "Python built-in max() vs Java Math.max()",
            "Python slicing nums[1:] vs Java index starting at 1",
            "Python unpacks multiple assignments on one line"
        ],
        "pseudocode": "1. Set max and current to first element\n2. For each remaining number:\n3.    current = max(number, current + number)\n4.    max_sum = max(max_sum, current)\n5. Return max_sum",
        "explanation": "Kadane's algorithm is identical in both languages. Python's built-in max() is cleaner than Java's Math.max() but does the same thing. Python's ability to slice with nums[1:] avoids index management that Java requires."
    },
    {
        "id": 9,
        "title": "Single Number",
        "difficulty": "Easy",
        "topic": "Arrays",
        "python_solution": "def single_number(nums):\n    result = 0\n    for num in nums:\n        result ^= num\n    return result",
        "java_solution": "public int singleNumber(int[] nums) {\n    int result = 0;\n    for (int num : nums) {\n        result ^= num;\n    }\n    return result;\n}",
        "differences": [
            "Logic is almost identical — XOR works the same in both",
            "Python for num in nums vs Java for (int num : nums)",
            "Java requires int type declaration"
        ],
        "pseudocode": "1. Initialize result = 0\n2. XOR every number with result\n3. Duplicate numbers cancel out\n4. Return result",
        "explanation": "XOR is one of the rare cases where Python and Java look almost identical. XOR of a number with itself is 0, so duplicates cancel out leaving only the unique number. The only difference is Java's type declaration requirement."
    },
    {
        "id": 10,
        "title": "3Sum",
        "difficulty": "Medium",
        "topic": "Arrays",
        "python_solution": "def three_sum(nums):\n    nums.sort()\n    result = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i-1]:\n            continue\n        left, right = i + 1, len(nums) - 1\n        while left < right:\n            s = nums[i] + nums[left] + nums[right]\n            if s == 0:\n                result.append([nums[i], nums[left], nums[right]])\n                while left < right and nums[left] == nums[left+1]: left += 1\n                while left < right and nums[right] == nums[right-1]: right -= 1\n                left += 1; right -= 1\n            elif s < 0: left += 1\n            else: right -= 1\n    return result",
        "java_solution": "public List<List<Integer>> threeSum(int[] nums) {\n    Arrays.sort(nums);\n    List<List<Integer>> result = new ArrayList<>();\n    for (int i = 0; i < nums.length - 2; i++) {\n        if (i > 0 && nums[i] == nums[i-1]) continue;\n        int left = i + 1, right = nums.length - 1;\n        while (left < right) {\n            int s = nums[i] + nums[left] + nums[right];\n            if (s == 0) {\n                result.add(Arrays.asList(nums[i], nums[left], nums[right]));\n                while (left < right && nums[left] == nums[left+1]) left++;\n                while (left < right && nums[right] == nums[right-1]) right--;\n                left++; right--;\n            } else if (s < 0) left++;\n            else right--;\n        }\n    }\n    return result;\n}",
        "differences": [
            "Python list vs Java List<List<Integer>>",
            "Python result.append([]) vs Java result.add(Arrays.asList())",
            "Java requires explicit generic types everywhere"
        ],
        "pseudocode": "1. Sort the array\n2. For each element as first number:\n3.    Use two pointers for remaining two numbers\n4.    If sum == 0 → add to result, skip duplicates\n5.    If sum < 0 → move left pointer right\n6.    If sum > 0 → move right pointer left",
        "explanation": "The two-pointer technique after sorting is identical in both languages. The biggest difference is Java's verbose generic type system — List<List<Integer>> vs Python's simple list. Java also needs Arrays.asList() to create a list from values inline."
    },
]
