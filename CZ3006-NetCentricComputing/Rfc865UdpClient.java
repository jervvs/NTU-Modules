package cz3006_lab2;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class Rfc865UdpClient {

	public static void main(String[] args) throws UnknownHostException {
		
		String host = args[0];
		
		//1. Open UDP Socket
		DatagramSocket socket = null;
		try {
			socket = new DatagramSocket();
			InetAddress IpAddress = InetAddress.getByName(host);
			socket.connect(IpAddress, 17);
		} catch(SocketException e){
			System.out.println("Socket error! " + e.getMessage());
		}
		
		try {
			//2. Send UDP request to server
			byte[] buffer = "Jervis Chan, TS8, 172.21.149.77".getBytes();
			DatagramPacket request = new DatagramPacket(buffer, buffer.length);
			socket.send(request);
			
			// 3. Receive UDP reply from server
			byte[] replyBuffer = new byte[512];
			DatagramPacket reply = new DatagramPacket(replyBuffer, replyBuffer.length);
			socket.receive(reply);
			
			
			String quote = new String(replyBuffer);
			System.out.println(quote);
		} catch (IOException e) {
			System.out.println("IOException error! " + e.getMessage());
		}
		
		
	}

}
