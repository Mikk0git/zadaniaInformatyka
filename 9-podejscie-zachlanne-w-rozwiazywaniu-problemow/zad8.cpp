#include <iostream>
#include <algorithm> 
#include <string>     
using namespace std;



const int N = 10; 

void Write(int K[], int P[], string ID[], int index)
{
    cout << "ID: " << ID[index] <<  " P: " << P[index] << " K: " << K[index] << "\n";
}


void Sort(int K[], int P[], string ID[])
{
   
    sort(P, P + N);

    
    cout << "---Posortowane seanse---\n" ;
    for (int i = 0; i < N; i++)
    {
        Write(K, P, ID, i);
    }
}


void Choose(int K[], int P[], string ID[])
{
    cout <<"---Wybrane seanse---\n";
    for (int i = 0; i < N; i++)
    {
        if (K[i] > 15)
        {
            Write(K, P, ID, i);
        }
    }
}

int main()
{
    int P[N] = {9, 16, 15, 18, 14, 10, 10, 13, 15, 18};
    int K[N] = {10, 17, 17, 21, 15, 14, 11, 14, 17, 20};
    string ID[N] = {"F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"};

    cout << "---Harmonogram--- \n";
    
    for (int i = 0; i < N; i++)
    {
        Write(K, P, ID, i);
        
    }

    Sort(K, P, ID);
    Choose(K, P, ID);


    return 0;
}
