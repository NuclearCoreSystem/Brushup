to_do_list = []

while True:
    task = input("Enter a task (or 'done' if you're...well.):")

    if task == 'done':
        break
    else:
        to_do_list.append(task)

print("Your tasks are:")
for task in to_do_list:
    print(task)
