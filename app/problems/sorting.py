sorting = [
    {
        "id": 41,
        "title": "Bubble Sort",
        "difficulty": "Easy",
        "topic": "Sorting",
        "python_solution": "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr",
        "java_solution": "public int[] bubbleSort(int[] arr) {\n    int n = arr.length;\n    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < n-i-1; j++) {\n            if (arr[j] > arr[j+1]) {\n                int temp = arr[j];\n                arr[j] = arr[j+1];\n                arr[j+1] = temp;\n            }\n        }\n    }\n    return arr;\n}",
        "differences": [
            "Python swaps in one line: arr[j], arr[j+1] = arr[j+1], arr[j]",
            "Java needs temp variable for swap",
            "Python len(arr) vs Java arr.length"
        ],
        "pseudocode": "1. For each pass i:\n2.    Compare adjacent elements\n3.    If out of order → swap\n4.    Largest bubbles to end each pass",
        "explanation": "The classic simultaneous swap in Python (a, b = b, a) eliminates the need for a temp variable. Java always needs a temp for swaps. This is one of the most visible Python advantages in sorting algorithms."
    },
    {
        "id": 42,
        "title": "Selection Sort",
        "difficulty": "Easy",
        "topic": "Sorting",
        "python_solution": "def selection_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        min_idx = i\n        for j in range(i+1, n):\n            if arr[j] < arr[min_idx]:\n                min_idx = j\n        arr[i], arr[min_idx] = arr[min_idx], arr[i]\n    return arr",
        "java_solution": "public int[] selectionSort(int[] arr) {\n    int n = arr.length;\n    for (int i = 0; i < n; i++) {\n        int minIdx = i;\n        for (int j = i+1; j < n; j++) {\n            if (arr[j] < arr[minIdx]) minIdx = j;\n        }\n        int temp = arr[i];\n        arr[i] = arr[minIdx];\n        arr[minIdx] = temp;\n    }\n    return arr;\n}",
        "differences": [
            "Python simultaneous swap vs Java temp variable",
            "Python uses snake_case, Java uses camelCase",
            "Logic is identical"
        ],
        "pseudocode": "1. For each position i:\n2.    Find minimum in remaining array\n3.    Swap minimum with position i\n4. Array is sorted",
        "explanation": "Selection sort finds the minimum and swaps it into place. Python's simultaneous swap makes the exchange clean. Java's camelCase (minIdx) vs Python's snake_case (min_idx) is a naming convention difference — both are valid in their respective languages."
    },
    {
        "id": 43,
        "title": "Insertion Sort",
        "difficulty": "Easy",
        "topic": "Sorting",
        "python_solution": "def insertion_sort(arr):\n    for i in range(1, len(arr)):\n        key = arr[i]\n        j = i - 1\n        while j >= 0 and arr[j] > key:\n            arr[j+1] = arr[j]\n            j -= 1\n        arr[j+1] = key\n    return arr",
        "java_solution": "public int[] insertionSort(int[] arr) {\n    for (int i = 1; i < arr.length; i++) {\n        int key = arr[i];\n        int j = i - 1;\n        while (j >= 0 && arr[j] > key) {\n            arr[j+1] = arr[j];\n            j--;\n        }\n        arr[j+1] = key;\n    }\n    return arr;\n}",
        "differences": [
            "Python j -= 1 vs Java j--",
            "Python range(1, len(arr)) vs Java i = 1; i < arr.length",
            "Logic is nearly identical"
        ],
        "pseudocode": "1. For each element from index 1:\n2.    Save element as key\n3.    Shift larger elements right\n4.    Insert key in correct position",
        "explanation": "Insertion sort is one of the most similar-looking algorithms in Python and Java. The main difference is j-- vs j -= 1 and the loop structure. The logic is virtually identical, making it a great starting point for understanding both languages."
    },
    {
        "id": 44,
        "title": "Merge Sort",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    return merge(left, right)\n\ndef merge(left, right):\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result",
        "java_solution": "public int[] mergeSort(int[] arr) {\n    if (arr.length <= 1) return arr;\n    int mid = arr.length / 2;\n    int[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid));\n    int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));\n    return merge(left, right);\n}\nprivate int[] merge(int[] left, int[] right) {\n    int[] result = new int[left.length + right.length];\n    int i = 0, j = 0, k = 0;\n    while (i < left.length && j < right.length)\n        result[k++] = left[i] <= right[j] ? left[i++] : right[j++];\n    while (i < left.length) result[k++] = left[i++];\n    while (j < right.length) result[k++] = right[j++];\n    return result;\n}",
        "differences": [
            "Python slicing arr[:mid] vs Java Arrays.copyOfRange()",
            "Python result.extend(left[i:]) vs Java while loop",
            "Java pre-allocates result array, Python builds dynamically"
        ],
        "pseudocode": "1. If array has 1 element → return\n2. Split in half recursively\n3. Merge two sorted halves:\n4.    Compare elements, take smaller\n5.    Append remaining elements",
        "explanation": "Python's slicing makes splitting arrays trivial. Java needs Arrays.copyOfRange() for the same effect. Python's extend() with a slice elegantly handles the leftover elements. Java needs explicit while loops for the same. Both are O(n log n)."
    },
    {
        "id": 45,
        "title": "Quick Sort",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)",
        "java_solution": "public void quickSort(int[] arr, int low, int high) {\n    if (low < high) {\n        int pivot = partition(arr, low, high);\n        quickSort(arr, low, pivot - 1);\n        quickSort(arr, pivot + 1, high);\n    }\n}\nprivate int partition(int[] arr, int low, int high) {\n    int pivot = arr[high];\n    int i = low - 1;\n    for (int j = low; j < high; j++) {\n        if (arr[j] <= pivot) {\n            i++;\n            int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;\n        }\n    }\n    int temp = arr[i+1]; arr[i+1] = arr[high]; arr[high] = temp;\n    return i + 1;\n}",
        "differences": [
            "Python uses list comprehensions for clean partition",
            "Java uses in-place partition for memory efficiency",
            "Python version creates new lists, Java modifies in place"
        ],
        "pseudocode": "1. Choose pivot\n2. Partition: smaller left, equal middle, larger right\n3. Recursively sort left and right\n4. Combine results",
        "explanation": "Python's functional approach with list comprehensions is elegant but uses extra memory. Java's in-place partition is more memory efficient. Python's list concatenation with + makes the recursive combination clean. Java requires explicit index tracking."
    },
    {
        "id": 46,
        "title": "Sort Colors (Dutch Flag)",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def sort_colors(nums):\n    low, mid, high = 0, 0, len(nums) - 1\n    while mid <= high:\n        if nums[mid] == 0:\n            nums[low], nums[mid] = nums[mid], nums[low]\n            low += 1\n            mid += 1\n        elif nums[mid] == 1:\n            mid += 1\n        else:\n            nums[mid], nums[high] = nums[high], nums[mid]\n            high -= 1",
        "java_solution": "public void sortColors(int[] nums) {\n    int low = 0, mid = 0, high = nums.length - 1;\n    while (mid <= high) {\n        if (nums[mid] == 0) {\n            int temp = nums[low]; nums[low] = nums[mid]; nums[mid] = temp;\n            low++; mid++;\n        } else if (nums[mid] == 1) {\n            mid++;\n        } else {\n            int temp = nums[mid]; nums[mid] = nums[high]; nums[high] = temp;\n            high--;\n        }\n    }\n}",
        "differences": [
            "Python simultaneous swap vs Java temp variable",
            "Python low, mid, high = 0, 0, len-1 (one line) vs Java three declarations",
            "Logic is identical — Dutch National Flag algorithm"
        ],
        "pseudocode": "1. Three pointers: low, mid, high\n2. While mid <= high:\n3.    If 0 → swap with low, advance both\n4.    If 1 → advance mid\n5.    If 2 → swap with high, retreat high",
        "explanation": "The Dutch National Flag algorithm. Python's simultaneous multi-variable assignment (low, mid, high = 0, 0, len-1) initializes three variables in one line. Java needs three separate declarations. The swap difference is the same as always — Python's is cleaner."
    },
    {
        "id": 47,
        "title": "Kth Largest Element",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def find_kth_largest(nums, k):\n    nums.sort(reverse=True)\n    return nums[k-1]",
        "java_solution": "public int findKthLargest(int[] nums, int k) {\n    Arrays.sort(nums);\n    return nums[nums.length - k];\n}",
        "differences": [
            "Python sort(reverse=True) sorts descending, Java sorts ascending",
            "Python nums[k-1] from front, Java nums[length-k] from back",
            "Python built-in sort vs Java Arrays.sort()"
        ],
        "pseudocode": "1. Sort the array\n2. Return the kth element from the end",
        "explanation": "Python's sort() has a reverse parameter for descending order. Java's Arrays.sort() only sorts ascending, so you index from the back. Both are valid O(n log n) approaches. Python's named parameter (reverse=True) is more readable than Java's index arithmetic."
    },
    {
        "id": 48,
        "title": "Meeting Rooms",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def can_attend_meetings(intervals):\n    intervals.sort(key=lambda x: x[0])\n    for i in range(1, len(intervals)):\n        if intervals[i][0] < intervals[i-1][1]:\n            return False\n    return True",
        "java_solution": "public boolean canAttendMeetings(int[][] intervals) {\n    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\n    for (int i = 1; i < intervals.length; i++) {\n        if (intervals[i][0] < intervals[i-1][1]) return false;\n    }\n    return true;\n}",
        "differences": [
            "Python lambda: lambda x: x[0] vs Java lambda: (a, b) -> a[0] - b[0]",
            "Python key= parameter vs Java Comparator pattern",
            "Both use lambda but syntax differs significantly"
        ],
        "pseudocode": "1. Sort intervals by start time\n2. For each interval:\n3.    If it starts before previous ends → overlap\n4. Return true if no overlaps",
        "explanation": "Lambda functions exist in both languages but look very different. Python's key= parameter with a single-value lambda is clean. Java uses a comparator lambda with two parameters that returns the comparison result. Both sort by the first element of each interval."
    },
    {
        "id": 49,
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def merge_intervals(intervals):\n    intervals.sort(key=lambda x: x[0])\n    merged = [intervals[0]]\n    for interval in intervals[1:]:\n        if interval[0] <= merged[-1][1]:\n            merged[-1][1] = max(merged[-1][1], interval[1])\n        else:\n            merged.append(interval)\n    return merged",
        "java_solution": "public int[][] merge(int[][] intervals) {\n    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\n    List<int[]> merged = new ArrayList<>();\n    merged.add(intervals[0]);\n    for (int i = 1; i < intervals.length; i++) {\n        int[] last = merged.get(merged.size() - 1);\n        if (intervals[i][0] <= last[1])\n            last[1] = Math.max(last[1], intervals[i][1]);\n        else\n            merged.add(intervals[i]);\n    }\n    return merged.toArray(new int[0][]);\n}",
        "differences": [
            "Python merged[-1] accesses last element, Java needs get(size-1)",
            "Java needs toArray() conversion at end, Python returns list directly",
            "Python max() vs Java Math.max()"
        ],
        "pseudocode": "1. Sort by start time\n2. Add first interval to result\n3. For each interval:\n4.    If overlaps with last → extend last\n5.    Otherwise → add new interval",
        "explanation": "Python's negative indexing (merged[-1]) to access the last element is cleaner than Java's get(size-1). Java's List needs toArray() conversion to return an array. Python's max() works the same as Java's Math.max() — just without the Math. prefix."
    },
    {
        "id": 50,
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "topic": "Sorting",
        "python_solution": "def top_k_frequent(nums, k):\n    count = {}\n    for num in nums:\n        count[num] = count.get(num, 0) + 1\n    return sorted(count, key=count.get, reverse=True)[:k]",
        "java_solution": "public int[] topKFrequent(int[] nums, int k) {\n    Map<Integer, Integer> count = new HashMap<>();\n    for (int num : nums)\n        count.put(num, count.getOrDefault(num, 0) + 1);\n    return count.entrySet().stream()\n        .sorted((a, b) -> b.getValue() - a.getValue())\n        .limit(k)\n        .mapToInt(Map.Entry::getKey)\n        .toArray();\n}",
        "differences": [
            "Python sorted with key=count.get vs Java Stream API",
            "Java uses Stream for functional pipeline, Python uses sorted()",
            "Java Stream is powerful but verbose compared to Python"
        ],
        "pseudocode": "1. Count frequency of each number\n2. Sort by frequency descending\n3. Return top k elements",
        "explanation": "Python's sorted() with key=count.get is remarkably clean — it uses the count dict's get method as the sort key. Java's Stream API is powerful but verbose. This is one of the cases where Python's functional tools are more concise than Java's newer Stream features."
    },
]
