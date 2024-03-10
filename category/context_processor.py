from .models import Category


def list_category(request):
    categories = Category.objects.all()
    return dict(categories=categories)