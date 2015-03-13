import os
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import crypto
from zion.avatar.forms import UploadAvatarForm
from zion.settings import AVATAR_ROOT
from PIL import Image


def random_string(length):
    return crypto.get_random_string(length, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

def resizeimage(image, size, target, info=None, format=None):
    if isinstance(image, basestring):
        image = Image.open(image)
    if not info:
        info = image.info
    if not format:
        format = image.format
    if format == "GIF":
        if 'transparency' in info:
            image = image.resize((size, size), Image.ANTIALIAS)
            image.save(target, image.format, transparency=info['transparency'])
        else:
            image = image.convert("RGB")
            image = image.resize((size, size), Image.ANTIALIAS)
            image = image.convert('P', palette=Image.ADAPTIVE)
            image.save(target, image.format)
    if format == "PNG":
        image = image.resize((size, size), Image.ANTIALIAS)
        image.save(target, quality=95)
    if format == "JPEG":
        image = image.convert("RGB")
        image = image.resize((size, size), Image.ANTIALIAS)
        image = image.convert('P', palette=Image.ADAPTIVE)
        image = image.convert("RGB", dither=None)
        image.save(target, image.format, quality=95)
        
# Create your views here.
@login_required
def change_avatar(request):
    return render(request,
                 'change_avatar.html',
                {'user':request.user,
                })


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.delete_avatar_temp()
            image = form.cleaned_data['avatar_upload']
            image_extension = image.name.lower()[-4:]
            image_name = '%s_tmp_%s%s' % (request.user.pk, random_string(8), image_extension)
            image_path = AVATAR_ROOT + image_name
            with open(image_path, 'wb+') as fp:
                for chunk in image.chunks():
                    fp.write(chunk)
            request.user.avatar_temp = image_name
            request.user.save()
            try:
            	source = Image.open(image_path)
            	if not source.format in ['PNG', 'GIF', 'JPEG']:
            		raise ValidationError()
            	source.save(image_path)
            except ValidationError:
                request.user.delete_avatar_temp()
            	errors = form._errors.setdefault("avatar_upload", ErrorList())
                errors.append(u"Only png, gif or jpeg is allowed")
            
            return redirect('crop/')

    else:
        form = UploadAvatarForm()
            
    return render(request,
                  'upload_avatar.html',
                  {'user':request.user,
                   'form':form,
                  })

@login_required
def crop(request):
    if request.method == 'POST':
        tmpimage_path = AVATAR_ROOT + request.user.avatar_temp
        source = Image.open(tmpimage_path)
		# Crop the uploaded temp image
        width, height = source.size
        aspect = float(width) / float(request.POST['crop_b'])
        crop_x = int(aspect * float(request.POST['crop_x']))
        crop_y = int(aspect * float(request.POST['crop_y']))
        crop_w = int(aspect * float(request.POST['crop_w']))
        crop = source.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_w))
        	
        image_extension = request.user.avatar_temp[-4:]
        image_name = '%s_%s%s' % (request.user.pk, random_string(8), image_extension)
		# Resize the crop image to 125 and save it as avatar image
        resizeimage(crop, 125, AVATAR_ROOT + image_name, info=source.info, format=source.format)
  	    # Create avatars of different sizes
        for size in (100, 80, 60, 40, 24):
            resizeimage(crop, size, AVATAR_ROOT + str(size) + '_' + image_name, info=source.info, format=source.format)
		# Update new avatar
        request.user.delete_avatar_image()
        request.user.avatar_image = image_name
        request.user.has_avatar = True
        request.user.save(force_update=True)
        return redirect('/user/chavatar/')

    return render(request,
                  'crop_avatar.html',
                  {'user':request.user,
				   'image_path': '/static/avatars/%s' % request.user.avatar_temp,
                  })


