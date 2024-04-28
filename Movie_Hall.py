class Star_Cinema:
    hall_list = []
    def entry_hall(self,hall):
        self.hall_list.append(hall)
        
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self._show_list=[]
        self._seats={}
        self.rows=rows
        self.cols=cols
        self.__hall_no=hall_no
        self.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        show_er_info=(id,movie_name,time)
        self._show_list.append(show_er_info)
        
        matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self._seats[id] = matrix
        
    def book_seats(self,show_id,seatList):
        if show_id in self._seats:
            r,c=seatList
            if 0 <= r <=self.rows and 0<= c <= self.cols:
                if self._seats[show_id][r][c] == 0:
                    self._seats[show_id][r][c] = 1
                    print("Congratulations! Your seat booked.")
                else:
                    print("Seat is already booked!")
            else:
                print("Invalid Show ID.")
        else:
            print("Your ID not found!")
                
    def view_show_list(self):
        for info in self._show_list:
            print(f"MovieName: {info[1]}, ID: {info[0]}, Time: {info[2]}")
            
    def view_available_seats(self,show_id):
            if show_id in self._seats:
                for row in range(self.rows):
                    for col in range(self.cols):
                        if self._seats[show_id][row][col] == 0:
                            print(f"Seat: ({row+1},{col+1})")
            else:
                print("Invalid Show ID.")
    
star_cinema = Star_Cinema()

movie = Hall(2,101,15)
movie = Hall(3,115,21)

star_cinema.entry_hall(movie)
star_cinema.entry_hall(movie)

movie.entry_show(11,"Mission Impossible","9:30 AM")
movie.entry_show(21,"Ra-One","9:00 PM")
movie.entry_show(31,"Dabang","11:30 PM")
movie.entry_show(41,"Bahubali","10:30 AM")

print("1. VIEW ALL SHOW TODAY")
print("2. VIEW AVAILABLE SEATS")
print("3. BOOK TICKET")
print("4. Exit")            
while True:
    # option = int(input())
    option=int(input("\nEnter Option: "))
    if option == 1:
        movie.view_show_list()
        
    elif option == 2:
        print(f"Please Insert Movie's Id For Available Seat: ")
        movie_ID = int(input())
        movie.view_available_seats(movie_ID)
    elif option == 3:
        movie_id=int(input())
        row=int(input())
        column=int(input())
        movie.book_seats(movie_id,(row,column))
    elif option == 4:
        print(f"Thank You.")
        break