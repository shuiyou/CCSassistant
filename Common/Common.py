from datetime import datetime


def format_timestamp(obj):
    if obj is not None:
        print(obj.strftime('%Y-%m-%d %H:%M:%S'))
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return ''

if __name__ == '__main__':
    now = datetime.now() # current date and time
    format_timestamp(now)
