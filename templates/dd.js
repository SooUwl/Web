ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 10
    });

    var myPlacemark = new ymaps.Placemark([55.76, 37.64], {}, {
        iconLayout: 'default#image',
        iconImageHref: 'https://yastatic.net/morda-logo/i/citylogos/yandex20/default.svg',
        iconImageSize: [30, 42],
        iconImageOffset: [-3, -42]
    });

    myMap.geoObjects.add(myPlacemark);
}