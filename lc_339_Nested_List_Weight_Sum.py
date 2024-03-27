class Solution:
    ## dfs
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
    
    ##  bfs
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)
        total = 0
        depth = 1
        while len(queue) > 0:
            for i in range(len(queue)):
                element = queue.pop()
                if element.isInteger():
                    total += element.getInteger() * depth
                else:
                    queue.extendleft(element.getList())
            depth += 1
        return total
