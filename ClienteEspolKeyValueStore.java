import java.io.*;
import java.net.*;

public class ClienteEspolKeyValueStore {

	public static void main(String[]args) throws IOException {
		
		if (args.length != 2) {
            System.err.println(
                "ERROR: faltan o sobran argumentos; ej: <ip del servidor> <puerto>");
            System.exit(1);
        }
		
		String hostName = args[0];
		int portNumber = Integer.parseInt(args[1]);

		try (
            System.out.println("Conectando...");
            Socket kkSocket = new Socket(hostName, portNumber);
            PrintWriter out = new PrintWriter(kkSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(kkSocket.getInputStream()));
        ) {
            System.out.println("ok");
            System.out.println(">> ");            
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            String fromServer;
            String fromUser;

            while ((fromServer = in.readLine()) != null) {
                System.out.println(">> " + fromServer);
                if (fromServer.equals("Bye"))
                    break;
                
                fromUser = stdIn.readLine();
                if (fromUser != null) {
                    System.out.println(">>> " + fromUser);
                    out.println(fromUser);
                }
            }
        } catch (UnknownHostException e) {
            System.err.println("El host " + hostName+" no es el correcto.");
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " +hostName);
            System.exit(1);
        }
	}
}