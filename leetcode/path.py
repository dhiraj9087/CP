def main():
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    # max_vertex = max(max(edge) for edge in edges) + 1
    # a=[[] for _ in range(max_vertex)]
    a={}
    for i in range(len(edges)):
        u,v=edges[i]

        a[u].append(v)
        a[v].append(u)
    print(a[source],a)
    # for i in a[source]:
    #     if i==destination:
    #         print("Y")
    #         return

main()