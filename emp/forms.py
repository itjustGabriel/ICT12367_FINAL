from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
from django.core.exceptions import ValidationError

# ✅ ฟอร์มพนักงาน พร้อม widget ป้อนวันที่แบบปฏิทิน
class EmployeeForm(forms.ModelForm):
    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='วันที่เริ่มงาน'
    )

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'first_name': 'ชื่อ',
            'last_name': 'นามสกุล',
            'position': 'ตำแหน่ง',
            'department': 'แผนก',
            'email': 'อีเมล',
            'phone': 'เบอร์โทรศัพท์',
        }

# ✅ ฟอร์มสมัครสมาชิก พร้อมข้อความภาษาไทย
class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='ชื่อผู้ใช้',
        help_text='ใช้ตัวอักษร ตัวเลข และ @/./+/-/_ ได้ ไม่เกิน 150 ตัวอักษร',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='รหัสผ่าน',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="""
            <ul class="text-muted small">
                <li>รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร</li>
                <li>ไม่ควรเป็นรหัสผ่านที่ใช้กันทั่วไป</li>
                <li>ไม่ควรเป็นตัวเลขล้วน</li>
            </ul>
        """
    )

    password2 = forms.CharField(
        label='ยืนยันรหัสผ่าน',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='กรอกให้เหมือนรหัสผ่านด้านบน'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('ชื่อผู้ใช้นี้ถูกใช้ไปแล้ว กรุณาใช้ชื่ออื่น')
        return username
