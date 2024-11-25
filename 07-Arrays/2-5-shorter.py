# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats): #in the place of seats will be cinema_seats
    return sum(len(row) for row in seats)

def seats_available(seats):
   return sum(row.count('A') for row in seats)

def seats_booked(seats):
   return sum(row.count('B') for row in seats)

def seat_status(seats, row, place):
   ...
   ...
   return ...

print('CINEMA INFORMATION TABLE')
print('Total seats:',...)
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', ...)
print('Seat in row 5, place 5:', ...)
print('Seat in row 3, place 5:', ...)