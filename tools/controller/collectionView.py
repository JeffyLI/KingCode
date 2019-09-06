from django.shortcuts import render


def collection(request):
    context = {
        "data":[
            {"title": "常用网站", "id": "collapse1", "collapses": [
                {"name":"GitHub", "href":"https://github.com/"},
                {"name":"知乎", "href":"https://www.zhihu.com"},
                {"name": "哔哩哔哩", "href": "https://www.bilibili.com/"},
            ]},
            {"title": "学习", "id": "collapse2", "collapses": [
                {"name":"网站导航(一个开始)", "href":"https://aur.one/"},
                {"name":"力扣", "href":"https://leetcode-cn.com/"}
            ]},
        ],
        "msg": "success",
    }
    return render(request,'collection.html', context)