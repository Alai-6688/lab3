 import socket
   import threading

   def handle_client(conn, addr):
       # Handle client requests here
       pass

   def start_server(host, port):
       server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_socket.bind((host, port))
       server_socket.listen()
       print(f"Server listening on {host}:{port}")

       while True:
           conn, addr = server_socket.accept()
           thread = threading.Thread(target=handle_client, args=(conn, addr))
           thread.start()

   if __name__ == "__main__":
       start_server('localhost', 51234)