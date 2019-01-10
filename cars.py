# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.

showroom = {"camry", "corolla", "outback", "rio"}
# print(len(showroom))
showroom.add("corolla")
# print(showroom)
showroom.update({"accord", "civic"})
# print(showroom)
showroom.discard("camry")
# print(showroom)

junkyard = {"corolla", "corvette", "beetle", "civic", "yaris"}

print(showroom)
print(junkyard)
duplicate_cars = showroom.intersection(junkyard)
print(duplicate_cars)
combined_cars = showroom.union(junkyard)
print(combined_cars)
cars_to_discard = set()

# if the junkyard is in the duplicate cars set then that means we don't want to put it in our showroom. It needs to stay in the junkyard. If it's not a duplicate then it will go into the showroom so it needs to be removed from the junkyard.
# iterate over the junkyard set, if the junkcar is in the duplicate set continue and do nothing, if it's not then add it to the cars_to_discard set. The iterate over the cars_to_discard and remove each one from the junkyard.
for junk_car in junkyard:
  if junk_car in duplicate_cars:
    continue
  else:
    cars_to_discard.add(junk_car)

for car in cars_to_discard:
  junkyard.discard(car)

print(cars_to_discard)
print(junkyard)


