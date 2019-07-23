import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import FormView

from core.forms.contact import ContactForm
from mysite.settings import ADMIN_EMAIL


class ContactView(FormView):
    template_name = 'contacts.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts')

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        captcha = form.cleaned_data['captcha']

        send_mail(subject, message, from_email, [ADMIN_EMAIL])
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        logger = logging.getLogger(__name__)
        logger.exception(messages)
        return super(ContactView, self).form_invalid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     subject = form.cleaned_data['subject']
    #     message = form.cleaned_data['message']
    #     from_email = form.cleaned_data['from_email']
    #     captcha = form.cleaned_data['captcha']
    #
    #     send_mail(subject, message, from_email, [ADMIN_EMAIL])
    #     # return super(ContactView, self).form_valid(form)
    #     if form.is_valid():
    #         messages.success(request, _('Message sended successfuly!'))
    #         return self.form_valid(form)
    #     else:
    #         messages.warning(request, _(
    #             'There was an unexpected error while sending the letter. Try using this form later.'))
    #         return self.form_invalid(form)