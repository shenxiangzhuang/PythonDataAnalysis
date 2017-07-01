class Person:
    has_hair = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhello(self, words):
        print("Hello, I'm", self.name)
        print(words)


if __name__ == '__main__':
    Sally = Person('Sally', 20)
    Sally.sayhello("Nice to meet you")

    Tom = Person('Tom', 19)
    Tom.sayhello("Nice to meet you too")
