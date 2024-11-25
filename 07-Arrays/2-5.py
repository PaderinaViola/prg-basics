# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]
if cinema_seats[1][1] == 'A':
    print("available")

def seats_total(seats): #in the place of seats will be cinema_seats
    return sum(len(row) for row in seats)

def seats_available(seats):
   available = 0
   for row in seats:
      for item in row:
            if item == 'A':
                available +=1
   return available

def seats_booked(seats):
   booked = 0
   for row in seats:
      for item in row:
            if item == 'B':
                booked +=1
   return booked

def seat_status(seats, row, place):
   if seats[row][place] == 'A':
       return "available"
   elif seats[row][place] == 'B':
       return "booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 0, 0))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 4, 4))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 2, 4))