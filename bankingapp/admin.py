from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bankingapp.models import UserProfile, UserBankAccount, UtilityCompany, UtilityPayment, FundsTransfer

class UserProfileAdmin(UserAdmin):
    pass

class UserBankAccountAdmin(admin.ModelAdmin):
    list_display = ('accountID','accountNumber','accountType','bankName','createdAt')
    list_filter = ('accountNumber','accountType','bankName','accountBalance','bankBranch')
    search_fields = ('accountNumber', 'accountID__first_name', 'accountID__last_name')
    #note the linking of accountID, a ForeignKey to the column of the table its linked to
    # without this, admin access will throw an icontains lookup error
    date_hierarchy = 'createdAt'
class UtilityCompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'companyAccountNum','companyAccountBalance')
    prepopulated_fields = {'slug':('companyName',)}
class UtilityPaymentAdmin(admin.ModelAdmin):
    list_display = ('billID', 'billName', 'billAmount', 'billDescription','customerName','paymentDate')
    date_hierarchy = 'paymentDate'
class FundsTransferAdmin(admin.ModelAdmin):
    list_display = ('transferID','transferAmount','transferAccount','transferDate','transferDescription')
    search_fields = ('transferAccount__accountID__first_name','transferAccount__accountID__last_name',)
    #note the chaining in the search because of the relationship between receipient and his bank account
    prepopulated_fields = {'slug':('transferID',)}

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserBankAccount, UserBankAccountAdmin)
admin.site.register(UtilityCompany, UtilityCompanyAdmin)
admin.site.register(UtilityPayment, UtilityPaymentAdmin)
admin.site.register(FundsTransfer, FundsTransferAdmin)
