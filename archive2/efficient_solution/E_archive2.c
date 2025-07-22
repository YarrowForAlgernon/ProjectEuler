#include <iostream>
#include <chrono>

int getNextEvenFibTerm(int previous3rdTerm, int currentTerm) {

	int nextTerm = (4 * currentTerm) + previous3rdTerm;
	return nextTerm;
}

int sumFibTerms() {
	int currentTerm = 8;
	int previousTerm = 2;
	int sum = 2;
	while (currentTerm < 4000000) {
		sum += currentTerm;
		int nextTerm = getNextEvenFibTerm(previousTerm, currentTerm);
		previousTerm = currentTerm;
		currentTerm = nextTerm;
	}
	return sum;
}

int main() {

	auto startTime = std::chrono::high_resolution_clock::now();
	int sum = sumFibTerms();
	auto stopTime = std::chrono::high_resolution_clock::now();
	std::cout << sum; 
	std::cout << "\nTime taken for algorithim to execute in nanoseconds: " << std::chrono::duration_cast<std::chrono::nanoseconds>(stopTime-startTime).count();
}
