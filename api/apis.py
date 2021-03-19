from django.http import response
import requests 
import json
from urllib.parse import urlencode,parse_qsl,urlparse




api_key="306cf1684a42e4be5ec0a1c60362c2ef"


params='platforms'
query='api_key=306cf1684a42e4be5ec0a1c60362c2ef'

import requests

def get_droplets(params):
    endpoint=f"https://libraries.io/api/{params}?{query}"
    r=requests.get(endpoint)

    droplets = r.json()
   

    return droplets












# """# 
# to_parse= "https://libraries.io/api/NPM/base62?api_key=306cf1684a42e4be5ec0a1c60362c2ef"

# # # qq=urlparse(to_parse)
# # parsed_url=urlparse(to_parse)
# # # q =parse_qsl(aaaa)
# # print(parsed_url)
# # 
# # ParseResult(
# #  scheme='https',
# #  netloc='libraries.io',
# #  path='/api/platforms',
# #  params='',
# #  fragment='')
# # """
# # b=
# # a=urlencode(b)
# path="/api/platforms"
# api_key="306cf1684a42e4be5ec0a1c60362c2ef"
# query="api_key=306cf1684a42e4be5ec0a1c60362c2ef "

# # def datamine(path):
# #     scheme="https" 
# #     netloc="https//libraries.io"

# #     end=f"{netloc}{path}?{query}"
    
# #     r=requests.get(end)
# #     print (r)
# #     params=f""
# #     endpoint=(params)

# #     print(end)

# # datamine(path)


# # def extreact_data( data_type='api/search'):    
# #     endpoint = f"https://libraries.io/{data_type}"    
# #     params={"q":"python","key":api_key}     
# #     url_parmas=urlencode(params)   
# #     url= f"{endpoint}?{url_parmas}"   
# #     r=requests.get(url)
# #     if r.status_code not in range(200,299):

# #         return{}
        

# #     return r.json()

# def Search_v(value):

#     data_type='search'
#     endpoint = f"https://libraries.io/api/{data_type}"
#     api_key="306cf1684a42e4be5ec0a1c60362c2ef"
    
#     # search?q=grunt&
        
#     params={"q":"{value}","key":api_key}    
#     url_parmas=urlencode(params)
#     url= f"{endpoint}?{params}"
#     print(url)
    
    
#     data=requests.get(url)
    
#     return response data()


# # search(value)    

# """# 
# to_parse= "https://libraries.io/api/NPM/base62?api_key=306cf1684a42e4be5ec0a1c60362c2ef"

# # # qq=urlparse(to_parse)
# # parsed_url=urlparse(to_parse)
# # # q =parse_qsl(aaaa)
# # print(parsed_url)
# # 
# # ParseResult(
# #  scheme='https',
# #  netloc='libraries.io',
# #  path='/api/platforms',
# #  params='',
# #  fragment='')
# # """
# # b=
# # a=urlencode(b)
# path="/api/platforms"
# api_key="306cf1684a42e4be5ec0a1c60362c2ef"
# query="api_key=306cf1684a42e4be5ec0a1c60362c2ef "

# # def datamine(path):
# #     scheme="https" 
# #     netloc="https//libraries.io"

# #     end=f"{netloc}{path}?{query}"
    
# #     r=requests.get(end)
# #     print (r)
# #     params=f""
# #     endpoint=(params)

# #     print(end)

# # datamine(path)


# # def extreact_data( data_type='api/search'):    
# #     endpoint = f"https://libraries.io/{data_type}"    
# #     params={"q":"python","key":api_key}     
# #     url_parmas=urlencode(params)   
# #     url= f"{endpoint}?{url_parmas}"   
# #     r=requests.get(url)
# #     if r.status_code not in range(200,299):

# #         return{}
        

# #     return r.json()

# def Search_v(value):

#     data_type='search'
#     endpoint = f"https://libraries.io/api/{data_type}"
#     api_key="306cf1684a42e4be5ec0a1c60362c2ef"
    
#     # search?q=grunt&
        
#     params={"q":"{value}","key":api_key}    
#     url_parmas=urlencode(params)
#     url= f"{endpoint}?{params}"
#     print(url)
    
    
#     data=requests.get(url)
    
#     return response data()

# """# 
# to_parse= "https://libraries.io/api/NPM/base62?api_key=306cf1684a42e4be5ec0a1c60362c2ef"

# # # qq=urlparse(to_parse)
# # parsed_url=urlparse(to_parse)
# # # q =parse_qsl(aaaa)
# # print(parsed_url)
# # 
# # ParseResult(
# #  scheme='https',
# #  netloc='libraries.io',
# #  path='/api/platforms',
# #  params='',
# #  fragment='')
# # """
# # b=
# # a=urlencode(b)
# path="/api/platforms"
# api_key="306cf1684a42e4be5ec0a1c60362c2ef"
# query="api_key=306cf1684a42e4be5ec0a1c60362c2ef "

# # def datamine(path):
# #     scheme="https" 
# #     netloc="https//libraries.io"

# #     end=f"{netloc}{path}?{query}"
    
# #     r=requests.get(end)
# #     print (r)
# #     params=f""
# #     endpoint=(params)

# #     print(end)

# # datamine(path)


# # def extreact_data( data_type='api/search'):    
# #     endpoint = f"https://libraries.io/{data_type}"    
# #     params={"q":"python","key":api_key}     
# #     url_parmas=urlencode(params)   
# #     url= f"{endpoint}?{url_parmas}"   
# #     r=requests.get(url)
# #     if r.status_code not in range(200,299):

# #         return{}
        

# #     return r.json()

# def Search_v(value):

#     data_type='search'
#     endpoint = f"https://libraries.io/api/{data_type}"
#     api_key="306cf1684a42e4be5ec0a1c60362c2ef"
    
#     # search?q=grunt&
        
#     params={"q":"{value}","key":api_key}    
#     url_parmas=urlencode(params)
#     url= f"{endpoint}?{params}"
#     print(url)
    
    
#     data=requests.get(url)
    
#     return response data()


# # search(value)    


# # search(value)    

