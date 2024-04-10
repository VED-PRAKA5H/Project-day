# Secret Auction  

A simple Python program to conduct a secret auction where multiple bidders can place their bids anonymously, and the highest bidder wins.  

### How It Works  
1. The program welcomes the user and prompts for bidder names and their bid amounts.  
2. Bids are stored in a dictionary with bidder names as keys and bid amounts as values.  
3. The program asks if there are more bidders and continues collecting bids until the auction ends.  
4. After all bids are collected, it determines and prints the winner with the highest bid.  

### Example  
```
Welcome to secret auction program  
what is your name?  
> Alice  
what is your bid?: ₹  
> 1500  
are there any other bidder? type yes or no  
> yes  
what is your name?  
> Bob  
what is your bid?: ₹  
> 1800  
are there any other bidder? type yes or no  
> no  
The winner is Bob with bid of ₹1800  
```

### How to Use  
- Run the script using Python:  
```
python main.py
```
- Enter bidder names and bids as prompted until the auction ends.

### Requirements  
- Python 3.x  
