library = {}

while True:
    print("-- Library Management System --")
    print("1️⃣ Add Book")
    print("2️⃣ Display Books")
    print("3️⃣ Borrow Book")
    print("4️⃣ Return Book")
    print("5️⃣ Exit")

    choice = input("Enter your choice: ").strip()
    print(choice)

    if choice == "1":
        title = input("Enter book title: ").strip()
        print(title)
        copies = int(input("Enter number of copies: "))

        if title in library:
            library[title] += copies  # Increase copies if book exists
        else:
            library[title] = copies  # Add new book

        print(f'✅ "{title}" added successfully!')
        
    elif choice == "2":
        if not library:
            print("📖 No books available.")
            
        print("\n\n\n📚 Available Books:")
        for title, copies in library.items():
            print(f"📖 {title} - {copies} copies\n\n\n")
            
    elif choice == "3":
        title = input("Enter the book title you want to borrow: ").strip()

        if title in library and library[title] > 0:
            library[title] -= 1  # Reduce book copy count
            print(f'✅ You borrowed "{title}". Enjoy reading!')
        else:
            print("❌ Book not available!")

    elif choice == "4":
        title = input("Enter the book title you are returning: ").strip()

        if title in library:
            library[title] += 1  # Increase book count
        else:
            library[title] = 1  # Add book if it was not in system

        print(f'✅ Thank you for returning "{title}".')

    elif choice == "5":
        print("📚 Thank you for using the Library System!\n\n\n")
        break

    else:
        print("❌ Invalid choice! Please select a valid option.")