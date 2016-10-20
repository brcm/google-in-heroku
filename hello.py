# coding=utf-8
import os
import sys
__import__('BaseHTTPServer').BaseHTTPRequestHandler.address_string = lambda x:x.client_address[0]
from wsgiref.simple_server import make_server
import urllib2

reload(sys)   
sys.setdefaultencoding('utf-8')

def application(environ,start_response):

    sourceUrl = "https://www.google.com"

    try:
        requestUrl = str(environ["PATH_INFO"])+"?"+str(environ["QUERY_STRING"])
        httpHost = str(environ["HTTP_HOST"])
        try:
            httpAccept = str(environ["HTTP_ACCEPT"])
        except:
            httpAccept = ""
        try:
            userAgent = str(environ["HTTP_USER_AGENT"])
        except:
            userAgent = ""
        try:
            httpCookie = str(environ["HTTP_COOKIE"])
        except:
            httpCookie = ""
        try:
            httpLang = str(environ["HTTP_ACCEPT_LANGUAGE"])
        except:
            httpLang = ""
        try:
            httpEncode = str(environ["HTTP_ACCEPT_ENCODING"])
        except:
            httpEncode = ""
        try:
            bodyLength = int(environ.get('CONTENT_LENGTH', '0'))
        except ValueError:
            bodyLength = 0
    except:
        requestUrl = ""
    
    # Google Change Options
    if requestUrl == "/?":
        requestUrl = "/?hl=zh-CN"
    requestUrl = requestUrl.replace('safe=strict','safe=off')
    
    # Advs block listener
    if str(environ["PATH_INFO"]) == '/cdn-dat/adb':
        html = ""
        status = '200 OK'
        response_headers  =  [('Content-Type', 'text/html;charset=utf-8'),('Cache-Control', 'public, max-age=2592000'),('Content-Length', str(len(html)))]
        start_response(status, response_headers)
        return html

    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('Accept',httpAccept)]
        opener.addheaders = [('Accept-Encoding',httpEncode)]
        opener.addheaders = [('Accept-Language',httpLang)]
        opener.addheaders = [('Cookie',httpCookie)]
        opener.addheaders = [('User-Agent', userAgent)]
        if bodyLength != 0:
            body = environ['wsgi.input'].read(bodyLength)
            html = opener.open(sourceUrl+requestUrl, body).read()
        else:
            html = opener.open(sourceUrl+requestUrl).read()

        # Replace the blocked resource
        html = html.replace('https://ajax.googleapis.com/ajax/libs/jquery/','//cdn.bootcss.com/jquery/')
        html = html.replace('https://ajax.googleapis.com/ajax/libs/angularjs/','//cdn.bootcss.com/angular.js/')
        html = html.replace('Google.com in English','RazerNiz Forwarder 1.0')
        html = html.replace(sourceUrl,'//' + httpHost)
        
        # Filter Advs Javascripts
        html = html.replace('//imasdk.googleapis.com/','/cdn-dat/adb?')
        html = html.replace('/xjs/_/js/','/cdn-dat/adb?')
        html = html.replace('//pagead2.googlesyndication.com/','/cdn-dat/adb?')
        html = html.replace('//partner.googleadservices.com/','/cdn-dat/adb?')
        html = html.replace('//www.googletagservices.com/','/cdn-dat/adb?')
        html = html.replace('//www.google-analytics.com/','/cdn-dat/adb?')
        html = html.replace('//apis.google.com','/cdn-dat/adb?')
        html = html.replace('//plus.google.com/','/cdn-dat/adb?')
        html = html.replace('//ogs.google.com/','/cdn-dat/adb?')
        html = html.replace('//client5.google.com/','/cdn-dat/adb?')
        html = html.replace('//client4.google.com/','/cdn-dat/adb?')
        html = html.replace('www.gstatic.com','www.baidu.com')
        
        status = '200 OK'
    except:
        html = "<html><head><title>Forwarder Unavailable</title></head><body><center><h1>Forwarder Unavailable</h1><hr/>RazerNiz Forwarder 1.0</center></body></html>"
        status = '503 Forwarder Unavailable'
    
    response_headers  =  [('Content-Type', 'text/html; charset=UTF-8'),('Cache-Control', 'public, max-age=86400'),('Content-Length', str(len(html)))]
    start_response(status, response_headers)

    return html

port = int(os.environ.get("PORT",5000))
httpd = make_server('0.0.0.0',port,application)
httpd.serve_forever()