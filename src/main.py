import thingspeak
import time
from pythonping import ping



def measure(channel):
    try:
        response_list = ping('www.google.de', size=40, count=3, timeout=3)
        ping_median = response_list.rtt_avg_ms
        print(ping_median)
        # write
        response = channel.update({'field1': ping_median})
        print(response)

    except:
        print("connection failed")


    # write
    #response = channel.update({'field1': ping})

if __name__ == "__main__":
    from credentials import *
    channel = thingspeak.Channel(id=CHANNEL_ID, api_key=READ_KEY)
    measure(channel)
    # while True:
    #     measure(channel)
    #     # free account has an api limit of 15sec
    #     time.sleep(15)