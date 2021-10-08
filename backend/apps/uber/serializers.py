import re
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        # Validating email structure:
        email = data.get('email')
        if not check(email):
            raise serializers.ValidationError({"error":"Invalid email structure"})
        return data
 
def check(email):
    # Email validation regex
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False