colors=['Red','Blue','Green']
states=['a','b','c','d']
neighbours={}
neighbours['a']=['b','c','d']
neighbours['b']=['a','d']
neighbours['c']=['a','d']
neighbours['d']=['c','b','a']
colors_of_states={}
def promising(state,color):
    for neighbour in neighbours.get(state):
        color_of_neighbour=colors_of_states.get(neighbour)
        if color_of_neighbour==color:
            return False
    return True
def get_color_for_state(state):
    for color in colors:
        if promising(state,color):
            return color
def main():
    for state in states:
        colors_of_states[state]=get_color_for_state(state)
    print(colors_of_states)
main()
