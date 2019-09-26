from django.shortcuts import render


def collection_html(request):
    context = {
        "data":[
            {"title": "常用网站", "id": "collapse1", "collapses": [
                {"name": "GitHub", "href":"https://github.com/"},
                {"name": "知乎", "href":"https://www.zhihu.com"},
                {"name": "哔哩哔哩", "href": "https://www.bilibili.com/"},
                {"name": "腾讯云", "href": "https://cloud.tencent.com/"},
            ]},
            {"title": "工具", "id": "collapse2", "collapses": [
                {"name": "网站导航(一个开始)", "href":"https://aur.one/"},
                {"name": "在线PS", "href":"https://ps.gaoding.com/#/?hmsr=zc-cc"},
                {"name": "JS在线测试","href":"https://www.w3school.com.cn/tiy/t.asp?f=html_basic"},
            ]},
            {"title": "电子书", "id": "collapse3", "collapses": [
            {"name": "epubw(优质)", "href":"https://epubw.com/"},
                    {"name": "万千合集站(学术)", "href":"http://www.hejizhan.com/bbs/"},
                    {"name": "周读(有评分)", "href":"http://www.ireadweek.com/"},
                    {"name": "田间小站(英文)", "href":"https://www.tianfateng.cn/"},
                    {"name": "杂志", "href":"http://www.ifblue.net/"},
                    {"name": "E书联盟", "href":"https://book118.com/"},
                    {"name": "搜索引擎汇总", "href":"https://ebook.chongbuluo.com/"},
             ]},
            {"title": "菜单栏", "id": "collapse_menu", "collapses": [
                {"name": "Notebook", "href": "/tools/notebook"},
                {"name": "Face Recognition", "href": "/tools/face_recognition"},
            ]},
        ],
        "msg": "success",
    }
    return render(request,'collection.html', context)
