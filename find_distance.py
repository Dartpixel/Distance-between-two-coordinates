from geopy.distance import geodesic

initial_location = eval(
    input("Enter the initial location latitides and longitudes: "))
final_location = eval(
    input("Enter the final location latitides and longitudes: "))

distance = geodesic(initial_location, final_location).kilometers

print("Distance between the locations is ", distance, "kilometers")
