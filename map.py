from datetime import datetime
import random
import CFS as cfs
import DFS as dfs
import DFS_FC as fc
import DFS_FC_SP as sp


class Map:
    def __init__(self,country_states, country_neighbors) -> None:
        self.country_states = country_states
        self.country_neighbors = country_neighbors

    def printStates(self):
        for state in self.country_states:
            print(state)

    def shuffleNeighors(self):
        random.shuffle(list(self.country_neighbors.items()))
        dict(self.country_neighbors)

    def printNeighbors(self):
        for key in self.country_neighbors:
            string = key + ": "
            for neighbor in self.country_neighbors[key]:
                string += neighbor + " "
            print(string)
            
numberOfBacktracks = 0


Australia = Map(
    ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria', 'Tasmania'],
    {
    'Western Australia' : ['Northern Territory', 'South Australia'],
    'Northern Territory' : ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia' : ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland' : ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales' : ['Queensland', 'Victoria', 'South Australia'],
    'Victoria' : ['New South Wales', 'South Australia'],
    'Tasmania' : []  
}
)

USA = Map(
    [
    'Alabama','Alaska','Arkansas','Arizona',
    'California','Colorado','Connecticut',
    'Delaware','Florida',
    'Georgia',
    'Hawaii',
    'Iowa','Idaho','Illinois','Indiana',
    'Kansas','Kentucky',
    'Louisiana',
    'Massachusetts','Maryland','Maine','Michigan','Minnesota','Missouri','Mississippi','Montana',
    'North Carolina','North Dakota','Nebraska','New Hampshire','New Jersey','New Mexico','Nevada','New York',
    'Ohio','Oklahoma','Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina','South Dakota',
    'Tennessee','Texas',
    'Utah',
    'Virginia','Vermont',
    'Washington','Wisconsin','West Virginia','Wyoming'
    ],
    {
    'Alabama' : ['Florida' , 'Georgia' , 'Mississippi' , 'Tennessee'],
    'Alaska' : [],
    'Arkansas' : ['Louisiana' , 'Missouri' , 'Mississippi' , 'Oklahoma' , 'Tennessee' , 'Texas'],
    'Arizona' : ['California' , 'Colorado' , 'New Mexico' , 'Nevada' , 'Utah'],
    'California' : ['Arizona' , 'Nevada' , 'Oregon'],
    'Colorado' : ['Arizona' , 'Kansas' , 'Nebraska' , 'New Mexico' , 'Oklahoma' , 'Utah' , 'Wyoming'],
    'Connecticut' : ['Massachusetts' , 'New York' , 'Rhode Island'],
    'Delaware' : ['Maryland' , 'New Jersey' , 'Pennsylvania' ],
    'Florida' : ['Alabama' , 'Georgia' ],
    'Georgia' : ['Alabama' , 'Florida' , 'North Carolina' , 'South Carolina' , 'Tennessee' ],
    'Hawaii' : [ ],
    'Idaho' : ['Montana' , 'Nevada' , 'Oregon' , 'Utah' , 'Washington' , 'Wyoming' ],
    'Illinois' : ['Iowa' , 'Indiana' , 'Michigan', 'Kentucky' , 'Missouri' , 'Wisconsin' ],
    'Indiana' : ['Illinois' , 'Kentucky' , 'Missouri' , 'Ohio' ],
    'Iowa' : ['Illinois' , 'Minnesota' , 'Missouri' , 'Nebraska' , 'South Dakota' , 'Wisconsin' ],
    'Kansas' : ['Colorado' , 'Missouri' , 'Nebraska' , 'Oklahoma' ],
    'Kentucky' : ['Illinois' , 'Indiana' , 'Missouri' , 'Ohio' , 'Tennessee' , 'Virginia' , 'West Virginia' ],
    'Louisiana' : ['Arkansas' , 'Mississippi' , 'Texas' ],
    'Massachusetts' : ['Connecticut' , 'New Hampshire' , 'New York' , 'Rhode Island' , 'Vermont' ],
    'Maryland' : [ 'Delaware' , 'Pennsylvania' , 'Virginia' , 'West Virginia' ],
    'Maine' : ['New Hampshire' ],
    'Michigan' : ['Indiana' , 'Ohio' , 'Wisconsin','Minnesota','Illinois' ],
    'Minnesota' : ['Iowa' , 'North Dakota' ,'Michigan', 'South Dakota' , 'Wisconsin' ],
    'Missouri' : ['Arkansas' , 'Iowa' , 'Illinois' , 'Kansas' , 'Kentucky' , 'Nebraska' , 'Oklahoma' , 'Tennessee' ],
    'Mississippi' : ['Alabama' , 'Arkansas' , 'Louisiana' , 'Tennessee' ],
    'Montana' : ['Idaho' , 'North Dakota' , 'South Dakota' , 'Wyoming' ],
    'North Carolina' : ['Georgia' , 'South Carolina' , 'Tennessee' , 'Virginia' ],
    'North Dakota' : ['Minnesota' , 'Montana' , 'South Dakota' ],
    'Nebraska' : ['Colorado' , 'Iowa' , 'Kansas' , 'Missouri' , 'South Dakota' , 'Wyoming' ],
    'New Hampshire' : ['Massachusetts' , 'Maine' , 'Vermont' ],
    'New Jersey' : ['Delaware' , 'New York' , 'Pennsylvania' ],
    'New Mexico' : ['Arizona' , 'Colorado' , 'Oklahoma' , 'Texas' , 'Utah' ],
    'Nevada' : ['Arizona' , 'California' , 'Idaho' , 'Oregon' , 'Utah' ],
    'New York' : ['Connecticut' , 'Massachusetts' , 'New Jersey' , 'Pennsylvania' , 'Vermont', 'Rhode Island' ],
    'Ohio' : ['Indiana' , 'Kentucky' , 'Michigan' , 'Pennsylvania' , 'West Virginia' ],
    'Oklahoma' : ['Arkansas' , 'Colorado' , 'Kansas' , 'Missouri' , 'New Mexico' , 'Texas' ],
    'Oregon' : ['California' , 'Idaho' , 'Nevada' , 'Washington' ],
    'Pennsylvania' : ['Delaware' , 'Maryland' , 'New Jersey' , 'New York' , 'Ohio' , 'West Virginia' ],
    'Rhode Island' : ['Connecticut' , 'Massachusetts', 'New York' ],
    'South Carolina' : ['Georgia' , 'North Carolina' ],
    'South Dakota' : ['Iowa' , 'Minnesota' , 'Montana' , 'North Dakota' , 'Nebraska' , 'Wyoming' ],
    'Tennessee' : ['Alabama' , 'Arkansas' , 'Georgia' , 'Kentucky' , 'Missouri' , 'Mississippi' , 'North Carolina' , 'Virginia' ],
    'Texas' : ['Arkansas' , 'Louisiana' , 'New Mexico' , 'Oklahoma' ],
    'Utah' : ['Arizona' , 'Colorado' , 'Idaho' , 'New Mexico' , 'Nevada' , 'Wyoming' ],
    'Virginia' : [ 'Kentucky' , 'Maryland' , 'North Carolina' , 'Tennessee' , 'West Virginia' ],
    'Vermont' : ['Massachusetts' , 'New Hampshire' , 'New York' ],
    'Washington' : [ 'Idaho' , 'Oregon' ],
    'Wisconsin' : ['Iowa' , 'Illinois' , 'Michigan' , 'Minnesota' ],
    'West Virginia' : ['Kentucky' , 'Maryland' , 'Ohio' , 'Pennsylvania' , 'Virginia' ],
    'Wyoming' : ['Colorado' , 'Idaho' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Utah' ]
})

def showTime():
    endTime = datetime.now()
    elapsedTime = (endTime - startTime).microseconds / 1000
    print("Elapsed Time: %sms" % (str(elapsedTime)))
#user selection input
country_choice =int(input("Enter '1' to use AUSTRALIA data , '2' to use USA data: "))
heuristic_choice = int(input("Enter '1' to use no heuristic , '2' to use a heuristic: "))
algorithm_choice = int(input("Enter '1' for Depth first search only, '2' for Depth first search + forward checking, '3' for Depth first search + forward checking + propagation through singleton domains: "))
startTime = datetime.now()
#user input choices based on country
if(country_choice == 1):    #Australia
    states = Australia.country_states
    neighbors = Australia.country_neighbors
    min_number = cfs.getChromaticNumber((states, neighbors))
    print("Minimum no of colors required for Australia map: ", min_number)
    if(heuristic_choice==1):    #choice of heuristic
        if(algorithm_choice == 1):  #DFS
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            numberOfBacktracks = 0
            result = dfs.DFS_Only((states, neighbors), colors, color_options)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
        elif(algorithm_choice == 2):    #DFS and FC
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = fc.Forwardcheck((states, neighbors), colors, color_options)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
        elif(algorithm_choice == 3):    #DFS and FC with propagation
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = sp.ForwardcheckSP((states, neighbors), colors, color_options)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
    else:   #use of heuristic
        if(algorithm_choice == 1):  #DFS
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = dfs.DFS_Only((states, neighbors), colors, color_options, True)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
        elif(algorithm_choice == 2):    #DFS and FC
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = fc.Forwardcheck((states, neighbors), colors, color_options, True)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
        else:   #DFS and FC with SP
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = sp.ForwardcheckSP((states, neighbors), colors, color_options, True)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
elif(country_choice == 2):  #USA
    states = USA.country_states
    neighbors = USA.country_neighbors
    min_number = cfs.getChromaticNumber((states, neighbors))
    print("Minimum no of colors required for USA map: ", min_number)
    if(heuristic_choice==1):
        if(algorithm_choice == 1):
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            numberOfBacktracks = 0
            result = dfs.DFS_Only((states, neighbors), colors, color_options)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
                
        elif(algorithm_choice == 2):
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = fc.Forwardcheck((states, neighbors), colors, color_options)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
        else:
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = sp.ForwardcheckSP((states, neighbors), colors, color_options)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
    else:
        if(algorithm_choice == 1):
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = dfs.DFS_Only((states, neighbors), colors, color_options, True)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
        elif(algorithm_choice == 2):
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = fc.Forwardcheck((states, neighbors), colors, color_options, True)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
        else:
            numberOfBacktracks = 0
            colors = cfs.color_dict(states)
            color_options = cfs.create_color_options(states, min_number)
            result = sp.ForwardcheckSP((states, neighbors), colors, color_options, True)
            numberOfBacktracks = result[1]
            if result[0] == 'Success':
                print(colors)
            else:
                print("Failure")

            print("No. of Backtracks: ", numberOfBacktracks)
            showTime()
                
else:
    print("Invalid choice.")
    exit()