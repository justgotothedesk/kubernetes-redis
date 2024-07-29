import redis
from flask import Flask, jsonify
from datetime import datetime
import threading
import time

rd = redis.StrictRedis(host='redis', port=6379, db=0)

app = Flask(__name__)

@app.route('/')
def home():
    rd.flushdb()
    return "시간이 Redis에 저장됩니다."

@app.route('/insert_times')
def insert_times():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    rd.set(f"{hour}si {minute}boon {second}cho", f"{hour}hour {minute}minute {second}second")
    return "데이터를 넣는 중입니다."

@app.route('/read_times')
def read_times():
    keys = rd.keys('*')
    times = {key.decode('utf-8'): rd.get(key).decode('utf-8') for key in keys}
    return jsonify(times)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# 데이터 저장
# rd.set('key', 'value')

# 데이터 조회
# rd.get('key')

# 데이터 삭제
# rd.delete('key')

# 데이터 전체 삭제
# rd.flushdb()