import math

def main():
    
    can_sizes = [
        (6.83, 10.16, 0.28), (7.78, 11.91, 0.43), (8.73, 11.59, 0.45),
        (10.32, 11.91, 0.61), (10.79, 17.78, 0.86), (13.02, 14.29, 0.83),
        (5.40, 8.89, 0.22), (6.83, 7.62, 0.26), (15.72, 17.78, 1.53),
        (6.83, 12.38, 0.34), (7.62, 11.27, 0.38), (8.10, 11.11, 0.42)
    ]

    for size in can_sizes:
        radius, height, cost = size
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(surface_area, volume)
        print(f"\nRadius: {radius}, Height: {height}, Cost: {cost}")
        print(f"Volume: {volume:.2f}, Surface Area: {surface_area:.2f}, Storage Efficiency: {storage_efficiency:.2f}\n")

def compute_volume(radius, height):

    pi_value = math.pi
    volume = pi_value * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):

    pi_value = math.pi
    surface_area = 2 * pi_value * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(surface_area, volume):

    storage_efficiency = volume / surface_area
    return storage_efficiency

main()
