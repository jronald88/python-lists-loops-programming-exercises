parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(matrix):
  parking_dict = {"total_slots": 0, "available_slots": 0, "occupied_slots": 0}
  for i in range(len(matrix)):
    
      for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
          parking_dict["occupied_slots"] += 1
          parking_dict["total_slots"] += 1
        elif matrix[i][j] == 2:
          parking_dict["available_slots"] += 1
          parking_dict["total_slots"] += 1
  return parking_dict

print(get_parking_lot(parking_state))         
