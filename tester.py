from geo.utils import distance, area_circle

if __name__ == "__main__":
    c = distance((0, 0), (3, 4))        
    area = area_circle(10)          
    print(f"c = {c}")
    print(f"area = {area}")
