class gamer{
	int name;
	int price;
	
	public void printinfo(){
		System.out.println(this.name);
		System.out.println(this.price);
		
		
		
	}
	
	
	
}

public class game {
	public static void main(String args[]) {
	gamer g1 = new gamer();
	g1.name=45;
	g1.price=123;
	
	g1.printinfo();
	}
}
