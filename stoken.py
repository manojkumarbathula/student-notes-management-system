from itsdangerous import URLSafeTimedSerializer
secret_key='manoj@143'
def endata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data,salt='manoj@123')

def dndata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.loads(data,salt='manoj@123')