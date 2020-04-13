import zmq

def main ():

    print("Zeus starting...")
    # Start child threads
    ctx = zmq.Context()
    subscriber = ctx.socket(zmq.XSUB)
    print("Going to bind to sub")
    subscriber.bind("tcp://*:6001")

    publisher = ctx.socket(zmq.XPUB)
    print("Going to bind to pub")
    publisher.bind("tcp://*:6000")

    zmq.proxy(subscriber, publisher)

    # We never get here…
    subscriber.close()
    publisher.close()
    ctx.term()

if __name__ == '__main__':
    main()