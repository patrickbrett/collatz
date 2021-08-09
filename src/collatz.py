from pyvis.network import Network
import networkx as nx

COLLATZ_DEPTH = 100

COLOR_GREEN = '#3ccf72'
COLOR_BLUE = '#6697cc'
COLOR_PINK = '#cc6697'

"""
Finds the next number in a Collatz sequence.
"""
def next_collatz(n):
  # Halve if even; triple then add one if odd.
  return n >> 1 if n % 2 == 0 else 3 * n + 1

"""
Returns a node or edge color based on the step taken.
"""
def get_color(curr, prev=None):
  if curr == 1:
    return COLOR_GREEN
  elif prev and curr > prev:
    return COLOR_BLUE
  else:
    return COLOR_PINK

"""
Generator to find a sequence of Collatz numbers.
Used for printing out the longest chain.
"""
def find_chain(n):
  while True:
    yield str(n)
    if n == 1:
      break
    n = next_collatz(n)

"""
"""
def print_longest_chain(chain_length_map, n):
  # Identify the max chain length, and print the corresponding chain
  starting_no, max_length = max(chain_length_map.items(), key=lambda x: x[1])
  print(f"Longest chain up with seed <= {n} occurs starting at {starting_no} with length {max_length}:")
  longest_chain = " -> ".join(list(find_chain(starting_no)))
  print(longest_chain)

"""
The main function.
Unfortunately this has two intertwined responsibilities for efficiency reasons:
building the graph, and finding the longest chain.
"""
def generate_graph(n):
  G = nx.DiGraph()

  chain_length = {}
  for i in range(1, n+1):
    if not G.has_node(i):
      G.add_node(i, color=get_color(i))

    curr = i
    iter_count = 0
    while curr > 1:
      iter_count += 1
      # Find next element in sequence and remember previous element
      prev, curr = curr, next_collatz(curr)

      # Iteratively build chain_length map
      if curr in chain_length:
        chain_length[i] = iter_count + chain_length[curr]

      # Add nodes and edges if they don't already exist.
      # These existence checks save a lot of unnecessary node/edge creation.
      if not G.has_node(curr):
        G.add_node(curr, color=get_color(curr, prev))
      if not G.has_edge(prev, curr):
        G.add_edge(prev, curr, color=get_color(curr, prev))

    # If we reach the end of the loop and still don't know the chain length
    # for this starting value, add it now
    if not i in chain_length:
      chain_length[i] = iter_count

  print_longest_chain(chain_length, n)

  return G


if __name__ == '__main__':
  graph = generate_graph(COLLATZ_DEPTH)
  net = Network(notebook=True, directed=True, width="800px", height="800px")
  net.from_nx(graph)
  net.show("output.html")
