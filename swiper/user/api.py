from django.http import JsonResponse
from django.utils import cache

from common import keys, errors
from lib.http import render_json
from lib.sms import send_sms
from django.core.cache import cache

from user.forms import ProfileForm
from user.models import User
from user.logics import handle_upload_avatar

# Create your views here.



def submit_phone(request):
    """先提交手机号码"""
    phonenum = request.POST.get('phone')
    # 拿到手机号码应该去发短信.
    send_sms(phonenum)
    return JsonResponse({'data': 'ok', 'code': 0})


def submit_vcode(request):
    """获取验证登录注册"""
    phonenum = request.POST.get('phone')
    vcode = request.POST.get('vcode')
    # 判断发送的短信验证码何获取的短信验证码是否一致.
    # 从缓存中取出验证码
    cached_vcode = cache.get(keys.VCODE_KEY % phonenum)
    print('缓存的验证码是:', cached_vcode)
    if vcode == cached_vcode:
        user, created = User.objects.get_or_create(phonenum=phonenum, nickname=phonenum)
        # 登录
        request.session['uid'] = user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(data='验证码错误', code=errors.VCODE_ERR)


def get_profile(request):
    """获取个人资料"""
    uid = request.session['uid']
    user = User.objects.get(id=uid)
    return render_json(user.profile.to.dict())

def edit_profile(request):
    """修改个人资料"""
    profileform = ProfileForm(request.POST)
    user = User.objects.get(id=request.session['uid'])
    if property.is_valid():
        profile = profileform.save(commit=False)
        user.profile = profile
        profile.save()
        return render_json(profile.to_dict())
    else:
        return render_json(profileform.errors, errors.FROFILE_ERR)


def upload_avatar(request):
    """头像上传"""
    avatar = request.FILES.get('avatar')
    print(type(avatar))
    print(avatar.name)
    uid = request.session['uid']
    user = User.objects.get(id=uid)
    handle_upload_avatar.delay(user, avatar)
    return render_json(user.avatar)
