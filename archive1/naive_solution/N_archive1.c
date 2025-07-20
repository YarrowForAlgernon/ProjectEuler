#include <iostream>
#include <chrono>

int sumOf3() {
	int sum = 0;

	for (int i = 0; i < 1000; i++) {
		if (i % 3 == 0) {
			sum += i;
		}
	}
	return sum;
}

int sumOf5() {

	int sum = 0;

	for (int i = 0; i < 1000; i++) {
		if (i % 5 == 0 && i % 3 != 0) {
			sum += i;
		}
	}
	return sum;
}

int main() {
        auto startTime = std::chrono::high_resolution_clock::now();
	int sum3 = sumOf3();
	int sum5 = sumOf5();
	int finalSum = sum3 + sum5;
	std::cout << finalSum;
	auto stopTime = std::chrono::high_resolution_clock::now();
	std::cout << "\nTime taken in nano seconds: " << std::chrono::duration_cast<std::chrono::nanoseconds>(stopTime-startTime).count();
}
