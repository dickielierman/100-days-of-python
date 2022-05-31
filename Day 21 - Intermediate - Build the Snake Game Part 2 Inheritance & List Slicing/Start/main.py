class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        lungs = ['inhale', 'exhale']
        print(lungs)


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("Flippy flappy splishy splashy!")
    def breath(self):
        super().breath()
        print("But underwater")

nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breath()