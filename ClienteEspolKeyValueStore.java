import java.io.*;
import java.net.*;
import java.util.*;

public class ClienteEspolKeyValueStore {

	public static void main(String[]args) throws IOException {
		
		if (args.length != 2) {
            System.err.println(
                "ERROR: faltan o sobran argumentos; ej: <ip del servidor> <puerto>");
            System.exit(1);
        }
		
		String hostName = args[0];
		int portNumber = Integer.parseInt(args[1]);
        System.out.println("Conectando...");

		try (
            Socket socket = new Socket(hostName, portNumber);
            DataOutputStream salida = new DataOutputStream(socket.getOutputStream());

            // PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            // BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        ) {
            System.out.println("Conexion establecida"); 
            Scanner scan = new Scanner(System.in);
            String input = scan.nextLine();
            salida.writeUTF(input);
            salida.close();
            // while(true) {
            //     dis = new DataInputStream(socket.getInputStream);
            //     System.out.println(dis.readUTF())

            //     if((fromServer = in.readLine()) != null){
            //         System.out.println("Server: "+ fromServer);
            //     }
            //     fromUser = stdIn.readLine();
            //     if (fromUser != null) {
            //         System.out.println(">> " + fromUser);
            //         out.writeUTF(fromUser);
            //         if (fromUser.equals("exit")){
            //             break;
            //         }
            //     }
            // }
        } catch (UnknownHostException e) {
            System.err.println("El host " + hostName+" no es el correcto.");
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " +hostName);
            System.exit(1);
        }
	}
}