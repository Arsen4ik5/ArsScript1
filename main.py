while True:
    print("Выберите действие:")
    print("1 - Калькулятор +")
    print("2 - Калькулятор -")
    print("3 - Калькулятор *")
    print("4 - Калькулятор /")
    print("5 - Сколько вам осталось жить")
    print("6 - Квест")
    print("0 - Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
        import cplus
    elif choice == '2':
        import cminus
    elif choice == '3':
        import cmultipe
    elif choice == '4':
        import cdelit
    elif choice == '5':
        import skolkoostalosjit
    elif choice == '6':
        import kvest
    elif choice == '0':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
