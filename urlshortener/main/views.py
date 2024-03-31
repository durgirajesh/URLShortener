from .models import url
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, random, string

@csrf_exempt
def url_shortener(request):
    if request.method == 'POST':
        try:
            url_data = json.loads(request.body.decode())
            url_ = url_data.get('long_url')
        except json.JSONDecodeError:
            return JsonResponse({'error' : 'Invalid JSON Data'})
        
        existing_shorturl = url.objects.filter(original_url=url_).first()
        if existing_shorturl is not None:
            return JsonResponse({'short url' : existing_shorturl.short_url})
        
        shorturl_ = "https://tinify.com/"
        while True:
            _shorturl= ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
            if not url.objects.filter(short_url=_shorturl).exists():
                break
        
        shorturl_ += _shorturl
        shorturl = url(original_url=url_, short_url=shorturl_)
        shorturl.save()

        return JsonResponse({'shorturl' : shorturl_})
    else:
        return JsonResponse({'error': 'only POST requests are allowed'})
