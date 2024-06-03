from .models import Category

def all_ctgry(request):
    ctg=Category.objects.all()
    context={"ctg":ctg}
    return context