from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import weasyprint
from io import BytesIO

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # Aquí solo procesamos el envío del correo electrónico

        # Crear correo de la factura
        subject = 'My Shop - Invoice no. {}'.format(order.id)
        message = 'Please, find attached the invoice for your recent purchase.'
        email = EmailMessage(subject,
                             message,
                             'admin@myshop.com',
                             [order.email])

        # Generar PDF
        html = render_to_string('orders/order/pdf.html', {'order': order})
        out = BytesIO()
        stylesheets = [weasyprint.CSS('staticfiles/css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out,
                                               stylesheets=stylesheets)
        # Adjuntar el archivo PDF
        email.attach('order_{}.pdf'.format(order.id),
                     out.getvalue(),
                     'application/pdf')
        # Enviar el correo
        email.send()

        return redirect('payment:done')
    else:
        return render(request, 
                      'payment/process.html', 
                      {'order': order})

def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
