# public static void dfs(List<List<Integer>> graph, int vertex, boolean[] visited) {
#     visited[vertex] = true;
#     System.out.print(vertex + " ");
#     for (int neighbor : graph.get(vertex)) {
#         if (!visited[neighbor]) {
#             dfs(graph, neighbor, visited);
#         }
#     }
# }