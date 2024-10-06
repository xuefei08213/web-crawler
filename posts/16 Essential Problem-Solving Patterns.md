
16 Essential Problem-Solving Patterns
=====================================

# 16 Essential Problem-Solving Patterns

# 16 个基本的问题解决模式
  
https://dev.to/saurabhkurve/16-essential-problem-solving-patterns-31p2?ref=dailydev  
![](https://media.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsc53zfv0jkweqssjp6uy.jpg)

Data Structures and Algorithms (DSA) are crucial for efficient problem-solving. Here are 16 key patterns, with use cases and examples, to help tackle real-world problems. This guide includes concise Java examples to demonstrate each pattern in action.

数据结构和算法（DSA）对于高效解决问题至关重要。这里有 16 种关键模式，包括用例和示例，可帮助解决实际问题。本指南包括简洁的 Java 示例，以演示每种模式的实际应用。  
### 1.Sliding Window Pattern  
### 滑动窗口模式

Used to track a subset of data that shifts over time, commonly in arrays or strings.

用于跟踪随时间推移而变化的数据集的一部分，通常在数组或字符串中。

- Use Case: Maximum sum of subarrays.
- 用例：子数组的最大和。
- Example: Maximum sum of subarray of size K.
- 给定一个大小为 n 的数组，和一个整数 k，找出数组中所有长度为 k 的连续子数组，并计算这些子数组的和，返回这些和的最大值。


```java
public int maxSubArraySum(int[] arr, int k) {
    int maxSum = 0, windowSum = 0;
    for (int i = 0; i < arr.length; i++) {
        windowSum += arr[i];
        if (i >= k - 1) {
            maxSum = Math.max(maxSum, windowSum);
            windowSum -= arr[i - (k - 1)];
        }
    }
    return maxSum;
}
```  
### 2.Two Pointer Pattern  
### 双指针模式

Two pointers work towards a solution by converging from different ends of an array.

两个指针从数组的两端向一个解决方案汇聚。

- Use Case: Find pairs in a sorted array.
- 用例：在排序数组中查找对。
- Example: Find two numbers that sum up to a target.
- 找出两个数，使它们的和等于目标数。


```java
public int[] twoSum(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return new int[]{left, right};
        else if (sum < target) left++;
        else right--;
    }
    return new int[]{};
}
```  
### 3.Fast & Slow Pointers Pattern  
### 快慢指针模式

Two pointers move at different speeds to detect cycles in sequences.

两个指针以不同的速度移动，以检测序列中的循环。

- Use Case: Detect cycles in linked lists.
- 用例：检测链表中的循环。
- Example: Check if a linked list has a cycle.
- 检查链表是否有环。


```java
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast!= null && fast.next!= null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```  
### 4.Merge Intervals Pattern  
### 4.合并区间模式

This pattern merges overlapping intervals.

这个模式会合并重叠的区间。

- Use Case: Scheduling meetings.
- 用例：安排会议。
- Example: Merge overlapping intervals.
- 合并重叠区间。


```java
public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    List<int[]> merged = new ArrayList<>();
    for (int[] interval : intervals) {
        if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) {
            merged.add(interval);
        } else {
            merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], interval[1]);
        }
    }
    return merged.toArray(new int[merged.size()][]);
}
```  
### 5.Cyclic Sort Pattern  
### 循环排序模式

Sort numbers when elements fall within a range.

当元素落在某个范围内时，对数字进行排序。

- Use Case: Finding missing numbers.
- 用例：查找丢失的数字。
- Example: Find the missing number from 1 to N.
- 从 1 到 N 中找出缺失的数字。


```java
public int findMissingNumber(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        if (nums[i]!= i && nums[i] < nums.length) {
            int temp = nums[nums[i]];
            nums[nums[i]] = nums[i];
            nums[i] = temp;
        } else {
            i++;
        }
    }
    for (i = 0; i < nums.length; i++) {
        if (nums[i]!= i) return i;
    }
    return nums.length;
}
```  
### 6.In-Place Reversal of Linked List Pattern  
### 链表反转模式

Reverse a linked list in-place.

原地反转链表。

- Use Case: Reversing a sublist of a linked list.
- 用例：反转链表的子列表。
- Example: Reverse a linked list.
- 反转链表。


```javascript
public ListNode reverseList(ListNode head) {
    ListNode prev = null, current = head;
    while (current!= null) {
        ListNode next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
```  
### 7.Tree Breadth-First Search (BFS) Pattern  
### 7. 树的广度优先搜索（BFS）模式

Explore nodes level by level in a tree.

在树中逐层探索节点。

- Use Case: Level-order traversal.
- 用例：层次遍历。
- Example: Traverse a binary tree level by level.
- 按层遍历二叉树。


```javascript
public List<List<Integer>> bfs(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<>();
    if (root!= null) queue.add(root);
    while (!queue.isEmpty()) {
        int levelSize = queue.size();
        List<Integer> currentLevel = new ArrayList<>();
        for (int i = 0; i < levelSize; i++) {
            TreeNode node = queue.poll();
            currentLevel.add(node.val);
            if (node.left!= null) queue.add(node.left);
            if (node.right!= null) queue.add(node.right);
        }
        result.add(currentLevel);
    }
    return result;
}
```  
### 8.Depth-First Search (DFS) Pattern  
### 深度优先搜索（DFS）模式

Explore as deep as possible along a branch before backtracking.

在回溯之前尽可能深入地沿着一个分支进行探索。

- Use Case: Searching in trees or graphs.
- 用例：在树或图中进行搜索。
- Example: Finding all root-to-leaf paths.
- 寻找所有从根到叶的路径。


```java
public void dfs(TreeNode node, List<Integer> path, List<List<Integer>> result) {
    if (node == null) return;
    path.add(node.val);
    if (node.left == null && node.right == null) result.add(new ArrayList<>(path));
    dfs(node.left, path, result);
    dfs(node.right, path, result);
    path.remove(path.size() - 1);
}
```  
### 9.Two Heap Pattern  
### 两个堆模式

Use two heaps to maintain dynamic datasets.

使用两个堆来维护动态数据集。

- Use Case: Finding the median in a data stream.
- 用例：在数据流中查找中位数。
- Example: Find the median of a stream of numbers.
- 示例：找到数据流中的中位数。


```java
class MedianFinder {
    private PriorityQueue<Integer> low = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> high = new PriorityQueue<>();

    public void addNum(int num) {
        low.offer(num);
        high.offer(low.poll());
        if (low.size() < high.size()) low.offer(high.poll());
    }

    public double findMedian() {
        return low.size() > high.size()? low.peek() : (low.peek() + high.peek()) / 2.0;
    }
}
```  
### 10.Subsets Pattern  
### 子集模式

Generate all possible subsets.

生成所有可能的子集。

- Use Case: Combination and permutation problems.
- 用例：组合和排列问题。
- Example: Find all subsets of a set.
- 示例：找出一个集合的所有子集。


```java
public class Main {
    public static void main(String[] args) {
        int[] nums = {1,2,3};
        List<List<Integer>> subsets = subsets(nums);
        for (List<Integer> subset : subsets) {
            for (Integer num : subset) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }

    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for (int num : nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                List<Integer> subset = result.get(i);
                subset.add(num);
                result.add(subset);
            }
        }
        return result;
    }
}
```  
### 11.Modified Binary Search Pattern  
### 二进制搜索模式的修改

Search in a rotated or partially sorted array.

在旋转或部分排序的数组中搜索。

- Use Case: Finding an element in rotated arrays.
- 用例：在旋转数组中查找元素。
- Example: Search for a target in a rotated sorted array.
- 在旋转排序数组中搜索目标。


```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[left] <= nums[mid]) {
            if (target >= nums[left] && target < nums[mid]) right = mid - 1;
            else left = mid + 1;
        } else {
            if (target > nums[mid] && target <= nums[right]) left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
}
```  
### 12.Bitwise XOR Pattern  
### 12. 位异或模式

Solve problems involving pairs using XOR.

使用异或解决涉及对的问题。

- Use Case: Finding unique numbers.
- 用例：寻找唯一数字。
- Example: Find the single number in an array.
- 在数组中找到唯一数字。


```java
public int singleNumber(int[] nums) {
    int result = 0;
    for (int num : nums) result ^= num;
    return result;
}
```  
### 13.Top 'K' Elements Pattern  
### 13. 前 K 个元素模式

Use heaps to find the top K elements in a dataset.

使用堆来在数据集找到前 K 个元素。

- Use Case: Finding top K frequent elements.
- 用例：找到前 K 个最频繁的元素。
- Example: Find the K most frequent numbers.
- 找出最频繁的 K 个数字。


```java
public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 2, 2, 2, 3, 3, 3, 3};
        int k = 2;
        List<Integer> topKFrequent = topKFrequent(nums, k);
        System.out.println(topKFrequent);
    }

    public static List<Integer> topKFrequent(int[] nums, int k) {
        // 存储每个数字出现的次数
        Map<Integer, Integer> countMap = new HashMap<>();
        // 存储每个数字及其出现的次数
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // 存储每个数字及其出现的次数，并按照出现的次数进行排序
        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
                (e1, e2) -> e2.getValue() - e1.getValue());
        // 遍历 countMap，将每个数字及其出现的次数添加到 heap 中
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            heap.offer(entry);
            // 如果 heap 的大小大于 k，则弹出堆顶元素
            if (heap.size() > k) {
                heap.poll();
            }
        }

        // 将 heap 中的元素转换为列表并返回
        return heap.stream()
                // 将 Map.Entry 转换为键
               .map(Map.Entry::getKey)
               .collect(Collectors.toList());
    }
}
```

- Use Case: Merging K sorted lists.
- 用例：合并 K 个已排序的列表。
- Example: Merge K sorted linked lists.
- 合并 K 个已排序的链表。


```java
public ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a.val));
    ListNode dummy = new ListNode(0), tail = dummy;
    for (ListNode list : lists) if (list!= null) heap.offer(list);
    while (!heap.isEmpty()) {
        tail.next = heap.poll();
        tail = tail.next;
        if (tail.next!= null) heap.offer(tail.next);
    }
    return dummy.next;
}
```  
### 15.0/1 Knapsack Dynamic Programming Pattern  
### 15.0/1 背包动态规划模式

Optimize selection under constraints.

在约束条件下优化选择。

- Use Case: Resource allocation.
- 用例：资源分配。
- Example: Solve the 0/1 knapsack problem.
- 解决 0/1 背包问题。


```java
public int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    return dp[n][capacity];
}
```  
### 16.Topological Sort Graph Pattern  
### 拓扑排序图模式

Find a valid task order in Directed Acyclic Graphs (DAG).

在有向无环图（DAG）中找到有效的任务订单。

- Use Case: Course scheduling.
- 用例：课程安排。
- Example: Find the correct order of courses.
- 找出正确的课程顺序。


以下是提取的代码：
```java
public int[] findOrder(int numCourses, int[][] prerequisites) {
    List<Integer>[] graph = new ArrayList[numCourses];
    int[] inDegree = new int[numCourses];
    for (int i = 0; i < numCourses; i++) {
        graph[i] = new ArrayList<>();
    }
    for (int[] pre : prerequisites) {
        graph[pre[1]].add(pre[0]);
        inDegree[pre[0]]++;
    }
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) {
            queue.add(i);
        }
    }
    int[] result = new int[numCourses];
    int idx = 0;
    while (!queue.isEmpty()) {
        int course = queue.poll();
        result[idx++] = course;
        for (int next : graph[course]) {
            inDegree[next]--;
            if (inDegree[next] == 0) {
                queue.add(next);
            }
        }
    }
    return idx == numCourses? result : new int[0];
}
```

These 16 problem-solving patterns are crucial for mastering DSA. Each pattern can be applied to a wide range of real-world problems, providing an efficient path to optimal solutions.

这些 16 种解题模式对于掌握 DSA 至关重要。每种模式都可以应用于广泛的实际问题，提供了一条通往最佳解决方案的高效路径。