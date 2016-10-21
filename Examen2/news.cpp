class News {
    private:
        int id;
        std::string pub;
    public:
        News(int i) {
            id = i;
            std::cout << "Saved publication with id: " << id << std::endl;
        }

        void publish(std::string pub) {
            std::cout << "Publish news with id: " << id << std::endl;
            this->pub = pub;
        }

};