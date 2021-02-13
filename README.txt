
Prepare to be blown away. You may have paid for the whole seat but you'll only need the edge!

1.	Download VMware Workstation Player (If you don't already have it)
	https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html
	
2.	Download Ubuntu Desktop
	https://ubuntu.com/download/desktop/thank-you?version=20.04.2.0&architecture=amd64
	
3.	Install a new VM with the Ubuntu image
	a.	Allocate at least 50Gb to Hard Disk
	b.	Give it as much RAM as possible
	c.	Right click the VM > Settings > Processor > Enable Virtualize Intel VT-x/EPT
	d.	Complete the Easy Install
	e.	Make sure that you add the user you create to the sudoers/wheel group/root whatever

4.	Download the scripts below and launch it from the VM's CLI
	https://drive.google.com/file/d/17Qvs8nnanddqTzNTe7JNWkta1Cqgukk6/view?usp=sharing
	https://drive.google.com/file/d/1LK1NAhAdLcY5h4fyZS6qmINcCc8JM-cs/view?usp=sharing

5.  Execute the first setup file.

	chmod +x ./setup1.sh
	./setup1.sh
	
6.  After a reboot, execute the second setup file.

	chmod +x ./setup2.sh
	./setup2.sh
