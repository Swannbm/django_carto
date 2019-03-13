function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
}

function getMarker(feature, latlng) {
    ze_icon = blueIcon;
    if (feature.properties && feature.properties.icon_color) {
        switch(feature.properties.icon_color) {
            case 1: ze_icon = blueIcon; break;
            case 2: ze_icon = redIcon; break;
            case 3: ze_icon = greenIcon; break;
            case 4: ze_icon = orangeIcon; break;
            case 5: ze_icon = yellowIcon; break;
            case 6: ze_icon = violetIcon; break;
            case 7: ze_icon = greyIcon; break;
            case 8: ze_icon = blackIcon; break;
            default: ze_icon = blueIcon;
        };
    };
    return L.marker(latlng, {icon: ze_icon});
}