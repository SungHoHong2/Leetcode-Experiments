### Alien Dictionary

**[General Approach](images/General.png)**
1. Extracting dependency rules from the input.
    -  `A must be before C`, `X must be before D`, or `E must be before B`
2. Putting the dependency rules into a graph with letters as nodes and dependencies as edges
3. Topologically sorting the graph nodes

**Breadth-First Search**
- Concepts
    - Filter the letters with no incoming links
    - Start the BFS search from the nodes with zero incoming links
- [Source code](source/BFS.py)
```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # set a hashmap accepting set as a value
        # set a hashmap to track of the number of incoming nodes for each char
        # iterate each pair of adjacent words
            # set a flag to check if the neighbors are identical
            # iterate each pair of characters from the adjacent words
                # if the character is different
                    # if the character from the second word is not part of the adjacency hashmap
                        # store the character in the adjacency list
                        # increase the number of incoming nodes
                    # mark as identical found
                    # break because there is no way to identify the order beyond this
            # if all the compared words are identical 
                # return empty string if the second word is a subset of the first word
        # set the list to collect the order of characters
        # create a BFS queue that contains nodes without incoming nodes
        # run the BFS
            # pop out the node 
            # append as the answer
            # explore the destinations of the current node
                # decrease the incoming node of the destination  
                # append the dest to the BFS queue if the number of incoming nodes is zero 
        # return the empty string if there are disconnected graphs 
        # return the order of the characters as a string
        pass
```

**DFS**
- Concepts
    - Do not need to count the incoming links 
    - Detect cycles by using graph coloring 
- [Source code](source/DFS.py)
```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # set a hashmap accepting set as a value
        # iterate each pair of adjacent words
            # set a flag to check if the neighbors are identical
            # iterate each pair of characters from the adjacent words
                # if the character is different
                    # store the character in the adjacency list
                    # mark as identical found
                    # break because there is no way to identify the order beyond this
            # return empty string if the second word is a subset of the first word
        # set a hashmap to check the visited nodes
        # set the list to collect the order of characters
        # run the DFS
            # return the result of the visited node
            # mark the node as grey
            # explore the adjacent nodes and return False if the cycle is detected
            # mark the node as black if there is no cycle or the node is a single
            # append the result
            # return True
        # return empty if one of the dfs returns False
        # return the order of the characters as a string
        pass
```