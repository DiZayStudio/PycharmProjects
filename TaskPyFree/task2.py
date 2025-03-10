HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

# tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(today)
    print(tomorrow)
    print(other)
  elif command == "add":
    date = input("Введите дату: ")
    task = input("Введите название задачи: ")
    if date == "Сегодня":
      today.append(task)
    elif date == "Завтра":
      tomorrow.append(task)
    else:
      other.append(task)

    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Неизвестная команда")
    break

print("До свидания!")