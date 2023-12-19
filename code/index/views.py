from django.shortcuts import render, HttpResponse


# Create your views here.


# Create your views here.
def index(request):
    return HttpResponse('''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>Devsapp</h1>
        <h2>William</h2>
        <span>ceshi</span>
        <br/>
        <p>您也可以快速体验： <br/>
            • 这个是第一个通过FC部署的应用
            • 下载Serverless Devs工具：npm install @serverless-devs/s<br/>
            • 初始化项目：s init start-django-v3<br/>

            • 项目部署：s deploy<br/>
            <br/>
            Serverless Devs 钉钉交流群：33947367
        </p>
    </div>
</div>
</body>
</html>''')
