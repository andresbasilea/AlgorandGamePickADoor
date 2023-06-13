# AlgorandGamePickADoor
Algorand based "Pick A Door" game, where the user is presented with a GUI where he/she can choose a bet amount and bet on one of three doors, with a prize behind one of them. If the user wins, he is paid double the amount he risked, if he loses he must pay the bet amount. 

INSTALLATION AND USAGE:

- Git clone the repository -> git clone https://github.com/andresbasilea/AlgorandGamePickADoor.git
- Try running the application using -> python GUI_main.py
- IF an error occurs due to missing dependencies, see the requirements file (requirements.txt) to install them all. Use:
    - pip install Pillow
    - pip install py_algorand_sdk
    - pip install tk or sudo apt-get install python3-tk


- Enter the application by connecting to the Basile Keller wallet with your credentials. For this example, you should click on "Browse" and select the accountAddressesKeysUser.txt text file to simulate the connection to the wallet. 
- The account with which you enter the application is the one to be used for the game. 
- Select a bet amount (1, 2 or 3 Algos) and click a door to start playing. 

