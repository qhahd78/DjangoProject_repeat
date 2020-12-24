from django.shortcuts import render

# Create your views here.

# main 함수를 정의해주고, main.html 을 연결해주기. 
# main 함수를 불러온다 => main.html 을 불러온다. 
def main(request):
    return render(request, 'main.html')