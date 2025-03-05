/*작성자: 임다희(2312282)
 *작성일: 2024-09-26
 *Lab3-2.Car 클래스 작성*/

class Car {//Car 클래스 작성

	//생성된 Car 개체의 개수를 나타내는 static 변수 정의
	//필드 변수 정의
	private static int numberOfCars=0;
	private String model, make;
	
	//Car 클래스의 생성자 정의. 
	//String 매개변수 2개를 입력받으며,
	//생성될 때마다 static 변수 numberOfCars가 1씩 증가. 
	Car(String model, String make){
		this.model=model;
		this.make=make;
		numberOfCars++;
	}
	
	//각 필드에 대한 접근자, 생성자 메소드 작성
	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String getMake() {
		return make;
	}

	public void setMake(String make) {
		this.make = make;
	}

	//static 변수 getNumberOfCars에 접근해 값을 반환하는 메소드.(접근자) 
	public static int getNumberOfCars() {
		return numberOfCars;
	}
	//getNumberOfCars의 생성자. 
	public static void setNumberOfCars(int numberOfCars) {
		Car.numberOfCars = numberOfCars;
	}

	//toString 메소드. 필드 값 정보를 String 값으로 반환한다.
	public String toString() {
		return "Car [model=" + model + ", make=" + make + "]";
	}
}

public class CarTest { //CarTest 클래스. 
	public static void main(String[] args) {
		new Car("35ERIES","BENZ");
		new Car("35ERIES","BENZ");
		new Car("35ERIES","BENZ");
		//새로운 Car 클래스의 객체를 3개 생성한다. 
		System.out.println("총 "+Car.getNumberOfCars()+"대의 자동차가 생산되었습니다.");
		//static 변수에 접근해 Car 클래스의 객체가 몇개인지를 출력한다. 
	}
}
