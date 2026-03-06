package com.example;

import org.junit.Assert;
import org.junit.Test;

public class paymentTest {
    
    @Test
    public void testPayment(){
        payment p = new payment();
        Assert.assertTrue( p.processPayment(1200, "Card"));
    }
}
