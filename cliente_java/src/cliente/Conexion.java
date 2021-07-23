/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cliente;

import entities.Brand;
import entities.Category;
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


	private HttpClient client;  

	public Conexion() {
		this.client = HttpClient.newHttpClient();
	}

	public String[][] getProducts() throws Exception {
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/products";
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.GET()
				.build();
		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());

		JSONArray jArray = new JSONArray(response.body());
		String[][] products = new String[jArray.length()][7];
		for (int i = 0; i < jArray.length(); i++) {
			products[i][0] = String.valueOf(jArray.getJSONObject(i).getInt("product_id"));
			products[i][1] = jArray.getJSONObject(i).getString("product_name");
			products[i][2] = jArray.getJSONObject(i).getString("product_description");
			products[i][3] = String.valueOf(jArray.getJSONObject(i).getDouble("product_price"));
			products[i][4] = String.valueOf(jArray.getJSONObject(i).getInt("product_quantity_available"));
			products[i][5] = jArray.getJSONObject(i).getString("category");
			products[i][6] = jArray.getJSONObject(i).getString("brand");
		}
		return products;

	}

	public String[][] getCategories() throws Exception {
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories";
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.GET()
				.build();

		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());

		JSONArray jArray = new JSONArray(response.body());
		String[][] categorias = new String[jArray.length()][2];

		for (int i = 0; i < jArray.length(); i++) {
			JSONObject jsonObj = jArray.getJSONObject(i);
			Category category = new Gson().fromJson(jsonObj.toString(), Category.class);
			categorias[i][0] = String.valueOf(category.getCategory_id());
			categorias[i][1] = category.getCategory_name();
		}
		return categorias;

	}

	public void crearCategoria(String nombre) throws Exception {
		JSONObject json = new JSONObject();
		json.put("category_name", nombre);
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories";
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.header("Content-Type", "application/json")
				.POST(BodyPublishers.ofString(json.toString()))
				.build();

		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());
		JSONObject jsonResponse = new JSONObject(response.body());
	}

	public void crearProducto(String nombre, String descripcion,
			Double precio, Integer cantidadDisponible, Category categoria,
			Brand brand) {
		JSONObject json = new JSONObject();
		json.put("product_name", nombre);
		json.put("product_description", descripcion);
		json.put("product_price", precio);
		json.put("product_quantity_available", cantidadDisponible);
		json.put("category_id", categoria.getCategory_id());
		json.put("brand_id", brand.getBrand_id());
		String url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories";
		
	}

	public void eliminarCategoria(String id) throws Exception {
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/categories/" + id;
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.DELETE()
				.build();
		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());
		System.out.println(response.body());
	}

	//Methods for Brands
	public String[][] getBrands() throws Exception {
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/brands";
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.GET()
				.build();

		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());

		JSONArray jArray = new JSONArray(response.body());
		String[][] marcas = new String[jArray.length()][2];

		for (int i = 0; i < jArray.length(); i++) {
			JSONObject jsonObj = jArray.getJSONObject(i);
			Brand brand = new Gson().fromJson(jsonObj.toString(), Brand.class);
			marcas[i][0] = String.valueOf(brand.getBrand_id());
			marcas[i][1] = brand.getBrand_name();
		}
		return marcas;

	}

	public void crearMarca(String nombre) throws Exception {
		JSONObject json = new JSONObject();
		json.put("brand_name", nombre);
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/brands";
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.header("Content-Type", "application/json")
				.POST(BodyPublishers.ofString(json.toString()))
				.build();

		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());
		JSONObject jsonResponse = new JSONObject(response.body());
		System.out.println(response.body());

	}

	public void eliminarMarca(String id) throws Exception {;
		String url;
		url = "https://proyecto-tienda-acz.herokuapp.com/catalog/brands/" + id;
		HttpRequest request = HttpRequest.newBuilder()
				.uri(new URI(url))
				.DELETE()
				.build();
		HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());
		System.out.println(response.body());
	}
}
