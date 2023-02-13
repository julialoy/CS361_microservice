# Server --- this is the microservice --- String example
import random
import zmq

PORT = 5555     # Change this value if a different port number is desired


def generate_numbers():
    """
    Generates and returns 3 pseudorandom integers between 1 and 500 (inclusive).

    Makes use of Python's random module.

    :params: none
    :return: string of 3 unique pseudorandom integers
    """
    rand_nums = []
    rand_nums_str = ""

    # Generate pseudorandom numbers, checks for uniqueness
    while len(rand_nums) < 3:
        candidate_num = random.randrange(1, 501, 1)
        if candidate_num not in rand_nums:
            rand_nums.append(candidate_num)
            if len(rand_nums_str) > 1:
                rand_nums_str += " " + str(candidate_num)
            else:
                rand_nums_str += str(candidate_num)

    return rand_nums_str


def run_server():
    """
    Runs a server utilizing PyMQ (ZeroMQ)'s socket API to handle requests from
    clients. Sends a payload of 3 unique pseudorandom integers from
    function generate_numbers(). Payload is sent as a byte string.

    :params: none
    :return: none
    """
    with zmq.Context() as context:
        serv_sock = context.socket(zmq.REP)
        serv_sock.bind(f"tcp://*:{PORT}")

        while True:
            print(f"Listening for connections on port {PORT}...")
            data = serv_sock.recv()    # Typical req is an empty string

            # Close sockets and destroy context if client quits
            # For easy shutdown while testing
            if data.decode().lower() == "q":
                serv_sock.send("Terminating connection.".encode())
                print("\nTerminating connection on client request.")
                break

            print(f"Received request {data.decode().lower()}")

            # Generate and send 3 unique pseudorandom integers
            payload = generate_numbers()
            serv_sock.send(payload.encode())

            print(f"Sent data: {payload}\n")

        print("All connections closed. Server shutting down. Goodbye.")


if __name__ == '__main__':
    run_server()
