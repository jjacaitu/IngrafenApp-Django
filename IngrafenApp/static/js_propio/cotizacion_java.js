function tipo_trabajo(item) {
  var id = item.options[item.selectedIndex].text
  if (id.slice(-4) == "True"){
    document.getElementById("interiores").style.display = "table-row";

  }else{
    document.getElementById("interiores").style.display = "none";



  }
}


function troquel_existente1_fun(item){
  if(item.value == "Troquel existente"){
    document.getElementById("troquel_existente1").style.display = "initial";

  }else{
document.getElementById("troquel_existente1").style.display = "none";

  }
}

function troquel_existente2_fun(item){
  if(item.value == "Troquel existente"){
    document.getElementById("troquel_existente2").style.display = "initial";

  }else{
document.getElementById("troquel_existente2").style.display = "none";

  }
}

function troquel_existente3_fun(item){
  if(item.value == "Troquel existente"){
    document.getElementById("troquel_existente3").style.display = "initial";

  }else{
document.getElementById("troquel_existente3").style.display = "none";

  }
}

function agregar1() {

  if (document.getElementById('luno').style.display = "none"){
    document.getElementById('luno').style.display = "table-row";
    document.getElementById("material1").required = true;
    document.getElementById("descripcion1").required = true;
    document.getElementById("alto1").required = true;
    document.getElementById("ancho1").required = true;
    document.getElementById("alto1").value = "";
    document.getElementById("ancho1").value = "";
    document.getElementById("uv1").required = true;
    document.getElementById("laminado1").required = true;
    document.getElementById("troquelado1").required = true;
    document.getElementById("impresiont1").required = true;
    document.getElementById("impresionr1").required = true;
  }
}

function agregar2() {

  if (document.getElementById('ldos').style.display = "none"){
    document.getElementById('ldos').style.display = "table-row";
    document.getElementById('boton_quitar').style.display = "none";
    document.getElementById("material2").required = true;
    document.getElementById("descripcion2").required = true;
    document.getElementById("alto2").required = true;
    document.getElementById("ancho2").required = true;
    document.getElementById("alto2").value = "";
    document.getElementById("ancho2").value = "";
    document.getElementById("uv2").required = true;
    document.getElementById("laminado2").required = true;
    document.getElementById("troquelado2").required = true;
    document.getElementById("impresiont2").required = true;
    document.getElementById("impresionr2").required = true;
  }
}

function quitar1() {

  if (document.getElementById('luno').style.display = "table-row"){
    document.getElementById('luno').style.display = "none";
    document.getElementById("material1").required = false;
    document.getElementById("descripcion1").required = false;
    document.getElementById("alto1").required = false;
    document.getElementById("ancho1").required = false;
    document.getElementById("uv1").required = false;
    document.getElementById("laminado1").required = false;
    document.getElementById("troquelado1").required = false;
    document.getElementById("impresiont1").required = false;
    document.getElementById("impresionr1").required = false;
    document.getElementById("material1").value = "";
    document.getElementById("descripcion1").value = "";
    document.getElementById("alto1").value = "";
    document.getElementById("ancho1").value = "";
    document.getElementById("uv1").value = "";
    document.getElementById("laminado1").value = "";
    document.getElementById("troquelado1").value = "";
    document.getElementById("impresiont1").value = "";
    document.getElementById("impresionr1").value = "";
  }
}

function quitar2() {

  if (document.getElementById('ldos').style.display = "table-row"){
    document.getElementById('ldos').style.display = "none";
    document.getElementById('boton_quitar').style.display = "table-cell";

    document.getElementById("material2").required = false;
    document.getElementById("descripcion2").required = false;
    document.getElementById("alto2").required = false;
    document.getElementById("ancho2").required = false;
    document.getElementById("uv2").required = false;
    document.getElementById("laminado2").required = false;
    document.getElementById("troquelado2").required = false;
    document.getElementById("impresiont2").required = false;
    document.getElementById("impresiont2").required = false;

    document.getElementById("material2").value = "";
    document.getElementById("descripcion2").value = "";
    document.getElementById("alto2").value = "";
    document.getElementById("ancho2").value = "";
    document.getElementById("uv2").value = "";
    document.getElementById("laminado2").value = "";
    document.getElementById("troquelado2").value = "";
    document.getElementById("impresiont2").value = "";
    document.getElementById("impresiont2").value = "";
  }
}

function pantonet1(item){
  if(item.value == "Pantones"  || item.value == "F/C + Pantones"){
    document.getElementById("num_pantonest1").style.display = "initial";

  }else{
document.getElementById("num_pantonest1").style.display = "none";

  }
}


function pantoner1(item){
  if(item.value == "Pantones"  || item.value == "F/C + Pantones"){
    document.getElementById("num_pantonesr1").style.display = "initial";

  }else{
document.getElementById("num_pantonesr1").style.display = "none";

  }
}

function pantonet2(item){
  if(item.value == "Pantones"  || item.value == "F/C + Pantones"){
    document.getElementById("num_pantonest2").style.display = "initial";

  }else{
document.getElementById("num_pantonest2").style.display = "none";

  }
}

function pantoner2(item){
  if(item.value == "Pantones"  || item.value == "F/C + Pantones"){
    document.getElementById("num_pantonesr2").style.display = "initial";

  }else{
document.getElementById("num_pantonesr2").style.display = "none";

  }
}

function pantonet3(item){
  if(item.value == "Pantones"  || item.value == "F/C + Pantones"){
    document.getElementById("num_pantonest3").style.display = "initial";

  }else{
document.getElementById("num_pantonest3").style.display = "none";

  }
}

function pantoner3(item){
  if(item.value == "Pantones"  || item.value == "F/C + Pantones"){
    document.getElementById("num_pantonesr3").style.display = "initial";

  }else{
document.getElementById("num_pantonesr3").style.display = "none";

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

function check(){
  var CheckBox = document.getElementById('con_cinta')
  if(CheckBox.checked == true){
    document.getElementById('cantidad_cintas').disabled = false;
    document.getElementById('cm_cintas').disabled = false;
    document.getElementById('tipo_cinta').disabled = false;
  }else{
    document.getElementById('cantidad_cintas').disabled = true;
    document.getElementById('cm_cintas').disabled = true;
    document.getElementById('tipo_cinta').disabled = true;
    document.getElementById('cantidad_cintas').value = "";
    document.getElementById('cm_cintas').value = "";
    document.getElementById('tipo_cinta').value = "";
  }
}

function verificar_tipo_trabajo(item){
  if(document.getElementById(item.value).value == "False"){
    document.getElementById('boton_agregar').style.display = "none";

  }else{
    document.getElementById('boton_agregar').style.display = "table-cell";

  }
  if (document.getElementById(item.value).name != ""){
    document.getElementById("adicional_row").style.display = "table-cell";
    document.getElementById("adicional").placeholder = document.getElementById(item.value).name;
    document.getElementById("adicional_texto").value = document.getElementById(item.value).name;
    document.getElementById("adicional").required = true;
  }else{
    document.getElementById("adicional_row").style.display = "none";
    document.getElementById("adicional").required = false;
    document.getElementById("adicional_texto").value = "";
    document.getElementById("adicional").value = "";
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
