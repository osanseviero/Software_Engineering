class Sistema
{
public:
    void interface() {
    	Hillary hillaryInterface;
	    Pena penaInterface;
	    Trump trumpInterface;
	                    
	    CNN cnnInterface("CNN");
	    Televisa televisaInterface("Televisa");
	    Azteca aztecaInterface("Azteca");
	    MVS mvsInterface("MVS");
	    Formula formulaInterface("Formula");

	    hillaryInterface.Attach(&cnnInterface);
		hillaryInterface.Attach(&televisaInterface);
		hillaryInterface.Attach(&aztecaInterface);
		hillaryInterface.Attach(&mvsInterface);
		hillaryInterface.Attach(&formulaInterface);

		trumpInterface.Attach(&cnnInterface);
		trumpInterface.Attach(&televisaInterface);
		trumpInterface.Attach(&aztecaInterface);
		trumpInterface.Attach(&mvsInterface);
		trumpInterface.Attach(&formulaInterface);

		penaInterface.Attach(&televisaInterface);
		penaInterface.Attach(&aztecaInterface);
		penaInterface.Attach(&mvsInterface);
		penaInterface.Attach(&formulaInterface);


    	std::string news;

    	for (int i; true;){
		    std::cout << "Exit[0], Enter User[1-P, 2-H, 3-T], Publish All Feeds[4]:";
		    std::cin >> i;
		    if (i == 0)
		    	break;
		  	else if(i == 1) {
		    	std::cout << "Hi Pena. Write a publication: ";
		    	std::cin.ignore();
		    	std::getline (std::cin, news);
		    	penaInterface.News(news);
		  	}
		  	else if(i == 2) {
		    	std::cout << "Hi Hillary. Write a publication: ";
		    	std::cin.ignore();
		    	std::getline (std::cin, news);
		    	hillaryInterface.News(news);
		  	}
		  	else if(i == 3) {
		    	std::cout << "Trump...Please don't write a publication: ";
		    	std::cin.ignore();
		    	std::getline (std::cin, news);
		    	trumpInterface.News(news);
		  	}
		  	else if(i == 4) {
		    	cnnInterface.ReadFeed();
			    televisaInterface.ReadFeed();
			    mvsInterface.ReadFeed();
			    aztecaInterface.ReadFeed();
			    formulaInterface.ReadFeed();
		  	}
		 }
	}
};