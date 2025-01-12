package after_mutating;

import org.testng.Assert;
import org.testng.annotations.Test;

public class TestSuite {
    @Test
    public void testComparePositive() {
        Assert.assertTrue(Sample.compare(5, 3));  // 5 > 3
    }

    @Test
    public void testCompareNegative() {
        Assert.assertFalse(Sample.compare(2, 3)); // 2 > 3
    }

    @Test
    public void testCompareEdgeCase() {
        Assert.assertTrue(Sample.compare(3, 3)); // 3 > 3 (boundary)
    }
}
