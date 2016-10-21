class Azteca : public Cadena
{
    std::string name;
    std::vector<std::string> news;

    Proxy newsHolder[100];
    int idx;
public:
    Azteca(std::string n) {
        this->name = name;
        idx = 0;
    }

    void Publish(std::string publication) {
    	news.push_back(publication);
        newsHolder[idx++].publish(publication);
    }

    void ReadFeed() {
    	std::cout << "Feed of Azteca" << std::endl;
    	for(int i = 0; i < news.size(); i++) {
    		std::cout << news[i] << std::endl;
    	}
        std::cout << "END OF FEED" << std::endl << std::endl;
    }
};