import random
import time

OTP_EXPIRE_SECONDS = 60

def generate_otp():
    return str(random.randint(1000,9999))

def create_otp_session(request,phone):
    
    code = generate_otp()
    
    request.session["otp"]= {
        "phone":phone,
        "code":code,
        "expire_at":time.time() + OTP_EXPIRE_SECONDS,
    }
    print(code)
    request.session.modified = True
    
def verify_otp(request,phone,code):
    otp_date = request.session.get("otp")
    
    if not otp_date:
        return False
    
    if otp_date["phone"] != phone:
        return False
    
    if time.time() > otp_date["expire_at"]:
        request.session.pop("otp",None)
        return False
    
    if otp_date["code"] != code:
        return False
    
    request.session.pop("otp",None)
    
    return True