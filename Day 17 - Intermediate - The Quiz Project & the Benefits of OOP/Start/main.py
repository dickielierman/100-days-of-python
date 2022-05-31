class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def print_user(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")


dickie = User('001', "Dickie")
kari = User('002', "Kari")
dickie.print_user()
kari.print_user()
dickie.follow(kari)
dickie.print_user()
kari.print_user()
