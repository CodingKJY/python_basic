class Grand:
    def __init__(self) -> None:
        print("Grand __init__()")

class Parent(Grand):
    def __init__(self) -> None:
        super().__init__()
        print("Parent __init__()")

class Children(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("Children __init__()")

c = Children()