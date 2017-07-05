from django.contrib.auth.models import User


def get_null_user():
    User.objects.get(username='Deleted user')


def format_number_to_present(num):
    num = int(num)
    if num < 1000:
        return str(num)
    elif 1000 < num < 1000000:
        return str(num / 1000) + 'k'
    else:
        return str(num / 1000000) + 'm'
