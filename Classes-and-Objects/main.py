class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name:str= name
        self.age:int= age
        self.tracks:list= tracks
        self.score:float= score
    

    def change_name(self,new_name:str):
        self.name=new_name
        return self.name
    
    def change_age(self,new_age:int):
        self.age=new_age
        return self.age
    
    def add_track(self, new_track:str):
        newTracks= self.tracks.append(new_track)
        # print(newTracks)
        return newTracks
    
    def get_score(self):
        print(self.score)
        return self.score

    def printinfo(self):
        print( "STUDENT DETAILS","\n Name: ",self.name, "\n Age: ", self.age ,"\n Tracks: ",self.tracks, "\n Score: ", str(self.score) )


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
Bob.printinfo()
