#include <iostream>
#include <chrono>

int sumOfDivisibility(int divisor, int dividend = 999) {

	int quotient = dividend / divisor;
	int sum = divisor * 0.5 * quotient * (quotient + 1);
	return sum;
}


int main() {

	auto startTime = std::chrono::high_resolution_clock::now();
	int sum = sumOfDivisibility(3) + sumOfDivisibility(5) - sumOfDivisibility(15); // application of PIE
	auto stopTime = std::chrono::high_resolution_clock::now();
	std::cout << sum;
	std::cout << "\nTime taken in nano seconds: " << std::chrono::duration_cast<std::chrono::nanoseconds>(stopTime-startTime).count();
}
