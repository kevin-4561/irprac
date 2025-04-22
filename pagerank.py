graph={
    'A':['B','C'],
    'B':['C','D'],
    'C':['A','D'],
    'D':['B']
    }

ranks={p:1/len(graph)for p in graph}
d=0.85

for _ in range(10):
    new_ranks={}
    for page in graph:
        rank=(1-d)/len(graph)
        for other in graph:
            if page in graph[other]:
                rank +=d*ranks[other]/len(graph[other])
        new_ranks[page]=rank
    ranks=new_ranks
for p in sorted(ranks):
    print(f"{p}:{ranks[p]:.4f}")
