print("Funciones Version 2")
print("Gabriel Montes")

celulares=["android","iphone","huawei"]
autos=("ford","nissan","Honda")
lenguas={"español","frances","italiano"}
colores={
    "verde": "amarillo/azul",
    "naranja": "amarillo/rojo",
    "morado": "rojo/azul"
}
instrumento=["piano","guitarra","trompeta"]

def vl(t):
    for uc in t:
        print(uc)

def vi(i):
    for ui in i:
        print(ui)

def va(a):
    for ua in a:
        print(ua)

def vle(le):
    for ul in le:
        print(ul)

def vc(c):
    for uco in c:
        print(uco)


vl(celulares)
print("")
vi(instrumento)
print("")
va(autos)
print("")
vle(lenguas)
print("")
vc(colores)
print("")

# python funcionesv2.py