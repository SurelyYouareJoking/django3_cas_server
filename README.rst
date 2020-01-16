**CAS Server**


CAS Server is a Django application implementing the CAS Protocol 3.0 Specification.

By default, the authentication process use django internal users but you can easily use any sources (see the Authentication backend section and auth classes in the auth.py file)


**Features**

- Support CAS version 1.0, 2.0, 3.0
- Support Single Sign Out
- Configuration of services via the django Admin application
- Fine control on which user's attributes are passed to which service
- Possibility to rename/rewrite attributes per service
- Possibility to require some attribute values per service
- Federated mode between multiple CAS
- Supports Django 3.0
- Supports Python 3.5+

**Dependencies**

django-cas-server depends on the following python packages:

- Django >= 3.0
- requests >= 2.4
- requests_futures >= 0.9.5
- lxml >= 3.4
- six >= 1.8
