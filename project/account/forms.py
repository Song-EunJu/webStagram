from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta: 
        # meta 클래스의 모델을 customuser로 바꿔주면서 custom user에 맞는 form으로 만들 수 있음
        model = CustomUser
        fields =['email', 'name', 'username', 'password']
