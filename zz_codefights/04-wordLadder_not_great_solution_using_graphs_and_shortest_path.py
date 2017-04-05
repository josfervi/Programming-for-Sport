from collections import deque

class GraphNode(object):
    
    def __init__(self, data = None, neighbors = None):
        self.data = data
        
        if not neighbors:
            neighbors = []
        self.neighbors = neighbors
        self.visited = False
    
    # node1 and node2 are instances of GraphNode,
    # but not the same instance
    # 
    # for perf,
    #   node1 should not be in node2.neighbors
    #   and vice versa
    #   
    #   a way around this is to first check
    #   or to use a set for neighbors instead of a list
    # 
    # the edge weight is implicitly 1
    @staticmethod
    def connect(node1, node2):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
    
    # graph is a hash map from string to GraphNode
    @staticmethod
    def find_length_of_shortest_path(graph, src, dst):
        
        # since edges are undirected and unweighted
        # (or equivalently, all of the same weight),
        # a BFS approach works
        
        node_q = deque()
        node_q.append(src)
        lvl = 0
        num_nodes_at_this_lvl = len(node_q)
        num_processed_nodes_at_this_lvl = 0
        
        while node_q:
            
            curr_node = node_q.popleft()
            
            if curr_node == dst:
                return lvl + 1
        
            curr_node.visited = True
            node_q.extend(n for n in curr_node.neighbors if not n.visited)
            
            num_processed_nodes_at_this_lvl += 1
            
            if num_processed_nodes_at_this_lvl == num_nodes_at_this_lvl:
                lvl += 1
                num_nodes_at_this_lvl = len(node_q)
                num_processed_nodes_at_this_lvl = 0
        
        return None


def wordLadder(begin_word, end_word, word_list):
    
    word_set = set(word_list)
    word_set.add(begin_word)
    
    if end_word not in word_set:
        return 0
    word_set.add(end_word)
    
    # hash map from string to GraphNode
    # word_graph = Graph.from_set(word_set)
    word_graph = generate_word_graph(word_set)
    
    # return word_graph.find_length_of_shortest_path(src=, dst=)
    res = GraphNode.find_length_of_shortest_path(word_graph, src=word_graph[begin_word], dst=word_graph[end_word])
    
    return res if res else 0


# words can be a set or a list w/o duplicates
def generate_word_graph(words):
    
    word_list = list(words)
    
    n = len(word_list)
    
    node_of = {}
    
    for word in word_list:
        node_of[word] = GraphNode(word)
    
    for i, word in enumerate(word_list):
        for other_word in word_list[i+1:]:
            if should_be_connected(word, other_word):
                GraphNode.connect(node_of[word], node_of[other_word])
    
    return node_of


def should_be_connected(word, other_word):
    
    if word == other_word:
        raise ValueError("Input string 'word' and input string 'other_word' must not be equal.")
    
    dist_soFar = 0
    for char, other_char in zip(word, other_word):
        if char != other_char:
            dist_soFar += 1
            if dist_soFar > 1:
                return False
    
    # dist_soFar == 1
    return True