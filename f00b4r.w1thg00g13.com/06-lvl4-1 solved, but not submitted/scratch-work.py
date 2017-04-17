# this is a classic network flow problem
#   # you do need to do some preprocessing
#   # you need:
#   #   # to convert all the entrances, hereby sources, into a single source
#   #   # to convert all the exits, hereby sinks, into a single sink
#   # then you can apply a standard network flow algorithm
# need to review network flow algorithms


# class Node(object):
    
#     def __init__(self, val, neighbors = []):
        
#         self.val = val
#         self.neighbors = neighbors
    
#     def get_neighbors(self):
#         return self.neighbors
    
#     def add_neighbor(self, neighbor, self_to_neighbor_edge_capacity):
        
#         assert isintance(neighbor, type(self))
        
#         self.neighbors.append(neighbor)

# class Edge(object):
    
#     def __init__(self, )

class Graph(list):
    
    # Q: how would you support other underlying representations simultaneously?
    #    e.g. an adjacency list too
    def __init__(self, adjacency_matrix):
        
        assert isinstance(adjacency_matrix, list)
        
        self.num_nodes = len(adjacency_matrix)
        
        for adj_row in adjacency_matrix:
            assert isinstance(adj_row, list)
            assert len(adj_row) == self.num_nodes
        
        self.adjacency_matrix = adjacency_matrix
    
    @classmethod
    def from_adjacency_matrix(cls, adjacency_matrix):
        return cls(adjacency_matrix)
        
    
    
    
    # Q: in python is there an equivalent of ruby's ! to indicate methods
    #    with side-effects (i.e. that transform the input)
    
    # side-effect: in-place tranforms self into
    #              a single-source single-sink
    #              flow network
    def to_flow_netwok(self, sources, sinks):
        ''' '''
        
        assert isinstance(sources, list)
        assert isinstance(sinks, list)
        
        self.merge_nodes(sources)
        self.merge_nodes(sinks)
        # cast self as an object of the FlowNetwork class
        # Q: WHAT IS BEST WAY TO DO THIS?
        # self = FlowNetwork(self) # I don't think this is correct???...
        # self is a local variable, so it won't work
        
        
    # mutates self    
    # side-effect: 
    # merge / consolidate
    def merge_nodes(self, nodes_to_be_merged, index):
        ''' Merges nodes_to_be_merged into aggregate_node == nodes_to_be_merged[index],
            the other nodes in nodes_to_be_merged are deleted.'''
        
        assert index in range(len(nodes_to_be_merged))
        assert nodes_to_be_merged has no duplicates
        assert nodes in nodes_to_be_merged are in range(num_nodes)
        
        nodes_being_merged = nodes_to_be_merged
        
        aggregate_node_adjanceny_matrix_row = [0]*self.num_nodes
        
        for node_being_merged in nodes_being_merged:
            
            node_being_merged_adjacency_matrix_row = self.adjacency_matrix[node_being_merged]
            aggregate_node_adjanceny_matrix_row.addRow(node_being_merged_adjacency_matrix_row)
            self.adjacency_matrix[node_being_merged] = None
        
        
        self.adjacency_matrix[nodes_to_be_merged[index]] = aggregate_node
    
    def compactify(self):
        
            
        
class FlowNetwork(Graph):
    
    # Q: how can you support creating a FlowNetwork from either a Graph obj
    #    or an adjacency matrix
    #    or an adjacency list
    #    using one __init__ method?
    #    Or should you @classmethods like from_adjacency_matrix
    #                                     from_adjacency_list
    
    # @classmethod
    # def from_adjacency_matrix(self, adjacency_matrix):
    #     # create a FlowNetwork obj from an adjacency matrix
    
    def __init__(self, graph, single_source = None, single_sink = None):
        assert isinstance(graph, Graph)
        
        self.single_source = single_source
        self.single_sink   = single_sink
        
        
    
    
    # mutates, modifies, changes
    # side-effect
    # in-place
    
    
    # Q: another from_Graphs(cls, graph) method where the implied source is node 0 and the implied sink is node n-1 (n := num_nodes)
    
    @ classmethod
    def from_Graph(cls, graph, sources, sinks):
        
        FIRST = 0
        
        flow_network_in_progress = cls(graph, single_source, single_sink) # a new obj, graph cast as a FlowNetwork
                                                                          # what if I wanted graph cast a FlowNetwork, but not in a new obj???
                                                                          
        flow_network_in_progress.merge_nodes(sources, FIRST)
        flow_network_in_progress.merge_nodes(sinks, FIRST)
        flow_network_in_progress.compactify_adjacency_matrix() # also changes self.single_source, self.single_sink appropriately
        
        completed_flow_network = flow_network_in_progress
        
        return completed_flow_network
        # return graph cast a FlowNetwork but not nec a new object or should it be a new obj?
    
    # @ classmethod
    # def from_adjacency_matrix(cls, adjacency_matrix, sources, sinks):
        
    def find_max_flow(self):
        
        # ford fulkerson's algo
        
    # Q: if you wanted to use a different algo based on inputs, what is the naming convention for this?
    #    for example:
    #        find_max_flow_using_Ford_Fulkerson()
    #        find_max_flow_using_
        

    # inner class
    class Flow(list):
        ''' a flow is a function, f : e -> int '''
        
        
        def __init__(self, flows):
            
            assert len(flows) = self.num_nodes
            
            self.flows = flows
            
        def calculate_value_of(self):
            
            # return the sum of the flows coming out of the source ==
            #        the sum of the flows going into the sink ==
            #        the sum of the flows across any cut (needs to be better defined), Q: is it the net flow out of any cut??? or is it the sum of the outgoing flows?
            
            value = 0
            for each edge going out of the source: # what about the edges going into the source??? I don't think 
                value += flows[edge]



def answer(entrances, exits, path):
    
    return _answer(sources = entrances, sinks = exits, adjacency_matrix = path)


def _answer(sources, sinks, adjacency_matrix):
    
    assert sources and sinks are disjoint
    
    
    # graph = Graph(adjacency_matrix)
    graph = Graph.from_adjacency_matrix(adjacency_matrix) # which is better???
    
    # flow_network = graph.to_FlowNetwok(sources, sinks)
    flow_network = FlowNetwork.from_Graph(graph, sources, sinks)
    
    max_flow = flow_network.find_max_flow()
                         # .get_max_flow()
                         # .calculate_max_flow()
                         # .compute_max_flow()
                         # .find_max_flow()      # should the function name even allude to what type of computation the function does??? is that considered part of the implementation???
    
    
    
    return max_flow.get_value_of() # I would want to call it like this instead: calculate_value_of(max_flow)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # num_nodes   = len(edge_capacities)
    # num_sources = len(source_labels)
    # num_sinks   = len(sink_labels)
    
    # new_num_nodes = num_nodes - num_sources + 1 - num_sinks + 1
    # new_edge_capacities = [ [None]*new_num_nodes for _ in range(new_num_nodes) ]
    
    # merged_sources__edge_capacities__row = [0]*new_num_nodes
    
    # # collapse/merge all sources into one source
    # for source_label in source_labels:
        
    #     current_source__edge_capacities__row = edge_capacities[source_label]
    #     merged_sources__edge_capacities__row = add_rows(merged_sources_edge_capacities_row, \
    #                                                   current_source_edge_capacities_row    )
    
    # new_edge_capacities[ single_source_label ] = merged_sources_edge_capacities_row
    
    # # collapse/merge all sinks into one sink
    