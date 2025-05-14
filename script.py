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

  [ {'N': True, 'E': False, 'S': True, 'W':False}, {'N': True, 'E': True, 'S': False, 'W':False}, {'N': True, 'E': True, 'S': False, 'W': True}, {'N': True, 'E': False, 'S': True, 'W':False},
    {'N': True, 'E': True, 'S': False, 'W':False}, {'N': False, 'E': True, 'S': True, 'W': True}, {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':False},
    {'N': False, 'E': True, 'S': True, 'W':False},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': True, 'S': False, 'W':False}, 
    {'N': False, 'E': False, 'S': False, 'W':True}, {'N': False, 'E': False, 'S': True, 'W':False} ],

  [ {'N': True, 'E': True, 'S': False, 'W':False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W': True}, {'N': True, 'E': True, 'S': False, 'W':True},
    {'N': False, 'E': False, 'S': False, 'W':True}, {'N': True, 'E': True, 'S': False, 'W': False}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True},
    {'N': True, 'E': True, 'S': False, 'W':True},{'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True}, {'N': False, 'E': True, 'S': False, 'W':True}, 
    {'N': False, 'E': True, 'S': False, 'W':True}, {'N': True, 'E': False, 'S': False, 'W':True} ]
  
]

def within_range(num):
  return True if num <= 13 and num >= 0 else False

def traverse(node, start = False):
  
  
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
  
  print(node)
  print(row)
  print(column)
  if node['cell'] == [11, 13]:
    return
  elif dead_end:
    try:
      print(' '.join(node['moves']) + f' stuck at ( {row} , {column} )')
      print(f'back to {node['history'][-1]}')
      print('before popping')
      # print(node)
      # node['history'].pop(-1)
      # node['queue'].pop(-1)
      # print('after popping')
      # print(node)
      # print(node['cell'] == [0, 3])
      # if node['cell'] == [0, 3]:
      #   #breakpoint()
      #   pass
    except:
      breakpoint()
    
    if not len(node['moves']) == 0:
      node['moves'].pop() 
  else:
    for i in range(len(node['queue'])):
      new_history = node['history']
      new_history.append(node['cell'])
      new_node = {'cell': node['queue'][-1], 'history': new_history, 'queue': [], 'moves': []}
      #node['cell'] = node['queue'][-1]
      node['queue'].pop(-1)
      traverse(new_node)
      print(' '.join(node['moves']) + f' stuck at ( {row} , {column} )')
      print(f'back to {node['history'][-1]}')

  

node = {'cell': [2, 0], 'history': [], 'queue': [], 'moves': []}
traverse(node)


print(f'Start at ({node['cell'][0]}, {node['cell'][1]})')