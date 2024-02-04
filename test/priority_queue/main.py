from src.controller.PriorityQueue import PriorityQueue

p = PriorityQueue([(-10, (10, 5)), (2, 5), (3, 15)])
p.update_priority((10, 5), 1)
p.put((1.5, (20, 20)))
p.put((1.5, (20, 21)))
print(p.get())
