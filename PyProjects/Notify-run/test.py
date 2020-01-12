from notify_run import Notify

notify = Notify()
#print(notify.register())
#print(notify.info())
msg = """Hello there\nthis is a new line"""
notify.send(msg)