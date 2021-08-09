from pyvis.network import Network
import networkx as nx

COLLATZ_DEPTH = 100


def next_collatz(n):
  return n >> 1 if n % 2 == 0 else 3 * n + 1


def get_color(n, prev):
  if n == 1:
    return '#3ccf72'
  return '#6697cc' if n > prev else '#cc6697'


def find_chain(n):
  while True:
    yield str(n)
    if n == 1:
      break
    n = next_collatz(n)


def generate_graph(n):
  G = nx.DiGraph()

  chain_length = { 1: 1 }
  for i in range(1, n+1):
    if not G.has_node(i):
      G.add_node(i, color=get_color(i, i*2))
    curr = i
    iter_count = 0
    while curr > 1:
      iter_count += 1
      prev, curr = curr, next_collatz(curr)

      if curr in chain_length:
        chain_length[i] = iter_count + chain_length[curr]

      if not G.has_node(curr):
        G.add_node(curr, color=get_color(curr, prev))
      if not G.has_edge(prev, curr):
        G.add_edge(prev, curr, color=get_color(curr, prev))

    if not i in chain_length:
      chain_length[i] = iter_count

  starting_no, max_length = max(chain_length.items(), key=lambda x: x[1])
  print(f"Longest chain up with seed <= {n} occurs starting at {starting_no} with length {max_length}:")
  longest_chain = " -> ".join(list(find_chain(starting_no)))
  print(longest_chain)

  return G


if __name__ == '__main__':
  graph = generate_graph(COLLATZ_DEPTH)
  net = Network(notebook=True, directed=True, width="1600px", height="1200px")
  net.from_nx(graph)
  net.show("output.html")
