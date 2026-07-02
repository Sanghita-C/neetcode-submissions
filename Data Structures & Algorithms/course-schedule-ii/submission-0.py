class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        [ai,bi]  bi prereq of ai
        - something doesn't have prereq - do that first. 
        - traverse the graph
        - check for cycles

        row --> prereq, col --> course

        graph : breadth first search traversal -- complete all prereq courses
        """

        #adj matrix
        course_matrix = [[0]*n for i in range(n)]
        foundation_course = [1]*n

        for item in prerequisites:
            course = item[0]
            prereq = item[1]
            foundation_course[course] = 0
            course_matrix[prereq][course] = 1

        visited = [0]*n
        final_order = []

        queue = deque()
        for i in range(n):
            if foundation_course[i] == 1:
                queue.append(i)
                #visited[i] = 1
                #final_order.append(i)

        while queue: 
            node = queue.popleft()
            print(f"node: {node}")
            #check if any dependency not visited yet
            dependencies_done = True
            for i in range(n):
                if course_matrix[i][node]==1 and visited[i]==0:
                    print(f"dependency {i} not completed")
                    dependencies_done = False
                    break
                
            if dependencies_done and visited[node]==0:
                print(f"node {node} downstream courses being processed")
                final_order.append(node)
                visited[node] = 1
                #add the dependent courses to queue:
                for i in range(n):
                    if course_matrix[node][i] == 1:
                        queue.append(i)


        courses_complete = True    
        for i in range(n):
            if visited[i] == 0:
                courses_complete = False
                break
        
        if courses_complete:
            return final_order

        return []
            
       

