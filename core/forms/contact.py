from django import forms
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contacts')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-md-3 control-label'
        self.helper.field_class = 'col-md-8'

        # form buttons
        self.helper.add_input(Submit('send_button', _('Send'), css_class="btn-dark"))

    from_email = forms.EmailField(label=_('Your email'))
    subject = forms.CharField(label=_('Title message'), max_length=128)
    message = forms.CharField(label=_('Text message'), max_length=2560, widget=forms.Textarea)
    captcha = ReCaptchaField()

