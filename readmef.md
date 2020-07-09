1. 每个页面验证用户登陆 
--Done
        # 导入django自带模块        
        from django.contrib.auth import authenticate, login, logout        
        # 使用authenticate进行认证，使用login方法将user写入session
        user = authenticate(username=username, password=password)
                if user:
                    print("passed authencation", user)
                    login(request, user)
        # 使用 logout(request)注销用户        
        # 自动跳转的实现：
        # 导入django自带装饰器
        from django.contrib.auth.decorators import  login_required
        # 在视图函数前加@login_required装饰器，当用户访问当前视图，若未登录则会自动跳转到登录页，
        #如何修改默认的登录页？在setting文件中配置登录页的url
        LOGIN_URL = '/login/'
        # 在登录的视图函数中获取next对应的url，认证成功之后跳转，这样就实现了登录之后自动跳转到原页面
        return redirect(request.GET.get('next', '/'))


2. 每个页面显示用户名:
--Done for list.html
        在 views里取值是这样的
        request.user.username

        而在模板页面取值是这样的：
        {{request.user}}

        判断是否通过验证是这样的
        {% if request.user.is_authenticated %}

3. 每个页面提供logout 功能:
--Done
        每个html添加以下，并引用自定义CSS
        <link rel="stylesheet" href="{% static 'bootstrap-3.3.7-dist/css/user-defined-theme.css' %}">
        <div class="user_label">
         <a href="">Welcome! {{ request.user }}</a>
         <label > </label>
         <a href="{% url 'logout' %}" class="logout"> Logout</a>
        </div>

4. 数据存入数据库；
5. 增加用户;
6. 用户登陆要求-done
7. 用户界面细化， 如未完成一个tab， 已完成一个tab， update comment功能；
8. Jira 数据展示；
9. List 界面 点击 task 计入详情页；
10. bug fix: refresh the last entered content will be saved.

4. 界面美化； update/delete etc..