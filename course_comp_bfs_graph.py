class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        #hashmap to store [dep: what its dep on]
        hashmap = {i: [] for i in range(numCourses)}

        #arr indegree to store each courses, list od prereq
        indegree= [0] * numCourses

        #traverse for loop for each "edge" in prereq
        for edge in prerequisites:
            dep = edge[0]
            indep = edge[1]
            hashmap[indep].append(dep)

            #after doing stuff to hashmap, go to dep's index in indegree
            #add one 
            indegree[dep]+=1

        #now, we have indeg, and hashmap,  if any indeg is 0 we need to 
        #start from there, and go to its connections in hashmap and 
        # reduce each value by 1, ideally after reducing, there should be
        #another indegree 0 guy who we can take as next course, else its 
        #false, so now itself we check, hey is indegree all 0 or atleast 
        #one 0, then only we can start

        queue=deque([])
        #to put all indegree 0 and traverse it, such that we have all 
        #the indep in queue now, and all its dep has -1 indegree

        count=0
        #if count is numcourses, then true, we cn take all courses

        #for i in indegree(NO CUZ INDEG HAS VALUE, INDEG'S INDEX IS NUMCORSE
        for i in range(0, len(indegree)):
            if indegree[i]==0:
                count+=1
                queue.append(i) 
                #i cuz thats the course num

        #checks to eliminate unneeded loops
        if count==0: return False
        if count== numCourses: return True


            #we're using coursenum to traverse hashmap
            #in hashmap we're finding all the dep nodes of this val
            #reduce its count by 1 in indeg
            #seeing if indeg is 0, then append it to queue
        
        while queue: #we're checking if there's an indep course at each pt
            curr_indep= queue.popleft()
            dep_of_curr_indep= hashmap[curr_indep]
            #at this pt all list vals are there for curr indep

            #what happs if dep_of_curr_indep is null, aka it doesnt have any 
            #child val? whole next for loop is discredited, so we check 

            if dep_of_curr_indep:
                for i in dep_of_curr_indep:
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
                        count+=1
                        #all nodes which are indep has to be appeneded
                    if count==numCourses: return True

        return count==numCourses
            