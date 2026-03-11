# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
def print_star_names(targets):
    for star in targets:
        print(star)
def print_star_types(targets):
    for star in targets:
        print(star, "-", targets[star]["Spectral Type"])
def print_magnitude_greater_than_point_one(targets):
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(star, "-", targets[star]["Magnitude"])
targets["Altair"] = {
    "RA": "19h 50m 47.0s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}
def dec_to_number(dec_string):
    clean = dec_string.replace("°", " ").replace("′", " ").replace("″", " ")
    clean = clean.replace('"', " ").replace("'", " ")
    parts = clean.split()
    sign = -1 if parts[0][0] == "-" else 1
    degrees = abs(float(parts[0]))
    minutes = float(parts[1])
    seconds = float(parts[2])
    return sign * (degrees + minutes / 60 + seconds / 3600)

def brightest_closest_to_20(targets):
    best_star = None
    best_diff = float("inf")
    best_mag = float("inf")

    for star in targets:
        dec_value = dec_to_number(targets[star]["Dec"])
        diff = abs(dec_value - 20)
        mag = targets[star]["Magnitude"]
        if diff < best_diff or (diff == best_diff and mag < best_mag):
            best_star = star
            best_diff = diff
            best_mag = mag
    return best_star

# 1) Write a function that uses a loop to print the name of each star.
print_star_names(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
print_star_types(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
print_magnitude_greater_than_point_one(targets)
# 4) Look up another target, add all the necessary information to the targets list. 
#done
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
print("Brightest star whose declination is closest to 20°:", brightest_closest_to_20(targets))
# 6) What is your favorite constellation?
print("Sagittarius is by fave constellation bc im a sag...")
