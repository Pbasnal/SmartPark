import bluetooth, requests, pprint
import subprocess
import json


class BlueIOT:
  def getDeviceId(self):
    p = subprocess.Popen(["hcitool", "dev"], stdout=subprocess.PIPE).communicate()[0]
    id = p.split("\t")[-1].strip()
    
    print( "Zone Id Found : " + id)

    return id
  
  def searchNearbyDevices(self):
    devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    print(devices)

    return devices

class SmartPark:
  url = "http://smartpark.cloudapp.net:8080/ble"

  def findPlacesAndPost(self):
    parking = ParkingData()
    blue = BlueIOT()
    
    ZoneId = blue.getDeviceId()
    devices = blue.searchNearbyDevices()

    if(len(devices) == 0):
      return False
    
    parking.ParkingZone = ZoneId

    for dev in devices:
      car = Car()
      car.CarId = dev[0]
      car.Rssi = 0
      parking.Cars.append({"car_ID": dev[0], "signal_strength": 0})

    postData = json.dumps({"parking": parking.ParkingZone, "cars": parking.Cars})
    print(postData);
    requests.post(self.url, data=postData)
    
    return True




smartPark = SmartPark()

smartPark.findPlacesAndPost()
