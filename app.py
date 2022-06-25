from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return "<!DOCTYPE>
<html>
<head>
    <meta charset="utf-8">
    <title>Хьюстон</title>
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
<body>
    <h1 id="top">Х'юстон</h1>
    <p><b>Х'юстон</b> (англ. Houston) - четверте за кількістю жителів місто в Сполучених Штатах Америки та найбільше місто в штаті Техас з населенням 2 319 603 особи на 2017 рік. Х'юстон є адміністративним центром округу Харріс, а також головним економічним центром агломерації Великого Х'юстона із загальним населенням 6772470 осіб на 2016 рік. Місто розташоване за 50 кілометрів від Мексиканської затоки на прибережній рівнині.</p>
    <p>Х'юстон був заснований 30 серпня 1836 і включений до складу республіки Техас 5 червня 1837, отримавши своє ім'я на честь Семюела Х'юстона - головнокомандувача армією Техасу під час Техаської революції і президента Республіки Техас. Швидкий розвиток порту і залізниць в XIX столітті, а також початок видобутку нафти і розвиток нафтової промисловості в XX столітті призвели до швидкого зростання населення. У 1960-ті роки кількість жителів перевищила один мільйон людей, а в 2000-х — два мільйони.</p>
    <p>Город является ведущим мировым центром энергетической промышленности, а экономика города также представлена предприятиями в области аэронавтики, транспорта и здравоохранения. Важнейшими объектами для экономики и инфраструктуры города являются космический центр имени Линдона Джонсона, крупнейший американский по международным грузоперевозкам порт, хьюстонский судоходный канал, крупнейший в мире Техасский медицинский центр.</p>
    <h2>Зміст</h2>
    <ol>
    <li><a href="#history">Історія</a></li>
        <ol>
        <li><a href="#surname">Етимологія, прізвища</a></li>
        <li><a href="#establishment">Заснування</a></li>
        <li><a href="#century">XX століття</a></li>
        </ol>
    <li><a href="#characteristic">Фізико-географічна характеристика</a></li>
        <ol>
        <li><a href="#climat">Географічне положення і клімат</a></li>
        <li><a href="#relief">Рельеф, підземні води</a></li>
        <li><a href="#flora">Флора і фауна</a></li>
        </ol>
    <li><a href="#economy">Економіка</a></li>
        <ol>
        <li><a href="#general">Загальне становище</a></li>
        <li><a href="#energ">Енергетика і нефтехімія</a></li>
        <li><a href="#avia">Авіакосмічна промисловість</a></li>
        </ol>
    <li><a href="#people">Населення</a></li>
        <ol>
        <li><a href="#dinamic">Динаміка і структура населення</a></li>
        <li><a href="#language">Етнічний і конфесійний склад, мови</a></li>
        </ol>
    <li><a href="#zmi">Засоби масової інформації</a></li>
    <li><a href="#town-brother">Міста-побратими</a></li>
    </ol>
    
    <h2 id="history">Історія</h2>
    <h3 id="surname">Етимологія, прізвища</h3>
    <figure class="sign">
    <img src="hust/Sam_Houston_portrait.jpg">
    <figcaption>Семюел Х'юстон</figcaption>
    </figure>
    <p>Місто названо на честь Семюела Х'юстона - головнокомандувача армії Техасу під час Техаської
революції (1835-1836) та президента Республіки Техас (1836-1838, 1841-1844).</p>
<p>Офіційне прізвисько Х'юстона - Space city, яке можна перекласти як космічний.
місто», «місто космонавтики» чи «космоград». Назва дана через те, що тут знаходиться
космічний центр імені Ліндона Джонсона. Загалом місто має 12 прізвиськ.</p>
<p>В американському розмовному мовленні є популярна фраза: «<b>Хьюстон, у нас проблема</b>» (англ.
Houston, we’ve had a problem), що з'явилася після невдалої місії Аполлон-13. У Х'юстоні
проходили зйомки фільму «Аполлон-13», основою сюжету якого стали реальні події місії.</p>
    <h3 id="establishment">Заснування</h3>
    <figure class="img">
    <img src="hust/Allen's_Landing_Houston_bayou_view.jpg">
    <figcaption>Allen’s Landing — місце, де було <br>засновано місто</figcaption>
    </figure>
    <p>Після закінчення війни за незалежність Техасу, у серпні 1836 року підприємці брати Август
і Джон Алени купили 26,9 км2 землі вздовж річки Буффало-Байю, плануючи заснувати на ній
населений пункт. Вони хотіли, щоб майбутнє місто стало столицею Техасу та великим торговим
        центром.</p>
    <p>Датою заснування міста прийнято вважати 30 серпня 1836 року, коли брати Олени розмістили
оголошення про появу міста. Місто назвали на честь генерала Сема Х'юстона, який очолював
армію техасців у битві при Сан-Хасінто під час війни проти Мексики, пізніше обраного
президентом Техасу. На січень 1837 року у селищі проживало лише 12 осіб, проте через чотири
місяця населення зросло до 1500 чоловік. 5 червня 1837 року місто було включено до округу Гаррісберг.
(нині Харріс) і став тимчасовою столицею Республіки Техас, якою залишався до 1839 року.
Першим мером Х'юстона став Джеймс Холман.</p>
    <br><br>
    <h3 id="century">XX століття</h3>
    <figure class="sign">
    <img src="hust/Main_Street_looking_south_Houston_Texas_(1908).jpg" >
    <figcaption>Мейн-Стріт у центрі, 1908 рік</figcaption>
    </figure>
    <p>У 1900 році на Х'юстон обрушився Галвестонський ураган, що тривав з 27 серпня до 12
вересня. У перерахунку на сьогоднішній курс збитки склали б $526 млн, загинуло 8 тисяч людей. В
наступного року було знайдено велике родовище нафти поблизу міста Бомонт, що послужило
початком розвитку нафтової промисловості у Техасі. У 1902 році президент США Теодор Рузвельт
затвердив проект вартістю $1 млн на реконструкцію Х'юстонського судноплавного каналу. До 1910
році чисельність населення міста досягла 78 800 осіб, майже вдвічі перевищивши кількість
жителів що у Х'юстоні 1900 року.У 1914 році президент США Вудро Вільсон прийняв
участь у відкритті нового глибоководного порту Х'юстона, а через рік було відкрито Х'юстонський
        судноплавний канал.</p>
    <p>У 1945 році було розпочато формування Техаського медичного центру. Наприкінці 1940-х кілька
передмістя були включені в межу, в результаті чого площа Х'юстона збільшилася
більш ніж удвічі. У 1950-ті роки управління багатьох великих (переважно нафтових) компаній
США перемістилися в Х'юстон, що сприятливо позначилося на економіці міста, одним із
приводів для переїзду стало масове оснащення всіх офісів кондиціонерами.</p>
    <blockquote>
    <p>Саме кондиціювання повітря! Саме воно було основою для стрімкого
зростання Х'юстона в 1950 році, коли він став найбільш оснащеним кондиціонерами
містом у світі. Саме це стимулювало багато корпорацій перемістити свої штаб-
квартири в Х'юстон.</p>
    </blockquote>
        <p>У 1962—1964 роках за двадцять п'ять миль на південь від центру Х'юстона, на землях, переданих
федеральному уряду університетом Райса, був побудований Центр управління космічними
кораблями, що з 1973 року носить ім'я Ліндона Джонсона. У 1960-х роках населення Х'юстона
досягло мільйона людей.</p>
    <h2 id="characteristic">Фізико-географічна характеристика</h2>
    <h3 id="climat">Географічне положення і клімат</h3>
    <figure class="img">
    <img src="hust/Large_Houston_Landsat.jpg">
    <figcaption>Х'юстон з супутника Landsat 7</figcaption>
    </figure>
    <p>Х'юстон розташований за 50 кілометрів від Мексиканської затоки на прибережній рівнині.
Значна частина міста була побудована на лісових угіддях, болотах та преріях, вони досі
збереглися у прилеглих районах біля Х'юстона. Місто розташоване на території, для якої
звичайні часті зливи та дощі, тому для Х'юстона повені - постійна проблема. Висота
міста над рівнем моря в середньому 15 метрів, найвища точка - північний захід Х'юстона (38
метрів). Площа міста складає 1552,9 км².</p>
    <p>Навесні та влітку у місті спекотно та волого: середня температура навесні 21 °C, а влітку – 28,8 °C. Через
високої температури майже у всіх транспортних засобах та будинках встановлені кондиціонери.
Абсолютний максимум температури був зареєстрований у 2000 та 2011 роках, коли вона склала
42,8 °C. На Х'юстон часто обрушуються урагани, найбільші з яких останні
десятиліття - "Еллісон" і "Айк". Осінь - досить тепла пора року, особливо вересень.
Температура цього місяця вища, ніж у травні.Середня температура восени становить 21,8 ° C, а
середня кількість опадів - найвища на рік (359,7 мм). Зима тепла. Найнижча
температура була зареєстрована 1930 року - −15 °C. Середня температура взимку становить
12,6 °C, а максимальна була зареєстрована в 1986 - 32,8 °C. 18 днів на рік температура
опускається нижче за 0 °C. Зазвичай взимку опади випадають як дощу, але рідко може бути і як
снігу.</p>
    <table>
    <tr><th colspan="14">Дні з ясною та дощовою погодою на місяць (сумарно по годинах)</th></tr>
    <tr><th>Місяць</th><th>Січ</th><th>Лют</th><th>Бер</th><th>Кві</th><th>Тра</th><th>Чер</th><th>Лип</th><th>Сер</th><th>Вер</th><th>Жов</th><th>Лис</th><th>Гру</th><th>Год</th></tr>
    <tr><th>Сонячне сяйво, день</th><td>10</td><td>10</td><td>9</td><td>8</td><td>8</td><td>8</td><td>10</td><td>9</td><td>7</td><td>7</td><td>8</td><td>9</td><td>106</td></tr>
    <tr><th>Дощ, день</th><td>14</td><td>12</td><td>12</td><td>10</td><td>10</td><td>14</td><td>13</td><td>12</td><td>10</td><td>9</td><td>10</td><td>12</td><td>136</td></tr>
    </table>
    <h3 id="relief">Рельєф, внутрішні води</h3>
    <p>Для ґрунтів Х'юстона характерна наявність осадових гірських порід та піску. На поверхні часті
ерозії, біля міста перебуває близько 300 розломів, їх загальна довжина приблизно 500 км. Один
їх — Long Point–Eureka Heights fault system. Також є унікальні відкладення із суміші пісків та
глин, завдяки ним, через певний час, з органічних речовин, що розкладаються, утворюються
нафту та природний газ. На околицях Х'юстона зустрічається чорний родючий ґрунт, на якому
вирощують рис, сою, зернові культури, овочі і розводять велику рогату худобу, коней, свиней і
домашню птицю. У місті та його околицях є дуже мала ймовірність сильного
землетрус, а найсильніший землетрус магнітудою 3,8 був у 1910 році.</p>
    <p>У Х'юстоні протікають чотири річки. Основна, Буффало-Байю, проходить через центр міста та
Х'юстонський судноплавний канал, і має три притоки. Брес-Байю протікає вздовж Техаського району
медичного центру, Сімс-Байю проходить через південну частину міста, Уайт-Ок-Байю - через
північну частину міста. Судноплавний канал слідує далі до Галвестону, аж до Мексиканського.
затоки. У передмісті знаходяться два озера: Конро та Х'юстон, які є водосховищем та
служать міськими джерелами води. На території міста протікає безліч підземних вод,
які раніше активно використовували для водопостачання, але перестали через повільний рух
земної поверхні.</p>
    <h3 id="flora">Флора і фауна</h3>
    <figure class="sign">
    <img src="hust/Discovery_green.jpg">
        <figcaption>Парк Discovery green у центрі Х'юстона</figcaption>
    </figure>
    <p>У флорі та фауні округу Харріс переважають види тварин і рослин, що мешкають у болотних
місцевостях, оскільки значна частина міста побудована на болотах та преріях.</p>
    <p>Серед земноводних та плазунів найбільш відомі х'юстонська жаба та техаська рогата
ящірка. Серед ссавців можна відзначити рудого вовка, оцелота та канадську видру. Серед
птахів помічаються американський клювач та білоголовий орлан. Чисельність більшості тварин за
останнє століття значно скоротилося в межах округу і знаходиться під загрозою зникнення через
їх винищення та погіршення екологічної обстановки. У місті також водяться комарі,
що становлять небезпеку людині.</p>
    <p>У місті та його передмістях ростуть сосни, пальми та інші дерева, що ростуть у субтропічному.
кліматі. Серед рослин, що виростають у місті, можна виділити орхідеї та магнолії.</p>
    <h2 id="economy">Економіка</h2>
    <h3 id="general">Загальне становище</h3>
    <table>
    <tr><th colspan="3">Найбільші компанії, що базуються у Х'юстоні за версією Fortune 500 на 2016 рік.</th></tr>
    <tr><td><b>Техас</b></td><td><b>Компанія</b></td><td><b>США</b></td></tr>
    <tr><td>3</td><td>Phillips 66</td><td>30</td></tr>
    <tr><td>5</td><td>Sysco</td><td>57</td></tr>
    <tr><td>8</td><td>ConocoPhillips</td><td>90</td></tr>
    <tr><td>10</td><td>Enterprise Products Partners</td><td>104</td></tr>
    <tr><td>12</td><td>Halliburton</td><td>117</td></tr>
    <tr><td>13</td><td>Plains All American Pipeline</td><td>121</td></tr>
    <tr><td>18</td><td>Baker Hughes</td><td>178</td></tr>
    <tr><td>20</td><td>National Oilwell Varco</td><td>192</td></tr>
    <tr><td>21</td><td>Kinder Morgan</td><td>198</td></tr>
    <tr><td>24</td><td>Waste Management</td><td>221</td></tr>
    <tr><td>25</td><td>Occidental Petroleum</td><td>225</td></tr>
    <tr><td>29</td><td>Group 1 Automotive</td><td>267</td></tr>
    <tr><td>34</td><td>Cameron International</td><td>319</td></tr>
    <tr><td>35</td>><td>EOG Resources</td><td>322</td></tr>
    <tr><td>38</td><td>Quanta Services</td><td>352</td></tr>
    <tr><td>39</td><td>CenterPoint Energy</td><td>363</td></tr>
    <tr><td>40</td><td>Targa Resources</td><td>387</td></tr>
    <tr><td>41</td><td>Apache</td><td>388</td></tr>
    <tr><td>42</td><td>Calpine</td><td>402</td></tr>
    <tr><td>45</td><td>FMC Technologies</td><td>410</td></tr>
    <tr><td>49</td><td>Marathon Oil</td><td>438</td></tr>
    <tr><td>52</td><td>Spectra Energy</td><td>493</td></tr>
    </table>
    <figure class="img">
    <img src="hust/Houston_Ship_Channel.jpg">
    <figcaption>Х'юстонський судноплавний канал</figcaption>
    </figure>
    <p>Х'юстон є одним з провідних міст світу у сферах видобутку та переробки нафти та
природного газу, через що часто називається «енергетичною столицею світу», а також
біомедичних досліджень та аеронавтики. Також Х'юстон має репутацію «зеленого міста»,
так як половина електроенергії виробляється за допомогою сонячних та вітряних установок.
Велику роль транспортній сфері міста грає порт. У Х'юстоні базується 22 компанії з
списку Fortune 500.</p>
    <p>Міжнародна дослідницька компанія Mercer у 2017 році відвела Х'юстону 67 місце у
рейтингу найзручніших для проживання міст світу — між британським Белфастом та
американським Майамі, і 75 місце серед міст світу за вартістю життя - нарівні з Бангкоком,
Дохой та Мюнхеном. Місто сильно знизило позиції через економічну ситуацію і на 2016 рік
займає лише 63 місце в США в категорії «найкращі місця для бізнесу та кар'єри» за версією
журналу Forbes. Дослідницька компанія A.T. Kearney поставила Х'юстон на 38 місце у списку
світових міст світу. У дослідженнях університету Лафборо про глобальні міста Х'юстона
поставлено категорію «Бета+», як і Дюссельдорфу, Монреалю, Тель-Авіву.</p>
    <p>Мінімальна заробітна плата в Х'юстоні за годину становить $7,25 або $1 257 на місяць. Безробіття на
початок 2017 року становив 5,8 %. За межею бідності перебувають 9,2% мешканців. Середні доходи
сім'ї на 2016 рік за даними Forbes становлять $60 840, а середня ціна будинку становить $219 000.</p>
    <h3 id="energ">Енергетика і нефтехімія</h3>
    <p>У Х'юстоні знаходиться понад 5 тисяч енергетичних компаній, пов'язаних із веденням бізнесу в цьому
регіоні. У місті знаходяться штаб-квартири безлічі енергетичних та нафтових компаній,
входять до списку Fortune 500. Х'юстон є членом Світового партнерства енергетичних
міст.</p>
    <figure class="sign">
    <img src="hust/Enron_Complex.jpg">
    <figcaption>Офіс компанії Chevron у Х'юстоні</figcaption>
    </figure>
    <p>Однією з найбільших компаній, що забезпечують електроенергією місто, є компанія
CenterPoint Energy, яка постачає електрику не тільки для Техасу, але й для Арканзасу,
Луїзіани, Міннесоти, Міссісіпі, Оклахоми. Послугами компанії користується понад 5 млн осіб.
Інша велика енергетична компанія Calpine займає 42 місце у Техасі та 402 у США у рейтингу
Fortune 500. Корпорація має парк з 84 електростанцій різних типів, розкиданих по всій
території США. Одна з них, Channel Energy Center, розташована у самому Х'юстоні, на березі
судноплавного каналу, ще одна, Baytown Energy Center – у передмісті Бейтаун. Максимальна
потужність х'юстонської електростанції - 808 мегават (базова - 723 МВт), бейтаунська
електростанція в піковому режимі здатна виробляти 842 мегават (базова електрична
потужність - 782 МВт). На території метрополії Великого Х'юстона діє вісім
електростанцій Calpine.</p>
    <p>Х'юстон є одним з найбільших виробничих центрів світу для нафтохімічної
промисловості. У місті розташовано більше 3 700 організацій, що працюють у сфері
нафтохімії. Також у Х'юстонському регіоні знаходяться 9 нафтопереробних заводів,
переробних 2,3 мільйона барелів щодня, що становить 13,2 % від усієї переробки США.
Також у Х'юстоні є 719 підприємств зі створення хімічних та пластмасових виробів. В
місті знаходиться 17,5% робочих місць, зайнятих у сфері нефетехімії, з усіх місць у США (112,6%)
тисячі із 643,3 тисяч). Місто займає лідируюче місце з виробництва товарів із поліетилену.
(38,7% від усього виробництва у США), полівінілхлориду (35,9%) та поліпропілену (48,4%).</p>
    <h3 id="avia">Авіакосмічна промисловість</h3>
    <figure class="img">
    <img src="hust/Aerial_View_of_the_Johnson_Space_Center.jpg">
    <figcaption>Космічний центр ім. Джонсона</figcaption>
    </figure>    
    <p>У Х'юстоні розташовується космічний центр імені Ліндона Джонсона, що є
науково-дослідне та проектно-конструкторське підприємство, в якому працюють 15000
людина (3000 інженерів та вчених, 12000 інших робочих). Загалом у місті розташовуються більше
150 організацій, що мають справу із космічною галуззю.</p>
    <p>У районі Х'юстона знаходяться виробничі потужності компанії Lockheed Martin, а також офіс
програми будівництва космічного корабля "Оріон" для NASA У місті розташовані
виробничі потужності компанії Boeing, а також штаб-квартира підрозділу Boeing Space
Exploration», що займається дослідженням космічних систем. Потужності компанії Beechcraft,
що знаходяться в аеропорту ім. Хобі, займаються технічним обслуговуванням та ремонтом повітряних
судів. Компанія Barrios Technology виконує контракти для NASA, пов'язані з кораблем «Оріон»,
а також розробляє програмне забезпечення повітряних суден Boeing. Іншими великими
виконавцями замовлень NASA у Х'юстоні є: Computer Sciences Corporation — технічне
обслуговування та модифікація літаків, Jacobs Engineering Group — машинознавство, L-3
Communications – роботехніка, MEI Technologies – електричні інженерні системи,
Oceaneering International — скафандри та апаратне забезпечення, що додається, Raytheon —
лабораторія нейтральної плавучості та макети космічних коробок, SAIC — безпека та
підтримка місій, United Space Alliance — координаційний центр інформації, United
Technologies – позакорабельна діяльність, Wyle Laboratories – космічна біологія.</p>
    <h2 id="people">Населення</h2>
    <h3 id="dinamic">Динаміка і структура населення</h3>
    <table>
    <tr><th colspan="3">Перепис населення</th></tr>
    <tr><td><b>Рік перепису</b></td><td><b>Населення</b></td><td><b>%±</b></td></tr>
    <tr><td>1850</td><td>2396</td><td>---</td></tr>
    <tr><td>1860</td><td>4845</td><td>102.2%</td></tr>
    <tr><td>1870</td><td>9332</td><td>92.6%</td></tr>
    <tr><td>1880</td><td>16513</td><td>77%</td></tr>
    <tr><td>1890</td><td>27557</td><td>66.9%</td></tr>
    <tr><td>1900</td><td>44633</td><td>62%</td></tr>
    <tr><td>1910</td><td>78800</td><td>76.7%</td></tr>
    <tr><td>1920</td><td>138276</td><td>75.5%</td></tr>
    <tr><td>1930</td><td>292352</td><td>111.4%</td></tr>
    <tr><td>1940</td><td>384514</td><td>31.5%</td></tr>
    <tr><td>1950</td><td>596163</td><td>55%</td></tr>
    <tr><td>1960</td><td>938219</td><td>57.4%</td></tr>
    <tr><td>1970</td><td>1232802</td><td>31.4%</td></tr>
    <tr><td>1980</td><td>1595138</td><td>29.4%</td></tr>
    <tr><td>1990</td><td>1630553</td><td>2.2%</td></tr>
    <tr><td>2000</td><td>1953631</td><td>19.8%</td></tr>
    <tr><td>2010</td><td>2100263</td><td>7.5%</td></tr>
    <tr><td>2017</td><td>2319603</td><td>10.4%</td></tr>
    <tr><td colspan="3">1850-2017 Переписи населення у 1790-2010 роках</td></tr>
    </table>
    <figure class="sign">
    <img src="hust/Race_and_ethnicity_2010_Houston.png">
    <figcaption>Етнічна карта Х'юстона</figcaption>
    </figure>
    <p>Згідно з даними перепису населення США у 2010 році у місті проживало 2 100 263 особи, це на
7,5% більше, ніж 2000 року. За оцінкою бюро перепису населення США на 1 січня 2017 року
населення становило 2 319 603 особи. Населення міста, починаючи з його заснування, постійно
зростає: у 1960-х роках воно досягло 1 млн жителів, а у 2000-х роках перевищило 2 млн. Щільність
населення становить 1494 чол./км².</p>
    <p>Віковий склад населення: до 19 років - 28,67%; від 20 до 44 років - 39,83%; від 45 до 64 років
22,45%; від 65 років - 9,05%. Середній вік становить 32 роки. Кількість жінок від усього
населення - 49,82%, чоловіків - 50,18%.</p>
    <h3 id="language">Етнічний і конфесійний склад, мови</h3>
    <p>Через близькість до Мексики частка вихідців із Латинської Америки становить 43,8% від усього
населення. В абсолютних цифрах чисельність латиноамериканців зросла з 731 до 920 тисяч
людина за період 2000-2010 років. Друге місце в расовому складі міста займають білі люди,
які становлять 25,6 % від міського населення - їх чисельність за десятиліття знизилася на
10% з 602 до 538 тисяч осіб. Також значне населення займають афроамериканці (23,1%)
та азіати (6,15 %), трохи більше 1 % становлять особи інших національностей. Імміграція у Х'юстон
у 2015 році становила 19 630 осіб. 28% жителів Х'юстона народилися в іншій країні: 72,5% -
з Латинської Америки, 18,9% - з Азії, 3,9% та 3,8% - з Африки та Європи відповідно, 0,2
% - з Океанії. До 1960-х років основними іммігрантами були люди з Європи, але з прийняттям у
1965 року нового закону про імміграцію та громадянство, що скасував квоти за національністю,
більшість іммігрантів почали приїжджати з Латинської Америки, Азії та Африки. У 2005 році 240
тисяч мешканців Нового Орлеана, на який обрушився ураган «Катріна», евакуювалися в
Х'юстон. Згодом, до 40 тис. людей залишилося жити у місті.</p>
    <p>50% мешканців міста розмовляють лише англійською мовою. 34% мешканців розмовляють на
іспанською мовою, по 1% - в'єтнамською та китайською, по 0,2-0,4% - французькою, урду,
арабською, хінді, тагальською та корейською мовами. Загалом у місті розмовляють більш ніж на 100
мовами.</p>
    <p>18,44% жителів сповідують католицизм, 16,29% - баптизм, 4,68% - методизм, 2,86% - іслам,
0,53% - іудаїзм. Усього сповідують релігію 58,4% х'юстонців, 41,6% – невіруючі.</p>
    <h2 id="zmi">Засоби масової інформації</h2>
    <figure class="img">
    <img src="hust/Melcher_Center_for_Public_Broadcasting.jpg">
    <figcaption>Мовний центр, звідки мовлять <br> радіостанції KUHT та KUHF</figcaption>
    </figure>
    <p>У Х'юстоні ведуть мовлення 19 телеканалів. Найбільш відомі телеканали є афілійованими
каналами великих телекомпаній: KPRC-TV (NBC), KHOU-TV (CBS), KTRK-TV (ABC), KRIV (Fox),
KIAH (The CW) та KTXH (MyNetworkTV). Телеканал KUHT є членом національної
громадської телемовної служби PBS.</p>
    <p>У Х'юстоні мовлять 29 радіостанцій. Одна з найбільших радіостанцій, KUHF, належить
Х'юстонської університетської системи.</p>
    <p>Houston Chronicle – найбільша щоденна газета Х'юстона та штату Техас, яка належить
Нью-Йоркської корпорації Hearst Corporation. У 2014 році щоденний тираж газети складав 356
347 екземплярів, що ставить її на 16 місце за тиражем серед усіх газет США. До 1995 року
існувала Houston Post, але була поглинена Houston Chronicle. На сьогоднішній день
єдиним основним альтернативним міським виданням залишається тижневик Houston Press,
його щотижневий тираж 2016 року становив 43 810 екземплярів. У Х'юстоні випускається газета
Houston Business Journal, яка є частиною компанії American City Business Journals.</p>
    <h2 id="town-brother">Міста-побратими</h2>
    <p>Згідно з міським сайтом, у Х'юстона 18 міст-побратимів (востаннє цей список
розширювався у 2015 році, коли до нього приєдналася Басра):</p>
    <ul>
    <li>Абу-Дабі (ОАЕ);</li>
    <li>Абердін (Шотландія);</li>
    <li>Гуаякіль (Еквадор);</li>
    <li>Карачі (Пакистан);</li>
    <li>Баку (Азербайджан);</li>
    <li>Лейпциг (Німеччина);</li>
    <li>Ніцца (Франція);</li>
    <li>Луанда (Ангола);</li>
    <li>Ставангер (Норвегія);</li>
    <li>Тайбей (Тайвань);</li>
    <li>Стамбул (Турція);</li>
    <li>Перт (Австралія);</li>
    <li>Тюмень (Росія);</li>
    <li>Тампіко (Мексика);</li>
    <li>Уельва (Іспанія);</li>
    <li>Тіба (Японія);</li>
    <li>Шеньчжень (Китай);</li>
    <li>Басра (Ірак)</li>
    </ul>
    <div style="text-align: center">
    <button><p class="top"><a href="#top">Наверх</a></p></button>
    </div>
    <script>
    document.write("Today is " + Date() );
</script>
        </body>
</html>"
