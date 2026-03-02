package com.example;


import org.junit.Assert;
import org.junit.Test;


public class cartTest {
    
    @Test
    public void testCartTotal(){
        cart c = new cart();
        c.addProduct(new product("laptop", 5000, 2));
        c.addProduct(new product("speaker", 1000, 1));
        Assert.assertEquals(11000.0, c.calculateTotal(), 0.0);
    }
}
