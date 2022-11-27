from inspiration.models import *
from datetime import datetime


def get_messages():
    msgs = MessageBoard.objects.raw(get_messages_sql())
    return to_messages(msgs)


def to_messages(msgs):
    out = []
    for msg in msgs:
        m = {
            "id": msg.id,
            "content": msg.content,
            "random_user": msg.random_user,
            "title": msg.title,
            "reply": msg.reply,
            "reply_user_id": msg.reply_user_id,
            "reply_username": msg.username,
            "reply_user_role": msg.role,
            "create_time": datetime.strftime(msg.create_time, "%Y-%m-%d %H:%M:%S"),
            "lastmodified_time": datetime.strftime(msg.lastmodified_time, "%Y-%m-%d %H:%M:%S")
        }
        out.append(m)
    return out


def get_messages_sql():
    sql = """
SELECT
    t1.id,
    t1.content,
    t1.random_user,
    t1.reply,
    t1.title,
    t1.reply_user_id,
    t2.username,
    t2.role,
    t1.create_time,
    t1.lastmodified_time
FROM
    message_board t1
LEFT JOIN
    users t2
ON
    t1.reply_user_id = t2.id
"""
    return sql