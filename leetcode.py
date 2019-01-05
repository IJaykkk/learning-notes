"""
精華整理：

- 求所有解，先暴力上 Backtracking
- 問最短/最少，先想 BFS, DP 這對基友
- 問環相關/重複訪問，DFS + visited state
- 問連通性，靜態靠 BFS/DFS，動態靠 Union Find
- 問依賴性，想想 Topological Sort 和 indegree
- DAG 萬能套路 DFS + memo，再到 DP
- DAG all pairs of points 最短路徑 Floyd-Warshall，single source of points 最短路徑 Dijkstra
- 建圖時想想 vertex, edges, cost 分別是什麼？
- 樹相關永遠有 bracktracking 和 pure recursion 兩條路
- 遇到字串/字典/char board相關，Trie 可以試試
- Range 求最大/最小/sum等特徵值，Segment Tree會是不錯選擇
- Matrix 和 Array，通常都是：
    1. Two Pointers
    2. Sliding Windows(fixed or not fixed)
    3. DP
- DP 題型往往是：
    1. 問你可不可以、數量有多少
    2. 兩個 strings match 來 match 去
    3. 1D/2D array 相關
    4. 博弈遊戲
- Reversed Idea 非常重要：
    1. 最長的相反就是最短
    2. 最多的相反就是最少
    3. obstacle 的相反就是 reachable
    4. subarray 相反就是剩下元素
    5. left 相反就是 right
- Lookup 別忘了 Hash，Hash + DLL 是常用的 hybrid 結構
- 找規律時別忘了旁門左道：monotone stack, deque
- 排序大法總可以 try try
- Time Complexity：
    1. backtracking 先想想 branching factor, height
    2. DFS + memo or DP，想想 state 數量和每個 state 的 cost
    3. tree 相關總是要想 balanced 和 singly linked list
    4. array/matrix，思考你有幾層 loops
    5. binary search 別忘了 checking function 開銷
    6. stack/queue/stack，吃進去一次吐出來一次
    7. Python/Java String 是 immutable，別亂 concatenate
- 不同 Solutions Trade-off：
    1. Time/Space Complexity
    2. Online/Offline 算法
    3. Pre-computation cost
    4. 不同 APIs call frequency 差別
    5. Extension：是否適合用於 generic parameters / streaming input
    6. Threaded-safe
"""

#####################################################
#                  SEQUENCE OPERATION               #
#####################################################

# str
s = "hey"
s.upper()
s.lower()
s.replace("hey", "yo")
s.find("hey") # return index or -1
"substring" in s # return True or False
s.isalpha()
s.isdigit()
s.split(',')
",".join(["123", "456"])
ord('a') == 97
chr(97) == 'a'
list(map(chr, range(ord('a'), ord('z')+1))) # a - z
s.strip("pattern") # remove leading or trailing substring

# list
l = []
l.append(0) # equals to l[len(l):] = [0]
l.pop() # remove last element
l.pop(0) # remove first element
l.insert(i, x) # O(N)
l.extend([1,2,3])
l.sort() # in-place
l.sort(reverse=True)
l.sort(key=lambda x: x[1])
l.sort(key=lambda x: (-x[1], x[0])) # sort by multiple attributes
sorted(l, key=lambda x: x) # return a new list
l.index("element") # return first index or raise Error
l.revsere()
list(reversed(l)) # reversed function turns list into an iterable. Thus, need to add list

#####################################################
#                 PRACTICAL LIBRARY                 #
#####################################################

# regex
import re
re.findall('\w+', 'app, book. code') # ['app', 'book', 'code']
re.search('\d{3,5}', '1234d(3333)').group(0) # 1234
# \d == [0-9]
# \w == [a-zA-Z0-9_]
# \W == [^a-zA-Z0-9_]

# bisect
import bisect
l = [1,3,3,6,8,12,15]
x = 3
# If not found, locate the insertion point for x in l to maintain sorted order.
# If found, return the insertion point before any existing entries.
bisect.bisect_left(l, x) # return 1
# If not found, locate the insertion point for x in l to maintain sorted order.
# If found, return the insertion point after any existing entries.
bisect.bisect_right(l, x) # return 3
bisect.insort_left(l, x)
bisect.insort_right(l, x)

# random
import random
random.randint(0, 10) # including 0 and 10

#####################################################
#          Python BUILT-IN DATA STRUCTURE           #
#####################################################

# list
l = [1,2,3,4,5,6]
t = [7,8,9]
3 in l
s + t == [1,2,3,4,5,6,7,8,9] # return a new list
t * 3 == [7,8,9,7,8,9,7,8,9]
len(l) # 6
max(l) # 6
min(l) # 1
l.count(1) # 1
l.index(1) # 0

# dict
hash = {'a': 1}
key in hash
hash[key] # raise KeyError if not found
hash.get(key) # return value or None
hash.get(key, 20) # return 20 if not found
hash.setdefault(key, 20) # return 20 if not found
hash.items()
hash.keys()
hash.values()
hash.values()
hash.popitem() # return a tuple

from collections import defaultdict
hash = defaultdict(int) # default value is 0

# set
s = set()
t = set()
s.add(1)
s.remove(1) # raise KeyError if not found
s.discard(1) # safer way
s | t # union
s & t # intersection
s ^ t # symmetric difference, either in s or t but not both

# stack
stack = [1,2]
stack.append(3)
stack.pop()
stack[-1] # the last element

# queue
from collections import deque
queue = deque([4])
queue.append(3)
queue.popleft()
queue[0] # raise error if empty

# deque
from collections import deque
queue = deque([4])
queue.append(5)
queue.appendleft(1)
queue.pop()
queue.popleft()

# linked list

# ordered map
from collections import OrderedDict
ordered_hash = OrderedDict()

# doubly linked list

# heap
from heapq import *
min_heap = []
heapify(min_heap) # O(N), build min heap
heappush(min_heap, (key1, key2)) # O(log n) , sorted by key1 -> key2
heappop(min_heap) # O(log n)
heappushpop(min_heap, item) # O(log n), push an element and pop the smallest one
min_heap[0] # get smallest

max_heap = []
heappush(max_heap, -element)
-heappop(max_heap)
-max_heap[0] # get smallest

# priority queue
from queue import PriorityQueue
pq = PriorityQueue(maxsize=3)
pq.put(3)
pq.get() # return 3
pq.queue # see all the elements


#####################################################
#          CUSTOM BUILT-IN DATA STRUCTURE           #
#####################################################

# dict

# stack

# queue

# dict + DLL

# trie

# union find
class UnionFind():
    def __init__(self, N):
        self.ids = list(range(N))
        self.rank = [0] * N
        self.count = N

    def find(self, p):
        ids = self.ids

        while p != ids[p]:
            ids[p] = ids[ ids[p] ]
            p = ids[p]

        return p

    def conntected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        ids = self.ids
        rank = self.rank

        p_root = ids[p]
        q_root = ids[q]

        if p_root == q_root:
            return

        self.count -= 1
        if rank[p_root] > rank[q_root]:
            ids[q_root] = p_root
        elif rank[p_root] < rank[q_root]:
            ids[p_root] = q_root
        else:
            rank[p_root] += 1
            ids[q_root] = p_root

# segement tree (sum)
class SegmentTreeNode():
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum # depends on use case
        self.left = self.right = None # children are SegementTreeNode as well

def buildS(start, end, A):
    if start > end:
        return None
    if start == end:
        return SegmentTreeNode(start, end, A[start])

    root = SegmentTreeNode(start, end, 0)
    mid = (start + end) // 2
    root.left = buildS(start, mid, A)
    root.right = buildS(mid + 1, end, A)
    root.sum = root.left.sum + root.right.sum # depends on use case

    return root

def queryS(root, start, end):
    if root.start == start and root.end == end:
        return root.sum # depends on use case

    mid = (root.start + root.end) // 2
    # depends on use case
    l_sum, r_sum = 0, 0
    if start <= mid:
        if end <= mid:
            l_sum = queryS(root.left, start, end)
        else:
            l_sum = queryS(root.left, start, mid)
    if end > mid:
        if start > mid:
            r_sum = queryS(root.right, start, end)
        else:
            r_sum = queryS(root.right, mid + 1, end)
    return l_sum + r_sum

def modifyS(root, index, val):
    if root.start == index and root.end == index:
        root.sum = val # depends on use case
        return

    mid = (root.start + root.end) // 2
    if root.start <= index <= mid:
        modifyS(root.left, index, val)
    if mid < index <= root.end:
        modifyS(root.right, index, val)
    root.sum = root.left.sum + root.right.sum # depends on use case
    return


a = [4,6,2,3]
root = buildS(0, len(a) - 1, a) # use array a to build a segement tree
queryS(root, 2, 3) # query the sum from index 2 to index 3 (including)
modifyS(root, 3, 20) # change the value at index 3 to 20

# binary indexed tree
class BIT():
    def __init__(self, A):
        n = len(A)
        self.bit = [0] * (n + 1)
        for i in range(0, n):
            self.update(i, n, A[i])

    def update(self, i, n, num):
        i += 1
        while i <= n:
            self.bit[i] += num
            i += i & (-i)

    def query(self, i):
        i += 1
        sum = 0
        while i > 0:
            sum += self.bit[i]
            i -= i & (-i)

        return sum

BIT = BIT([1,2,3,4,5])
BIT.query(2) # query the sum from index 0 to index 2

#####################################################
#                    BACKTRACKING                   #
#####################################################

# https://leetcode.com/problems/subsets/description
def dfs(self, pos, nums, path, res):
    # preorder operations
    res.append(path[:])

    # terminating condition
    if pos >= len(nums):
        return

    # inorder operations
    for i in range(pos, len(nums)):
        # pre-backtracking
        path.append(nums[i])

        # recursion
        self.dfs(i + 1, nums, path, res)

        # post-backtracking
        path.pop()

    # postorder
