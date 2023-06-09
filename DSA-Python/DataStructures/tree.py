"""
GENERAL TREE
    Data is stored in hierarchical form

                                            ROOT                                            --- Level 0
                         ____________________|____________________
                         A                   B                   C                          --- Level 1
                    _____|_____         _____|_____         _____|_____
                    |         |         |    |     |        |   |   |  |
                    D         E         F    G     H        I   J   K  L                    --- Level 2
               _____|_____              _____|_____
               |   |  |  |              |         |
               M   N  O   P             Q         R                                         --- Level 3




         Here, ROOT is "ROOT NODE" and A, B, C are "CHILD NODE"
            > B-D-F-G is a sub-tree
            > B is 'ROOT NODE' for F, G, H and G is 'ROOT NODE' for Q, R
            > Those nodes [E, F, H, I, J, K, L...] who do not have any child node are "LEAF NODE"
            > For (D, E), A will be Ancestor and for A, (D, E) would be Descendants
    Tree is a recursive dta structure where a child node is another tree in itself

"""


class TreeNode:
    """ Class TreeNode """
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """ Adds children elements to Tree """
        child.parent = self # child is an instance of class(node)
        # adding a child node to tree
        self.children.append(child)


    def get_level(self):
        """ Gets the level of Tree by counting ancestors: if a node has no ancestor, it is root node """
        level = 0 # initialised level to 0
        p = self.parent
        while p:
            """keep on going through parents and increasing levels"""
            level += 1 # increase level by 1
            p = p.parent
        return level


    def print_tree(self):
        """Display Tree in hierarchical format"""
        spaces = ' ' * self.get_level() * 3 # printing 3 spaces for each level
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data) # prints prefix(probably spaces) based on level

        # At leaf nodes, self.children will be an empty array... so we create a check if self.children() is an empty array or not
        if self.children: # checks if len(self.children > 0)
            for child in self.children:
                child.print_tree() # It will recursively call this fn and print the sub-trees




def electronic_product():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphones = TreeNode("cell Phone")
    cellphones.add_child(TreeNode("iphone"))
    cellphones.add_child(TreeNode("Samsung"))
    cellphones.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("MI"))


    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(tv)

    # print(laptop.get_level()) # 1
    # print(cellphones.get_level()) # 1
    # print(tv.get_level()) # 1

    return root





# main method
if __name__ == '__main__':
    root = electronic_product()
    root.print_tree() # prints tree in hierarchical format

    # print(root.get_level()) # 0 // get level of root node





