import thingspeak
import time
from pythonping import ping

from credentials import channel_id
from credentials import write_key
from credentials import read_key


def measure():
    response_list = ping('www.google.de', size=40, count=3, timeout=3)
    print(response_list.rtt_avg_ms)
    # write
    #response = channel.update({'field1': ping})

if __name__ == "__main__":
    measure()