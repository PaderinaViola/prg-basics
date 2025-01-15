test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]
cool_students = list(filter(lambda student: 70 > student["result"] > 50, test_results))
print(cool_students)