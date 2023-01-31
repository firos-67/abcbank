from .models import District


def branch_links(request):
    branches = District.objects.all()
    return dict(branches=branches)
