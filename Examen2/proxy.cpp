class Proxy
{
    private:
        int id;
        News* news;
        static int next;
        
    public:
        Proxy() {
            id = next++;
            news = NULL;
        }

        void publish(std::string pub) {
            if(!news) {
                news = new News(id);
            }
            news->publish(pub);
        }
};

int Proxy::next = 1;