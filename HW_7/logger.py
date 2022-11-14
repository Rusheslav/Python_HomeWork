from datetime import datetime as dt

def make_record(activity: str):
    timestamp = dt.now().strftime('%m/%d/%Y, %H:%M:%S')
    record = f'{timestamp} - {activity}'
    with open('log.txt', 'a') as f:
        f.write(f'{record}\n')