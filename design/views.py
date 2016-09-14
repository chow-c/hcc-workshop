## views.py
from django.shortcuts import render

def index(request):
    images = [ {'name': 'image1.png', 'answer': 'Yep, Psychology is a big part of HCI!' },
					{'name': 'image2.png','answer': 'Yep, Psychology is a big part of HCI!'},
					{'name': 'image3.png','answer': 'Yep, Psychology is a big part of HCI!'},
					{ 'name': 'image4.jpg', 'answer': 'Yep, Psychology is a big part of HCI!'},
					{'name': 'image5.png','answer': 'Yep, Psychology is a big part of HCI!'},
					{'name': 'image6.png','answer': 'Yep, Psychology is a big part of HCI!'},
					{'name': 'image7.png', 'answer': 'Yep, Psychology is a big part of HCI!'},
					{'name': 'image8.png','answer': 'Yep, Psychology is a big part of HCI!'},
					{ 'name': 'image9.png','answer': 'Yep, Psychology is a big part of HCI!'}]
    context = {'images': images}
    return render(request, 'design/index.html', context)