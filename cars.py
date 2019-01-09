showroom = {"camry", "corolla", "outback", "rio"}
# print(len(showroom))
showroom.add("corolla")
# print(showroom)
showroom.update({"accord", "civic"})
# print(showroom)
showroom.discard("camry")
# print(showroom)

junkyard = {"corolla", "corvette", "beetle", "civic", "yaris"}

duplicate_cars = showroom.intersection(junkyard)
print(duplicate_cars)
combined_cars = showroom.union(junkyard)
print(combined_cars)