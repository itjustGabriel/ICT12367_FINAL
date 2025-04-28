# โปรเจควิชา ICT 12367 หัวข้อ ระบบจัดการรายชื่อพนักงาน

โปรเจกต์นี้เป็นระบบจัดการพนักงานเบื้องต้น พัฒนาด้วย Django 4.2 และ Bootstrap 5
สามารถเพิ่มพนักงาน, ดูรายชื่อพนักงาน และบันทึกข้อมูลลงฐานข้อมูลได้จริง

---

## ฟีเจอร์ที่มีในระบบ

- ➕ เพิ่มพนักงานใหม่ (Add Employee)
- 📋 แสดงรายชื่อพนักงานทั้งหมด (List Employee)
- 📅 บันทึกวันเริ่มงานของพนักงาน
- 💰 บันทึกเงินเดือนพนักงาน
- ✅ เลือกสถานะการทำงาน (ทำงาน / ลาออก)
- 🛠 ใช้ Bootstrap5 UI เรียบง่ายสวยงาม
- 💾 ข้อมูลถูกบันทึกลงฐานข้อมูล (SQLite)

---

## เทคโนโลยีที่ใช้

- Python 3.10+
- Django 4.2
- Bootstrap 5
- HTML5 + CSS3
- SQLite Database

---

## ตัวอย่างการใช้งานระบบจัดเก็บข้อมูลพนักงาน
- การ สมัครสมาชิก และ Login เข้าใช้งานระบบ


https://github.com/user-attachments/assets/2b1b4eff-7917-434f-bf85-962cd23d4113

📝 หน้า รายชื่อพนักงานทั้งหมด (List Employee)
คำอธิบายสำหรับหน้านี้:

แสดง ตารางรายชื่อพนักงานทั้งหมด ที่มีในระบบ

ตารางประกอบด้วยคอลัมน์: ชื่อ, ตำแหน่ง, แผนก, อีเมล, เบอร์โทรศัพท์, วันที่เริ่มงาน, การจัดการ

มี ฟังก์ชันการค้นหา พนักงานจากช่องค้นหาด้านบน (ตามชื่อ/ตำแหน่ง/แผนก)

แต่ละแถวของข้อมูล มีปุ่ม แก้ไข (Edit) และ ลบ (Delete)

![home](https://github.com/user-attachments/assets/a2c90b21-3b3c-4f10-a2fc-8057a0dffe2c)

➕ หน้าเพิ่มพนักงาน (Add Employee)

กรอกชื่อ นามสกุล รหัสพนักงาน เบอร์โทร อีเมล เงินเดือน วันที่เริ่มงาน

กด บันทึกข้อมูล เพื่อเพิ่มข้อมูลใหม่

![add employee](https://github.com/user-attachments/assets/7763ddff-153e-4b3b-a565-068afed43e20)

😁 มีปุ่ม Export CSV เพื่อดาวน์โหลดข้อมูลพนักงานเป็นไฟล์ .csv

🏠 หน้า Dashboard

แสดงข้อมูลสรุปจำนวนพนักงานแต่ละแผนก

กดปุ่ม เพิ่มพนักงาน เพื่อไปหน้าเพิ่มข้อมูล

![dash](https://github.com/user-attachments/assets/fc2d0433-5afe-4be4-a79c-d8c6c2c0a78f)


https://github.com/user-attachments/assets/5130b15d-f3bc-4d9b-a504-25b402dbbc4d

---

## ติดตั้งและรันโปรเจกต์

### 1. Clone โปรเจกต์จาก GitHub
```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### 2. สร้าง Virtual Environment (แนะนำให้ทำ)
```bash
python -m venv venv
source venv/bin/activate        # สำหรับ Mac/Linux
venv\Scripts\activate           # สำหรับ Windows
```

### 3. ติดตั้ง Dependencies
```bash
pip install django
```

### 4. เช็คการตั้งค่า Database
ในไฟล์ emp_project/settings.py ใช้ฐานข้อมูล SQLite เริ่มต้นแล้ว ไม่ต้องตั้งค่าเพิ่มเติม

### 5. ดำเนินการ Migrations
```bash
python manage.py migrate
```

### 6. สร้าง Superuser (สำหรับเข้าสู่ระบบแอดมิน)
```bash
python manage.py createsuperuser
```

### 7. รันเซิร์ฟเวอร์
```bash
python manage.py runserver
```
เปิดเบราว์เซอร์ไปที่: http://127.0.0.1:8000/
