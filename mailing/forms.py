from django import forms

from common.views import StyleFormMixin
from mailing.models import MailingSettings, MailingMessage
from recipient.models import Recipient


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, request=None, **kwargs):
        # self.request = kwargs.pop('request')
        # user = self.request.user
        # super().__init__(*args, **kwargs)
        # self.fields['recipients'].queryset = Recipient.objects.filter(owner=user)
        # self.fields['message'].queryset = MailingMessage.objects.filter(owner=user)
        super().__init__(*args, **kwargs)
        if request is not None:
            self.fields['recipients'].queryset = Recipient.objects.filter(owner=request.user)
            self.fields['message'].queryset = MailingMessage.objects.filter(owner=request.user)


    class Meta:
        model = MailingSettings
        fields = ('sending', 'recipients', 'message', 'end_time',)


class MailingMessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('title', 'content',)


class MailingModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('setting_status',)