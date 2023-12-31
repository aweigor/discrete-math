import graphviz
def graph_abba():
    f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')
    f.edge('1', '2', label='a, 0')
    f.edge('1', '1', label='b, 0')
    f.edge('2', '2', label='a, 0')
    f.edge('2', '3', label='b, 0')
    f.edge('3', '2', label='a, 0')
    f.edge('3', '4', label='b, 0')
    f.edge('4', '2', label='a, 1')
    f.edge('4', '1', label='b, 0')
    f.view()

def graph_a2ia():
    f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')
    f.edge('p', 'q', label='a, 0')
    f.edge('p', 'p', label='b, 0')
    f.edge('q', 'r', label='a, 0')
    f.edge('q', 'r', label='b, 0')
    f.edge('q', 't', label='a, 1')
    f.edge('r', 's', label='b, 0')
    f.edge('r', 's', label='a, 0')
    f.edge('s', 'p', label='b, 0')
    f.edge('s', 'q', label='a, 1')
    f.view()

# muliplication of a2ia and abba
def graph_multiply():
    f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')
    f.edge('p,1', 'p,1', label='b,(0,0)')
    f.edge('p,1', 'q,2', label='a,(0,0)')
    f.edge('q,2', 'r,2', label='a,(0,0)')
    f.edge('q,2', 'r,3', label='b,(0,0)')
    f.edge('q,2', 't,2', label='a,(1,0)')
    f.edge('t,2', 's,2', label='a,(0,0)')
    f.edge('t,2', 's,3', label='b,(0,0)')
    f.edge('r,2', 's,2', label='a,(0,0)')
    f.edge('r,2', 's,3', label='b,(0,0)')
    f.edge('r,3', 's,2', label='a,(0,0)')
    f.edge('r,3', 's,4', label='b,(0,0)')
    f.edge('s,2', 'p,3', label='b,(0,0)')
    f.edge('s,2', 'q,2', label='a,(1,0)')
    f.edge('s,3', 'q,2', label='a,(1,0)')
    f.edge('s,3', 'p,4', label='b,(0,0)')
    f.edge('s,4', 'q,2', label='a,(1,1)')
    f.edge('s,4', 'p,1', label='b,(0,0)')
    f.edge('p,3', 'q,2', label='a,(0,0)')
    f.edge('p,3', 'p,4', label='b,(0,0)')
    f.edge('p,4', 'q,2', label='a,(1,0)')
    f.edge('p,4', 'p,1', label='b,(0,0)')
    f.view()

graph_abba()