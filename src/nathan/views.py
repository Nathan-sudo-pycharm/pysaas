import pathlib
from django.shortcuts import render
from django.http import HttpResponse

this_dir=pathlib.Path(__file__).resolve().parent

def home_page_view(request , *args ,**kwargs):
    print(this_dir)
    my_title="My page"
    my_context={
     "page_title":my_title
    }
    html_template="home.html"
    return render(request,html_template , my_context) 



def my_old_home_page_view(request , *args ,**kwargs):
    print(this_dir)
    my_title="Mypage"
    my_context={"page_title":my_title}
    html_="""

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <h1>{page_title}anything this anything?</h1>
  </body>
</html>

""".format(**my_context)
   # html_file_path=this_dir/"home.html"
    #html_=html_file_path.read_text()
    return HttpResponse(html_) 











