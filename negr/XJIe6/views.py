import img as img
import menu as menu
from django.core.exceptions import PermissionDenied

from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseServerError, \
    HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from XJIe6.models import TheBestBooks

data_db = [
    {'id': 2, 'Author': 'Джеймс Джойс',
     'Summary': 'Роман повествует об одном дне дублинского обывателя еврейского происхождения Леопольда Блума (в настоящее время эта дата, 16 июня 1904 года, поклонниками романа отмечается как день Блума). Этот день Блум проводит в издательстве, на улицах и в кафе Дублина, на похоронах своего знакомого, на берегу залива, в родильном доме, где он знакомится со Стивеном Дедалом, молодым учителем в местной школе, в притоне и, наконец, в собственном доме, куда он поздно ночью приводит изрядно выпившего Дедала, лишившегося крова. Главной интригой романа является измена жены Блума, о которой Блум знает, но не предпринимает против неё никаких мер.Канва романа и его композиционное построение имеют явные и неявные аналогии с поэмой Гомера Одиссея. В произведении выведены и аналогичные персонажи: во многом автобиографичный Стивен Дедал (сюжетная линия Телемаха), Леопольд Блум (Одиссей, латинская форма этого имени Улисс послужила названием романа), Молли Блум (Пенелопа). Одной из главных тем романа является тема отец-сын, где в роли первго символически выступает Блум, в роли второго  Стивен. В романе находят отражение литературные стили и жанры различных эпох, стилевые особенности писателей, которых Джойс пародирует или которым подражает.'}

]


def index(request):
    posts = TheBestBooks.objects.all()
    data = {
        'title': 'Cтраница моей любимой книги',
        'menu': menu,
        'posts': posts,
    }
    print(posts)
    return render(request, 'XJIe6/index.html', context=data)


basa = {'id': 13, 'title': 'Игра в бисер', 'DateOfBith': '2 июля 1877',
        'Summary': 'В центре романа  легенда об одном из бывших Магистров игры, Йозефе Кнехте. Рассказ начинается с момента призвания совсем юного Йозефа Кнехта в касталийскую школу. Там он, среди прочего, знакомится с другим юношей, Плинио Дезиньори. Имена у персонажей говорящие. Кнехт  это слуга или раб, а Дезиньори  от сеньор  господин. Кнехт вынужден вступать в длительные дискуссии с Дезиньори, который по-мальчишески максималистски отрицает важность и значение всего касталийского уклада жизни. Плинио уезжает из Касталии с целью продолжить полноценную жизнь в настоящем мире, однако клянётся всегда оставаться другом и защитником касталийского мирка.Возмужавший Кнехт включается в иерархию руководителей Касталии. Вскоре ему поручают важную миссию  наладить контакт между Касталией и бенедиктинским монастырем Мариафельс. В этом монастыре проживает отец Иаков, имеющий большой авторитет в католической церкви, отношения с которой у кастальского братства далеки от идеальных. Кнехт блестяще справляется с этим заданием. В чертах отца Иакова угадывается его прототип  известный швейцарский историк Якоб Буркхардт.Кнехт поднимается до вершин иерархии и становится Мастером Игры. Но постепенно он приходит к мысли, что интеллектуалы не вправе замыкаться в башне из слоновой кости, а должны участвовать в реальной жизни. С этой целью Кнехт оставляет свой пост, покидает Касталию, приезжает к своему другу Дезиньори и соглашается стать наставником его сына. Через несколько дней он погибает, утонув в озере. '}


def negroid(request):
    data = {
        'title': 'Cтраница моей любимой книги',
        'menu': menu,
        'posts': basa,
        'cat_selected': 0,
    }


def show_book(request, book_slug):
    post = get_object_or_404(TheBestBooks, slug=book_slug)
    data = {
        'title': 'Cтраница моей любимой книги',
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'XJIe6/post.html', data)


def categories(request, cat_id, ):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Cтатьи по категориям<h1><p>{cat_id}</p>")


def archive(request, years):
    if years > 2023:
        uri = reverse('cats', args=('music'))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам<h1><p>{years}</p>")


def sdghsdfh(request, cat_slug, ):
    if cat_slug in '56a':
        raise PermissionDenied
    else:
        return HttpResponse(f"<h1>asgsdhdsfh1<h1><p>slug: {cat_slug}</p>")


def SFASFGAS(request):
    3 / 0
    return HttpResponse(f"<h1>asgsdhdsfh1<h1><p>slug: {3 / 0}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Cтраница не найдена<h1>')


def page403(request, exception):
    return HttpResponseForbidden('<h1>СМЕРТЬ<h1>')


def kub(request):
    return render(request, 'XJIe6/OMG3.html')


def animales(request):
    return render(request, 'XJIe6/animales.html')
