from django.shortcuts import render

# Minimal View
def post_list(request):
    return render(request,'blog/post_list.html',{})
