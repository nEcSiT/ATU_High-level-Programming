class MyData:
    def __init__(self, name, age, color, food, city, shs, soccer_team, hobbies, dream_job):
        self.name = name
        self.age = age
        self.color = color
        self.food = food
        self.city = city
        self.shs = shs
        self.soccer_team = soccer_team
        self.hobbies = hobbies
        self.dream_job = dream_job

    def summary(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Favorite Color: {self.color}\n"
            f"Favorite Food: {self.food}\n"
            f"City: {self.city}\n"
            f"SHS Attended: {self.shs}\n"
            f"Favorite Soccer Team: {self.soccer_team}\n"
            f"Hobbies: {self.hobbies}\n"
            f"Dream Job: {self.dream_job}"
        )
