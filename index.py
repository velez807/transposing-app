from flask import Flask, render_template, request, url_for

def conversion(tono_original, tono_nuevo, notain):
    lista_notas=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        
    #funcion para revisar que las notas esten bien escritas
    def revisar_notas(tono):
        c=0
        for i in lista_notas:
            if tono==i:
                numero_tono=lista_notas.index(i)
                break
            c+=1
            if c==12:
                print("Nota no reconocida")
                exit()

        return numero_tono

    #funcion para convertir los bemoles si son ingresados
    def convertir_bemol(notas):
        for i, n in enumerate(notas):
            if n=='CB':
                notas[i]='B'
            if n=='DB':
                notas[i]='C#'
            if n=='EB':
                notas[i]='D#'
            if n=='FB':
                notas[i]='E'
            if n=='GB':
                notas[i]='F#'
            if n=='AB':
                notas[i]='G#'
            if n=='BB':
                notas[i]='A#'
            else: 
                pass
        
        return notas


    numero_tono_original=revisar_notas(tono_original)

    numero_tono_nuevo=revisar_notas(tono_nuevo)


    #Funcion para saber hacia donde hay que hacer el recorrido en la lista de notas
    if numero_tono_original < numero_tono_nuevo:
        recorrido=numero_tono_nuevo-numero_tono_original
    else:
        recorrido=12-numero_tono_original+numero_tono_nuevo


    #Funcion para convertir las notas
    notain=notain.upper()
    lista1 = notain.split(' ')
    lista = convertir_bemol(lista1)
    listaout=[]
    # recorrer la lista y si encuentra un - eliminarlo
    for i in reversed(lista):
        if i=='-':
            lista.remove(i)

    #Elimina un espacio al final en caso de existir
    for i in reversed(lista):
        if i=='':
            lista.remove(i)

    #Se recorre la lista de notas y se convierte en notas nuevas
    for j in lista:
        c=0
        for i in lista_notas:
            if i==j:
                numero_nota=lista_notas.index(i)
                notaout=lista_notas[numero_nota-recorrido]
                listaout.append(notaout)

                break
            c+=1
            if c==12:
                msg="???"
                listaout.append(msg)
                break

    #Se imprime la lista de notas nuevas
    result= ' - '.join(listaout)
    return result

def conversion1(tono_original, tono_nuevo, notain):
    lista_notas=['Do','Do#','Re','Re#','Mi','Fa','Fa#','Sol','Sol#','La','La#','Si']


        
    #funcion para revisar que las notas esten bien escritas
    def revisar_notas(tono):
        c=0
        for i in lista_notas:
            if tono==i:
                numero_tono=lista_notas.index(i)
                break
            c+=1
            if c==12:
                print("Nota no reconocida")
                exit()

        return numero_tono

    #funcion para convertir los bemoles si son ingresados
    def convertir_bemol(notas):
        for i, n in enumerate(notas):
            if n=='Dob':
                notas[i]='Si'
            if n=='Reb':
                notas[i]='Do#'
            if n=='Mib':
                notas[i]='Re#'
            if n=='Fab':
                notas[i]='Mi'
            if n=='Solb':
                notas[i]='Fa#'
            if n=='Lab':
                notas[i]='Sol#'
            if n=='Sib':
                notas[i]='La#'
            else: 
                pass
        
        return notas

    numero_tono_original=revisar_notas(tono_original)

    numero_tono_nuevo=revisar_notas(tono_nuevo)


    #Funcion para saber hacia donde hay que hacer el recorrido en la lista de notas
    if numero_tono_original < numero_tono_nuevo:
        recorrido=numero_tono_nuevo-numero_tono_original
    else:
        recorrido=12-numero_tono_original+numero_tono_nuevo


    #Funcion para convertir las notas
    notain=notain.upper()
    lista1 = notain.split(' ')
    r=[]
    for i in lista1:
        i = i.capitalize()
        r.append(i)
    lista = convertir_bemol(r)
    listaout=[]

    #Elimina un espacio al final en caso de existir
    for i in reversed(lista):
        if i=='':
            lista.remove(i)

    #Se recorre la lista de notas y se convierte en notas nuevas
    for j in lista:
        c=0
        for i in lista_notas:
            if i==j:
                numero_nota=lista_notas.index(i)
                notaout=lista_notas[numero_nota-recorrido]
                listaout.append(notaout)

                break
            c+=1
            if c==12:
                msg="???"
                listaout.append(msg)
                break

    #Se imprime la lista de notas nuevas
    result= ' - '.join(listaout)
    return result

# Servidor:
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clasicas')
def clasicas():
    return render_template('clasicas.html')


@app.route('/convertir', methods=['GET', 'POST'])
def convertir():
    tono_original=str(request.form['tono_original'])
    tono_nuevo=str(request.form['tono_nuevo'])
    notain=str(request.form['notain'])
    result=conversion(tono_original, tono_nuevo, notain)
    return render_template('home.html', result=result, notas=notain, original=tono_original, nuevo=tono_nuevo)

@app.route('/convertir1', methods=['GET', 'POST'])
def convertir1():
    tono_original=str(request.form['tono_original'])
    tono_nuevo=str(request.form['tono_nuevo'])
    notain=str(request.form['notain'])
    result=conversion1(tono_original, tono_nuevo, notain)
    return render_template('clasicas.html', result=result, notas=notain, original=tono_original, nuevo=tono_nuevo)

# vea ni por el hpta borre o mueva esto
if __name__ == '__main__':
    app.run(debug=True)