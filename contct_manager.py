import re

class Contact:

    def __init__(self,ism, telefon,email):
        self.ism = ism
        self.telefon = telefon
        self.email = email


contact1 = Contact('Ali', '+998959698575','lutullo@gmail.com')

baza = [contact1]

baza2 = []


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


def sms_send():
        telefon15 = input("Telefon raqam kiriting: ").strip()
        if re.fullmatch(r"^\+998[0-9]{9}$", telefon15):
            for i in baza:
                if i.telefon == telefon15:
                    yoz = input("SMS Xabar kiriting: ")
                    print("SMS yuborildi!")

                    baza2.append({
                        "Telefon": telefon15,
                        "Sms Xabar": yoz
                    })
                else:
                    print("Bazada Malumot topilmadi!")
        else:
            print("Xato: Bu (+998xxxxxxxxx) formatda bulish kerak")


def view_sms():
    if not baza2:
        print("SMS lar Mavjud emas")
        return
    print(" Yuborilgan SMSlar ")
    for i in baza2:
        print(f"Telefon: {i['Telefon']}, Xabar: {i['Sms Xabar']}")

def delete_sms():
    telefon10 = input("Telefon raqam kiriting: ").strip()
    if re.fullmatch(r"^\+998[0-9]{9}$", telefon10):
        for i in baza2:
            if i["Telefon"] == telefon10:
                print("O'chirilayotgan SMS")
                print(f"Telefon: {i['Telefon']}, Xabar: {i["Sms Xabar"]} ")

                sms_x_y = input("Haqiqatdan ham O'chirmoqchimisiz (Ha/Yo'q) : ").lower()
                if sms_x_y == "ha":
                    baza2.remove(i)
                    print("SMS Xabar Mufaqiyatli O'chirildi ")
            print("Bazada bu raqamga tegishli sms topilmadi")


def contact_man(s:list):
    while True:
        print("1. Contact Qo'shish \n 2. Contact Tahrilash \n 3. Contact O'chirish \n 4. Barchasini Ko'rish \n 5. Break")
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

def sms_man(s:list):
    while True:
        print("1. SMS yuborish \n 2. SMS O'chirish \n 3. View all \n 4. Orqaga Qaytish \n 5. Exit")
        kod = input("Tanlang (1-5): ")
        if kod == "1":
            sms_send()
        elif kod == "2":
            delete_sms()
        elif kod == "3":
            view_sms()
        elif kod == "4":
            kirish(s)
        elif kod == "5":
            print("Siz Dasturdan Chiqdingiz ")
            break
        else:
            print("Faqat (1-5) Tanlang!")



def  kirish(s):
    print("1. Contact Manager Kirish \n 2. SMS Manager Kirish \n 3. Exit")
    while True:
        kod = input("Tanlang (1-3): ")
        if kod == "1":
            print("=== Siz Contact Managerdasiz === ")
            contact_man(s)
        elif kod == "2":
            print("=== Siz SMS Managerdasiz === ")
            sms_man(s)
        elif kod == "3":
            print(" Siz Dasturdan chiqdingiz ")
            break
        else:
            print("Faqat (1-3) Tanlang ")

if __name__ == "__main__":
    kirish(baza)


