from main.models import RefferalLink

class RefferalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.GET.get("refferal", False):
            try:
                refferal = RefferalLink.objects.get(refferal_link=request.GET.get("refferal"))
                refferal.count_of_view = refferal.count_of_view + 1
                refferal.save()
            except RefferalLink.DoesNotExist:
                pass
        response = self.get_response(request)
        return response