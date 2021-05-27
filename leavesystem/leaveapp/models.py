import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    picture = models.ImageField(upload_to = 'picture', default='profile_pics.jpg')
    department_setting = models.ForeignKey('Department_Setting', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    leave_form = models.ForeignKey('Leave_Form', on_delete=models.CASCADE)

    class Meta:
        db_table = "leaveapp_profile"

    def __str__(self):
        return str(self.user)

class Department_Setting(models.Model):
    department_name = models.CharField(max_length=200)

class Member(models.Model):
    member_type = models.CharField(max_length=200)

SORT_NAME = (
    ('ลากิจส่วนตัว', 'ลากิจส่วนตัว'),
    ('ลาคลอดบุตร', 'ลาคลอดบุตร'),
    ('ลาป่วย', 'ลาป่วย'),
    ('ลาพักร้อน', 'ลาพักร้อน'),
    ('ลาเข้าตรวจรับเลือกทหารหรือเข้ารับการเตรียมพล', 'ลาเข้าตรวจรับเลือกทหารหรือเข้ารับการเตรียมพล'),
    ('ลาไปช่วยเหลือภรรยาที่คลอดบุตร', 'ลาไปช่วยเหลือภรรยาที่คลอดบุตร'),
    ('ลาไปศึกษา ฝึกอบรม ปฏิบัติการวิจัย หรือดูงาน', 'ลาไปศึกษา ฝึกอบรม ปฏิบัติการวิจัย หรือดูงาน'),
)

DEPARTMENT_NAME = (
    ('บริหาร', 'บริหาร'),
    ('จัดซื้อจัดจ้าง', 'จัดซื้อจัดจ้าง'),
    ('บุคคล', 'บุคคล'),
)

DURATION1 = ( 
    ('เต็มวัน', 'เต็มวัน'),
    ('ครึ่งเช้า', 'ครึ่งเช้า'),
    ('ครึ่งบ่าย', 'ครึ่งบ่าย'),
)

DURATION2 = (
    ('เต็มวัน', 'เต็มวัน'),
    ('ครึ่งเช้า', 'ครึ่งเช้า'),
    ('ครึ่งบ่าย', 'ครึ่งบ่าย'),
)


class Leave_Form(models.Model):
    leave_sort_name = models.CharField(max_length=200, choices=SORT_NAME, default='ลากิจส่วนตัว')
    leave_department = models.CharField(max_length=200, choices=DEPARTMENT_NAME, default='บริหาร')
    leave_reason = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today)
    duration1 = models.CharField(max_length=100, choices=DURATION1, default='เต็มวัน')
    end_date = models.DateField(default=datetime.date.today)
    duration2 = models.CharField(max_length=100, choices=DURATION2, default='เต็มวัน')
    upload = models.FileField(upload_to='leaveapp/file_uploads', default='')
    leave_contact = models.CharField(max_length=200)

    class Meta:
        db_table = "leaveapp_leave_form"
    
    def __str__(self):
        return self.leave_sort_name
