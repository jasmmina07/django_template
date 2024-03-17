from django.shortcuts import render

# Create your views here.

def main(request):
    data={
        "users":{"user1":{
            "name":"kshdjhd",
            "age":12
            },
         "user2":{
            "name":"kshdjhd",
            "age":12
            }
    }
}
    return render(request,"index.html",data)