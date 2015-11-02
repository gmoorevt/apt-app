from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Address(models.Model):
    ADDRESS_TYPE = (
        (1, u'Permeate'),
        (2, u'Work'),
        (3, u'Apartment'),
        )

    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=12)
    type = models.IntegerField(choices=ADDRESS_TYPE,default=1)

    def __str__(self):
        s = '%s %s %s %s'% (self.street,self.city,self.state,self.zip)

        return s

class Building(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    building_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address)
    description = models.TextField()

    def __str__(self):
        s = '/n Building Name: %s'% self.building_name
        s += '/n Description: %s '% self.description
        return s

class Unit(models.Model):
    building = models.ForeignKey(Building)
    name = models.CharField(max_length=50)
    description = models.TextField()
    number_bedrooms = models.IntegerField()
    number_bathrooms = models.IntegerField()

    def __str__(self):
        s = '/n Unit Name: %s'% self.building
        s += '/n Name: %s' % self.name
        s += '/n Description: %s' % self.description
        s += '/n Number of Bedrooms: %s' %  self.number_bedrooms
        s += '/n Numbrer of Bathrooms: %s' % self.number_bathrooms
        return s


class Tenant(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20)
    cell_number = models.CharField(max_length=20)

    def __str__(self):
        s = '/n First Name: %s %s' % (self.first_name, self.last_name)
        s += '/n Phone Number: %s'% self.phone_number
        s += '/n Cell Number: %s'% self.cell_number
        return s

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant)
    start_date = models.DateField()
    end_date = models.DateField()
    security_dep = models.DecimalField(max_digits=8,decimal_places=2)
    rent_amount = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        s = '/n Tenant %s %s'% (self.tenant.first_name, self.tenant.last_name)
        s += '/n Start Date: %s'% self.start_date
        s += '/n End Date: %s'% self.end_date
        s += '/ Security deposit %s'% self.security_dep
        s += '/Rent %s'% self.rent_amount
        return s

class Payment(models.Model):
    lease = models.ForeignKey(Lease)
    tenant = models.ForeignKey(Tenant)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    payment_date = models.DateField()
    description = models.TextField()
    def __str__(self):
        s = '/n Payment amount %s'% self.amount
        s+= '/n Description %s'% self.description
        return s


class Receivable(models.Model):
    lease = models.ForeignKey(Lease)
    tenant = models.ForeignKey(Tenant)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    due_date = models.DateField()
    description = models.TextField()
    payment = models.ForeignKey(Payment)

    def __str__(self):
        s = '/n Payment %s'% self.payment
        s += '/n Description %s'% self.description
        return s
