#breakpoint() - stops coded execution and enters the Python debugger (Pdb)
#l - list surrounding lines
#ll - list more surrounding lines
#n
#c

number_of_floors = int(input("Number of floors: "))
rooms_per_floor = int(input("Rooms per floor: "))

total_guests = 0
room_records = []

for floor in range(1,number_of_floors + 1):
    for room in range(1,rooms_per_floor + 1):
        guests = int(input(f"Floor {floor}, Room {room} - enter the number of guests: "))     
        print(f"Floor {floor}, Room {room} - enter number of guests: {guests}")                
        total_guests += guests
        room_records.append((floor,room,guests))

print(room_records)

print ("\nHOTEL ROOM SUMMARY\n")
for floor, room, guest in (room_records):
    print(f"Floor {floor} | Room {room} | Guest {guest}")

print(f"\nTotal number of guests: {total_guests}")

print ("\nHOTEL ROOM SUMMARY\n")

print(f"{"FLOOR":<6}{"ROOM":<6}{"GUESTS":<6}")
print("-" * 18)
for floor, room, guest in (room_records):
    print(f"{floor:<6}{room:<6}{guest:<6}")
       

