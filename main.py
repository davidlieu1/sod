from datetime import datetime
import json

#gets input with confirmation
def getin(name):
    while True:
        item = input("ENTER \t- ("+name+"): ")
        reply = input("CONFIRM\t- ("+name+"):'"+str(item)+ "' (y): ")
        if reply.lower() == 'y':
            return item

def exists():
    try:
        with open('data.txt', 'r'):
            pass
    except:
        with open('data.txt', 'w') as f:
            json.dump({'$date of creation': str(datetime.now())}, f)

def load():
    exists()
    with open('data.txt', 'r') as f:
        data = json.load(f)
    return data

def save(data):
    with open('data.txt', 'w') as f:
        json.dump(data, f)

def entry(data, time, song, artist):
    data[time] = (song, artist)

if __name__ == "__main__":
    data = load()
    print(data['2021-02-17 20:53:20.967787'])
    song = getin('song title')
    artist = getin('artist name')
    time = str(datetime.now()) 
    entry(data, time, song, artist)
    print(time+'\t'+song+'\t'+artist)
    save(data)
    print('SAVED')