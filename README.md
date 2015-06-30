#Wolfson Patchbay Mixer

A GUI utility for configuring input/output connections in a **Wolfson Pi Audio Card**.

Just drag a button with a Jack connector icon and drop it into any input connector. You can for example, drag the jack of the Line In and connect it to Line Out, or connect DMIC to the Dynamic Range Controller and then to the Headphones.

##Requirements:
- Raspberry Pi Model B
- Wolfson Pi Audio Card
- Python 2.7 or later. Already included in Raspbian distribution.
- PyQT4 library. Install it from Raspbian repository with `sudo apt-get install python-qt4`


##Usage:
Get into the project directory and run `python wolfson-pbm.py`

To connect a device to another: 
- Press a button with a jack 1/8 connector icon of a device desired and select from the context menu where you want to connect. 
- Or *right-click and drag* a button with the jack connector icon and *drop* it into a input female connector icon of the device you want to connect.
In both cases a cable appears representing the connection.

To Disconnect:
-Just click the input female connector icon.

###Important note:
This is currently incomplete. I implemented the most relevant devices only.
I just code this in my spare time. Any aportation to code will be appreciated. Any refork to make the code more Object-Oriented is welcome.
I didn't tested all outputs because I don't have all the gear required for testing like SPDIF equipment, 4-pole jack headsets or loudspeakers.

###TODO:
- Load current connections in alsamixer at opening.
- Add Volume Controls
- Add EQ inputs/outputs
- Support to the Cirrus Audio Card (for the B+ models)
