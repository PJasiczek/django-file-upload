from django.shortcuts import render

from adcpwr_api.models import Document, Order

def create_order_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        telephone_number = request.POST.get('telephone_number')
        description = request.POST.get('description')

        order = Order.objects.create(
            first_name = first_name,
            last_name = last_name,
            email_address = email_address,
            telephone_number =  telephone_number,
            description =  description
        )

        for file_num in range(0, int(length)):

            Document.objects.create(
                order = order,
                documents = request.FILES.get(f'documents{file_num}')
            )


    return render(request, 'create-order.html')