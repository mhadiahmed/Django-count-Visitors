# class Blog(models.Model):
#     #fields you need
#     blog_views=models.IntegerField(default=0)
# views.py

# def blog_post(request,post_id):
#     #your code
#     blog_object=Blog.objects.get(id=post_id)
#     blog_object.blog_views=blog_object.blog_views+1
#     blog_object.save()
#     #your code

# get one value from the models
# var = [] #empty list
# query = Newsletter.Objects.all().values('email')
# s = list(query)
# print the s value to check it if list or not after doing that loop throe the items to get only the text value
# for i in s:
#     print(i)
#     for f in i.values():
#         print(f)
#         g.append(f)
