# tspweb
# Thrift Saving Plan
## Django Shell     

### Start the Shell    
```
> python manage.py shell
```

### Import Model    

```
>>> from Events.models import Event
```

### First Object       

```
>>> obj1 = Event.objects.first()
>>> obj1.name
'SALARY INCREASE'
>>> obj1.description
'salary increase by 2.5'
```

### All Objects      
```
>>> objAll = Event.objects.all()
>>> objAll
<QuerySet [<Event: Event object (1)>, <Event: Event object (2)>, <Event: Event object (3)>, <Event: Event object (4)>, <Event: Event object (5)>, <Event: Event object (6)>, <Event: Event object (7)>]>
```

### Object Seven      
```
>>> obj7 = Event.objects.get(id=7)
>>> obj7.name
'SALARY INCREASE'
```
