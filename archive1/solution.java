
public class archive1 {

	public static void main(String[] args) {

		int sum3 = Sum3();
		int sum5 = Sum5();
		int finalSum = sum3 + sum5;
		System.out.println(finalSum);

	}

	// what the helly
	public static int Sum3() {

		int sum = 0;
		for (int i = 0;i < 1000;i++) {
			if (i % 3 == 0) {
				sum += i;
			}
		}
		return sum;
	}

	public static int Sum5() {
		int sum = 0;
		for (int i = 0; i<1000; i++) {
			if (i % 5 == 0 && i % 3 != 0) {
				sum += i;
			}
		}
		return sum;
	}
}

