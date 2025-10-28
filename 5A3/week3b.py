colors=['red','green','blue','yellow','black']
states=['TS','KA','TN','KL']
neighbors={}
neighbors['TS']=['KA','TN']
neighbors['KA']=['TS','TN','KL']
neighbors['TN']=['TS','KA','KL']
neighbors['KL']=['KA','TN']
colors_of_states={}
def promising(state,color):
    for neighbor in neighbors.get(state):
        color_of_neighbor=colors_of_states.get(neighbor)
        if color_of_neighbor==color:
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
