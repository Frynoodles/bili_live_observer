from bilibili_api import live, sync
import pprint

room = live.LiveDanmaku(42062)


@room.on('DANMU_MSG')
async def on_danmuku(event):
    pprint.pprint(event)


@room.on('SEND_GIFT')
async def on_gift(event):
    pprint.pprint(event)


sync(room.connect())
