maze = [
  [ {'N': False, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': True, 'W': True}, {'N': False, 'E': False, 'S': False, 'W':True},
    {'N': False, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W': True}, {'N': False, 'E': False, 'S': True, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':False},
    {'N': False, 'E': True, 'S': True, 'W':True},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': True, 'W':False}, 
    {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':True} ],

  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': False, 'W': True}, {'N': False, 'E': False, 'S': False, 'W':True},
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W': False}, {'N': True, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': True, 'W':True},
    {'N': True, 'E': False, 'S': True, 'W':True},{'N': False, 'E': True, 'S': False, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': True, 'S': False, 'W':True}, 
    {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False} ],

  [ {'N': True, 'E': True, 'S': True, 'W':True}, {'N': False, 'E': True, 'S': True, 'W':True}, {'N': False, 'E': False, 'S': False, 'W': True}, {'N': False, 'E': True, 'S': True, 'W':False},
    {'N': True, 'E': False, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': True, 'W': False}, {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': True, 'S': False, 'W':False},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':True}, 
    {'N': False, 'E': True, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':True} ],
  
  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': True, 'W': False}, {'N': True, 'E': True, 'S': True, 'W':True},
    {'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W': True}, {'N': False, 'E': True, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': False, 'W':True},
    {'N': False, 'E': False, 'S': False, 'W':True},{'N': False, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':True}, 
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False} ],

  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W': False}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': False, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W': True}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':True},
    {'N': False, 'E': True, 'S': True, 'W':False},{'N': True, 'E': False, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, 
    {'N': True, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False} ],
  
  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': False, 'W': False}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': True, 'W': False}, {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': False, 'S': True, 'W':False},{'N': False, 'E': True, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':True}, {'N': False, 'E': True, 'S': True, 'W':False}, 
    {'N': False, 'E': False, 'S': True, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':False} ],

  [ {'N': True, 'E': False, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': False, 'S': True, 'W': True}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W': False}, {'N': False, 'E': True, 'S': True, 'W':False}, {'N': True, 'E': True, 'S': False, 'W':True},
    {'N': True, 'E': False, 'S': False, 'W':True},{'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, 
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': False, 'S': True, 'W':False} ],

  [ {'N': False, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W': False}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W': False}, {'N': True, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': False, 'S': False, 'W':True},
    {'N': False, 'E': False, 'S': True, 'W':True},{'N': True, 'E': False, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': False, 'W':True}, 
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False} ],

  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': True, 'W': False}, {'N': True, 'E': False, 'S': False, 'W':True},
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': True, 'S': False, 'W': False}, {'N': True, 'E': False, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':False},
    {'N': True, 'E': False, 'S': False, 'W':True},{'N': False, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': False, 'S': True, 'W':False}, 
    {'N': True, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':True} ],

  [ {'N': True, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': True, 'S': False, 'W': True}, {'N': False, 'E': False, 'S': False, 'W':True},
    {'N': True, 'E': True, 'S': False, 'W':False}, {'N': False, 'E': True, 'S': False, 'W': True}, {'N': False, 'E': False, 'S': True, 'W':True}, {'N': True, 'E': True, 'S': False, 'W':False},
    {'N': False, 'E': True, 'S': False, 'W':True},{'N': True, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False}, 
    {'N': False, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False} ],

  [ {'N': True, 'E': False, 'S': True, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':False}, {'N': False, 'E': True, 'S': True, 'W': False}, {'N': False, 'E': True, 'S': False, 'W':True},
    {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W': True}, {'N': True, 'E': True, 'S': True, 'W':False}, {'N': False, 'E': False, 'S': True, 'W':True},
    {'N': False, 'E': True, 'S': True, 'W':False},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False}, 
    {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':False} ],

  [ {'N': False, 'E': True, 'S': True, 'W':False}, {'N': True, 'E': False, 'S': True, 'W':True}, {'N': True, 'E': False, 'S': True, 'W': False}, {'N': False, 'E': True, 'S': True, 'W':False},
    {'N': False, 'E': False, 'S': True, 'W':True}, {'N': True, 'E': True, 'S': False, 'W': False}, {'N': True, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': True, 'S': False, 'W':False},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':True}, {'N': True, 'E': False, 'S': True, 'W':False}, 
    {'N': True, 'E': True, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': False, 'W':True} ],

  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': True, 'S': False, 'W':False}, {'N': True, 'E': False, 'S': False, 'W': True}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': True, 'S': False, 'W':False}, {'N': False, 'E': True, 'S': True, 'W': True}, {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':False},
    {'N': False, 'E': True, 'S': True, 'W':False},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': True, 'S': False, 'W':False}, 
    {'N': False, 'E': False, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':False} ],

  [ {'N': True, 'E': True, 'S': False, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W': True}, {'N': True, 'E': True, 'S': False, 'W':True},
    {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': True, 'S': False, 'W': False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True},
    {'N': True, 'E': True, 'S': False, 'W':True},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True}, 
    {'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':True} ]
  
]

class FoundFinal(Exception):
    pass

def within_range(num):
  return True if num <= 13 and num >= 0 else False

def find_move(first_square, next_square):

  if first_square[0] < next_square[0]:
    return 'South'
  if first_square[0] > next_square[0]:
    return 'North'
  if first_square[1] > next_square[1]:
    return 'West'
  if first_square[1] < next_square[1]:
    return 'East'

steps = 0
lines = []

def traverse(node, start = False):
  global steps
  global lines
  
  row = node['cell'][0]
  column = node['cell'][1]
  dead_end = True
  if within_range(row) and within_range(column-1) and maze[row][column]['W'] and (node['history'] == [] or not node['history'][-1] == [row, column-1]) :
    node['queue'].append([row, column-1])
    dead_end = False
  if within_range(row+1) and within_range(column) and maze[row][column]['S'] and (node['history'] == [] or not node['history'][-1] == [row+1, column]) :
    node['queue'].append([row+1, column])
    dead_end = False
  if within_range(row) and within_range(column+1) and maze[row][column]['E'] and (node['history'] == [] or not node['history'][-1] == [row, column+1]) :
    node['queue'].append([row, column+1])
    dead_end = False
  if within_range(row-1) and within_range(column) and maze[row][column]['N'] and (node['history'] == [] or not node['history'][-1] == [row-1, column]) :
    node['queue'].append([row-1, column])
    dead_end = False
  
  if node['cell'] == [11, 13]:
    node['history'].append(node['cell'])
    old_moves_list = node['moves'].copy()
    for i in range(steps):
      node['moves'].pop()
    new_moves_list = node['moves'].copy()
    difference = old_moves_list[(len(new_moves_list)):]
    lines.append(' '.join(difference) + f' Leaving at ( 11 , 13 )')
    raise FoundFinal(node)

  elif dead_end:
    old_moves_list = node['moves'].copy()
    for i in range(steps):
      node['moves'].pop()
    new_moves_list = node['moves'].copy()

    difference = old_moves_list[(len(new_moves_list)):]

    lines.pop()
    lines.append(' '.join(difference) + f' stuck at ( {row} , {column} )')

    steps = 0
    return False
  else:
    for i in range(len(node['queue'])):
      new_history = node['history'].copy()
      new_history.append(node['cell'])
      new_moves = node['moves'].copy()
      new_moves.append(find_move(node['cell'], node['queue'][-1]))
      new_node = {'cell': node['queue'][-1], 'history': new_history, 'queue': [], 'moves': new_moves, 'steps': node['steps'] + 1}
      steps += 1
      node['queue'].pop(-1)
      stuck_not_printed = traverse(new_node)
      lines.append(f'Back to ({node['cell'][0]} , {node['cell'][0]})')
      if not stuck_not_printed:
        lines.append(f'Stuck at ({node['cell'][0]} , {node['cell'][0]})')

node = {'cell': [2, 0], 'history': [], 'queue': [], 'moves': [], 'steps': 0}
try:
  lines.append('start here')
  traverse(node)
except FoundFinal as e:
  pass

lines.pop(-2)
print(f'Start at ({node['cell'][0]}, {node['cell'][1]})')

for line in lines:
  print(line)