"""
Binary Tree Data Structure
    Data is stored in hierarchical form where a parent node can have at most 2 child nodes
                A
             ___|___
            B       C
         ___|___
        D       E
      /  \       \
     F    G       H
         Here, A is "ROOT NODE" and B, C are "CHILD NODE"
            (B-D-F-G), (B-E-H) is a sub-tree
            B is 'ROOT NODE' for D, E & D is 'ROOT NODE' for F, G & E is root node for H
            Those nodes [C, F, G, H] who do not have any child node are "LEAF NODE"

    Rules for Binary Search Tree:
        > All nodes are unique
        > Right sub-tree > Left sub-tree ===== Left sub-tree < Right sub-tree
            [Value(B<A AND C>A), Value(D<B AND E>B), Value(F<D AND G>D), Value(H>E)]
        > One parent node can not have more than 2 child nodes
        > Elements are not duplicated
    Searching in Binary Tree:
        Suppose we want to search E in the Tree:
            > At Root Node(A) :: IF A>E THEN element would be at Left sub-Tree
            > At Left sub-Tree(B) :: IF B<E THEN element would be at Right of the sub-tree

Significance of BST:
    With every iteration, search space is reduced by 1/2 (half)
        Let no of nodes in a tree (n) be 8 then:
            n = 8   [8->4->2->1]    {Search completed in 3 iterations}
            3 compared to 8 is log(2)8 = 2
        Search Complexity : O(log n)
        Insertion Complexity : O(log n)


Types of BST:
    Breadth First Search


    Depth First Search
        order here means base node
        > In Order Traversal : first visit left sub-tree >> root node >> right sub-tree [F-D-G-B-H-E-A-C]
                            {Root node in between left and right tree}
        > Pre Order Traversal : root node >> left sub-tree >> right sub-tree [A-B-D-F-G-E-H-C]
                            {Root node before left and right tree}
        > Post Order Traversal : left sub-tree >> right sub-tree >> root node [F-G-D-H-E-B-C-A]
                            {Root node after left and right tree}



"""


class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """Insert data as child in Tree"""

        # checking if entered data is already present
        if data == self.data:
            return

        # if tree is empty means no node(root) at tree else incoming data will be treated as node(root(tree))
        if self.data:
            ''' check if data(right) > data(left) & node(parent)'''
            if data < self.data:  # data is smaller than data of node(parent)
                if self.left is None:  # and if no element is present at left of node
                    self.left = Node(data)  # insert data at left
                else:
                    # consider node(left) {current node} as node(root)
                    self.left.add_child(data)

            elif data > self.data:  # if data is greater than root node
                if self.right is None:  # and if no data(right) is None
                    # insert data at right of node(parent)
                    self.right = Node(data)
                else:  # if data is already present at right of node
                    # consider node(right) {current node} as node(root)
                    self.right.add_child(data)
        else:
            self.data = data  # if tree is empty; treat incoming data as root of the tree

    def InOrderTraversal(self):
        elements = []  # list to be filled with all elements of BST in specific order

        # In-order-Traversal : left sub-tree >> root node >> right sub-tree
        if self.left:  # put elements of left sub-tree in list[elements]
            elements += self.left.InOrderTraversal()

        elements.append(self.data)  # put root node data in list[elements]

        if self.right:   # put elements of right sub-tree in list[elements]
            elements += self.right.InOrderTraversal()

        return elements  # return list[elements]

    def PreOrderTraversal(self):
        elements = []

        # Pre-Order-Traversal : root node >> left sub-tree >> right sub-tree

        elements.append(self.data)  # put root node data in list[elements]

        if self.left:  # put elements of left sub-tree in list[elements]
            elements += self.left.InOrderTraversal()

        if self.right:  # put elements of right sub-tree in list[elements]
            elements += self.right.InOrderTraversal()

        return elements  # return list[elements]

    def PostOrderTraversal(self):
        elements = []

        # Pre-Order-Traversal : left sub-tree  >> right sub-tree >> root node

        if self.left:  # put elements of left sub-tree in list[elements]
            elements += self.left.InOrderTraversal()

        if self.right:  # put elements of right sub-tree in list[elements]
            elements += self.right.InOrderTraversal()

        elements.append(self.data)  # put root node data in list[elements]

        return elements  # return list[elements]

    def search(self, val):
        """ Search element in binary search tree"""
        if self.data == val:
            return True

        if val < self.data:
            # search for val in left sub-tree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # search for val in right sub-tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def max(self):
        '''Maximum element of tree: keep searching on right sub-tree to find maximum element '''
        if self.right is None:  # leaf node
            return self.data
        return self.right.max()

    def min(self):
        ''' Minimum element of tree: keep searching on left sub-tree to find minimum element '''
        if self.left is None:  # leaf node
            return self.data
        return self.left.min()

    def delete(self, val):
        if val < self.data:  # search for element in left sub-tree
            if self.left:  # check if there is any left sub-tree
                self.left = self.left.delete(val)  # delete recursion
        elif val > self.data:  # search for element in right sub-tree
            if self.right:  # check if there is any right sub-tree
                self.right = self.right.delete(val)  # delete recursion
        else:
            if self.left is None and self.right is None:  # if left & right sub-tree are empty
                return None
            if self.left is None:  # right sub-tree is present but not left sub-tree
                return self.right  # return right sub-tree-child
            if self.right is None:  # left sub-tree is present but not right sub-tree
                return self.right  # return left sub-tree-child

            min_val = self.right.min()  # find minimuum element from right sub-tree
            self.data = min_val  #
            self.right = self.right.delete(min_val)

        return self

    def display(self):
        """ Display tree """
        if self.left:
            self.left.display()  # display tree(left)
        print(self.data)  # display node(root)
        if self.right:
            self.right.display()  # display tree(right)


def build_tree(elements):
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


# If build_tree() is not used
# root = Node(4)
# root.add_child(6)
# root.add_child(7)
# root.add_child(2)
# root.add_child(3)
# root.add_child(8)
# root.add_child(5)

''' smaller elements will be displayed at left/top of root node <--> greater elements will be displayed at 
 right/bottom of root node '''
# root.display()

# main method
if __name__ == '__main__':

    # Numeric BST
    # repeated elements are removed
    num_list = [20, 18, 37, 15, 7, 5, 9, 18, 24, 0]
    list_tree = build_tree(num_list)
    print(list_tree.InOrderTraversal())  # return list in sorted order
    print(list_tree.PreOrderTraversal())  # return list in sorted order
    print(list_tree.PostOrderTraversal())  # return list in sorted order
    # list_tree.display()  # display tree using display function
    print(list_tree.search(20))  # True
    print(list_tree.search(4))  # False
    list_tree.delete(20)
    print("Deleted element: ", list_tree.InOrderTraversal())

    # String BST
    country = ["India", "Australia", "France", "Japan", "Sweden"]
    country_tree = build_tree(country)
    print(country_tree.InOrderTraversal())  # return list in sorted order
    print(country_tree.search("UK"))  # False
    print(country_tree.search("Japan"))  # True
