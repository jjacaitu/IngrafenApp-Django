function tipo_trabajo(item) {
  var id = item.options[item.selectedIndex].text
  if (id.slice(-4) == "True"){
    document.getElementById("interiores").style.display = "table-row";

  }else{
    document.getElementById("interiores").style.display = "none";



  }
}





function filtros_busqueda(item) {
  if (item.value == "Todo"){
    document.getElementById("parametro").style.display = "none";
    document.getElementById("cl").style.display = "none";
    document.getElementById("tr").style.display = "none";
    document.getElementById("cot").style.display = "none";
    document.getElementById("ven").style.display = "none";
  } else if (item.value == "Cliente") {
    document.getElementById("parametro").style.display = "none";
    document.getElementById("cl").style.display = "initial";
    document.getElementById("tr").style.display = "none";
    document.getElementById("cot").style.display = "none";
    document.getElementById("ven").style.display = "none";

  } else if (item.value == "Trabajo") {
    document.getElementById("parametro").style.display = "none";
    document.getElementById("cl").style.display = "none";
    document.getElementById("tr").style.display = "initial";
    document.getElementById("cot").style.display = "none";
    document.getElementById("ven").style.display = "none";

  }else if (item.value == "Cotizador") {
    document.getElementById("parametro").style.display = "none";
    document.getElementById("cl").style.display = "none";
    document.getElementById("tr").style.display = "none";
    document.getElementById("cot").style.display = "initial";
    document.getElementById("ven").style.display = "none";
  }else if (item.value == "Vendedor") {
    document.getElementById("parametro").style.display = "none";
    document.getElementById("cl").style.display = "none";
    document.getElementById("tr").style.display = "none";
    document.getElementById("cot").style.display = "none";
    document.getElementById("ven").style.display = "initial";
  }else{
    document.getElementById("parametro").style.display = "initial";
    document.getElementById("cl").style.display = "none";
    document.getElementById("tr").style.display = "none";
    document.getElementById("cot").style.display = "none";
    document.getElementById("ven").style.display = "none";
  }

  if(item.value == "Cliente" || item.value == "Vendedor"){
    document.getElementById("b_por_cliente").style.display = "none";
    document.getElementById("b_por_trabajo").style.display = "initial";
    document.getElementById("totales").selected = true;

  }else if (item.value == "Trabajo"){
    document.getElementById("b_por_cliente").style.display = "initial";
    document.getElementById("b_por_trabajo").style.display = "none";
    document.getElementById("totales").selected = true;
  }else{
    document.getElementById("b_por_cliente").style.display = "initial";
    document.getElementById("b_por_trabajo").style.display = "initial";
    document.getElementById("totales").selected = true; 
  }
}


// Regular map
function regular_map() {
var var_location = new google.maps.LatLng(-2.1545748, -79.9270623);

var var_mapoptions = {
center: var_location,
zoom: 17
};

var var_map = new google.maps.Map(document.getElementById("map-container"),
var_mapoptions);

var var_marker = new google.maps.Marker({
position: var_location,
map: var_map,
title: "Ingrafen"
});
}

// Initialize maps
google.maps.event.addDomListener(window, 'load', regular_map);
