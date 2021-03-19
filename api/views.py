import requests
from urllib.parse import urlencode,parse_qsl,urlparse
# from .forms import SearchForm

from django.shortcuts import render

from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from .apis import get_droplets


class GetDroplets(TemplateView):

    template_name = 'platform.html'

    def get_context_data(request, *args, **kwargs):  
            # if request.method == 'GET':
        params='/platforms'
        data=get_droplets(params)
        array_length = len(data)
        droplet_list = []

        for i in range(array_length):
            droplet_list.append(data[i])

        context = {
            'droplets' : droplet_list,
        }
            
    
        return context





class Get_search(TemplateView):

    template_name = 'search.html'
    
    def get_context_data(request, *args, **kwargs):  
            # if request.method == 'GET':
        params='/search'
        data=get_droplets(params)
        array_length = len(data)
        droplet_list = []
        for i in range(array_length):
            droplet_list.append(data[i])

        context = {
            'drop' : droplet_list,
        }    
        
        return context      
        
        # return render(request,"search.html")
    
    
class github(TemplateView):

    template_name = 'git.html'
    
    def get_context_data(request, *args, **kwargs):  
            # if request.method == 'GET':
        params='/github/python?'
        data=get_droplets(params)
        array_length = len(data)
        droplet_list = []
        
        for i in range(array_length):
            droplet_list.append(data[i])

        context = {
            'droplets' : droplet_list,
        }    
        
                
        return context


    # from .apis import datamine



# def  post_search(request):
#     path="/api/platforms"

#     pas=datamine(path)
#     print(pas)






# def  post_search(request):
#     form =SearchForm() 
#     query=None
#     results=[]
#     if 'query' in request.GET:
#         form=SearchForm(request.GET)
#         if form.is_valid():
#             query=form.cleaned_data['query']
#     return render(request,'search.html',{
#            'form':form,
#            'query':query,     
#             }  )



# def extreact_data(request, find,data_type='api/search'):    
#     endpoint = f"https://libraries.io/{data_type}"    
#     params={"q":find,"key":api_key}     
#     url_parmas=urlencode(params)   
#     url= f"{endpoint}?{url_parmas}"   
#     r=requests.get(url).json()
#     if r.status_code not in range(200,299):

#         return{}
#     return render(request,'index.html',{
        
#     })


