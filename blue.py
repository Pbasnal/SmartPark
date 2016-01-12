import bluetooth, requests, subprocess, json, time


class BlueIOT:
  def getDeviceId(self):
    p = subprocess.Popen(["hcitool", "dev"], stdout=subprocess.PIPE).communicate()[0]
    id = p.split("\t")[-1].strip()
    
    #print( "Zone Id Found : " + id)

    return id
  
  def searchNearbyDevices(self):
    devices = bluetooth.discover_devices(lookup_names=True)
    #print(devices)

    return devices

class SmartPark:
  url = "http://smartpark.cloudapp.net:8080/ble"

  def findPlacesAndPost(self):
    blue = BlueIOT()
    
    ZoneId = blue.getDeviceId()
    devices = blue.searchNearbyDevices()

    #if(len(devices) == 0):
      #return False
    
    Cars = []
    for dev in devices:
      Cars.append({"car_ID": dev[0], "signal_strength": 0})

    postData = json.dumps({"parking": ZoneId, "cars": Cars})
    print(postData);
    requests.post(self.url, data=postData)
    
    return True




smartPark = SmartPark()

while True:
  result = smartPark.findPlacesAndPost()
  #print result
  print
  #time.sleep(10)





















