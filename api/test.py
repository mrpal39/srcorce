from django.shortcuts import redirect,render
from django.conf import request

from . apis import Search_v


def find(value):

    a="grunt"
    content=Search_v(value=a)
    print(content)
    return render(request,'')



    

# paths="/api/platforms"

# def  post_search(request,paths):
#     pas=datamine(path=paths)
#     print(pas)

















# msg_template = """Hello {name},
# Thank you for joining {website}. We are very
# happy to have you with us.
# """ # .format(name="Justin", website='cfe.sh')

# def format_msg(my_name="Justin", my_website="cfe.sh"):
#     my_msg = msg_template.format(name=my_name, website=my_website)
#     return my_msg