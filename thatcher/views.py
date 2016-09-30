## views.py
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required


# Create your views here.

@requires_csrf_token
@login_required
def index(request):
    images = [('margaret_thatcher.jpg', 'Margaret Thatcher'),
                    ('adele.jpg', 'Adele'),
                    ('barack_obama.jpg', 'Barack Obama'),
                    ('chris-hemsworth.jpg', 'Chris Hemsworth'),
                    ('hugh_jackman.jpg', 'Hugh Jackman'),
                    ('jennifer_lawrence.jpg', 'Jennifer Lawrence'),
                    ('justin_bieber.jpg', 'Justin Bieber'),
                    ('kanye_west.jpg', 'Kanye West'),
                    ('kate-middleton.jpg', 'Kate Middleton'),
                    ('kim_kardashian.jpg', 'Kim Kardashian'),
                    ('Margot-Robbie.jpg', 'Margot Robbie'),
                    ('taylor_swift.jpg', 'Taylor Swift'),
                    ('tony_abbott.jpg', 'Tony Abbott'),
                    ('will-smith.jpg', 'Will Smith')]
    (first_image_name, first_image_description) = images[0]
    context = {'images': images, 'first_image_name':first_image_name, 'first_image_description':first_image_description}
    return render(request, 'thatcher/index.html', context)