from decimal import Decimal
from traceback import print_list
from urllib import response
from django.shortcuts import render
import pytz
# Create your views here.
from django.http import HttpResponse
from apis.models import Device, Humidity
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_device_with_id(request, uid):
    if request.method == "GET":
        try:
            device = Device.objects.get(uid=uid)
            device_details = {
                "uid": device.uid,
                "name": device.name,
            }
            readings = {
                'temperature' : [],
                'humidity' : [],
            }
            for reading in device.temperature_set.all():
                readings['temperature'].append({
                    'temperature':reading.temperature,
                    'time':reading.time,
                })
            for reading in device.humidity_set.all():
                readings['humidity'].append({
                    'humidity':reading.humidity,
                    'time':reading.time,
                })
            print(readings)
            response = json.dumps({'device': device_details , 'readings': readings},indent=4, sort_keys=True, default=str)
        except:
            response = json.dumps({"Error": "There is some problem accrued"})
        return HttpResponse(response, content_type='application/json')
    elif request.method == "DELETE":
        try:
            device = Device.objects.get(uid=uid)
            device.delete()
            response = json.dumps({'result' : 'Device deleted successfully'})
        except:
            response = json.dumps({"Error": "There is some problem accrued"})
        return HttpResponse(response, content_type='application/json')
    else:
        return HttpResponse("Sorry, This method not implemented", content_type='text/json')

            
@csrf_exempt
def get_devices(request):
    if request.method == "GET":
        try:
            # print('try start')
            devices = Device.objects.all()
            # print(devices)
            results = []
            for item in devices:
                device = {
                    # "id" : item.id,
                    "uid": item.uid,
                    "name": item.name,
                }
                results.append(device)
            # print(results)
            response = json.dumps({'devices': results})
        except:
            response = json.dumps({"Error": "There is some problem accrued"})
        return HttpResponse(response, content_type='application/json')
    
    elif request.method == 'POST':
        payload = json.loads(request.body)
        uid = payload.get('uid', None)
        name = payload.get('name', None)
        device = Device(name=name, uid=uid)
        try:
            device.save()
            response = json.dumps({'Success': 'Device added successfully!'})
        except:
            response = json.dumps({'Error': 'Device could not be added!'})
        return HttpResponse(response, content_type='application/json')
    
    else:
        return HttpResponse("Sorry, This method not implemented", content_type='text/json')


def get_readings_time(request,uid,parameter):
    if request.method == "GET":
        try:
            device = Device.objects.get(uid=uid)
            readings = []
            start = request.GET.get('start_on')
            end = request.GET.get('end_on')
            # print(start,end)
            start_on = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
            end_on = datetime.strptime(end, '%Y-%m-%dT%H:%M:%S')
            utc=pytz.UTC
            start_on = start_on.replace(tzinfo=utc)
            end_on = end_on.replace(tzinfo=utc)
            if parameter=='temperature':
                temperature = device.temperature_set.all()
                for temp in temperature:
                    if temp.time>=start_on and temp.time<=end_on:
                        readings.append({
                            'temperature':temp.temperature,
                            'time': temp.time,
                        })
                    
            elif parameter=='humidity':
                humidity = device.humidity_set.all()
                for temp in humidity:
                    # time = temp.time.strftime("%Y-%m-%d-%H:%M:%S")
                    if temp.time>=start_on and temp.time<=end_on:
                        readings.append({
                            'humidity':temp.humidity,
                            'time':temp.time,
                        })
                        
            # print(readings)
            response = json.dumps({'readings':readings },indent=4, sort_keys=True, default=str)
        except Exception as ex:
            print(ex)
            response = json.dumps({"Error": "There is some problem accrued"})
        return HttpResponse(response, content_type='application/json')
    else:
        return HttpResponse("Sorry, This method not implemented", content_type='text/json')


def plot_graph(request):
    if request.method=='GET':
        try:
            uid = request.GET.get('uid')
            device = Device.objects.get(uid=uid)
            readings = {
                'temperature' : [],
                'humidity' : [],
            }

            for reading in device.temperature_set.all():
                readings['temperature'].append({
                    'y': reading.temperature,
                    'x' : reading.time,
                })
            for reading in device.humidity_set.all():
                readings['humidity'].append({
                    'y': reading.humidity,
                    'x':reading.time,
                })
            dataJSON = json.dumps(readings,default=str)
            return render(request, 'apis/graph.html', {'readings':dataJSON})
        except Exception as ex:
            print(ex)
            response = json.dumps({'error':'error'})
            return HttpResponse(response, content_type='application/json')

    else:
        return HttpResponse("Sorry, This method not implemented", content_type='text/json')