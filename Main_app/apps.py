from django.apps import AppConfig

# 해당 app의 class 를 정의해준다. 
# 이 class 를 setting.py 에 알려주면 된다. 

class MainAppConfig(AppConfig):
    name = 'Main_app'
