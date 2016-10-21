class Usuario {
    std::vector<Cadena*> list;

public:
    void Attach(Cadena *product) {
        list.push_back(product);
    }

    void Detach(Cadena *product) {
         list.erase(std::remove(list.begin(), list.end(), product), list.end());    
    }
    void Notify(std::string news) {
        for(std::vector<Cadena*>::const_iterator iter = list.begin(); iter != list.end(); ++iter)
        {
            if(*iter != 0)
            {
                (*iter)->Publish(news);
            }
        }
    }
};