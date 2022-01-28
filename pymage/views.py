import glob
import os
import pickle
from PIL import Image, ImageEnhance
import numpy as np

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import csv
import pandas
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

from pymage.feature import feature

fe = feature()
features = []
img_paths = []
for feature_path in glob.glob("C:/Users/engas/mysite/media/ciri/*"):
    features.append(pickle.load(open(feature_path, 'rb')))
    img_paths.append('/media/img/' + os.path.splitext(os.path.basename(feature_path))[0] + '.jpg')


class Home(TemplateView):
    template_name = 'index.html'


def index(request):
    indexActive = 'active'
    pageTitle = 'Greyscale'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 2
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = url
        x = 0.1
        y = 0

        for i in range(1, 20, 1):
            direction = "C:/Users/engas/mysite" + url
            picturegreyscale = Image.open(direction)
            namafilebaru = direction[:-4] + ("%d.jpg" % (y + 1)) + direction[-4:]
            enhancer = ImageEnhance.Brightness(picturegreyscale)
            filebaru = enhancer.enhance(x).save(namafilebaru)
            i += 1
            x = x + 0.1
            y += 1
            print(x)
            print(y)
            print(i)
        return render(request, 'pymage/index.html', {
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'indexActive': indexActive,
            'displayFile': displayFile
        })
    return render(request, 'pymage/index.html', {
        'pageStatus': pageStatus,
        'pageTitle': pageTitle,
        'indexActive': indexActive
    })


def resolution(request):
    resolutionActive = 'active'
    pageTitle = 'resolution'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 2
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = url
        x = 7
        y = 0

        for i in range(1, 10, 1):
            direction = "C:/Users/engas/mysite" + url
            picturegreyscale = Image.open(direction)
            namafilebaru = direction[:-4] + ("%d.jpg" % (y + 1)) + direction[-4:]
            enhancer = ImageEnhance.Sharpness(picturegreyscale)
            filebaru = enhancer.enhance(x).save(namafilebaru)
            i += 1
            x = x - 1
            y += 1
            print(x)
            print(y)
            print(i)
        return render(request, 'pymage/resolution.html', {
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'resolutionActive': resolutionActive,
            'displayFile': displayFile
        })
    return render(request, 'pymage/resolution.html', {
        'pageStatus': pageStatus,
        'pageTitle': pageTitle,
        'resolutionActive': resolutionActive
    })


def contrast(request):
    contrastActive = 'active'
    pageTitle = 'contrast '
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 2
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = url
        x = 0.5
        y = 0

        for i in range(1, 5, 1):
            direction = "C:/Users/engas/mysite" + url
            picturegreyscale = Image.open(direction)
            namafilebaru = direction[:-4] + ("%d.jpg" % (y + 1)) + direction[-4:]
            enhancer = ImageEnhance.Contrast(picturegreyscale)
            filebaru = enhancer.enhance(x).save(namafilebaru)
            x = x + 0.2
            y += 1
        return render(request, 'pymage/contrast.html', {
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'contrastActive': contrastActive,
            'displayFile': displayFile
        })
    return render(request, 'pymage/contrast.html', {
        'pageStatus': pageStatus,
        'pageTitle': pageTitle,
        'contrastActive': contrastActive
    })


def rotate(request):
    rotateActive = 'active'
    pageTitle = 'Rotate'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 2
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = url
        return render(request, 'pymage/rotate.html', {
            'displayFile': displayFile,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'rotateActive': rotateActive
        })
    if request.GET.get('degree'):
        displayFile = request.GET['displayFromPallet']
        x = 10
        y = 0
        w = int(request.GET['degree'])
        for i in range(0, w, 10):
            direction = "C:/Users/engas/mysite" + displayFile
            pictureRotate = Image.open(direction)
            namafilebaru = direction[:-4] + ("%d.jpg" % (y + 1)) + direction[-4:]
            filebaru = pictureRotate.rotate((x), expand=1).save(namafilebaru)
            x = x + 10
            y += 1

        displayFileMod = displayFile[:-4] + ("%d.jpg" % y) + displayFile[-4:]
        pageStatus = 3
        print(displayFile)
        print(displayFileMod)
        return render(request, 'pymage/rotate.html', {
            'displayFile': displayFile,
            'displayFileMod': displayFileMod,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'rotateActive': rotateActive
        })
    return render(request, 'pymage/rotate.html', {
        'pageStatus': pageStatus,
        'pageTitle': pageTitle,
        'rotateActive': rotateActive
    })


def flip(request):
    flipActive = 'active'
    pageTitle = 'Flip'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = url
        pageStatus = 2
        return render(request, 'pymage/flip.html', {
            'displayFile': displayFile,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'flipActive': flipActive
        })
    if request.GET.get('leftright'):
        displayFile = request.GET['displayFromPallet']
        tujuan = "C:/Users/engas/mysite" + displayFile
        gambarFlip = Image.open(tujuan)
        namafilebaru = tujuan[:-4] + "_flip" + tujuan[-4:]
        # CONVERT MULAI DISINI MENGGUNAKAN FUNGSI transpose()
        filebaru = gambarFlip.transpose(Image.FLIP_LEFT_RIGHT).save(namafilebaru)
        displayFileMod = displayFile[:-4] + "_flip" + displayFile[-4:]
        print(displayFile)
        print(displayFileMod)
        pageStatus = 3
        return render(request, 'pymage/flip.html', {
            'displayFile': displayFile,
            'displayFileMod': displayFileMod,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'flipActive': flipActive
        })
    if request.GET.get('topbottom'):
        displayFile = request.GET['displayFromPallet']
        tujuan = "C:/Users/engas/mysite" + displayFile
        gambarFlip = Image.open(tujuan)
        namafilebaru = tujuan[:-4] + "_flip" + tujuan[-4:]
        filebaru = gambarFlip.transpose(Image.FLIP_TOP_BOTTOM).save(namafilebaru)
        displayFileMod = displayFile[:-4] + "_flip" + displayFile[-4:]
        pageStatus = 3
        print(displayFile)
        print(displayFileMod)
        return render(request, 'pymage/flip.html', {
            'displayFile': displayFile,
            'displayFileMod': displayFileMod,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'flipActive': flipActive
        })
    return render(request, 'pymage/flip.html', {
        'pageStatus': pageStatus,
        'pageTitle': pageTitle,
        'flipActive': flipActive
    })


def crop(request):
    cropActive = 'active'
    pageTitle = 'Crop'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 2
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = url
        return render(request, 'pymage/crop.html', {
            'displayFile': displayFile,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'cropActive': cropActive
        })
    if request.GET.get('x'):
        displayFile = request.GET['displayFromPallet']
        tujuan = "C:/Users/engas/mysite" + displayFile
        gambarCrop = Image.open(tujuan)
        namafilebaru = tujuan[:-4] + "_crop" + tujuan[-4:]
        # CONVERT MULAI DISINI MENGGUNAKAN FUNGSI crop()
        filebaru = gambarCrop.crop((float(request.GET['x']), float(request.GET['y']),
                                    float(request.GET['w']) + float(request.GET['x']),
                                    float(request.GET['h']) + float(request.GET['y']))).save(namafilebaru)
        displayFileMod = displayFile[:-4] + "_crop" + displayFile[-4:]
        pageStatus = 3
        print(displayFile)
        print(displayFileMod)
        return render(request, 'pymage/crop.html', {
            'displayFile': displayFile,
            'displayFileMod': displayFileMod,
            'pageStatus': pageStatus,
            'pageTitle': pageTitle,
            'cropActive': cropActive
        })
    return render(request, 'pymage/crop.html', {
        'pageStatus': pageStatus,
        'pageTitle': pageTitle,
        'cropActive': cropActive
    })
