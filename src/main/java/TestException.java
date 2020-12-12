/*
 * Copyright 2017 Datalogics, Inc.
 */
improt org.mizux.cmakeswig.foo;

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
