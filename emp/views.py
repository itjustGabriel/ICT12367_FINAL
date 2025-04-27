import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomRegisterForm, EmployeeForm
from .models import Employee

# ✅ Dashboard หน้าแสดงข้อมูลรวม
@login_required
def dashboard(request):
    total = Employee.objects.count()
    by_department = Employee.objects.values('department').annotate(count=Count('id'))
    by_month_qs = (
        Employee.objects.annotate(month=TruncMonth('hire_date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    by_month = list(by_month_qs)
    return render(request, 'emp/dashboard.html', {
        'total': total,
        'by_department': by_department,
        'by_month': by_month,
    })

# ✅ หน้าแสดงรายชื่อพนักงาน + ค้นหา
@login_required
def list_employee(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            first_name__icontains=query
        ) | Employee.objects.filter(
            last_name__icontains=query
        ) | Employee.objects.filter(
            position__icontains=query
        ) | Employee.objects.filter(
            department__icontains=query
        )
    else:
        employees = Employee.objects.all()

    return render(request, 'emp/list_emp.html', {
        'employees': employees,
        'query': query
    })

# ✅ เพิ่มพนักงาน
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employee')  # ✅ กลับหน้าแรกหลังเพิ่ม
    else:
        form = EmployeeForm()
    return render(request, 'emp/add_emp.html', {'form': form})

# ✅ แก้ไขพนักงาน
@login_required
def edit_employee(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    form = EmployeeForm(request.POST or None, instance=emp)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_employee')
    return render(request, 'emp/edit_emp.html', {'form': form})

# ✅ ลบพนักงาน
@login_required
def delete_employee(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    emp.delete()
    return redirect('list_employee')

# ✅ Export เป็น CSV
@login_required
def export_employees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    writer = csv.writer(response)
    writer.writerow(['ชื่อ', 'นามสกุล', 'ตำแหน่ง', 'แผนก', 'อีเมล', 'เบอร์โทร', 'วันที่เริ่มงาน'])
    for emp in Employee.objects.all():
        writer.writerow([
            emp.first_name, emp.last_name, emp.position,
            emp.department, emp.email, emp.phone, emp.hire_date
        ])
    return response

# ✅ สมัครสมาชิก
def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_employee')  # ✅ กลับหน้า list
    else:
        form = CustomRegisterForm()
    return render(request, 'emp/register.html', {'form': form})


