from flask import Blueprint,render_template,request,redirect,url_for,send_file,session
import os
from pytube import YouTube
from io import BytesIO



views=Blueprint('views',__name__)


           

       
       



@views.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
           session['url_vid']=request.form.get('url_vid')
           try:
            vid = YouTube(session['url_vid'])
            vid.check_availability()
           except:
            return "<p>ERROR</>" 
           return render_template('download.html',vid=vid)
        
    return render_template('home.html')


@views.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
           vid = YouTube(session['url_vid'])
           stream=vid.streams.filter(only_audio=True).first()
           buffer=BytesIO()
           stream.stream_to_buffer(buffer)
           buffer.seek(0)
           return send_file(buffer , as_attachment=True,download_name='music.mp3',mimetype='audio/mp3')



           
    return render_template('download.html')



