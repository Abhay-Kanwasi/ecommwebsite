import razorpay
from django.conf import settings

# Client Initialization
client = razorpay.Client(auth=(
    settings.RAZORPAY_KEY_ID,
    settings.RAZORPAY_KEY_SECRET_ID
    )
)
