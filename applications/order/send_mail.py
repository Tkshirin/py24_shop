from django.core.mail import send_mail


def send_confirmation_email(email, code, title, price):
    full_link = f'привет, подтверди заказ на продукт {title} на сумму {price} \n\nhttp://localhost:8000/api/v1/order/confirm/{code}'

    send_mail(
        f'Order from py24 shop',
        full_link,
        'toktobekkyzysirin@gmail.com',
        ['toktobekkyzysirin@gmail.com']
    )

