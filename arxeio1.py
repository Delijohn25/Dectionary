students = {
    "Chris": {"age": 23, "lessons": ["HTML", "CSS"]},
    "Panos": {"age": 25, "lessons": ["Python", "C++"]},
    "Mike": {"age": 18, "lessons": ["JS", "react"]},
}

students["Stam"] = {"age": 19, "lessons": ["sql", "HTML"]}

for name, info in students.items():
    print(f"mathiths: {name}, hlikia: {info['age']}, mathimata:{','.join(info['lessons'])}")