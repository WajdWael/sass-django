import pathlib
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "my page"
    my_context = {
        "page_title": my_title ,
        "queryset": queryset,
        "page_visit_count": queryset.count()
    }
    path = request.path
    html_tamplate = "home.html"
    print(path)
    PageVisit.objects.create()
    return render(request, html_tamplate, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "my page"
    my_context = {
        "page_title": my_title 
    }
    html_ = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>{page_title}</h1>
        </body>
    </html>
    """.format(**my_context)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
