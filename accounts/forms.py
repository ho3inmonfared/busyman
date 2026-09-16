from django import forms


class PhoneForm(forms.Form):

    phone = forms.CharField(
        max_length=11,
        min_length=11
    )

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if not phone.isdigit():
            raise forms.ValidationError(
                "شماره موبایل باید فقط شامل عدد باشد."
            )

        if not phone.startswith("09"):
            raise forms.ValidationError(
                "شماره موبایل معتبر نیست."
            )

        return phone


class OTPForm(forms.Form):

    code = forms.CharField(
        max_length=4,
        min_length=4
    )

    def clean_code(self):
        code = self.cleaned_data["code"]

        if not code.isdigit():
            raise forms.ValidationError(
                "کد تایید باید عددی باشد."
            )

        return code


class ProfileForm(forms.Form):

    first_name = forms.CharField(
        max_length=255
    )

    last_name = forms.CharField(
        max_length=255
    )