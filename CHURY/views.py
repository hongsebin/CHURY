from django.shortcuts import render

# Create your views here.


from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


# 이메일 전송
# def password_reset_request(request): 
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = get_user_model().objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "registration/password_reset_subject.txt"
# 					email_template_name = "registration/password_reset_email.txt"
# 					c = {
# 						"email": user.email,
# 						'domain': settings.HOSTNAME,
# 						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 						"user": user,
# 						'token': default_token_generator.make_token(user),
# 						'protocol': settings.PROTOCOL,
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(
#           					subject, email, 'churybooks@gmail.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(
# 		request=request,
# 		template_name='registration/password_reset.html',
# 		context={'password_reset_form': password_reset_form})