from celery import Celery

app = Celery('academic',
             broker='amqp://',
             backend='rpc://',
             include=['RiserAcademicAPI.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()