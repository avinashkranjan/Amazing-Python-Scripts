import sys
import copy

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        temp = copy.deepcopy(self.domains)
        for variable in self.domains:
            for word in temp[variable]:
                if len(word) != variable.length:
                    self.domains[variable].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]
        updated = False
        temp = copy.deepcopy(self.domains[x])

        if overlap is not None:
            x_overlap, y_overlap = overlap
            for x_word in temp:
                for y_word in self.domains[y]:
                    if x_word[x_overlap] == y_word[y_overlap]:
                        break
                else:
                    self.domains[x].remove(x_word)
                    updated = True

        return updated

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        if arcs == None:
            arcs = list(self.crossword.overlaps.keys())

        while len(arcs) > 0:
            x, y = arcs.pop(-1)
            if self.revise(x, y):
                # no solution
                if len(self.domains[x]) == 0:
                    return False
                for a, b in self.crossword.overlaps.keys():
                    if x == b and (a, b) not in arcs:
                        arcs[:0] = [(a, b)]

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if all(x in assignment.keys() for x in self.crossword.variables):
            return True

        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # check unique words
        if len(assignment.values()) != len(set(assignment.values())):
            return False

        for var in assignment:
            if var.length != len(assignment[var]):
                return False
            for neighbour in self.crossword.neighbors(var):
                if neighbour in assignment and (var, neighbour) in self.crossword.overlaps:
                    var_index, neighbour_index = self.crossword.overlaps[var, neighbour]
                    if assignment[var][var_index] != assignment[neighbour][neighbour_index]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        least_constraining_words = []

        for selected_word in self.domains[var]:
            count = 0

            for neighbour in self.crossword.neighbors(var):
                if neighbour not in assignment and (neighbour, var) in self.crossword.overlaps:
                    neighbour_index, var_index = self.crossword.overlaps[neighbour, var]

                    for neighbour_word in self.domains[neighbour]:
                        if neighbour_word[neighbour_index] != selected_word[var_index]:
                            count += 1

            least_constraining_words.append((selected_word, count))

        sorted_words = sorted(least_constraining_words,
                              key=lambda word: word[1])
        return [word[0] for word in sorted_words]

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        best_var = None
        best_length = None

        for var in self.domains:
            if var not in assignment:
                if best_length == None or len(self.domains[var]) < best_length:
                    best_length = len(self.domains[var])
                    best_var = var
                elif len(self.domains[var]) == best_length:
                    if len(self.crossword.neighbors(var)) > len(self.crossword.neighbors(best_var)):
                        best_var = var

        return best_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment

        next_var = self.select_unassigned_variable(assignment)
        for word in self.order_domain_values(next_var, assignment):
            assignment[next_var] = word
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(next_var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
