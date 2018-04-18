import math

perc = 1/3
coco_wt = 1450
macaw_wt = 900
macaw_limit = macaw_wt * perc
print(macaw_limit)

num_macaws = coco_wt / macaw_limit

# round up to get full number of birds
print(math.ceil(num_macaws))