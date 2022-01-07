import RPi.GPIO as GPIO
from flask import Flask, request, jsonify

app = Flask(__name__)

pinLuz = 33
pinVentilador = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pinLuz,GPIO.OUT)
GPIO.setup(pinVentilador,GPIO.OUT)

#Pongo en HIGH los pines porque estos reles se activan con el LOW.
GPIO.output(pinLuz, GPIO.HIGH)
GPIO.output(pinVentilador, GPIO.HIGH)

@app.route('/', methods=['POST'])
def enciende():
    print("Voy a encender")
    data = request.get_json()
    obj_a_encender = data['obj']
    
    print(obj_a_encender)
    
    if obj_a_encender == "luz":
        print("enciendo luz")
        GPIO.output(pinLuz, GPIO.LOW)
    elif obj_a_encender == "ventilador":
        print("enciendo luz")
        GPIO.output(pinVentilador, GPIO.LOW)

    return "encendido"

@app.route('/apagar', methods=['POST'])
def apaga():
    print("Voy a apagar")
    data = request.get_json()
    obj_a_apagar = data['obj']
    
    print(obj_a_apagar)
    
    if obj_a_apagar == "luz":
        print("apago luz")
        GPIO.output(pinLuz, GPIO.HIGH)
    elif obj_a_apagar == "ventilador":
        print("apago ventilador")
        GPIO.output(pinVentilador, GPIO.HIGH)
    
    
    return "apagado"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)

