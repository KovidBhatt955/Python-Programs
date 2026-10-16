import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('Lebron James', 5, 48.5), ('Kobe Bryant', 6, 52.5), ('Michael Jordan', 5, 42.10), ('Sam May', 5, 40.11)]
# Create a structured array
students = np.array(students_details, dtype=data_type)
print("Original Array:")
print(students)
print("Sort by Height:")
print(np.sort(students, order='height'))