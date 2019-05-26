import uuid
from random import randint
import sys

class UserPersistenceService:

    def session_id(self, request):
        if not "session_id" in request.session:
            request.session["session_id"] = str(uuid.uuid1()).replace('-', '')

        return request.session["session_id"]

    def user_id(self, request):
        user_id = request.GET.get("user_id")

        if user_id:
            request.session['user_id'] = user_id

        if not "user_id" in request.session:
            request.session['user_id'] = randint(10000000000, 90000000000)

        print("ensured id: ", request.session['user_id'])

        return request.session['user_id']