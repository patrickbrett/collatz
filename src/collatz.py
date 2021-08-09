from pyvis.network import Network
import networkx as nx

def next_collatz(n):
  return n >> 1 if n % 2 == 0 else 3 * n + 1

def generate_graph(n):
  G = nx.DiGraph()
  for i in range(1, n+1):
    if not G.has_node(i):
      G.add_node(i)
    curr = i
    while curr > 1:
      prev, curr = curr, next_collatz(curr)
      if not G.has_node(curr):
        G.add_node(curr)
      G.add_edge(prev, curr)

  return G

CHECK_COUNT = 100

if __name__ == '__main__':
  graph = generate_graph(CHECK_COUNT)
  net = Network(notebook=True, directed=True)
  net.from_nx(graph)
  net.show("output.html")
