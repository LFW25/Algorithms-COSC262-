from collections import defaultdict

def change_greedy(amount, coinage):

    coin_count = defaultdict(int)

    while amount > 0 and len(coinage) > 0:

        highest_coin = max(coinage)
        if amount - highest_coin >= 0:
            coin_count[highest_coin] += 1
            amount -= highest_coin
        else:
            coinage.remove(highest_coin)
    if amount > 0:
        return None
    else:
        counter = []
        for key in coin_count:
            counter.append((coin_count[key], key))
        return counter 

def print_shows(show_list):

    show_list.sort(key = lambda x:x[1] + x[2])
    current_time = 0

    for (show_name, start_time, duration) in show_list:
        end_time = start_time + duration
        if start_time >= current_time:
            current_time = end_time
            print("{} {} {}".format(show_name, start_time, end_time))

def fractional_knapsack(capacity, items):

    items.sort(key = lambda x: x[1]/x[2], reverse = True)
    current_weight = 0
    value = 0

    for (item, it_value, it_weight) in items:
        weight_dif = capacity - current_weight
        if weight_dif > 0:
            if weight_dif >= it_weight:
                value += it_value
                current_weight += it_weight
            else:
                ratio = weight_dif/it_weight
                value += it_value * ratio
                current_weight += it_weight * ratio
    
    return value


"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re
import heapq as hp
HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')
    
    def __lt__(self, other):
        return self.count < other.count

class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph

    def __lt__(self, other):
        return self.count < other.count

class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root

    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        node_dict = self.make_codewords(self.root)
        code_string = ''
        for letter in text:
            code_string += node_dict[letter]
        
        return code_string
    
    def make_codewords(self, root):
        def helper(node, codeword):
            if node.is_leaf() == True:
                yield (node.char, codeword)
            else:
                yield from helper(node.left, codeword + '0')
                yield from helper(node.right, codeword + '1')


        # convert (codeword, letter) pairs to dictionary
        return dict(helper(root, ''))

    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        current = self.root
        letters = ''

        for num in binary:
            if current.is_leaf() is False:
                if int(num) == 0:
                    current = current.left
                elif int(num) == 1:
                    current = current.right
            if current.is_leaf() is True:
                letters += current.char
                current = self.root
        return letters

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        self.root = None          # *** FIXME ***
        trees = []
        for (letter, frequency) in freqs.items():
            trees.append(Leaf(frequency, letter))
 
        while len(trees) > 1:
            # sort all the nodes in ascending order
            # based on theri frequency
            trees = sorted(trees, key=lambda x: (x.count, x.min_char))
 
            left = trees.pop(0)
            right = trees.pop(0)
 
 
            # combine the 2 smallest nodes to create
            # new node as their parent
            newNode = Node(left, right)
 
            # remove the 2 nodes and add their
            # parent as new node among others

            trees.append(newNode)

        self.root = trees[-1]
        return trees

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


# Example from Q11
freqs = {
   'p': 27,
   'q': 11,
   'r': 27,
   'u': 8,
   't': 5,
   's': 3}
tree = HuffmanTree()
tree.build_from_freqs(freqs)
print(tree)
"""
Node(81,↩
  Leaf(27, 'r'),↩
  Node(54,↩
    Leaf(27, 'p'),↩
    Node(27,↩
      Leaf(11, 'q'),↩
      Node(16,↩
        Node(8,↩
          Leaf(3, 's'),↩
          Leaf(5, 't')),↩
        Leaf(8, 'u')))))
"""