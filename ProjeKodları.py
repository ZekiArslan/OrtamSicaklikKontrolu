import RPi.GPIO as GPIO  // GPIO Pinlerini kullanmak için tanımlama
from time import sleep  // time ve sleep kütüphaneleri
import Adafruit_DHT  // DHT 11 kullanımı için gerekli kütüphane terminal üzerinden kuruldu
import time 

DHT_SENSOR=Adafruit_DHT.DHT11   // Sensör tipi belirlendi
DHT_PIN=14 // Sensörün bağlı olduğu GPIO pin numarası
GPIO.setmode(GPIO.BOARD) //Pin modu belirleme BCM-BOARD 

Motor1A = 16 // Motor sağ sol 
Motor1B = 18 // Motor sağ sol
Motor1E = 22  // motorun aktif pasif hareketini belirleyen pin ve atandığı GPIO numarası
LED = 11

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)  // GPIO modunu çıkış olarak ayarlıyoruz
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(LED,GPIO.OUT) // çıkış ayarlama

print ("Fan Çalışmaya Hazır.") 
GPIO.output(Motor1A,GPIO.HIGH)  // Motor yönü sağ olarak belirlendi
GPIO.output(Motor1B,GPIO.LOW)  // motor sol taraf için pasif durumda
GPIO.output(Motor1E,GPIO.LOW)  // sistem başlangıcı motora güç gitmiyor



while True:
    nem,sicaklik = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) 
    if nem is not None and sicaklik is not None:
        print("Sıcaklık= {0:0.1f}C Nem= {1:0.1f}%".format(sicaklik,nem))

        if sicaklik==27:
            print("Ortam Uygun Sıcaklıkta")
            GPIO.output(Motor1E,GPIO.LOW)
            GPIO.output(LED,GPIO.LOW)
            print("Fan ve Isıtıcı devre dışı.")

        if sicaklik>27:

            print ("Fan Çalışıyor.")
            GPIO.output(Motor1E,GPIO.HIGH)
            GPIO.output(LED,GPIO.LOW)

        if sicaklik<27:
            print("Isıtıcı Çalışıyor")
            GPIO.output(Motor1E,GPIO.LOW)
            GPIO.output(LED,GPIO.HIGH)



GPIO.cleanup()  // GPIO Çıkıç pin loglarını temizliyor