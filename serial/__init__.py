class Serial:
    def __init__(url, *args, **kwargs):
        self.url = url
        self.args = args
        self.kwargs = kwargs

def serial_for_url(url, *args, **kwargs):
    do_open = not kwargs.pop("do_not_open", False)
    instance = Serial(url, *args, **kwargs)
    if do_open:
        instance.open()
    return instance

