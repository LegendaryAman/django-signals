from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import MyModel
import threading
import time

@receiver(post_save, sender=MyModel)
def signal_is_sync(sender, instance, **kwargs):
    print("Signal Q1: Started")
    time.sleep(5)
    print("Signal Q1: Finished")

@receiver(post_save, sender=MyModel)
def signal_thread_check(sender, instance, **kwargs):
    print("Signal Q2: Thread ID:", threading.get_ident())

@receiver(post_save, sender=MyModel)
def signal_transaction_check(sender, instance, **kwargs):
    print("Signal Q3: In transaction:", connection.in_atomic_block)

@receiver(post_save, sender=MyModel)
def signal_basic(sender, instance, **kwargs):
    print("Signal Q4: Basic signal received -", instance.name)
