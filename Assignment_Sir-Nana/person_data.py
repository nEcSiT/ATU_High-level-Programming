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

    def greeting(self):
        """Display a personalized greeting with key information"""
        return (
            f"Hello, {self.name}!\n"
            f"You are {self.age} years old, love the color {self.color}, and enjoy eating {self.food}.\n"
            f"Life must be awesome in {self.city}!"
        )

    def summary(self):
        """Display complete detailed summary"""
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

    def display_all(self):
        """Display greeting first, then detailed summary"""
        print("\n" + "🎉" * 20)
        print(self.greeting())
        print("🎉" * 20)
        print("\n📋 Here are your complete details:")
        print("-" * 40)
        print(self.summary())
        print("-" * 40)
