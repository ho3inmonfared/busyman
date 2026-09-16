from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model

from .forms import PhoneForm, OTPForm, ProfileForm
from .otp import create_otp_session, verify_otp


User = get_user_model()


def phone_login(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = PhoneForm(request.POST)

        if form.is_valid():

            phone = form.cleaned_data["phone"]

            request.session["auth_phone"] = phone

            create_otp_session(
                request,
                phone
            )

            return redirect("accounts:verify_otp")

    else:
        form = PhoneForm()

    return render(
        request,
        "accounts/phone.html",
        {
            "form": form
        }
    )


def verify_otp_view(request):

    phone = request.session.get("auth_phone")

    if not phone:
        return redirect("accounts:phone_login")

    if request.method == "POST":

        form = OTPForm(request.POST)

        if form.is_valid():

            code = form.cleaned_data["code"]

            valid = verify_otp(
                request,
                phone,
                code
            )

            if not valid:

                form.add_error(
                    "code",
                    "کد تایید اشتباه یا منقضی شده است."
                )

            else:

                user = User.objects.filter(
                    phone=phone
                ).first()

                if user:

                    login(request, user)

                    request.session.pop(
                        "auth_phone",
                        None
                    )

                    return redirect("home")

                request.session["verified_phone"] = phone

                return redirect(
                    "accounts:complete_profile"
                )

    else:

        form = OTPForm()

    return render(
        request,
        "accounts/verify_otp.html",
        {
            "form": form,
            "phone": phone
        }
    )


def complete_profile(request):

    phone = request.session.get("verified_phone")

    if not phone:
        return redirect("accounts:phone_login")

    if request.method == "POST":

        form = ProfileForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                phone=phone,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )

            login(request, user)

            request.session.pop(
                "verified_phone",
                None
            )

            return redirect("home")

    else:

        form = ProfileForm()

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form
        }
    )


def logout_view(request):

    if request.user.is_authenticated:

        logout(request)

    return redirect("accounts:phone_login")