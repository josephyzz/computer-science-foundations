from collections import deque

grafos = {}
grafos["I"] = ["A", "B"]
grafos["A"] = ["C", "F"]
grafos["B"] = ["C", "D"]
grafos["D"] = ["F"]


search_queue = deque()
verified = []
for item in grafos:
    search_queue.append(grafos[item])


print(search_queue)
