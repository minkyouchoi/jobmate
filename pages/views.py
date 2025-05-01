from django.shortcuts import render

# ✅ 랜딩페이지 뷰
def home(request):
    return render(request, 'pages/index.html')
