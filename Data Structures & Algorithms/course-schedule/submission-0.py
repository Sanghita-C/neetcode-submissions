class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [x1, x2] , [x2 ,x3], [x3 , x1]

        - we do bfs start on every node with 0 indegree:
        - everytime I am putting something in queue the edge gets processed - imdegree decreases
        - only push something to queue whose indegree <= 0.
        

        at the end just see if all nodes have been visited or not - if not then not possible


        """

        indegree = [0]*numCourses
        visited = [0] * numCourses
        adj_list = {}

        for prereq in prerequisites: #o(m)
            first_course = prereq[1]
            second_course = prereq[0]

            indegree[second_course] +=1

            if first_course in adj_list.keys():
                adj_list[first_course].append(second_course)
            else:
                nextcourse_list = [second_course]
                adj_list[first_course] = nextcourse_list

        
        def bfs(start, adj_list, visited , indegree):

            queue = deque()
            queue.append(start)

            while queue : 
                node = queue.pop()
                visited[node] = 1
                #print(adj_list[node])

                for adj_node in adj_list.get(node, []):
                    indegree[adj_node] -= 1
                    if indegree[adj_node] == 0:
                        queue.append(adj_node)
            

        for i in range(numCourses): 
            if visited[i]==0 and indegree[i] == 0: 
                bfs(i,adj_list, visited, indegree)

        for i in range(numCourses):
            if visited[i]==0:
                return False

        return True



        