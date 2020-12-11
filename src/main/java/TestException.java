/*
 * Copyright 2017 Datalogics, Inc.
 */

public class TestException {
    static {
        System.loadLibrary("jnicmakeswig");
    }

    private native void throwException();

    // Test Driver
    public static void main(String[] args) {
        new Foo().justThrow();
    }
}
