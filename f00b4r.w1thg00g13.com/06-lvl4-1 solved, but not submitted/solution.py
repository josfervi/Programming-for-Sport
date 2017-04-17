# Tags:
# Network Flow
# Flow Network
# Max Flow
# Maximum Flow
# Min Cut
# Minimum Cut
# Ford-Fulkerson Algorithm
# Ford Fulkerson Algorithm
# Residual Network
# Residual Graph
# Augmenting Path
# Augmenation Path
# s-t Path
# s t Path
# st Path
# Iterative DFS Path
# Iterative Depth First Search Path
# Single Source
# Single Sink
# Graph
# Graph Operations
# Merging Nodes
# Node Merging
# Merge Nodes
# Adjacency Matrix
# Matrix Operations


def answer(entrances, exits, path):
    """Returns the total number of bunnies per time step that can get through at
         at peak throughput.
    """
    return FlowNetwork.value_of_max_flow(sources = entrances,
										 sinks = exits,
										 adjacency_matrix = path)


def _merge_rows(matrix, row_labels, into):
    
    aggregate_row_label = into
    aggregate_row = matrix[aggregate_row_label]
    for row_label in row_labels:
        current_row = matrix[row_label]
        _add_list(current_row, into = aggregate_row)


def _add_list(current_row, into):

    aggreagate_row = into
    n = len(aggreagate_row)
    assert len(current_row) == n
    
    for i in range(n):
        aggreagate_row[i] += current_row[i]
    
    
def _merge_cols(matrix, col_labels, into):
    
    _transpose(matrix)
    _merge_rows(matrix, col_labels, into)
    _transpose(matrix)


def _transpose(matrix):

    matrix[:] = zip(*matrix)

    # convert each row from a tuple to a list
    matrix[:] = map(list, matrix)


def _remove_rows(matrix, row_labels):

    row_labels.sort()

    for row_label in reversed(row_labels):
        del matrix[row_label]


def _remove_cols(matrix, col_labels):
    
    _transpose(matrix)
    _remove_rows(matrix, col_labels)
    _transpose(matrix)


def _relabel_in_matrix(matrix, pair):

    _swap_rows(matrix, pair)
    _swap_cols(matrix, pair)


def _swap_rows(matrix, pair):

    label, other_label = pair
    matrix[label], matrix[other_label] = matrix[other_label], matrix[label]


def _swap_cols(matrix, pair):

    _transpose(matrix)
    _swap_rows(matrix, pair)
    _transpose(matrix)


def _relabel_in_list(lst, pair):
    
    n = len(lst)

    label1, label2 = pair
    
    for i in range(n):
        if   lst[i] == label1: lst[i] = label2
        elif lst[i] == label2: lst[i] = label1


def _clear_row(matrix, row_label):
    
    matrix[row_label] = [0]*len(matrix[row_label])


def _clear_col(matrix, col_label):
    
    _transpose(matrix)
    _clear_row(matrix, col_label)
    _transpose(matrix)


def _clear_diagonal(matrix):
    
    n = len(matrix)
    
    for i in range(n):
        matrix[i][i] = 0


def _square_matrix_of_zeros(n):
    
    return [ [0]*n for _ in range(n) ]


class Graph(object):
    
    def __init__(self, adjacency_matrix):
        self.num_nodes = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
    
    def merge_nodes(self, nodes, into):
        
        aggregate_node = into

        assert aggregate_node not in nodes
        
        matrix = self.adjacency_matrix
        _merge_rows(matrix, row_labels = nodes, into = aggregate_node)
        _merge_cols(matrix, col_labels = nodes, into = aggregate_node)

    # overridden by FlowNetwork
    def remove_nodes(self, nodes_to_be_removed):
        
        matrix = self.adjacency_matrix
        nodes_to_be_removed.sort()

        _remove_rows(matrix, row_labels = nodes_to_be_removed)
        _remove_cols(matrix, col_labels = nodes_to_be_removed)
        
        self.num_nodes -= len(nodes_to_be_removed)

    def __setitem__(self, tup, val):
        """Set the capacity of edge (u,v).
        """
        u, v = tup
        self.adjacency_matrix[u][v] = val

    def __getitem__(self, tup):
        """Return the capacity of edge (u,v).
        """
        u, v = tup
        return self.adjacency_matrix[u][v]

    def cap(self, u, v):
        """A more readable alias for self[(u, v)].
        """
        return self[(u, v)]

    def get_reachable_neighbors_of(self, u):

        n = self.num_nodes
        return [v for v in range(n) if self.cap(u, v) > 0]
    
    def find_path(self, s, t):
        """Returns a path from s to t if one exists
               along with its bottleneck as a tuple.
               Otherwise returns (None, 0).
        """
        node_stack = [s]
        visited_nodes = []
        node_before = {}

        while node_stack:
            u = node_stack.pop()
            if u == t:
                break
            if u in visited_nodes:
                continue
            visited_nodes.append(u)
            for v in self.get_reachable_neighbors_of(u):
                node_stack.append(v)
                node_before[v] = u
        
        if u != t:
            return (None, 0)
        
        bottleneck = 2**31 - 1
        path_stack = [] # a list of edges
        v = t
        while v != s:
            u = node_before[v]
            path_stack.append( (u,v) )
            bottleneck = min( bottleneck, self.cap(u,v) )
            v = u
        
        return reversed(path_stack), bottleneck


class Flow(object):
    
    def __init__(self, flow_network):
        self.flow = _square_matrix_of_zeros(flow_network.num_nodes)

    def __setitem__(self, tup, val):
        u, v = tup
        self.flow[u][v] = val
    
    def __getitem__(self, tup):
        u, v = tup
        return self.flow[u][v]


class FlowNetwork(Graph):
    """Maintains a FlowNetwork."""
    
    @classmethod
    def from_adjacency_matrix_multiple_sources_sinks(cls,
                                                     adjacency_matrix,
                                                     sources,
                                                     sinks):
        
        assert len(sources) > 0
        assert len(sinks)   > 0
        
        flow_network_in_progress = cls(adjacency_matrix,
                                       single_source = None,
                                       single_sink = None)
        
        # A flow network must have a single source and a single sink, so
        # merge the multiple sources into a single source and
        # merge the multiple sinks   into a single sink.

        FIRST, SECOND, LAST = 0, 1, flow_network_in_progress.num_nodes-1
        
        sources.sort()
        sinks.sort()

        single_source = sources[FIRST]
        all_sources_except_single_source = sources[SECOND:LAST+1]
        
        single_sink = sinks[FIRST]
        all_sinks_except_single_sink = sinks[SECOND:LAST+1]
        
        flow_network_in_progress.merge_sources(all_sources_except_single_source,
                                               into = single_source)
        
        flow_network_in_progress.merge_sinks(all_sinks_except_single_sink,
                                             into = single_sink)
        
        flow_network_in_progress.remove_nodes(nodes_to_be_removed = 
                                              (all_sources_except_single_source + all_sinks_except_single_sink) )
        
        flow_network_in_progress.clean()

        completed_flow_network = flow_network_in_progress
        return completed_flow_network
    
    def __init__(self, adjacency_matrix, single_source = None, single_sink = None):
        super(FlowNetwork, self).__init__(adjacency_matrix)
        self.single_source = single_source
        self.single_sink   = single_sink
    
    def merge_sources(self, sources, into):
        single_source = into
        self.merge_nodes(sources, into = single_source)
        self.single_source = single_source
    
    def merge_sinks(self, sinks, into):
        single_sink = into
        self.merge_nodes(sinks, into = single_sink)
        self.single_sink = single_sink
    
    def remove_nodes(self, nodes_to_be_removed):

        single_source = self.single_source
        single_sink = self.single_sink
        
        assert self.single_source not in nodes_to_be_removed
        assert self.single_sink not in nodes_to_be_removed

        matrix = self.adjacency_matrix
        nodes_to_be_removed.sort()
        
        _relabel_in_matrix(matrix,            (0, single_source) )
        _relabel_in_list(nodes_to_be_removed, (0, single_source) )
        self.single_source = 0

        _relabel_in_matrix(matrix,            (1, single_sink) )
        _relabel_in_list(nodes_to_be_removed, (1, single_sink) )
        self.single_sink = 1
        
        super(self.__class__, self).remove_nodes(nodes_to_be_removed)

    def clean(self):
        """Removes edges that go into the singe source,
               edges that go out from the single sink,
               and self-loops.
               A self-loop is an edge that connects a vertex to itself.
        """
        matrix = self.adjacency_matrix
        
        # remove edges that go into the single source
        _clear_col(matrix, col_label = self.single_source)

        # remove edges that go out from the single sink
        _clear_row(matrix, row_label = self.single_sink)

        # remove self-loops
        _clear_diagonal(matrix)
    
    def find_max_flow(self):
        
        # The residual network / flow invariant:
        # residual_network.cap(u,v) = original_flow_network.cap(u,v) - flow[(u,v)]

        residual_network = self
        best_flow_soFar = Flow(self)
        value_of_best_flow_soFar = 0

        s, t = self.single_source, self.single_sink

        augmenting_path, bottleneck = residual_network.find_path(s, t)
        
        while augmenting_path:
            
            for edge in augmenting_path:
                
                u, v = edge
                
                # Send flow along the path and maintain the invariant.
                best_flow_soFar[(u, v)]  += bottleneck
                residual_network[(u, v)] -= bottleneck

                # The flow that might be "returned later". Also maintain the invariant.
                best_flow_soFar[(v, u)]  -= bottleneck
                residual_network[(v, u)] += bottleneck

            value_of_best_flow_soFar += bottleneck
            
            augmenting_path, bottleneck = residual_network.find_path(s, t)
        
        max_flow = best_flow_soFar
        value_of_max_flow = value_of_best_flow_soFar
        return max_flow, value_of_max_flow
    
    @staticmethod
    def value_of_max_flow(sources, sinks, adjacency_matrix):
        """Returns the value of the maximum flow of the flow network.
        """
        
        flow_network = FlowNetwork.from_adjacency_matrix_multiple_sources_sinks(adjacency_matrix,
																		        sources,
																		        sinks)
        max_flow, value_of_max_flow = flow_network.find_max_flow()
        return value_of_max_flow


# TESTS

entrances = [4,2]
exits = [1,5,3]
paths = [ [0,2, 0,9,0,40],
          [0,0, 0,0,0,20],
          [7,0, 0,6,0, 0],
          [0,0, 0,0,0, 0],
          [5,0,10,0,0, 8],
          [0,0, 0,0,0, 0] ]

flow_network = [ [0, 14, 12],
                 [0,  0,  0],
                 [0, 51,  0] ]

expected_result = 26

actual_result = answer(entrances, exits, paths)
print actual_result == expected_result
print actual_result