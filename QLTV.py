# Siêu nhân lập trình web
# Học phần 1

# Kiến thức cần đạt
# Học sinh biết đặt tên biến, phân biệt kiểu dữ liệu
# Học sinh biết cách sử dụng print() và kết hợp với \n, \t, end = “”, * chuỗi
# Học sinh biết cách sử dụng input() và ép kiểu dữ liệu
# Học sinh biết cách sử dụng cấu trúc rẽ nhánh if – elif – else
# Học sinh biết cách sử dụng vòng lặp while, for kết hợp với continue và break 
# Học sinh biết cách sử dụng String với upper(), lower(), replace(), find(), capitalize(), split(), len()....
# Học sinh biết cách sử dụng list []: len(), append(), insert(), extend(), remove(), del()

# Cách đặt tên biến
# Tên của biến chỉ chứa các chữ cái, số và ‘_’
# Tên của biến không được bắt đầu bằng số
# Tên biến không được trùng với các từ khóa của Python như: and, as, else, if, elif, not, or,...
# Tên biến trong Python có phân biệt chữ in hoa và in thường.

# Một trong số kiểu dữ liệu phổ biến nhất là:
# Số nguyên (integer): là một loại dữ liệu số vô hướng, ví dụ như 1, 2, 3, 4, 5.
# Số thực (float): là một loại dữ liệu số có dấu thập phân, ví dụ như 1.5, 2.7, 3.14.
# Chuỗi (string): là một loại dữ liệu chứa một chuỗi ký tự, ví dụ như "hello", "goodbye".
# Boolean: là một loại dữ liệu có hai giá trị là True hoặc False.
# Danh sách (list): là một loại dữ liệu chứa một tập hợp các giá trị, ví dụ như [1, 2, 3, 4, 5].
# Từ điển (dictionary): là một loại dữ liệu chứa các cặp khóa-giá trị, ví dụ như {"name": "John", "age": 30}.

# Quản lý thư viện

# Du lieu sach mac dinh
library_books = [
    {"id": 1, "name": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "name": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 3, "name": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "name": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 6, "name": "Moby Dick", "author": "Herman Melville", "year": 1851},
    {"id": 7, "name": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
]
# Tai khoan & mat khau mac dinh
USERNAME = "admin"
PASSWORD = "abc@123"

# Ham dang nhap voi gioi han 3 lan thu
def login():
    print("\n\t===== DANG NHAP HE THONG QUAN LY =====\n")
    attempts = 3  # Gioi han so lan dang nhap
    while attempts > 0:
        username = input("Nhap ten dang nhap: ").lower().strip()  # Dung lower() va strip()
        password = input("Nhap mat khau: ").strip()
        
        if username == USERNAME and password == PASSWORD:
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Sai ten dang nhap hoac mat khau. Ban con {attempts} lan thu.\n")
            else:
                print("Ban da nhap sai qua nhieu lan. Dang nhap that bai.\n")
    return False

# Ham hien thi thong tin cua tung cuon sach
def view_book_info():
    try:
        book_id = int(input("Nhap ID cua sach: ").strip())  # Ep kieu int
        found = False
        for book in library_books:
            if book["id"] == book_id:
                print(f"Thong tin sach (ID: {book_id}):\n")
                print(f"\tTen sach: {book['name'].capitalize()}") 
                print(f"\tTac gia: {book['author']}")
                print(f"\tNam xuat ban: {book['year']}")
                words = book['name'].split()  # Tách tên sách thành các từ
                print(f"\tCac tu trong ten sach la:", words)
                found = True
                break
        if not found:
            print("Khong tim thay sach voi ID da nhap.\n")
    except ValueError:
        print("ID phai la so nguyen. Vui long thu lai.\n")

# Ham them sach moi
def add_book():
    new_name = input("Nhap ten sach moi: ").strip().title()  # title() de viet hoa moi tu
    new_author = input("Nhap tac gia: ").strip()
    try:
        new_year = int(input("Nhap nam xuat ban: ").strip())  # Ep kieu int
        new_id = len(library_books) + 1
        library_books.append({
            "id": new_id,
            "name": new_name,
            "author": new_author,
            "year": new_year
        })
        print(f"\n* Da them sach '{new_name}' vao thu vien.\n")
    except ValueError:
        print("Nam xuat ban phai la so nguyen.\n")

# Ham chen sach vao vi tri mong muon
def insert_book_at_position():
    book_id = int(input("Nhap ID sach: "))
    name = input("Nhap ten sach: ")
    author = input("Nhap ten tac gia: ")
    year = int(input("Nhap nam xuat ban: "))
    
    position = int(input("Nhap vi tri muon chen sach: "))  # Vị trí muốn thêm sách vào
    
    new_book = {"id": book_id, "name": name, "author": author, "year": year}
    library_books.insert(position, new_book)  # Chèn sách vào vị trí đã chỉ định
    print("Da them sach vao vi tri:", position)

# Ham them nhieu sach
def add_multiple_books():
    new_books = [
        {"id": 8, "name": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
        {"id": 9, "name": "Brave New World", "author": "Aldous Huxley", "year": 1932}
    ]
    
    library_books.extend(new_books)  # Thêm nhiều sách từ danh sách khác
    print("Da them nhieu sach vao thu vien.")

# Ham xoa sach theo id bang phuong thuc remove
def delete_book():
    try:
        book_id = int(input("Nhap ID sach can xoa: ").strip())
        for book in library_books:
            if book["id"] == book_id:
                print(f"* Da xoa sach '{book['name']}' (ID: {book_id})\n")
                library_books.remove(book)
                break  # break khi da xoa thanh cong
        else:
            print(f"Khong tim thay sach co ID {book_id}.\n")
    except ValueError:
        print("ID phai la so nguyen. Vui long thu lai.\n")

# Ham xoa sach theo vi tri bang phuong thuc del
def delete_book_by_position():
    position = int(input("Nhap vi tri sach can xoa: "))  # Yêu cầu nhập vị trí sách cần xóa
    
    if 0 <= position < len(library_books):  # Kiểm tra vị trí hợp lệ
        del library_books[position]  # Xóa sách theo vị trí
        print("Da xoa sach tai vi tri:", position)
    else:
        print("Vi tri khong hop le.")

# Ham sua thong tin sach
def edit_book():
    try:
        book_id = int(input("Nhap ID sach can sua: ").strip())
        for book in library_books:
            if book["id"] == book_id:
                print(f"\n* Dang sua sach '{book['name']}' (ID: {book_id}):\n")
                new_name = input("Nhap ten moi cua sach: ").strip().capitalize()
                new_author = input("Nhap ten tac gia moi: ").strip()
                new_year = input("Nhap nam xuat ban moi: ").strip()
                if new_year.isdigit():  # Kiem tra neu la so
                    book["name"] = new_name
                    book["author"] = new_author
                    book["year"] = int(new_year)
                    print(f"\n* Da cap nhat thong tin cho sach ID {book_id}.\n")
                else:
                    print("Nam xuat ban phai la so nguyen.")
                return
        print(f"Khong tim thay sach co ID {book_id}.\n")
    except ValueError:
        print("ID phai la so nguyen. Vui long thu lai.\n")

# Ham sua doi ten sach
def update_book_name():
    old_name = input("Nhap ten sach cu: ").lower()  # Yêu cầu tên sách cũ và chuyển về chữ thường
    new_name = input("Nhap ten sach moi: ")
    
    for book in library_books:
        if old_name == book['name'].lower():  # Tìm kiếm sách theo tên không phân biệt hoa thường
            book['name'] = book['name'].replace(book['name'], new_name)  # Thay thế tên sách
            print(f"Da cap nhat ten sach thanh: {new_name}")
            break
    else:
        print("Khong tim thay sach.")

# Ham hien thi danh sach tat ca sach
def list_books():
    if len(library_books) == 0:
        print("Thu vien khong co sach nao.\n")
    else:
        print("\n\t===== DANH SACH SACH =====\n")
        
        # Dinh dang tieu de bang su dung center()
        print(f"{'ID'.center(5)} | {'Ten sach'.ljust(30)} | {'Tac gia'.ljust(20)} | {'Nam'.rjust(5)}")
        print("-" * 65)

        # Dinh dang tung dong sach
        for book in library_books:
            book_id = str(book['id']).center(5)
            book_name = book['name'].ljust(30)
            book_author = book['author'].ljust(20)
            book_year = str(book['year']).rjust(5)
            
            # Hien thi thong tin sach theo dinh dang
            print(f"{book_id} | {book_name} | {book_author} | {book_year}")
        print()

# Ham hien thi danh sach tat ca sach theo ten tren cùng 1 dòng
def list_books_inline():
    print("Danh sach cac sach: ", end="")
    for book in library_books:
        print(book['name'], end=", ")  # In tên sách và không xuống dòng, cách nhau dấu phẩy
    print()  # Kết thúc bằng xuống dòng sau khi in xong

# Ham tim kiem sach theo tu khoa
def search_books():
    keyword = input("Nhap tu khoa tim kiem (ten sach hoac tac gia): ").lower()
    
    print("\nKet qua tim kiem:")
    found = False
    for book in library_books:
        # Tìm kiếm trong tên sách và tác giả, không phân biệt hoa thường
        if book['name'].lower().find(keyword) != -1 or book['author'].lower().find(keyword) != -1:
            print(f"{book['id']} - {book['name']} - {book['author']} - {book['year']}")
            found = True
    
    if not found:
        print("Khong tim thay ket qua phu hop.")

# Ham sap xep sach theo ten sach khong phan biet in hoa in thuong
def sort_books_by_name():
    library_books.sort(key=lambda x: x['name'].lower()) 
    print("Danh sach da duoc sap xep theo ten sach.")

# Ham dao nguoc thu tu sap xep
def reverse_books_order():
    library_books.reverse() 
    print("Danh sach da duoc dao nguoc thu tu.")

# Ham in so luong sach 
def count_books():
    print(f"So luong sach hien co: {len(library_books)}")  

# Ham xoa toan bo sach
def clear_books():
    confirmation = input("Ban co chac chan muon xoa tat ca cac sach? (y/n): ").lower()
    if confirmation == 'y':
        library_books.clear()  
        print("Tat ca cac sach da bi xoa.")
    else:
        print("Xoa sach da bi huy.")

# Ham hien thi menu chuc nang
def show_menu():
    print("\n===== HE THONG QUAN LY THU VIEN =====")
    print("1. Xem thong tin sach")
    print("2. Them sach")
    print("3. Xoa sach")
    print("4. Sua thong tin sach")
    print("5. Xem danh sach sach")
    print("6. Tim kiem sach")
    print("7. Chen sach")
    print("8. Them nhieu sach")
    print("9. Xoa sach theo vi tri")
    print("10. Cap nhat ten sach")
    print("11. Xem danh sach ten sach")
    print("12. Sap xep danh sach theo ten sach")
    print("13. Dao nguoc danh sach")
    print("14. Xem so luong sach")
    print("15. Xoa toan bo ")
    print("0. Thoat chuong trinh")
    print("======================================")

# Ham chinh dieu khien chuong trinh
def main():
   
    if login():
        print("Dang nhap thanh cong.".upper())
        while True:
            show_menu()
            choice = input("Nhap lua chon: ").strip()
            if choice == "1":
                view_book_info()
            elif choice == "2":
                add_book()
            elif choice == "3":
                delete_book()
            elif choice == "4":
                edit_book()
            elif choice == "5":
                list_books()
            elif choice == "6":
                search_books()  
            elif choice == "7":
                insert_book_at_position()
            elif choice == "8":
                add_multiple_books()
            elif choice == "9":
                delete_book_by_position()
            elif choice == "10":
                update_book_name()
            elif choice == "11":
                list_books_inline()
            elif choice == "12":
                sort_books_by_name()
            elif choice == "13":
                reverse_books_order()
            elif choice == "14":
                count_books()
            elif choice == "15":
                clear_books()
            elif choice == "0":
                print("Thoat chuong trinh. Hen gap lai!")
                break
            else:
                print("Lua chon khong hop le. Vui long thu lai.")
    else:
        print("Dang nhap that bai. Vui long thu lai sau.\n")

# Chay chuong trinh
main()
