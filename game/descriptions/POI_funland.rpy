define funland_name = "Фанленд"
define funland_desc = """Некогда наш прекрасный мегаполис был небольшим городком под названием - «Фантинель», стоявшим здесь с эпохи первых поселенцев. Многие годы маленький городок выживал, пока не пришла производственная революция и капитализм!
Именно поэтому, чтобы не напоминать о печальном прошлом, центр города перенесли, а сам район переименовали. Но тут до сих пор сохранилась изначальная архитектура, странно смешавшаяся с современными постройками, и частенько живут потомки первых поселенцев. Хотя может жить кто угодно — жилье в Фанленде недорогое."""


define funland_dead = POI(
    x=135, y=140,
    icon="logo_funland_dead.png",
    name="“Мертвый район”",
    desc="В центре Фанленд расположился архитектурный ансамбль, который местные прозвали “Мертвый район”. Вопреки своему прозвищу, район очень даже живой и заселенный, а прозвище к нему пришло после очередного скандала. Городские власти планировали снести все постройки, оставшиеся от города Фантинель, но местным жителям через протесты и суды удалось доказать, что остатки старого города являются исторической достопримечательностью. Эта конфронтация привела к тому, что обслуживание “Мертвого района” ведется в штатном режиме, а вот денег на реставрацию никто не выделяет. Все деревянные дома в этом районе находятся в плачевном состоянии и власти только и ждут момента, когда останки былых зданий окончательно рухнут и освободят место для современной застройки."
)

define funland_cemetery = POI(
    x=190, y=90,
    icon="logo_funland_cemetery.png",
    name="Кладбище “Хонор”",
    desc="Тихое и спокойное место, в отличии от классических протестантских кладбищ, с ровными рядами одинаковых табличек, “Хонор” — кладбище католическое. Тут, на огороженной территории, под сенью дубов и елей расположилось более десяти тысяч могил, большая часть которых с различными памятниками, мемориальными плитами и крестами. В самом центре кладбища есть даже самый настоящий склеп, где долгие годы хоронили семейства отцов-основателей Города. Подземные катакомбы под кладбищем это еще одна городская легенда, жаль туда не водят экскурсии."
)

define funland_mall = POI(
    x=135, y=272,
    icon="logo_funland_mall.png",
    name="Торговый центр “Вариомолл”",
    desc="На самой границе Фанлэнда и Брэйнвуда расположилось то, что местные жители зовут позором, а остальные жители - самым удобным магазином Вариаполиса. Четырехэтажный торговый центр с подземной парковкой и целой кучей различных бутиков, магазинов и салонов. Просто очень хорошее место для покупок для всей семьи!"
)

define funland_hospital = POI(
    x=199, y=222,
    icon="logo_funland_hospital.png",
    name="Больница “Брес”",
    desc="Когда-то, много лет назад, когда Вариаполиса еще не существовало, эта больница была самым современным, капитальным и внушительным зданием Фантинель. Шесть этажей, три корпуса, расходящиеся треугольником от центральной части, небольшой парк за самой Больницей, красные кирпичные стены. Что удивительно, больница до сих пор является функционирующей, при этом часть медицинских кабинетов сохранили изначальное расположение и оборудование. Молодые врачи до сих пор проходят тут практику, и во врачебных кругах даже поговаривают, что врач Вариаполиса только тогда станет настоящим спецом, когда пол годика отработает в Брэс."
)

define funland_museum = POI(
    x=145, y=190,
    icon="logo_funland_museum.png",
    name="Дом-музей истории Фантинель",
    desc="Неподалеку от “Мертвого района”, на самой его границе расположился особняк Видогастов: одной из старейших семей старого города. В дальнем конце этого особняка до сих пор живут потомки этой благородной семьи, но большая часть дома отдана под музей, посвященный истории города Фантинель. Тут можно посмотреть самые ранние фотографии этого города, полюбоваться залами, в которых принимались важнейшие решения в жизни города и прочесть самые ранние указы и документы города. Внешне особняк остался таким же как и был с момента построения — тёмно-зеленое двухэтажное строение с темно-бордовой облицовкой дверей и окон и покатая черепичная красная крыша. Если вы любите старину - это место которое стоит посетить!"
)


define poi_list_funland = [funland_dead, funland_cemetery, funland_mall, funland_hospital, funland_museum]