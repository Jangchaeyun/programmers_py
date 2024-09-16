def solution(edges):
    def count_edges(edges):
        edges_counts = {}
        for a, b in edges:
            if not edges_counts.get(a):
                edges_counts[a] = [0, 0]
            if not edges_counts.get(b):
                edges_counts[b] = [0, 0]
            
            edges_counts[a][0] += 1
            edges_counts[b][1] += 1
        return edges_counts
    
    def check_answer(edges_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edges_counts.items():
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
        answer[1] = (edge_count[answer[0]][0] - answer[2] - answer[3])
        return answer
    
    edge_count = count_edges(edges)
    answer = check_answer(edge_count)

    return answer