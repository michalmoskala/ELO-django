from django import forms


from .models import Msg


class MessageForm(forms.ModelForm):
    content = forms.CharField(
                        required=True, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your message",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    
    class Meta:
        model = Msg
        fields = [
            'content',
            'receiver_id',
            'sender_id',
        ]