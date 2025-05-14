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

def traverse(node, start = False):
  global steps
  
  
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
  
  #print(node)
  if node['cell'] == [11, 13]:
    node['history'].append(node['cell'])
    #print('move is ')
    print(find_move(node['history'][-2], node['cell']))
    raise FoundFinal(node)

  elif dead_end:
    #print(' '.join(node['moves']) + f' stuck at ( {row} , {column} )')
    #print(f'back to {node['history'][-1]}')
    #print('before popping')
    global steps
    old_list = node['moves'].copy()
    for i in range(steps):
      #print(node['moves'][-(i + 1)])
      #print(node['history'][-(i + 1)])
      node['moves'].pop()
      node['history'].pop()
    new_list = node['moves'].copy()

    print(old_list[(len(new_list)):])
    
    steps = 0
  else:
    for i in range(len(node['queue'])):
      new_history = node['history'].copy()
      new_history.append(node['cell'])
      new_moves = node['moves'].copy()
      new_moves.append(find_move(node['cell'], node['queue'][-1]))
      #print(f'stesps are {steps}')
      new_node = {'cell': node['queue'][-1], 'history': new_history, 'queue': [], 'moves': new_moves, 'steps': node['steps'] + 1}
      steps += 1
      node['queue'].pop(-1)
      traverse(new_node)


      #print(' '.join(node['moves']) + f' stuck at ( {row} , {column} )')
      #print(f'back to {node['history'][-1]}')

  

node = {'cell': [2, 0], 'history': [], 'queue': [], 'moves': [], 'steps': 0}
try:
  traverse(node)
except FoundFinal as e:
  print('found a path')
  print(e)


print(f'Start at ({node['cell'][0]}, {node['cell'][1]})')