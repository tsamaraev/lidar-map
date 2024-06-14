import json
import time
from adafruit_rplidar import RPLidar


PORT_NAME = 'COM3'  


lidar = RPLidar(None, PORT_NAME)

def collect_lidar_data(lidar, num_samples=100):
    """Функция для сбора данных с RPLidar."""
    lidar_data = []
    try:
        for i, scan in enumerate(lidar.iter_scans()):
            for (_, angle, distance) in scan:
                lidar_data.append({'angle': angle, 'distance': distance})
                if len(lidar_data) >= num_samples:
                    return lidar_data
    except KeyboardInterrupt:
        print("Прервано пользователем")
    finally:
        lidar.stop()
        lidar.disconnect()
    return lidar_data


lidar_data = collect_lidar_data(lidar)


for i in range(1, len(lidar_data)):
    if lidar_data[i]['distance'] == 0:
        lidar_data[i]['distance'] = lidar_data[i-1]['distance']


output_path = 'lidar/lidar_data.json'
with open(output_path, 'w') as json_file:
    json.dump(lidar_data, json_file, indent=4)

print(f"Обработанные данные LiDAR сохранены в {output_path}")