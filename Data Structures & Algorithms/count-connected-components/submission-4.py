class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edges.sort()
        component_id = 0
        node_to_component = {}
        merged_components = set()
        seen = 0

        for edge in edges:
            if edge[0] in node_to_component:
                if edge[1] in node_to_component:
                    # merge
                    if node_to_component[edge[0]] != node_to_component[edge[1]]:
                        merged_components.add(node_to_component[edge[0]])
                        merged_components.add(node_to_component[edge[1]])
                else:
                    node_to_component[edge[1]] = node_to_component[edge[0]]
                    seen += 1
            elif edge[1] in node_to_component:
                node_to_component[edge[0]] = node_to_component[edge[1]]
                seen += 1
            else:
                # new component
                node_to_component[edge[0]] = component_id
                node_to_component[edge[1]] = component_id
                component_id += 1
                seen += 2

        print(node_to_component)
        print(merged_components)
        print(seen)
        if len(merged_components) > 0:
            deduct = len(merged_components) - 1
        else:
            deduct = 0
        return component_id - deduct + (n - seen)