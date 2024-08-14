class LibraryItem:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0

    def increment_play_count(self):
        self.play_count += 1

    def info(self):
        return f"{self.name} - {self.director} {'*' * self.rating}"

    def stars(self):
        return '*' * self.rating