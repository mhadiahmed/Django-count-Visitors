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
