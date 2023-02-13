# Client Example --- String example
import zmq

MSG = ""    # Serves as dummy message for alerting server client is ready
USER_MSG = "Enter 'n' to see 3 random numbers. Enter 'q' to quit: "


def parse_data(d):
    """
    Attempts to turn string into a list of integers.
    Assumes parameter is a whitespace delimited string.

    :params: d: data as string
    :return: list of 3 integers
    """
    try:
        temp_list = d.split(' ')
        int_list = [int(item) for item in temp_list]
        return int_list
    except ValueError:
        return []


def run_client():
    """
    Example client that on input from user will handle requesting data
    from a server. Expects server data to be a Python string. Prints
    data received from server.

    :params: none
    :return: none
    """
    print("Client program running...")
    user_input = input(USER_MSG)

    # Simple UI
    while True:
        if user_input.lower().strip() == 'n':
            nums = connect_to_server()
            nums_list = parse_data(nums)
            (print(f"\nYour list of numbers is: {nums_list}")
             if len(nums_list) == 3
             else print("\nAn error occurred. Unable to show your list."))
            user_input = input(USER_MSG)
        elif user_input.lower().strip() == 'q':
            confirm = connect_to_server(user_input.lower().strip())
            if confirm:
                print(f"\nConnection with server successfully closed.")
            else:
                print("\nError: No response from server.")
            break
        else:
            print("Option not recognized.")
            user_input = input(USER_MSG)

    print("Client program shutting down. Goodbye!")


def connect_to_server(client_msg=MSG):
    """
    Connects to a server via PyMQ (ZeroMQ)'s socket API.
    Sends a message to server indicating it is ready for data and receives
    server data as a byte string.

    Returns the decoded data.

    :params: string: default is empty string to request data, sends 'q' to
                     tell server client is terminating the connection
    :return: data as string
    """
    with zmq.Context() as context:
        print("Connecting to server...")
        client_sock = context.socket(zmq.REQ)
        client_sock.connect("tcp://localhost:5555")

        client_sock.send(client_msg.encode())

        data = client_sock.recv().decode()

    return data


if __name__ == '__main__':
    run_client()
