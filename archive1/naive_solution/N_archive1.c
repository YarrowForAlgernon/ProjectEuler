#include <iostream>
#include <chrono>

int sumOfMultiplesUnderN(int multiple, int N = 1000) {
	
	int sumOfMultiples = 0;

	for (int i = 0; i < N; i++) {

		if (i % multiple == 0) {
			sumOfMultiples += i;
		}
	}
	return sumOfMultiples;
}


int main() {
        auto startTime = std::chrono::high_resolution_clock::now();
	int sum3 = sumOfMultiplesUnderN(3);
	int sum5 = sumOfMultiplesUnderN(5);
	int sum15 = sumOfMultiplesUnderN(15);
	int finalSum = sum3 + sum5 - sum15; # application of PIE
	auto stopTime = std::chrono::high_resolution_clock::now();
	std::cout << finalSum;
	std::cout << "\nTime taken in nano seconds: " << std::chrono::duration_cast<std::chrono::nanoseconds>(stopTime-startTime).count();
}
