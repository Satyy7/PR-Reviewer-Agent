import redis

try:

    r = redis.Redis(
        host="127.0.0.1",
        port=6379,
        db=0,
        decode_responses=True
    )

    print("CLIENT CREATED")

    result = r.ping()

    print("PING RESULT:", result)

except Exception as e:

    print(type(e))
    print(e)