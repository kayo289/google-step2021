from collections import deque

def get_key(val, my_dict):
    """
    Return the key based on the value
    Args:
       val : dict val
       my_dict : dict
    Returns:
       key: The key that corresponds to val
    """
    for key, value in my_dict.items():
         if val == value:
             return key
    return None

def filter_notsame(list_path):
    filter_path = []
    for item in list_path:
        if item[0] != item[1]:
            filter_path.append(item)
    return filter_path

def get_ans_path(history, start_id, end_id):
    """
    Obtain the path of the shortest path from the search history.
    Args:
        history : Search history
        start_id : start id
        end_id : end id
    Returns:
        Path : Path from start to end
    """
    path = []
    history = filter_notsame(history)
    target = history[-1][0]
    path.insert(0,end_id)
    path.insert(0,target)
    while target != -1 and target != end_id:
        for item in history:
            if item[1] == target:
                path.insert(0,item[0])
                target = item[0]
                break
    if target == -1:
      return path[1:]
    else:
      return path

def read_pages():
  pages = {}
  sign = {}
  with open('data/pages_small.txt') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]
      sign[page[0]] = -1
  return pages,sign

def read_links():
  links = {}
  with open('data/links_small.txt') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}
  return links

def bfs(sign, pages, links, start_id, end_id):
  """
    bfs
    Args:
        sign : checked list
        pages : The id and the page correspond.
        links : links list
        start_id : start id
        end_id : end id
    Returns:
        Path : search history list
  """
  history = []
  found = 0
  queue = deque()
  queue.append(start_id)
  history.append([-1,start_id])
  while queue:
      node = queue.popleft()
      if node in links.keys():
          nears = links[node]
      else:
          continue
      for near in nears:
          history.append([node,near]) #[mother, child]
          if near == end_id:
             print("??? found!!")
             found = 1
             break
          if sign[near] == -1: # not checked
              queue.append(near)
              sign[near] = 1
      if found == 1:
          break
  if found == 0:
      print("??????  not link path")
      exit(1)
  else:
      return history

def print_path(pages, path):
  for i in range(len(path)):
    if i == len(path) - 1:
      print(pages[path[i]])
    else:
      print(pages[path[i]]+"->",end="")

def main(start_name, end_name):
  pages,sign = read_pages()
  links = read_links()
  history = []
  start_id = get_key(start_name, pages)
  end_id = get_key(end_name, pages)
  if start_id == None or end_id == None:
      print("??????  start or end does not exist")
      exit(1)
  history = bfs(sign, pages, links, start_id, end_id)
  path = get_ans_path(history, start_id, end_id)
  print_path(pages, path)

if __name__ == '__main__':
  main("Google","?????????")
