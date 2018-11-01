# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

#Not right to use generic views without form Class

def upload_to_cloud_storage(file_name):

    from google.cloud import storage

    client = storage.Client.from_service_account_json('test-engine-service.json')
    bucket = client.get_bucket("senesence-bkt-1")
    blob = bucket.blob("user_demo/user_list.txt")
    blob.upload_from_filename(file_name)

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        print(username,email)

        file_name = "users.txt"

        f = open(file_name,"a+")
        f.write(username + "  " + email + "\n")
        f.close()

        upload_to_cloud_storage(file_name)

    return render(request,'index.html')
