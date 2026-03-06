package com.example;

public class payment {
    public boolean processPayment(int amount, String method){
        if(amount <= 0){
            return false;
        }
        if(method == null || method.isEmpty()){
            return false;
        }
        if(method.equalsIgnoreCase("UPI") || method.equalsIgnoreCase("CARD")){
            return true;
        }
        return false; 
    }
}
