# pythonUdpMessage

The user datagram protocol (UDP) works differently from TCP/IP. Where TCP is a stream oriented protocol, ensuring that all of the data is transmitted in the right order, UDP is a message oriented protocol. UDP does not require a long-lived connection, so setting up a UDP socket is a little simpler. On the other hand, UDP messages must fit within a single packet (for IPv4, that means they can only hold 65,507 bytes because the 65,535 byte packet also includes header information) and delivery is not guaranteed as it is with TCP.

Run server.py first

python server.py

Run client.py second

After running, type meesage to send in client, there will display message in server side.

