from pprint import pprint

file_path = 'lidar/lidar_data.txt'

lidar_data = []

with open(file_path, 'r') as file:
    for line in file:
        angle, distance = map(float, line.split())
        lidar_data.append({'angle': angle, 'distance': distance})

for i in range(1, len(lidar_data)):
    if lidar_data[i]['distance'] == 0:
        lidar_data[i]['distance'] = lidar_data[i-1]['distance']

pprint(lidar_data)
