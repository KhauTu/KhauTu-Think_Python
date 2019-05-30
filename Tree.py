class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree):
    ''' prefix '''
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_postorder(tree):
    ''' postfix '''
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")

def print_tree_inorder(tree):
    ''' infix '''
    if tree is None: return
    print("(", end=" ")
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
    print(")", end=" ")

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("\t" * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list) # Get the subexpression
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis") # Remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return Tree("*", a, b)
    return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a

def parse_int(s):
    try:
        res = int(eval(str(s)))
        if type(res) == int:
            return res
    except:
        return

# val = parse_int("1")
# print(val)

def token(string):
    lst = (string + " end").split()
    for i in range(len(lst)):
        if type(parse_int(lst[i])) == int:
            lst[i] = parse_int(lst[i])
            # print(lst[i])
    return lst

if __name__ == '__main__':
    # token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
    # ['(', '9', '+', '8', ')', '*', '(', '6', '+', '5', ')', 'end']
    token_list = token("( 9 + 8 ) * ( 6 + 5 )")
    tree = get_sum(token_list)
    print_tree_inorder(tree)

