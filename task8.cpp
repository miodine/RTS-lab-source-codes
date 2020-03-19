#include "task8.hpp"

std::pair<int,int> busy_period(std::vector<std::vector<bool>> &timeline, unsigned int DISPATCH)
{
    for(unsigned int i = DISPATCH; i < timeline.size();i++)
    {
        bool task_executing = false;
        for(unsigned int j = 0; j<timeline[i].size();j++)
        {
            if(timeline[i][j])
            {
                task_executing = true;
                break;
            }
        }
        if(!task_executing)
        { 
            std::cout << "Busy period from: " << DISPATCH << " to: " << i << std::endl; 
            return {DISPATCH,i};
        }
        if(i++ == timeline.size())
        {
        return {-1,-1};
        std::cout << "Busy period does not end in the specified range" << std::endl;
        }
    }      
}