package initial;

import org.testng.Assert;
import org.testng.annotations.Test;

public class TestSuite {
    @Test
    public void testComparePositive() {
        // 测试 a > b 的正例
        Assert.assertTrue(Sample.compare(5, 3));  // 5 > 3
    }

    @Test
    public void testCompareNegative() {
        // 测试 a > b 的负例
        Assert.assertFalse(Sample.compare(2, 3)); // 2 > 3
    }

    @Test
    public void testCompareEdgeCase() {
        // 测试 a == b 的边界情况
        Assert.assertTrue(Sample.compare(3, 3)); // 3 > 3 (boundary)
    }
}
