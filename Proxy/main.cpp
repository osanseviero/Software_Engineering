#include <iostream>
using namespace std;

/*
    Example: If we have a document where there are high quality images, we want the document to load fast. 
    We associate access of the images to another object, so the document can load fast.
    The images will be loaded on demand. A proxy is ubicated instead of the image, but it works just as one.
    The proxy will load the image just when it is required.

*/

class Image {
    private:
        int id;
    public:
        Image(int i) {
            id = i;
            std::cout << "created img with id: " << id << std::endl;
        }

        void draw() {
            std::cout << "drawing image with id: " << id << std::endl;
        }

};

class Proxy
{
    private:
        Image *realImage;
        int id;
        static int next;
        
    public:
        Proxy() {
            id = next++;
            realImage = NULL;
        }

        void draw() {
            if(!realImage) {
                realImage = new Image(id);
                realImage->draw();
            }
        }
};

int Proxy::next = 1;

int main()
{
    Proxy images[5];
    for (int i; true;){
    cout << "Exit[0], Image[1-5]: ";
    cin >> i;
    if (i == 0)
      break;
    images[i - 1].draw();
  }
}




