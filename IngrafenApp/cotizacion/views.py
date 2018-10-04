from django.shortcuts import render
from cotizacion.forms import Crear_usuario, Solicitud_cot, Materiales, Clientes, TipoDeTrabajo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cotizacion.models import CotizacionesSolicitadas
from datetime import datetime, timedelta
from cotizacion import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.
def home(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")

    if request.method == 'POST':

        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'home.html', {"cotizaciones_existentes":cotizaciones_existentes})


def contactenos(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    if request.method == 'POST':

        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "contactanos.html",{"cotizaciones_existentes":cotizaciones_existentes})

def quienes_somos(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    if request.method == 'POST':

        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "compañia.html",{"cotizaciones_existentes":cotizaciones_existentes})

def servicios(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    if request.method == 'POST':

        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "servicios.html",{"cotizaciones_existentes":cotizaciones_existentes})

def solicitud(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    return render( request, "solicitud.html", {"cotizaciones_existentes":cotizaciones_existentes})

def creacion_usuario(request):
    registered = False
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    if request.method == 'POST':

        usuario = Crear_usuario(data=request.POST)
        if usuario.is_valid():
            usuario_creado = usuario.save()
            usuario_creado.set_password(usuario_creado.password)
            usuario_creado.save()

            registered = True
            # do something.
    else:
        usuario = Crear_usuario()
    return render(request, 'registro.html', {'usuario': usuario, "registered":registered,"cotizaciones_existentes":cotizaciones_existentes})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'home.html', {})

@login_required
def solicitud_cot(request):
    solicitado = False
    cot_modelo = ""
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    if request.method == 'POST':

        cotizacion = Solicitud_cot(data=request.POST)
        if cotizacion.is_valid():
            stock = cotizacion.save(commit=False)
            stock.vendedor = request.user
            stock.tipo_trabajo = request.POST.get("opciones")
            stock.detalles = request.POST.get("detalles")

            if "imagen" in request.FILES:
                stock.imagen = request.FILES["imagen"]
            stock.save()
            solicitado = True
            cot_modelo = models.TipoDeTrabajo.objects.all()
            # do something.
    else:
        cotizacion = Solicitud_cot()
        solicitado = False
        cot_modelo = models.TipoDeTrabajo.objects.all().order_by("trabajo")
    return render(request, 'solicitud.html', {"cotizacion":cotizacion,"solicitado":solicitado, "cot_modelo":cot_modelo, "cotizaciones_existentes":cotizaciones_existentes})

@login_required
def solicitudes_existentes(request):
    buscar = False
    if request.method == "GET":
        cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
        print(cotizaciones_existentes)
        return render(request, "solicitudes_existentes.html",{"cotizaciones_existentes":cotizaciones_existentes,"buscar":buscar})
    elif request.method == "POST" and request.POST.get("boton_regresar") == "REGRESAR":
        buscar=False
        cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
        return render(request, "solicitudes_existentes.html",{"cotizaciones_existentes":cotizaciones_existentes,"buscar":buscar})

    elif request.method == "POST" and request.POST.get("boton_completar") == "COMPLETAR":
        buscar=False
        numero_1 = request.POST.get("numero1")
        cotizacion = CotizacionesSolicitadas.objects.get(num_solicitud=numero_1)
        print("esto es!" + str(cotizacion))
        cotizacion.fecha_completada = datetime.now()
        cotizacion.cotizador = str(request.user)
        cotizacion.numero_cotizacion = request.POST.get("cotizacion_papyrus")


        cotizacion.save()




        #return render(request,"solicitudes_existentes.html",{"cotizacion_completada":cotizacion_completada,"buscar":buscar,"numero_a_ver":numero_a_ver})
        return HttpResponseRedirect(reverse('solicitudes_existentes'))

    elif request.method == "POST":
        buscar = True
        numero_a_ver = request.POST.get("numero")
        cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
        cotizacion_existentes = CotizacionesSolicitadas.objects.all().filter(num_solicitud=numero_a_ver)
        return render(request, "solicitudes_existentes.html",{"cotizacion_existentes":cotizacion_existentes, "buscar":buscar, "numero_a_ver":numero_a_ver, "cotizaciones_existentes":cotizaciones_existentes})

@login_required
def cotizaciones_completadas(request):
    ver = False
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    clientes_creados = models.Clientes.objects.all().order_by("nombre")
    trabajos_creados = models.TipoDeTrabajo.objects.all().order_by("trabajo")
    cotizadores = models.Usuarios.objects.all().filter(categoria="COT").order_by("username")
    vendedores = models.Usuarios.objects.all().filter(categoria="VEN").order_by("username")
    if request.method == "GET":
        cotizaciones = CotizacionesSolicitadas.objects.all().exclude(cotizador__exact="")
        paginator = Paginator(cotizaciones,10)
        page = request.GET.get('page')
        cotizaciones_completadas = paginator.get_page(page)

        return render(request,"cotizaciones_completadas.html",{"cotizaciones_completadas":cotizaciones_completadas,"ver":ver,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"cotizadores":cotizadores,"vendedores":vendedores, "cotizaciones_existentes":cotizaciones_existentes})
    if request.method == "POST" and request.POST.get("buscar") == "BUSCAR":
        try:
            ver = False
            desde = request.POST.get("desde")
            hasta = request.POST.get("hasta")
            print(desde)
            print(hasta)

            print("SIRVE " + request.POST.get("parametro"))
            if request.POST.get("seleccion") == "Cliente":
                print(request.POST.get("cl"))
                b = models.Clientes.objects.get(nombre=request.POST.get("cl"))
                cotizaciones = b.client.all().filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="")


            elif request.POST.get("seleccion") == "Todo":
                print("TODO")

                cotizaciones = CotizacionesSolicitadas.objects.filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="")

            elif request.POST.get("seleccion") == "Trabajo":

                cotizaciones = CotizacionesSolicitadas.objects.all().filter(tipo_trabajo=request.POST.get("tr")).filter(fecha_completada__range=[desde,hasta]).exclude(cotizador__exact="")
            elif request.POST.get("seleccion") == "Vendedor":

                cotizaciones = CotizacionesSolicitadas.objects.all().filter(vendedor=request.POST.get("ven")).filter(fecha_completada__range=[desde,hasta]).exclude(cotizador__exact="")
            elif request.POST.get("seleccion") == "Cotizador":

                cotizaciones = CotizacionesSolicitadas.objects.all().filter(cotizador=request.POST.get("cot")).filter(fecha_completada__range=[desde,hasta])
            elif request.POST.get("seleccion") == "Solicitud":
                cotizaciones = CotizacionesSolicitadas.objects.all().filter(num_solicitud=request.POST.get("parametro"))

            elif request.POST.get("seleccion") == "Promocion":
                cotizaciones = CotizacionesSolicitadas.objects.all().filter(trabajo=request.POST.get("parametro")).filter(fecha_completada__range=[desde,hasta])
            print("si")
            clientes_creados = models.Clientes.objects.all().order_by("nombre")
            trabajos_creados = models.TipoDeTrabajo.objects.all().order_by("trabajo")
            cotizadores = models.Usuarios.objects.all().filter(categoria="COT").order_by("username")
            vendedores = models.Usuarios.objects.all().filter(categoria="VEN").order_by("username")
            paginator = Paginator(cotizaciones,10)
            page = request.GET.get('page')
            cotizaciones_completadas = paginator.get_page(page)
            return render(request,"cotizaciones_completadas.html",{"cotizaciones_completadas":cotizaciones_completadas,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"ver":ver,"cotizadores":cotizadores,"vendedores":vendedores,"cotizaciones_existentes":cotizaciones_existentes})
        except:

            return render(request, "cotizaciones_completadas.html", {"cotizaciones_existentes":cotizaciones_existentes,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"ver":ver,"cotizadores":cotizadores,"vendedores":vendedores})
    if request.method == "POST" and request.POST.get("ver") == "ver cotizacion":
        ver = True

        cotizacion_buscada = CotizacionesSolicitadas.objects.all().filter(num_solicitud=request.POST.get("cot_ver"))
        return render(request, "cotizaciones_completadas.html", {"cotizacion_buscada":cotizacion_buscada,"ver":ver,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"ver":ver,"cotizadores":cotizadores,"vendedores":vendedores,"cotizaciones_existentes":cotizaciones_existentes})
    if request.method == "POST" and request.POST.get("regresar") == "REGRESAR":
        ver = False
        cotizaciones = CotizacionesSolicitadas.objects.all().exclude(cotizador__exact="")
        paginator = Paginator(cotizaciones,10)
        page = request.GET.get('page')
        cotizaciones_completadas = paginator.get_page(page)
        return render(request,"cotizaciones_completadas.html",{"cotizaciones_completadas":cotizaciones_completadas,"ver":ver,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"cotizadores":cotizadores,"vendedores":vendedores, "cotizaciones_existentes":cotizaciones_existentes})


@login_required
def creacion_material(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    creado = False
    if request.method == "POST":
        material = Materiales(data=request.POST)
        if material.is_valid():
            creacion = material.save(commit=False)
            creacion.usuario = request.user
            creacion.material = creacion.material.title()
            creacion.save()
            creado = True
    else:
            material = Materiales()
    return render(request, "materiales.html",{"material":material, "creado":creado, "cotizaciones_existentes":cotizaciones_existentes})

@login_required
def creacion_trabajo(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    creado = False
    if request.method == "POST":
        trabajo = TipoDeTrabajo(data=request.POST)
        if trabajo.is_valid():
            creacion = trabajo.save(commit=False)
            creacion.trabajo = creacion.trabajo.title()
            creacion.usuario = request.user
            creacion.save()
            creado = True
    else:
            trabajo = TipoDeTrabajo()
    return render(request, "tipos_trabajo.html",{"trabajo":trabajo, "creado":creado, "cotizaciones_existentes":cotizaciones_existentes})

@login_required
def creacion_cliente(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    creado = False
    if request.method == "POST":
        cliente = Clientes(data=request.POST)
        if cliente.is_valid():
            creacion= cliente.save(commit=False)
            creacion.nombre = creacion.nombre.title()
            creacion.usuario = request.user
            creacion.save()


            creado = True
    else:
            cliente = Clientes()
    return render(request, "clientes.html",{"cliente":cliente, "creado":creado, "cotizaciones_existentes":cotizaciones_existentes})


@login_required
def reportes(request):
    cotizaciones_existentes = CotizacionesSolicitadas.objects.all().filter(cotizador__exact="")
    clientes_creados = models.Clientes.objects.all().order_by("nombre")
    trabajos_creados = models.TipoDeTrabajo.objects.all().order_by("trabajo")
    cotizadores = models.Usuarios.objects.all().filter(categoria="COT").order_by("username")
    vendedores = models.Usuarios.objects.all().filter(categoria="VEN").order_by("username")
    tiempos = {}
    tiempo_promedio_dict = {}
    resultados_dict = {}
    texto_busqueda = ""
    if request.method == "GET":
        return render(request,"reportes.html", {"resultados_dict":resultados_dict,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"cotizadores":cotizadores,"vendedores":vendedores,"cotizaciones_existentes":cotizaciones_existentes})

    if request.method == "POST" and request.POST.get("buscar") == "BUSCAR":
        desde = request.POST.get("desde")
        hasta = request.POST.get("hasta")
        por_cotizador_dict = {}
        texto_busqueda += "Intervalo de busqueda: " + str(desde) + " hasta " + str(hasta)
        usuarios = models.Usuarios.objects.filter(date_joined__range=[str(desde),str(hasta)]).filter(categoria="COT")
        if request.POST.get("seleccion") == "Cliente":
            print(request.POST.get("cl"))
            b = models.Clientes.objects.get(nombre=request.POST.get("cl"))
            cotizaciones = b.client.all().filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="")
            texto_busqueda += "\n"+"Reporte de cliente: " + str(request.POST.get("cl"))

        elif request.POST.get("seleccion") == "Todo":
            print("TODO")
            texto_busqueda += "\n"+"Todas las cotizaciones"
            cotizaciones = CotizacionesSolicitadas.objects.filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="")

        elif request.POST.get("seleccion") == "Trabajo":
            texto_busqueda += "\n"+"Reporte de tipo de trabajo: " + str(request.POST.get("tr"))
            cotizaciones = CotizacionesSolicitadas.objects.all().filter(tipo_trabajo=request.POST.get("tr")).filter(fecha_completada__range=[desde,hasta]).exclude(cotizador__exact="")
        elif request.POST.get("seleccion") == "Vendedor":
            cotizaciones = CotizacionesSolicitadas.objects.all().filter(vendedor=request.POST.get("ven")).filter(fecha_completada__range=[desde,hasta]).exclude(cotizador__exact="")
            texto_busqueda += "\n"+"Reporte de vendedor: " + str(request.POST.get("ven"))


        if request.POST.get("tipo") == "por_tipo_trabajo" or request.POST.get("tipo") == "solo_totales":
            parametro_busqueda = trabajos_creados
            if request.POST.get("tipo") == "solo_totales":
                texto_busqueda += "\n"+"Mostrar por: " + "totales"
                header = "Totales"
            else:
                texto_busqueda += "\n"+"Mostrar por: " + "tipo de trabajo"
                header = "Tipo de trabajo"
            for i in usuarios:
                por_cotizador_dict[str(i)] = {}
                resultados_dict[str(i)] = {}
                if request.POST.get("tipo") != "solo_totales":
                    for item in parametro_busqueda:


                        por_cotizador_dict[str(i)][str(item)] = cotizaciones.filter(cotizador=str(i)).filter(tipo_trabajo=str(item))
                        resultados_dict[str(i)][str(item)] = {"Horas":0,"Cantidad":0}
                por_cotizador_dict[str(i)]["TOTAL"] = cotizaciones.filter(cotizador=str(i))
                resultados_dict[str(i)]["TOTAL"] = {"Horas":0,"Cantidad":0}
            por_cotizador_dict["Total"] = {}
            resultados_dict["Total"] = {}
            if request.POST.get("tipo") != "solo_totales":
                for item in parametro_busqueda:

                    por_cotizador_dict["Total"][str(item)] = cotizaciones.filter(tipo_trabajo=str(item))
                    resultados_dict["Total"][str(item)] = {"Horas":0,"Cantidad":0}
                    print("AQUI ESTA",por_cotizador_dict)
            por_cotizador_dict["Total"]["TOTAL"] = cotizaciones
            resultados_dict["Total"]["TOTAL"] =  {"Horas":0,"Cantidad":0}

        if request.POST.get("tipo") == "por_cliente":
            header = "Cliente"
            texto_busqueda += "\n"+"Mostrar por: " + "cliente"
            #b = models.Clientes.objects.get(nombre=item).client.all().filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="").filter(cotizador=str(i))
            #cotizaciones = b.client.all().filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="")
            parametro_busqueda = clientes_creados
            for i in usuarios:
                por_cotizador_dict[str(i)] = {}
                resultados_dict[str(i)] = {}
                if request.POST.get("tipo") != "solo_totales":
                    for item in parametro_busqueda:


                        por_cotizador_dict[str(i)][str(item)] = models.Clientes.objects.get(nombre=str(item)).client.filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="").filter(cotizador=str(i))
                        resultados_dict[str(i)][str(item)] = {"Horas":0,"Cantidad":0}
                por_cotizador_dict[str(i)]["TOTAL"] = cotizaciones.filter(cotizador=str(i))
                resultados_dict[str(i)]["TOTAL"] = {"Horas":0,"Cantidad":0}
            por_cotizador_dict["Total"] = {}
            resultados_dict["Total"] = {}
            if request.POST.get("tipo") != "solo_totales":
                for item in parametro_busqueda:

                    por_cotizador_dict["Total"][str(item)] = models.Clientes.objects.get(nombre=str(item)).client.filter(fecha_completada__range=[str(desde),str(hasta)]).exclude(cotizador__exact="")
                    resultados_dict["Total"][str(item)] = {"Horas":0,"Cantidad":0}
                    print("AQUI ESTA",por_cotizador_dict)
            por_cotizador_dict["Total"]["TOTAL"] = cotizaciones
            resultados_dict["Total"]["TOTAL"] =  {"Horas":0,"Cantidad":0}
        for e,query in por_cotizador_dict.items():
            tiempos[e] = {}
            tiempo_promedio_dict[e] = {}
            for trabajo in query:
                tiempos[e][trabajo] = []
                for items in por_cotizador_dict[e][trabajo]:
                    dias = 0
                    solicitada =items.fecha_solicitada
                    completada = items.fecha_completada
                    if items.fecha_solicitada.time()>datetime(2009, 12, 1, 17, 30).time():
                        solicitada = solicitada + timedelta(days=1)
                        solicitada = solicitada.replace(hour=8,minute=0)
                        print("AQUI",solicitada)
                    if solicitada.weekday()>completada.weekday():
                        completada = completada - timedelta(days=2)
                    segundos_totales = (completada-solicitada).total_seconds()
                    while (segundos_totales//3600)>15:
                        dias += 1
                        segundos_totales -= (15*3600)
                    if dias > 0:
                        segundos_totales = (segundos_totales + ((dias) * 9 * 3600))
                    else:
                        pass


                    tiempos[e][trabajo].append(segundos_totales)
                try:
                    tiempo_promedio_dict[e][trabajo] = (sum(tiempos[e][trabajo])/len(tiempos[e][trabajo]))
                except:
                    tiempo_promedio_dict[e][trabajo] = 0


        for key in tiempo_promedio_dict:
            for trabajo in tiempo_promedio_dict[key]:
                if tiempo_promedio_dict[key][trabajo] != 0:
                    resultados_dict[key][trabajo]["Horas"] = "{} hora(s) {} minuto(s)".format(str(int(tiempo_promedio_dict[key][trabajo])//3600),str(int(tiempo_promedio_dict[key][trabajo])%60))
                    resultados_dict[key][trabajo]["Cantidad"] = len(tiempos[key][trabajo])
                else:
                    resultados_dict[key][trabajo]["Horas"] = "---------"
                #resultados_dict[key][trabajo]["Minutos"] = int(tiempo_promedio_dict[key][trabajo])%60
    print(tiempos)
    print(tiempo_promedio_dict)
    print(resultados_dict)
    print("AQUI ESTA",por_cotizador_dict)


    #tiempo_promedio = sum(tiempos)/len(tiempos)
    #print(tiempo_promedio)
    #tiempo_real = "{} horas con {} minutos".format(str(tiempo_promedio//3600),str(int(tiempo_promedio % 60)))
    #print(tiempo_real)
    return render(request,"reportes.html", {"header":header,"texto_busqueda":texto_busqueda,"resultados_dict":resultados_dict,"clientes_creados":clientes_creados,"trabajos_creados":trabajos_creados,"cotizadores":cotizadores,"vendedores":vendedores,"cotizaciones_existentes":cotizaciones_existentes})
