class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()
        Star_Cinema().entry_hall(self)

    def _initialize_seats(self):
        print("Initializing seats:")
        print("Enter the initial status of each seat (0 for free, 1 for booked):")

        seats = []
        for row_num in range(1, self._rows + 1):
            row = []
            for col_num in range(1, self._cols + 1):
                status = input(f"Seat ({row_num}, {col_num}): ")
                while status not in {'0', '1'}:
                    print("Invalid input! Please enter 0 for free or 1 for booked.")
                    status = input(f"Seat ({row_num}, {col_num}): ")
                row.append(int(status))
            seats.append(row)

        print('--------------------X-----------------\n')
        print("Matrix representation of seats:")
        print('--------------------X-----------------\n')
        for row in seats:
            print(row)

        self._seats = {show_id: [row[:] for row in seats] for show_id, _, _ in self._show_list}
        print("Seats initialized successfully.")


    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

    def view_show_list(self):
        if not self._show_list:
            print("No shows available.")
            return

        print("Shows running:")
        for show_id, movie_name, time in self._show_list:
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print(f"Show with ID {show_id} not found.")
            return 

        print(f"Available seats for show {show_id}:")
        for i, row in enumerate(self._seats[show_id], start=1):
            for j, seat_status in enumerate(row, start=1):
                if seat_status == 0:
                    print(f"Seat ({i}, {j})") 

        seats = []
        for row_num in range(1, self._rows + 1):
            row = []
            for col_num in range(1, self._cols + 1):
                status = input(f"Seat ({row_num}, {col_num}): ")
                while status not in {'0', '1'}:
                    print("Invalid input! Please enter 0 for free or 1 for booked.")
                    status = input(f"Seat ({row_num}, {col_num}): ")
                row.append(int(status))
            seats.append(row)

        print('--------------------X-----------------\n')
        print("Matrix representation of seats:")
        print('--------------------X-----------------\n')
        for row in seats:
            print(row)

        self._seats = {show_id: [row[:] for row in seats] for show_id, _, _ in self._show_list}

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            print(f"Show with ID {show_id} not found.")
            return 

        for seat in seat_list:
            row, col = seat
            if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                print(f"Invalid seat: ({row}, {col}). Seat is outside the hall bounds.")
                continue

            elif self._seats[show_id][row - 1][col - 1] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self._seats[show_id][row - 1][col - 1] = 1
                print(f"Seat ({row}, {col}) booked successfully for show {show_id}.")


def ticket_booking_system():
    while True:
        print("\nTicket Booking System Menu:")
        print("1. View all shows running")
        print("2. View available seats for a show")
        print("3. Book tickets for a show")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nViewing all shows running:")
            for hall in Star_Cinema.hall_list:
                hall.view_show_list()

        elif choice == "2":
            show_id = int(input("Enter the ID of the show to view available seats: "))
            print(f"\nViewing available seats for show {show_id}:")
            for hall in Star_Cinema.hall_list:
                hall.view_available_seats(show_id)

        elif choice == "3":
            show_id = int(input("Enter the ID of the show to book tickets: "))
            num_seats = int(input("Enter the number of seats to book: "))
            seat_list = []
            for _ in range(num_seats):
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                seat_list.append((row, col))
            print("\nBooking tickets...")
            for hall in Star_Cinema.hall_list:
                hall.book_seats(show_id, seat_list)

        elif choice == "4":
            print("Exiting the Counter Replica System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


hall_1 = Hall(rows=4, cols=4, hall_no=1)
hall_1.entry_show(id=1, movie_name="Avengers", time="10:00 AM")
hall_1.entry_show(id=2, movie_name="Batman", time="1:00 PM")

ticket_booking_system()
