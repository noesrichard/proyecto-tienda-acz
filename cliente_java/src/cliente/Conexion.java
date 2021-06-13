/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cliente;
import com.google.gson.Gson;
import java.net.URI; 
import java.net.http.HttpClient; 
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;  
import java.net.http.HttpRequest.BodyPublishers; 
import java.util.ArrayList;
import java.util.List;
import org.json.JSONArray; 
import org.json.JSONObject; 

/**
 *
 * @author carri
 */
public class Conexion {
        
        public Conexion(){ 
            
        }
	public static void get_call() throws Exception {
        //Seteamos la url a la API del proyecto para recuperar las categorias
        String url;
        url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories";
        HttpClient client = HttpClient.newHttpClient();
        
        //Creamos la request especificando la url y que usamos el metodo GET
        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI(url))
                .GET()
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());

        JSONArray jArray = new JSONArray(response.body());
        List<Category> categories = new ArrayList<Category>();
        JSONObject jObj = jArray.getJSONObject(0);
        for (int i = 0; i < jArray.length(); i++) {
            JSONObject jsonObj = jArray.getJSONObject(i);
            Category category = new Gson().fromJson(jsonObj.toString(), Category.class); 
            System.out.println(category.getCategory_name());
            categories.add(category); 
            //System.out.println(jsonObj.toString());
        }
        //System.out.println(jObj.toString());
        //Category category = new Gson().fromJson(jObj.toString(), Category.class); 
        //System.out.println(category.getCategory_name());
         
    }
        
    public static String [][] getCategories() throws Exception {
        String url;
        url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories";
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI(url))
                .GET()
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        

        JSONArray jArray = new JSONArray(response.body());
        String [][] categorias = new String[jArray.length()][2];
        
        for (int i = 0; i < jArray.length(); i++) {
            JSONObject jsonObj = jArray.getJSONObject(i);
            Category category = new Gson().fromJson(jsonObj.toString(), Category.class);
            categorias[i][0] = String.valueOf(category.getCategory_id());
            categorias[i][1] = category.getCategory_name();
        }
        return categorias; 
         
    }
    
    public static void crearCategoria(String nombre) throws Exception{ 
        JSONObject json = new JSONObject(); 
        json.put("category_name", nombre); 
        String url;
        url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories";
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI(url))
                .header("Content-Type", "application/json")
                .POST(BodyPublishers.ofString(json.toString()))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
		JSONObject jsonResponse = new JSONObject(response.body());
		System.out.println(response.body());
		System.out.println(jsonResponse.getString("error_exists"));
        
    }
    
    public static void eliminarCategoria(String id) throws Exception{ 
        String url;
        url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories/"+id;
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI(url))
                .DELETE()
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
		System.out.println(response.body());
    }
}
