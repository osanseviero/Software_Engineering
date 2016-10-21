class MVS : public Cadena
{
    std::string name;
    std::vector<std::string> news;
public:
    MVS(std::string n) {
         this->name = name;
    }

    void Publish(std::string publication) {
    	news.push_back(publication);
    }

    void ReadFeed() {
    	std::cout << "Feed of MVS" << std::endl;
    	for(int i = 0; i < news.size(); i++) {
    		std::cout << news[i] << std::endl;
    	}
        std::cout << "END OF FEED" << std::endl << std::endl;
    }
};