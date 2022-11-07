from django.db import models

class Address(models.Model):
    address = models.TextField(default="")

class Phone(models.Model):
    phone = models.TextField(default="")

class Email(models.Model):
    email = models.TextField(default="")

class OtdelProdaj(models.Model):
    ph = models.TextField(default="")

class Contact(models.Model):
    address = models.ForeignKey(Address,
                                on_delete=models.CASCADE,
                                related_name="c_ad"
                                )
    phone = models.ForeignKey(Phone,
                                on_delete=models.CASCADE,
                                related_name="c_ph"
                                )
    email = models.ForeignKey(Email,
                                on_delete=models.CASCADE,
                                related_name="c_em"
                                )


