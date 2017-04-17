nodes = {} # id : node
children_to_be_added = {} # id : list of ids

class Node(object):
    
    global children_to_be_added
    
    def __init__(self, id, name, parent_id, children = None):
                
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.children = children if children else []
        
        if parent_id is None:
            return
        if parent_id in nodes:
            # parent node has been created
            nodes[parent_id].children.append(self)
        else:
            # parent node hasn't been created yet
            # make a note, after you creat parent node
            # add self to the list of parent node's children
            if parent_id in children_to_be_added:
                children_to_be_added[parent_id].append(id)
            else:
                children_to_be_added[parent_id] = [id]
            # previous four lines can be compacted into
            #   children_to_be_added[parent_id].append(id)
            # if the default value of dictionary
            # children_to_be_added is an empty list
            
    def __str__(self):
        
        # do not include the root node's empty string
        return self._str_helper_(0)[1:]
    
    def _str_helper_(self, num):
        
        res = [self.name]
        self.children.sort(key = lambda node : node.name)
        for child in self.children:
            res.append('-'*num + child._str_helper_(num+1))
        
        return '\n'.join(res)
    
    def adopt(self, children_ids):
        for child_id in children_ids:
            child = nodes[child_id]
            self.children.append(child)

def answer(locations):
    ''' PRECONDITION: no location has an id of -1
    '''
    
    global nodes
    
    root_node = Node(id = -1, name = "", parent_id = None)
    nodes[-1] = root_node
    
    for location in locations:
        id = location["id"]
        name = location["name"]
        parent_id = location["parent_id"]
        
        if parent_id is None:
            # top level nodes will be parented by the root_node
            parent_id = -1
        
        nodes[id] = Node(id, name, parent_id)
    
    # all nodes have been created
    
    for parent_id, children_ids in children_to_be_added.items():
        parent = nodes[parent_id]
        parent.adopt(children_ids)
    
    return str(root_node)

# locations = [{"id":??, "name":??, "parent_id":??}, ...]

locations = [
    {"id": 1, "name":"San Francisco", "parent_id":2},
    {"id": 2, "name":"California", "parent_id": 12},
    {"id": 3, "name":"Pereira", "parent_id":6},
    {"id": 4, "name":"North Carolina", "parent_id":12},
    {"id": 5, "name":"Charleston", "parent_id":9},
    {"id": 6, "name":"Colombia", "parent_id":11},
    {"id": 7, "name":"Canada", "parent_id":17},
    {"id": 8, "name":"Arequipa", "parent_id":13},
    {"id": 9, "name":"South Carolina", "parent_id":12},
    {"id":10, "name":"Bogota", "parent_id":6},
    {"id":11, "name":"South America", "parent_id":None},
    {"id":12, "name":"United States", "parent_id":17},
    {"id":13, "name":"Peru", "parent_id":11},
    {"id":14, "name":"Berkeley", "parent_id":2},
    {"id":15, "name":"Lima", "parent_id":13},
    {"id":16, "name":"Mexico", "parent_id":17},
    {"id":17, "name":"North America", "parent_id":None},
    {"id":18, "name":"Palo Alto", "parent_id":2},
    {"id":19, "name":"Los Angeles", "parent_id":2},
    {"id":20, "name":"Ithaca", "parent_id":23},
    {"id":21, "name":"Cali", "parent_id":6},
    {"id":22, "name":"Queens", "parent_id":23},
    {"id":23, "name":"New York", "parent_id":12},
    {"id":24, "name":"Greenville", "parent_id":9},
    {"id":25, "name":"Manhattan", "parent_id":23},
    {"id":26, "name":"Myrtle Beach", "parent_id":9} ]

print answer(locations)
