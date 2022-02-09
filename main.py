import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 15
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print(cost_per_class, type(cost_per_class))
print("You are paying $", cost_per_class, " for every class you take! That is very cheap!")
#Part B
list_of_objects = [1,"aviva", 4.66, 7, "hi"]
random_object = random.choice(list_of_objects)
print(random_object)