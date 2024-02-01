import os
# import multiprocessing

mode = os.environ.get("MODE", "development")
host = os.environ.get("HOST", "localhost")
port = os.environ.get("PORT", "9000")

# https://docs.gunicorn.org/en/latest/design.html#how-many-workers
def number_of_workers():
    # return (multiprocessing.cpu_count() * 2) + 1
    return 4


config = {
    "mode": mode,
    "host": host,
    "port": port,
    'bind': '%s:%s' % (host, port),
    'workers': number_of_workers(),
}
