define port_name = "Порт"
define port_desc = """Думаешь я открою тебе тайну? В районе под названием Порт — располагается Порт. Широкая и судоходная река обеспечивает удобную и быструю связь как с северными, так и с южными регионами нашей прекрасной страны! Самые буйные пьянки в местных барах это то, о чем можно рассказывать внукам в старости!
Поговаривают что Порт, как район с наименьшей жилой застройкой, стал прибежищем для всяких темных делишек... Но это только слухи, не так ли мистер офицер?!"""

define port_port = POI(
    x=125, y=328,
    icon="logo_port_port.png",
    name="Причалы",
    desc="На всей протяженности района Порт вдоль линии побережья раскинулись Причалы. Длинные платформы, готовые принять даже самые крупные транспортные корабли. Портальные краны, устремившиеся своими башнями в небеса, рельсы, по которым эти краны двигаются от одного причала к другому. Часть причалов находятся в муниципальной собственности, часть в частной. Часть ограничено заборами, а часть используется для личного водного транспорта. Увлекательное место, ну а еще можно снять лодку или яхту и прокатиться по всему городу!",
)

define port_warehouses = POI(
    x=42, y=234,
    icon="logo_port_warehouses.png",
    name="Транспортные склады",
    desc="Представьте себе место, где круглосуточно суетятся люди, работают погрузчики, кричат друг на друга подрядчики и не переставая снуют туда-сюда машины! Поздравляю, вы представили транспортные склады Вариаполиса! Здесь решаются дела не только тех грузов, что пришли кораблями, здесь огромная стоянка грузовых машин, и даже отсек с частными складскими ячейками. Шум, гомон, и ровные ряды складских ангаров, уходящие вдаль. Достаточно тихо, чтобы заниматься чем угодно, достаточно громко, чтобы потеряться среди этого шума!",
)

define port_bar = POI(
    x=65, y=321,
    icon="logo_port_bar.png",
    name="Бар “Салти Салмон”",
    desc="Вы можете сколько угодно относиться с предубеждением к тематическим заведениям, но “Салти Салмон” — это тот бар, который стоит посетить. Никакого чванства, никаких лакшери напитков или премиумных блюд - только чистая, душевная атмофера. Этот бар построен бывшим моряком и для моряков. Вкусная свежая рыба, лучший ром в Америке, отличная живая музыка! Зал, кстати, не просто так разделен на две части: в одной сидят обычные посетители, а во второй те, кто не против почесать кулаками по пьяни! Там дороже напитки и еда, потому что посуда и мебель включены в стоимость. Никто не знает, когда начнется драка, но все знают, что она начнется.",
)

define port_ring = POI(
    x=111, y=420,
    icon="logo_port_ring.png",
    name="Боксерский клуб “Блюбэлт”",
    desc="Знаменитая “кузница чемпионов”! Вступая в этот клуб, ты навсегда закрываешь себе доступ в “Салти”, но открываешь большую семью. Они качаются вместе, едят вместе, живут вместе - их ведет мечта стать чемпионами! Эти парни и девушки всегда готовы выйти на спарринг, всегда готовы бороться! Этот клуб - настоящий памятник целеустремленности.",
)

define port_police = POI(
    x=170, y=430,
    icon="logo_port_police.png",
    name="Центральное полицейское управление",
    desc="Огромный памятник Фемиде, держащий меч и весы, неустанно напоминает всем, что именно в этом здании позади властвует Закон! Огромный автопарк современных полицейских машин, включая бронированные микроавтобусы спецназа. Просто смотря на это величественное пятиэтажное здание, понимаешь, что есть те, кто следит за безопасностью, и на душе становится спокойней!",
)


define poi_list_port = [port_port, port_warehouses, port_bar, port_ring, port_police]
