### Design Search Autocomplete System
**Hashmap**
- [Concepts](images/)
- [Source code](source/Hashmap.py)
```python
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # set a global hashmap[sentence]=times
        # set a global prefix
        # store the history in the hashmap
        pass

    def input(self, c: str) -> List[str]:
        # if the search ended
            # store the new history to the hashamp
            # reset the prefix
        # if ongoing search
            # accumulate the characters
            # create a return list
            # iterate the hashmap
                # if the accumulated characters are the subset and starts at the beginning of the keys
                    # append to the return list
            # sort the return list by frequency and ascii order
            # return three recommendations
        pass 
```

**Using One level Indexing**
- [Concepts](images/)
    - make use of a Two level HashMap
- [Source code](source/OneLevel.py)
```python
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # set a global prefix
        # store the history in the hashmap
        pass
    def input(self, c: str) -> List[str]:
        # if the search ended
            # store the new history to the hashamp
        # if ongoing search
            # accumulate the characters
            # create a return list
            # iterate the hashmap
                # if the accumulated characters are the subset and starts at the beginning of the keys
                    # append to the return list
            # sort the return list by frequency and ascii order
            # return three recommendations
        pass
```

**Using Trie**
- [Concepts](images/)
- [Source code](source/Trie.py)
```python
class AutocompleteSystem:
    def __init__(self, sentences, times):
        # create a Trie and store the input 
        # set the global head of the Trie 
        # set global variable of the ongoing search 
        pass

    def createTrie(self, sent, time):
        # create a Trie using characters from input 
        # record the frequency at the finishing sentence 
        pass

    def appendTrie(self, cur):
        # increase the frequency the new or existing sentence in the Trie 
        pass

    def dfs(self, cur, path, ans):
        # explore append all the finishing sentence to the returning list
        pass       

    def input(self, c):
        # if search is finished, add a new sentence in the Trie 
        # accumulate the input 
        # explore deeper or create a new leaf in the Trie 
        # set a list to collect the possible candidates 
        # explore the candidates using dfs 
        # return the at most three best candidates
        pass
```