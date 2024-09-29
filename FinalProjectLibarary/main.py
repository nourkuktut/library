import os
import self as self
self.fout1 = open('cat1.txt', 'a')
self.fout2 = open('cat2.txt', 'a')
self.fout3 = open('cat3.txt', 'a')
self.fout4 = open('cat4.txt', 'a')
self.fout11 = open('book1.txt', 'a')
self.fout12 = open('book2.txt', 'a')
self.fout13 = open('book3.txt', 'a')
self.fout14 = open('book4.txt', 'a')


# *********************************Main screen**************************************************************

def fun1():
    print("^^" * 9 + " Welcome in Books Library ".center(10) + "^^" * 9)
    print("1 - Create Category")
    print("2 - Show Categories")
    print("3 - Exit")

    # ************************************show_category_menu()**********************************************

    def show_category_menu():
        print("^^" * 9 + "Category Menu".center(10) + "^^" * 9)
        print("1-Create New Book ")
        print("2- Show Category Books")
        print("3- Delete Category Books")
        print("4- Exit Main Menu")

        try:
            category_menu_option = int(input("Enter your choice: "))
            if category_menu_option == 1:
                if category_option == 1:
                    print("^^" * 9 + "Create New Book:".center(10) + "^^" * 9)
                    book_name1 = input("Enter the book name: ")
                    book_author1 = input("Enter the book author: ")
                    try:
                     book_pages1 =int(input("Enter the number of pages to the book: "))
                    except ValueError:
                        print("'This is Not Number,Please Enter Number ^^'")
                        book_pages1 = int(input("Enter the number of pages to the book: "))
                    self.fout11.writelines(
                        f"book_name:{book_name1}\nbook_author:{book_author1}\nbook_pages:{book_pages1}\n")
                    self.fout11 = open('book1.txt', 'r')
                    try:
                       filesize11 = os.path.getsize("book1.txt")
                       if filesize11 != 0:
                           print(book_name1 + "  'Book created successfully'")
                           show_category_menu()
                    except FileNotFoundError:
                        print("Sorry the operation failed,try again")

                elif category_option == 2:
                    print("^^" * 9 + "Create New Book:".center(10) + "^^" * 9)
                    book_name2 = input("Enter the book name: ")
                    book_author2 = input("Enter the book author: ")
                    try:
                      book_pages2 =int(input("Enter the number of pages to the book: "))
                    except ValueError:
                        print("'This is Not Number,Please Enter Number ^^'")
                        book_pages2 = int(input("Enter the number of pages to the book: "))
                    self.fout12.writelines(
                        f"book_name:{book_name2}\nbook_author:{book_author2}\nbook_pages:{book_pages2}\n")
                    self.fout12 = open('book2.txt', 'r')
                    try:
                       filesize12 = os.path.getsize("book2.txt")
                       if filesize12 != 0:
                           print(book_name2 + "  'Book created successfully'")
                           show_category_menu()
                    except FileNotFoundError:
                        print("Sorry the operation failed,try again")

                elif category_option == 3:
                    print("^^" * 9 + "Create New Book:".center(10) + "^^" * 9)
                    book_name3 = input("Enter the book name: ")
                    book_author3 = input("Enter the book author: ")
                    try:
                     book_pages3 = int(input("Enter the number of pages to the book: "))
                    except ValueError:
                        print("'This is Not Number,Please Enter Number ^^'")
                        book_pages3 = int(input("Enter the number of pages to the book: "))
                    self.fout13.writelines(
                        f"book_name:{book_name3}\nbook_author:{book_author3}\nbook_pages:{book_pages3}\n")
                    self.fout13 = open('book3.txt', 'r')
                    try:
                       filesize13 = os.path.getsize("book3.txt")
                       if filesize13 != 0:
                           print(book_name3 + "  'Book created successfully'")
                           show_category_menu()
                    except FileNotFoundError:
                        print("Sorry the operation failed,try again")

                elif category_option == 4:
                    print("^^" * 9 + "Create New Book:".center(10) + "^^" * 9)
                    book_name4 = input("Enter the book name: ")
                    book_author4 = input("Enter the book author: ")
                    try:
                     book_pages4 =int(input("Enter the number of pages to the book: "))
                    except ValueError:
                        print("'This is Not Number,Please Enter Number ^^'")
                        book_pages4 = int(input("Enter the number of pages to the book: "))
                    self.fout14.writelines(
                        f"book_name:{book_name4}\nbook_author:{book_author4}\nbook_pages:{book_pages4}\n")
                    self.fout14 = open('book4.txt', 'r')
                    try:
                       filesize14 = os.path.getsize("book4.txt")
                       if filesize14 != 0:
                           print(book_name4 + "  'Book created successfully'")
                           show_category_menu()
                    except FileNotFoundError:
                        print("Sorry the operation failed,try again")
            # ****************************************************************************************************
            # method show_category_books()
            elif category_menu_option == 2:
                show_category_books()
                show_category_menu()

            # ****************************************************************************************************
            # method delted books
            elif category_menu_option == 3:

                if category_option == 1:
                    filesize11 = os.path.getsize("book1.txt")
                    if filesize11 == 0:
                        print("Books empty^")
                        show_category_menu()
                    else:
                        self.fout11 = open("book1.txt", "w")
                        print("'Book delete successfully'")
                        show_category_menu()

                elif category_option == 2:
                    filesize12 = os.path.getsize("book2.txt")
                    if filesize12 == 0:
                        print("Books empty^")
                        show_category_menu()
                    else:
                        self.fout12 = open("book2.txt", "w")
                        print("'Book delete successfully'")
                        show_category_menu()

                elif category_option == 3:
                    filesize13 = os.path.getsize("book3.txt")
                    if filesize13 == 0:
                        print("Books empty^")
                        show_category_menu()
                    else:
                        self.fout13 = open("book3.txt", "w")
                        print("'Book delete successfully'")
                        show_category_menu()

                elif category_option == 4:
                    filesize14 = os.path.getsize("book4.txt")
                    if filesize14 == 0:
                        print("Books empty^")
                        show_category_menu()
                    else:
                        self.fout14 = open("book4.txt", "w")
                        print("'Book delete successfully'")
                        show_category_menu()
            # ****************************************************************************************************
            elif category_menu_option == 4:
                fun1()
            # ****************************************************************************************************
            else:
                print("Please choose a category between 1-4 ^^")
                show_category_menu()

        except ValueError:
            print("This is not Number^^")
            show_category_menu()
    # **************************************show_category_books()**********************************************************

    def show_category_books():
        if category_option == 1:
           print("================= Books =================")
           filesize11 = os.path.getsize("book1.txt")
           if filesize11 == 0:
               print("Not Books yet ^^")
           else:
              self.fout11 = open("book1.txt", "r")
              print(f"{self.fout11.read()}")

        elif category_option == 2:
           print("================= Books =================")
           filesize12 = os.path.getsize("book2.txt")
           if filesize12 == 0:
               print("Not Books yet ^^")
           else:
              self.fout12 = open("book2.txt", "r")
              print(f"{self.fout12.read()}")

        elif category_option == 3:
           print("================= Books =================")
           filesize13 = os.path.getsize("book3.txt")
           if filesize13 == 0:
               print("Not Books yet ^^")
           else:
              self.fout13 = open("book3.txt", "r")
              print(f"{self.fout13.read()}")

        elif category_option == 4:
            print("================= Books =================")
            filesize14 = os.path.getsize("book4.txt")
            if filesize14 == 0:
                print("Not Books yet ^^")
            else:
                self.fout14 = open("book4.txt", "r")
                print(f"{self.fout14.read()}")
    # *************************************************************************************************************************
    try:

        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            print("*You are allowed to enter four categories* ")
            categories1 = str(input("Enter your Categories1 : "))
            self.fout1.writelines(f"{categories1}".strip())
            categories2 = str(input("Enter your Categories2 : "))
            self.fout2.writelines(f"{categories2}".strip())
            categories3 = str(input("Enter your Categories3 : "))
            self.fout3.writelines(f"{categories3}".strip())
            categories4 = str(input("Enter your Categories4 : "))
            self.fout4.writelines(f"{categories4}".strip())
            filesize1 = os.path.getsize("cat1.txt")
            filesize2 = os.path.getsize("cat2.txt")
            filesize3 = os.path.getsize("cat3.txt")
            filesize4 = os.path.getsize("cat4.txt")
            print("'categories created successfully'")
            fun1()

        # ****************************************************************************************************
        # method show categories:

        elif choice1 == 2:
            print("^^" * 9 + "Categories".center(10) + "^^" * 9)
            filesize1 = os.path.getsize("cat1.txt")
            filesize2 = os.path.getsize("cat2.txt")
            filesize3 = os.path.getsize("cat3.txt")
            filesize4 = os.path.getsize("cat4.txt")
            if filesize1 or filesize2 or filesize3 or filesize4 != 0:
                self.fil1 = open("cat1.txt", "r");
                print(f"'1-{self.fil1.read()}'")
                self.fil2 = open("cat2.txt", "r");
                print(f"'2-{self.fil2.read()}'")
                self.fil3 = open("cat3.txt", "r");
                print(f"'3-{self.fil3.read()}'")
                self.fil4 = open("cat4.txt", "r");
                print(f"'4-{self.fil4.read()}'")
                category_option = int(input("Enter category choice: "))
                # ****************************************************************************************************
                if category_option == 1:
                    self.fil1 = open("cat1.txt", "r");
                    print(f"1-{self.fil1.read()}")
                    show_category_menu()

                elif category_option == 2:
                    self.fil2 = open("cat2.txt", "r");
                    print(f"2-'{self.fil2.read()}'")
                    show_category_menu()

                elif category_option == 3:
                    self.fil3 = open("cat3.txt", "r");
                    print(f"3-'{self.fil3.read()}'")
                    show_category_menu()

                elif category_option == 4:
                    self.fil4 = open("cat4.txt", "r");
                    print(f"4-'{self.fil4.read()}'")
                    show_category_menu()

                else:
                    print(" Please choose a category between 1-4 ^^'")
                    show_category_menu()

            else:
                print("Not category yet ")
                fun1()


        elif choice1 == 3:
            print("'Thank you for using the program , good luck ^^'")
            exit()
            self.fout.close()

        else:
            print("' Please choose a number between 1-3 ^^'")
            fun1()

    except ValueError:
        print("'This is Not Number,Please Enter Number ^^'")
        fun1()


fun1()

