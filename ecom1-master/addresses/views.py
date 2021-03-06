from django.shortcuts import render,redirect
from django.views.generic import View,CreateView
from django.utils.http import is_safe_url
from billing.models import BillingProfile
from .forms import AddressForm
def checkout_address_create_view(request):
	form=AddressForm(request.POST,None)
	next_=request.GET.get('next')
	next_post=request.POST.get('next')
	redirect_path=next_ or next_post or None
	if form.is_valid():
		instance=form.save(commit=False)
		billing_profile,billing_profile_created=BillingProfile.objects.new_or_get(request)
		if billing_profile is not None:
			instance.billing_profile=billing_profile
			address_type=request.POST.get('address_type')
			print("address_type :".format(request.POST.get('address_type')))
			instance.address_type=address_type
			instance.save()
			request.session[address_type + '_address_id']=instance.id
			print(address_type + '_address_id')
		else:
			print("some thing error here.")
			return redirect('carts:checkout')
		if is_safe_url(redirect_path,request.get_host()):
			return redirect(redirect_path)
		else:
			return redirect('carts:checkout')
	return redirect('carts:checkout')
