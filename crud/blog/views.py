from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author)
    paginator = Paginator(blogs, 3)
    # 블로그를 세개씩 쪼갬
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': paginated_blogs})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})


def new_with_django_form(request):
    form = BlogForm()
    return render(request, 'new_with_django_form.html', {'form': form})


def new(request):
    return render(request, 'new.html')


def create_with_django_form(request):
    form = BlogForm(request.POST, request.FILES)
    # form 데이터를 처리하기 위해 request.POST와 request.FILES가 필요하다는 뜻
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        if request.user.is_authenticated:
            new_blog.user = request.user
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
    return redirect('home')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES('image', '')
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('blog:detail', new_blog.id)


def update(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('blog:detail', blog.id)
    return render(request, 'update.html', {"blog": blog})


def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')


# request.FILES 찾아보기