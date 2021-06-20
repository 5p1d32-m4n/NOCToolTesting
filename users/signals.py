from django.db.models.signals import pre_save
from django.dispatch import receiver

from users.models import CustomUser


# @receiver(pre_save, sender=CustomUser)
# def generate_usernname(sender, instance, *args, **kwargs):
#     fn_letter = instance.first_name[0]
#     ln_letter = instance.last_name[0]
#     emp_num_str = str(instance.employee_number)
#     instance.username = fn_letter + ln_letter + emp_num_str
