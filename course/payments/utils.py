import uuid
from payments.models import Payment

def generate_unique_transaction_id():
    while True:
        tmp_id = f"tmp_{uuid.uuid4().hex}"
        if not Payment.objects.filter(transaction_id=tmp_id).exists():
            return tmp_id