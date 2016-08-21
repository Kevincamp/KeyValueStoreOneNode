import java.io.*;
import java.net.*;

public class ConnectionToBD {
	String hostName = args[0];
	int portNumber = Integer.parseInt(args[1]);

	public ConnectionToBD(){}

	public void connecting(hostName, portNumber) {
		try (
            Socket kkSocket = new Socket(hostName, portNumber);
            PrintWriter out = new PrintWriter(kkSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(kkSocket.getInputStream()));
        ) {
            System.out.println("Connected ...");
        } catch (UnknownHostException e) {
            System.err.println("Don't know about host " + hostName);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " +
                hostName);
            System.exit(1);
        }
	}
}
