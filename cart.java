package com.example;
import java.util.ArrayList;
import java.util.List;

public class cart {
    private List<product> products = new ArrayList<>();

    public void addProduct(product prod){
        products.add(prod);
    }
    public List<product> getProducts(){
        return products;
    }
    public double calculateTotal(){
        int total  = 0 ; 
        for(product p : products){
            total += p.getTotalPrice();
        }
        return total;
    }
    public boolean isEmpty(){
        return products.isEmpty();
    }
}
