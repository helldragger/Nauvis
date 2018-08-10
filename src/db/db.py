def does_table_exists(link, name):
    return link.execute("SELECT name FROM sqlite_master WHERE type='table' "
                        "AND name=?;",name)


def add_event(*args):
    pass


def add_date(*args):
    pass


def update_event(*args):
    pass


def update_date(*args):
    pass


def info_event(*args):
    pass


def info_date(*args):
    pass