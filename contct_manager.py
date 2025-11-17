import re

class Contact:

    def __init__(self,ism, telefon,email):
        self.ism = ism
        self.telefon = telefon
        self.email = email


contact1 = Contact('Ali', '+998959698575','lutullo@gmail.com')

baza = [contact1]


def view_contact(s:list):
    for i in s:
        print(f"Ismi: {i.ism}, telefon: {i.telefon}, Email: {i.email}")


def add_contact(s:list):
    while True:
        ism = input("Ism kiriting: ").strip()
        if re.fullmatch(r"[A-Za-zА-Яа-яЁё’ʻʼ\- ]{2,30}", ism):
            break
        print("Xato: Faqat harflardan iborat bulish kerak")

    while True:
        telefon = input("Telefon raqam kiriting: ").strip()
        if re.fullmatch(r"^\+998[0-9]{9}$", telefon):
            break
        print("Xato: Bu (+998xxxxxxxxx) formatda bulish kerak")

    while True:
        email = input("Email kiriting: ").strip()
        if re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            break
        print("Xato: Email Noto'g'ri formatda (misol: user@gmail.com) ")

    addcontact = Contact(ism,telefon,email)
    s.append(addcontact)

    print("Mufaqiyatli qo'shildi")

def update_contact(s:list):
    if not s:
        print("Contactlar ro'yxati bo'sh")
        return

    while True:
        print("=== Tahrirlash uchun Telefon Raqam Kiriting ===")
        phone = input("Telefon Raqam kiriting: ")
        if re.fullmatch(r"^\+998[0-9]{9}$", phone):
            break
        print("Xato: Bu (+998xxxxxxxxx) formatda bulish kerak")

    contacttop = None
    for iy in s:
        if iy.telefon == phone:
            contacttop = iy
            break

    if contacttop is None:
        print("Telefon raqam buyicha Malumot topilmadi")
        return
    print(f"Topildi: {contacttop.ism} - {contacttop.telefon} - {contacttop.email}")


    while True:
        yangi_ism = input("Yangi Ism kiriting: ").strip()
        if yangi_ism == "":
            yangi_ism = contacttop.ism
            break
        if re.fullmatch(r"[A-Za-zА-Яа-яЁё’ʻʼ\- ]{2,30}", yangi_ism):
            break
        print("Xato: Faqat harflardan iborat bulish kerak")

    while True:
        yangi_telefon = input("Telefon raqam kiriting: ").strip()
        if yangi_telefon == "":
            yangi_telefon = contacttop.telefon
            break
        if re.fullmatch(r"^\+998[0-9]{9}$", yangi_telefon):
            break
        print("Xato: Bu (+998xxxxxxxxx) formatda bulish kerak")

    while True:
        yangi_email = input("Email kiriting: ").strip()
        if yangi_email == "":
            yangi_email = contacttop.email
            break
        if re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", yangi_email):
            break
        print("Xato: Email Noto'g'ri formatda (misol: user@gmail.com) ")

    contacttop.ism = yangi_ism
    contacttop.telefon = yangi_telefon
    contacttop.email = yangi_email

    print("Contact Mufaqiyatli Tahrirlandi")

def delete_contact(s:list):
    if not s:
        print("Contactlar ro'yxati bo'sh")
        return

    while True:
        print("=== O'chirish uchun Telefon Raqam Kiriting ===")
        phone = input("Telefon Raqam kiriting: ")
        if re.fullmatch(r"^\+998[0-9]{9}$", phone):
            break
        print("Xato: Bu (+998xxxxxxxxx) formatda bulish kerak")

    contacttop = None
    for iy in s:
        if iy.telefon == phone:
            contacttop = iy
            break

    if contacttop is None:
        print("Telefon raqam buyicha Malumot topilmadi")
        return
    print(f"Topildi: {contacttop.ism} - {contacttop.telefon} - {contacttop.email}")

    tasdiq = input("Haqiqatdan ham O'chirmoqchimizsiz  (Ha/Yo'q):  ").lower()
    if tasdiq == 'ha':
        s.remove(contacttop)
        print("Contact Mufaqiyatli O'chirildi ")
    else:
        print("O'chiris bekor qilindi")



def menu(s:list):
    print("1. Contact Qo'shish \n 2. Contact Tahrilash \n 3. Contact O'chirish \n 4. Barchasini Ko'rish \n 5. Break")
    while True:
        kod = input("Tanlang (1-5): ")
        if kod == "1":
            add_contact(s)
        elif kod == "2":
            update_contact(s)
        elif kod == "3":
            delete_contact(s)
        elif kod == "4":
            view_contact(s)
        elif kod == "5":
            print("Bekor qilindi ")
            break
        else:
            print("Faqat (1-5) Tanlang ")
if __name__== "__main__":
    menu(baza)