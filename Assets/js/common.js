function changeLanguage($language) {
    $.get("changeLanguage/"+$language,{"post":"Hack"},function(data,status) {
       location.reload();
    });
 }