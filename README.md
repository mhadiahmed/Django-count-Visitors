# Django-count-Visitors
Django App for counting Page Visits

how to use it 
==============

`from Pageviews.signals import object_viewed_signal`

to your views.py file 

and then use it with you views for example lets use it with the detail views

```
def detail(request,id):
    post = get_object_or_404(Post,id=id)
    object_viewed_signal.send(post.__class__,instance=post,request=request)
    context = {
        'post':post,
    }
    return render(request,'detail.html',context)
```

you can use it with CBV as will it will be like 


make this import in your views

`from Pageviews.mixins import ObjectViewMixin`

and use it on your detail class like this 

```
class PostDetailView(ObjectViewMixin, DetailView):
    model = Post
```
