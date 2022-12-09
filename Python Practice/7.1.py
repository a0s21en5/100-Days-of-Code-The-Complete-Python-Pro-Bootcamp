res = ""


def abc(end, start):
    global res
    dest = end.get(start)
    if not dest:
        return

    res += " —> " + dest
    abc(end, dest)


def xyz(tickets):

    destinations = {*tickets.values()}

    for k, v in tickets.items():
        global res
        for _ in range(1):
            res += k

        if k not in destinations:

            abc(tickets, k)
            return


tickets = {
    'LAX': 'DXB',
    'DFW': 'JFK',
    'LHR': 'DFW',
    'JFK': 'LAX'
}
xyz(tickets)

res = res[6:]
print(res)
