import datetime

from asgiref.sync import sync_to_async

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.http import HttpResponse

from deposits.models import DepositProductMaster


@sync_to_async
@receiver(post_save, sender=DepositProductMaster, dispatch_uid="create_deposit_product")
def create_deposit_product(sender, instance, created, **kwargs):
    if not created:
        DepositProductMaster.objects.using('funds_master').create(
            deposit_product_master_name=instance.name,
            deposit_product_master_description=instance.description,
            deposit_product_active=True,
            deposit_product_master_revenue_share=instance.revenue,
            deposit_product_minimum_fluctuate_revenue=instance.type,
            deposit_product_minimum_amount=instance.minimum_value,
            deposit_product_master_created_by=instance.user,
        )
    else:
        return HttpResponse("Error Created Log Reset Password")
