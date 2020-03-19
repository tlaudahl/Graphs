# 2: Build the graph

# Load words from dictionary
f = open('words.txt', 'r')
words = f.read().lower().split('\n')
f.close()

def get_neighbors(word):
    '''
    Get all words that are one letter
    away from the given word
    '''
    # Get same length words first
    
    result = []

def words_are_neighbors(w1, w2):
    '''
    return True if words are one letter apart
    False otherwise
    '''

    # Go through each letter in the word
    # swap with each letter in the alphabet
    # Check if that equals given word


from util import Stack, Queue
# 3: Traverse the graph (BFS)
def word_ladder(self, begin_word, end_word):
    

    # Create a queue
    q = Queue()
    # Enqueue a path to the starting word
    q.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # Check if its our target word
    while q.size() > 0:
        path = q.dequeue()
        w = path[-1]
        if w == end_word:
            return path
        if w not in visited:
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)