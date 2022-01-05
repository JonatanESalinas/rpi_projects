import RPi.GPIO as GPIO
from flask import Flask, request, jsonify

app = Flask(__name__)

pin = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
#GPIO.output(pin, GPIO.LOW)

@app.route('/', methods=['POST'])
def enciende():
    print("Voy a encender")
    data = request.get_json()
    obj_a_encender = data['obj']
    
    print(obj_a_encender)
    
    if obj_a_encender == "luz":
        print("enciendo luz")
        GPIO.output(pin, GPIO.HIGH)    

    return "encendido"

@app.route('/apagar', methods=['POST'])
def apaga():
    print("Voy a apagar")
    data = request.get_json()
    obj_a_apagar = data['obj']
    
    print(obj_a_apagar)
    
    if obj_a_apagar == "luz":
        print("apago luz")
        GPIO.output(pin, GPIO.LOW)    
    
    
    return "apagado"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)

