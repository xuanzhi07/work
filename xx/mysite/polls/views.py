from django.shortcuts import render

# Create your views here.
def index(request):
    
    args = {
        'name' : 'John',
        'age' : '11',
        'vip' : 'ture'
        
        'dc' : {
            'a' : 10,
            'b' : 20

        }
    }

    return render(request,'./polls/index.html',args)
