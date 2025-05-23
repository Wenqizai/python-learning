metro_areas = [
    ("Tokyo", "JP", 36.933, (35.681236, 139.770366)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.432607, -99.133209)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f"{'':15} | {'latitude':>9} | {'longitude':>9}")
    for name, _, _, (latitude, longitude) in metro_areas:
        if longitude < 0:
            print(f"{name:15} | {latitude:9.4f} | {longitude:9.4f}")

if __name__ == "__main__":
    main()
