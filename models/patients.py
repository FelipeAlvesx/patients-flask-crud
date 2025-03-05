class Patient:
    def __init__(self, id, name, age, description, room, discharge=False) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.description = description
        self.room = room
        self.discharge = discharge
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "description": self.description,
            "room": self.room,
            "discharge": self.discharge,
        }