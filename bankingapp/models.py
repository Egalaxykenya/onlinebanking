from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(User):
    idNumber = models.CharField(max_length=30, verbose_name="Customer ID number", blank=True)
    city = models.CharField(max_length=20,verbose_name="Customer City", null=True, default=None)
    lastAccess = models.DateTimeField(auto_now=True, verbose_name="Time of last successful login")
    slug = models.SlugField(unique=True)

    # Create automatically the slugfield entry
    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name

class UserBankAccount(models.Model):
    ACCOUNT_CHOICES = (
    ('current', 'Current Account'),
    ('savings', 'Savings Account'),
    )
    accountID = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True, related_name="account_number")
    accountNumber = models.CharField(max_length=10, verbose_name="Customer Account Number", default=None)
    bankName = models.CharField(max_length=50, verbose_name="Customer Bank Name", default=None)
    accountType = models.CharField(max_length=10, verbose_name="Customer Account Type", choices=ACCOUNT_CHOICES,default='current')
    accountBalance = models.IntegerField(verbose_name=" Customer Current Account Balance", default=0)
    createdAt = models.DateField(verbose_name="Date of Account Creation", auto_now_add=True)
    bankBranch = models.CharField(max_length=50, verbose_name="Name of Account Branch", default=None)

    class Meta:
        ordering = ('-createdAt',)

    def __str__(self):
        return self.accountNumber


class UtilityCompany(models.Model):
    companyName = models.CharField(max_length=50, verbose_name=" Company Name", default=None)
    companyAccountNum = models.CharField(max_length=10,verbose_name="Company Account Number", default=None)
    companyAccountBalance = models.IntegerField(verbose_name=" Company Account Balance", default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.companyName)
        super(UtilityCompany, self).save(*args, **kwargs)

    def __str__(self):
        return self.companyName


class UtilityPayment(models.Model):
    UTILITY_CHOICES = (
    ('Water Bill','Monthly Water Bill'),
    ('Gas Bill', 'Monthly Gas Bill'),
    ('Power Bill', 'Monthly Power Bill')
    )
    billID = models.ForeignKey(UtilityCompany, on_delete=models.CASCADE, related_name='bill_ID')
    billName = models.CharField(max_length=30, verbose_name="Utility Bill Name", choices=UTILITY_CHOICES, default='Water Bill')
    billAmount = models.IntegerField(default=0, verbose_name="Bill Amount")
    customerName = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    paymentDate = models.DateField(verbose_name="Date of Payment", auto_now=True)
    billDescription = models.CharField(verbose_name="Description of Bill to be Paid", max_length=100, default=None)

    def __str__(self):
        return self.billName

class FundsTransfer(models.Model):
    transferID = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Money Sender")
    transferAmount = models.IntegerField(verbose_name="Amount to transfer", default=0)
    transferAccount = models.OneToOneField(UserBankAccount, on_delete=models.CASCADE, related_name="transfer_account", verbose_name="Money Recipient")
    transferDate = models.DateField(verbose_name="Date of Funds Transfer", auto_now=True)
    transferDescription = models.CharField(max_length=200, verbose_name="Funds Transfer Description", default=None)
    
    def __str__(self):
        return str(self.transferID)
