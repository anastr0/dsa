def canFinish(n, prereqs):
    print("\n\nCanfinish")
    graph = {}
    for c in prereqs:
        a, b = c
        if a == b:
            return False
        if a in graph:
            if b not in graph[a]:
                graph[a].append(b)
        else:
            graph[a] = [b]

    print(graph)
    visited_courses = set()
    for course in graph.keys():
        print('course', course)
        visited = set()
        queue = [course]
        visited_courses.add(course)

        while len(queue) > 0:
            c = queue.pop(0)
            print(c)
            if c in graph:
                for pre in graph[c]:
                    if pre in visited:
                        print('pre', pre, 'visited', visited)
                        if pre in visited_courses:
                            return False
                    if pre not in visited:
                        queue.append(pre)
                        visited.add(pre)
    return True





    # print(graph)
    # full_visited = set()
    # for course in graph.keys():
    #     queue = [course]
    #     visited = set(queue)

    #     print('\n', course, visited, "\nBFS starting for ", course)
        
    #     while len(queue) > 0:
    #         c = queue.pop(0)
    #         if c in graph.keys():
    #             print("Uhm", 'c', c, 'fullvisited', full_visited)
    #             full_visited.add(c)
    #         print('visiting:', c)

    #         if c in graph:
    #             for pre in graph[c]:
    #                 if pre in full_visited:
    #                     print("pre", pre, "is in queue:", queue, 'full_visited:', full_visited)
    #                     return False
    #                 if pre not in visited:
    #                     queue.append(pre)
    #                     visited.add(pre)

    # return True


# false
numCourses = 2
prerequisites = [[1,0],[0,1]]

print(canFinish(numCourses, prerequisites))

# # True
# numCourses = 2
# prerequisites = [[1,0]]

## False
# numCourses = 20
# prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

# # False
# numCourses = 4
# prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]

# True
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]


print(canFinish(numCourses, prerequisites))


# True
numCourses = 5
prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]

print(canFinish(numCourses, prerequisites))