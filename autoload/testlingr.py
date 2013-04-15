

import time
import lingr

m = lingr.Message({
            'id': '-1',
            'local_id': '-1',
            'public_session_id': '-1',
            'room': '',
            'type': 'dummy',
            'nickname': '-',
            'speaker_id': '-1',
            'icon_url': '',
            'text': '-',
            'timestamp': time.strftime(lingr.Message.TIMESTAMP_FORMAT, time.gmtime())
            })


print dir(m)

m = lingr.Member({
    "username": "thinca the manbou",
    "name": "thinca",
    "icon_url": "google.com",
    'timestamp': time.strftime(lingr.Message.TIMESTAMP_FORMAT, time.gmtime()),
    "is_owner": True, #Ugh!
    "is_online": True,
    "pokeable": False,
    })

print dir(m)
print m

import lingrvim

jar = lingrvim.SQLMessageJar();

jar.add_message("", lingr.Message({
            'id': '-1',
            'local_id': '-1',
            'public_session_id': '-1',
            'room': '',
            'type': 'dummy',
            'nickname': '-',
            'speaker_id': '-1',
            'icon_url': '',
            'text': '-',
            'timestamp': time.strftime(lingr.Message.TIMESTAMP_FORMAT, time.gmtime())
            }))
print jar.get_count('')

