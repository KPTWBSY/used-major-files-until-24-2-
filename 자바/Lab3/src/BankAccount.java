/*
class BankAccount {
	private int balance;

	BankAccount(int balance) {
		this.balance = balance;
	}

	public int getBalance() {
		return balance;
	}

	public void setBalance(int balance) {
		this.balance = balance;
	}

	public int deposit(int amount) {
		if (amount > 0) {
			balance += amount;
		}
		return balance;
	}

	public int withdraw(int amount) {
		if (amount <= balance) {
			balance -= amount;
		}
		return balance;
	}

	public String toString() {
		return String.format("잔액 : %d ", balance);
	}

	public void transfer(int amount, BankAccount otherAccount) {
		if (amount <= this.balance) {
			this.balance -= amount;
			otherAccount.balance += amount;
		} else {
			System.out.println("잔액이 부족합니다. ");
		}
	}
}*/


