import locky

# Simple example where we ensure that everyone has joined the bus and bus is ready

people = ["Jack", "Jill", "James", "Virginia"]
bus_status = {'has_driver': False,
              'has_fuel': False}

def join_bus(name:str):
    locker.toggle_lockpick(name)

def add_fuel():
    locker.toggle_lockpick(name = 'has_fuel', status = True)

def add_driver():
    locker.toggle_lockpick(name = 'has_driver', status = True)

def go_to_party():
    if not locker.picklock():
        print("Something isnt ready yet!")
    else:
        print("Everyone is there and bus is ready. Lets go to party!")

locker = locky.Locker()

for person in people:
    locker.add_lockpick(person)

for item in bus_status:
    locker.add_lockpick(name = item, status = bus_status[item])

print(locker.get_lockpicks())
join_bus("Jack")
join_bus("Jill")
add_fuel()
print(locker.get_lockpicks())
go_to_party()

join_bus("James")
join_bus("Virginia")
print(locker.get_lockpicks())
go_to_party()

add_driver()
print(locker.get_lockpicks())
go_to_party()
