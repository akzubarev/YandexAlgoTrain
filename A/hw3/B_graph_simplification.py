if __name__ == '__main__':
    with open('multigraph.in', 'r') as fin:
        nodes, edges_num = map(int, fin.readline().split())
        edges = set()
        for i in range(edges_num):
            from_, to_ = map(int, fin.readline().split())
            if from_ != to_:
                from_, to_ = min(from_, to_), max(from_, to_)
                edges.add((from_, to_))

    print(nodes, len(edges))
    for e in edges:
        print(f"{e[0]} {e[1]}")
