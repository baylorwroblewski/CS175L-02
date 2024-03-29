#Bestsellers
#Baylor, Shabbar, Ty
#CS 175 L
def create_booklist(filename):
    with open(filename, 'r') as book_list:
        booklist = []
        for line in book_list:
            data = line.strip().split('\t')
            if len(data) == 5:
                title, author, publisher, date, category = data
                booklist.append(data)

        return booklist

def print_books(book):
    print(f"{book[0]} by: {book[1]} (pub date: {book[3]})")

def search_author(books, author):
    for book in books:
        if author.lower() in book[1].lower():
            print_books(book)
    menu()
    
def search_title(books, title):
    for book in books:
        if title.lower() in book[0].lower():
            print_books(book)

    menu()
def search_yearRange(books, year1, year2):
    found = False
    for book in books:
        date = book[3].split('/')
        year = book[3][-4:]
        year = int(year)
        if year1 <= year <= year2:
            found = True
            print_books(book)
    if not found:
            print("No books found for this search.")
            
def search_specificDate(books, month, year):
    found = False
    for book in books:
        date = book[3].split('/')
        month1, day1, year1 = date
        month_g = month1
        year_g = year1
        month_g = int(month_g)
        year_g = int(year_g)
        if month == month_g and year == year_g:
            found = True
            print_books(book)
    if not found:
        print("No books found for this search.")
    menu()
def menu():
    try:
        books = create_booklist('bestsellers.txt')
    except IOError:
        print("Error: Could not read from file")
        return False
    again = True
    print("\nWhat would you like to do?")
    print("\t1. Display all books in a year range")
    print("\t2. Display all books in a specific month and year")
    print("\t3. Search for an author")
    print("\t4. Search for a title")
    print("\tQ. Quit")
    option = input("\tOption: ")
    if option == "1":
        year1 = int(input("Enter Year 1: "))
        year2 = int(input("Enter Year 2: "))
        search_yearRange (books, year1, year2)
    if option =="2":
        month = int(input("Enter Month (1-12): "))
        year = int(input("Enter Year: "))
        search_specificDate (books, month, year)
    if option == "3":
        author = input("Author: ")
        search_author(books, author)
    elif option == "4":
        title = input("Title: ")
        search_title(books, title)
    elif option == "Q" or option == "q":
        print("Done")
        return again == False
    else:
        print("I don't understand this command.")
        menu()
    while again == False:
        return None


def main():
    menu()
              
if __name__ == '__main__':
    main()

