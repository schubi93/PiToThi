import thingspeak
import time
from pythonping import ping



def measure(channel):
    try:
        server = '8.8.8.8'
        timenow = time.asctime( time.localtime(time.time()))
        response_list = ping(server, size=40, count=10, timeout=3)
        ping_median = response_list.rtt_avg_ms
        print(f'The ping to {server} at {timenow} is {ping_median}ms')
        # write
        response = channel.update({'field1': ping_median})
        #print(response)

    except:
        print("connection failed")


    # write
    #response = channel.update({'field1': ping})

if __name__ == "__main__":
    from credentials import *
    channel = thingspeak.Channel(id=CHANNEL_ID, api_key=API_KEY)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(20)

