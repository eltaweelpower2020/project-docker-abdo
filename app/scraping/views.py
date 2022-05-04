from asyncio import sleep
from genericpath import exists
from lib2to3.pgen2 import driver
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import urllib
import requests

import csv
from itertools import zip_longest
import re
from selenium.common.exceptions import ElementClickInterceptedException

import requests
import os

from .forms import FaceBookForm
from .models import FaceBook_Data_Login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


BASE_DIR = Path(__file__).resolve().parent.parent
@login_required(login_url='/login/')
def home(request):
     form = FaceBookForm()
     if request.method =='POST':
        form = FaceBookForm(request.POST)
        if form.is_valid():
               facebook_data_login = form.save(commit=False)
               facebook_data_login.owner=request.user
               facebook_data_login.save()
               return redirect('get_all_adds_face_insta')

     return render(request,'home.html',{'form':form})

@login_required(login_url='/login/')
def get_all_face_insta_accounts(request):
     accounts=FaceBook_Data_Login.objects.filter(owner=request.user)
     
     return render(request,'list-all-accounts.html',{'accounts':accounts})

@login_required(login_url='/login/')
def get_all_adds_face_insta(request):
     # facebook_info=FaceBook_Data_Login.objects.filter(owner=request.user).first()
     facebook_info=FaceBook_Data_Login.objects.filter(owner=request.user).last()
     created_by_all=scrapingfunction(facebook_info)
     if created_by_all:
          print(facebook_info,"infooooooooooooooooooooooooooooo")
          print("user exist ")
     else:
          print('user face book not valid')
          return HttpResponse("Facebook or Instagram account is not valid ")
     return render(request,'all_ads.html',context={'created_by_all':created_by_all})

@login_required(login_url='/login/')
def home(request):
     form = FaceBookForm()
     if request.method =='POST':
        form = FaceBookForm(request.POST)
        if form.is_valid():
               facebook_data_login = form.save(commit=False)
               facebook_data_login.owner=request.user
               facebook_data_login.save()
               return redirect('get_all_adds_face_insta')

     return render(request,'home.html',{'form':form})

@login_required(login_url='/login/')
def get_all_face_insta_accounts(request):
     accounts=FaceBook_Data_Login.objects.filter(owner=request.user)
     
     return render(request,'list-all-accounts.html',{'accounts':accounts})

@login_required(login_url='/login/')
def get_specific_account(request,faceid):
     facebook_info=FaceBook_Data_Login.objects.get(owner=request.user,id=faceid)
     created_by_all=scrapingfunction(facebook_info)
     if created_by_all:
          print(facebook_info,"infooooooooooooooooooooooooooooo")
          print("user exist ")
     else:
          print('user face book not valid')
          return HttpResponse("Facebook or Instagram account is not valid ")
     
     # print(created_by_all,"alllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
     return render(request,'all_ads.html',context={'created_by_all':created_by_all})















def scrapingfunction(facebook_info):
     facebook_email=facebook_info.facebook_email
     facebook_password=facebook_info.facebook_password     

     option = Options()
     option.headless = True
     option.add_argument("--disable-infobars")
     option.add_argument("start-maximized")
     option.add_argument("--disable-extensions")
     option.add_experimental_option("prefs", { 
     "profile.default_content_setting_values.notifications": 1 
     })

     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
     
     driver.get("http://www.facebook.com")
     
     driver.maximize_window()
    
     username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
     password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

     username.clear()
     # username.send_keys("Abdelrahmanmahersoliman@gmail.com")
     username.send_keys(facebook_email)
     password.clear()
     # password.send_keys("MarketerMaher&@2022")
     password.send_keys(facebook_password)
     button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
     time.sleep(1)
     driver.get("https://business.facebook.com/latest/ad_center/all_ads?asset_id=103805231874047&nav_ref=pages_classic_isolated_section_inbox_redirect")
     parent_ads_window=driver.current_window_handle
     print(parent_ads_window)
     ads_table_header=driver.find_elements_by_xpath("//*[contains(@class, 'e7u0oozg snfsxcfg hgenzi0p oysqpf8i tpry4lk2 svz86pwt aa8h9o0m a53abz89')]")
     ads_table_header=[a.text for a in ads_table_header]

     ads_table_body_all=driver.find_elements_by_xpath("//div[@class='a53abz89 rgsc13q7 dfy4e4am rwb8dzxj tnsgtkb9 tq305v7h']")
     created_by_all=[]
     for index,ads_row in enumerate(ads_table_body_all):
          created_by=ads_row.find_element_by_xpath(".//div[@class='e7u0oozg svdiirva jbfqbifr all6rvt3 tpry4lk2 a53abz89 lgsfgr3h mcogi7i5 ih1xi9zn kiex77na']")
          boosted=ads_row.find_element_by_xpath(".//div[@class='e7u0oozg snfsxcfg oysqpf8i tpry4lk2 svz86pwt aa8h9o0m jrvjs1jy a53abz89']")
          status=ads_row.find_element_by_xpath(".//div[@class='e7u0oozg svdiirva all6rvt3 qwtvmjv2 kiex77na lgsfgr3h mcogi7i5 ih1xi9zn ippphs35 a53abz89']")
          reach=ads_row.find_element_by_xpath('//*[@id="facebook"]/body/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/span[1]/div')
          objective=ads_row.find_element_by_xpath(".//div[@class='e7u0oozg svdiirva all6rvt3 c17vnioq svz86pwt aa8h9o0m jrvjs1jy a53abz89 n4assd27 lgsfgr3h mcogi7i5 mb1d602y'][contains(text(),'li')]")
          amount_spent=ads_row.find_element_by_xpath(".//div[@class='gdqlzcdm fywgc7xc kzv4m4hs tpry4lk2 svz86pwt aa8h9o0m jrvjs1jy a53abz89'][contains(text(),'.')]")
          total_amount=ads_row.find_element_by_xpath(".//div[@class='e7u0oozg svdiirva all6rvt3 c17vnioq svz86pwt aa8h9o0m jrvjs1jy a53abz89 n4assd27 lgsfgr3h mcogi7i5 mb1d602y'][contains(text(),'.')]")
          view_result_button=ads_row.find_element_by_xpath('.//div[@class="rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t d2edcug0 hpfvmrgz rj1gh0hx buofh1pr g5gj957u ph5uu5jm b3onmgus e5nlhep0 ecm0bbzt"]')
          view_all_results_numbers=ads_row.find_elements_by_xpath('//*[@aria-level="3"][@class="gdqlzcdm fywgc7xc kzv4m4hs tpry4lk2 svz86pwt aa8h9o0m jrvjs1jy a53abz89"][@role="heading"]')
          first=(index+2)+((index-1)*2)
          last=(index+3)+(index*2)
          results_numbers=[number.text for number in view_all_results_numbers][first:last]
          reach=(results_numbers[0])
          objective=float(results_numbers[1])
          amount_spent=float(results_numbers[2].split('EGP')[1])
          Cost_per_Link_Click=round(amount_spent/objective,2)
          image_url=''
          try:
               view_result_button.click()
               time.sleep(3)
               ads_row.find_element_by_xpath('//*/div/div[2]/div/div[1]/div/div/div/div/span/div/div').click()
               time.sleep(2)

               driver.switch_to.frame(driver.find_elements(by=By.TAG_NAME,value='iframe')[0])
               time.sleep(2)
               image_url=driver.find_element_by_xpath(".//img[@class='_8b2z img']").get_attribute("src")
               print(image_url,"imageeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees")
               driver.switch_to.parent_frame()
               
               view_cancel_button=driver.find_element_by_xpath( './/div[@class="oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv j83agx80 taijpn5t jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 tv7at329 thwo4zme tdjehn4e"]')
          except ElementClickInterceptedException:
               print("Trying to click on the button again 222222222222222222222222222222222222222222222")
               view_cancel_button.click()
          view_cancel_button.click()
          time.sleep(3)
          ads_row.find_element_by_xpath('//*[@id="facebook"]/body/div[6]/div[2]/div[1]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/span/div/div/div').click()
          
          time.sleep(3)

          created_by_all.append({
               'created_by':created_by.text,
               'boosted':boosted.text,
               'status':status.text,
               'reach':reach,
               'objective':objective,
               'amount_spent':amount_spent,
               'total_amount':total_amount.text,
               'view_result_button':view_result_button.text,
               'view_result_button_function':view_result_button,
               'Cost_per_Link_Click':Cost_per_Link_Click,
               'image_url':image_url
          })

          
     

     print(created_by_all)
     time.sleep(1)
     driver.close()
     return created_by_all
