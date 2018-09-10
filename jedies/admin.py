from django.contrib import admin
from .models import Candidate
from .models import Jedi
from .models import Planet
from .models import Test
from .models import Answer


admin.site.register(Candidate)
admin.site.register(Jedi)
admin.site.register(Planet)
admin.site.register(Test)
admin.site.register(Answer)
# Register your models here.
