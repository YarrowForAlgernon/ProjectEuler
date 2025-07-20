public class E_archive1 {

	public static void main(String[] args) {

		long startTime = System.nanoTime();
		double sum = sumOfdivisibility(3) + sumOfdivisibility(5) - sumOfdivisibility(15);
		System.out.println(sum);
		long stopTime = System.nanoTime();
		System.out.println("Time Taken in nanoseconds: " + (stopTime - startTime));

	}

	public static double sumOfdivisibility(int divisor) {

		int dividend = 999;
		double quotient = dividend / divisor;
		double sum = divisor * 0.5 * quotient * (quotient + 1);
		return sum;
	}
}

