import streamlit as st

# Initialize the seating layout
ROWS = 5
COLUMNS = 8
seats = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]  # 0 means seat available, 1 means booked

# Title of the app
st.title("Cinema Seat Booking System")

# Display the seating layout
def display_seats():
    for i in range(ROWS):
        cols = st.columns(COLUMNS)
        for j in range(COLUMNS):
            if seats[i][j] == 0:
                cols[j].button(f"Seat {i+1}-{j+1}", key=f"{i}-{j}", on_click=book_seat, args=(i, j))
            else:
                cols[j].button(f"Booked", key=f"booked-{i}-{j}", disabled=True)

# Function to book a seat
def book_seat(row, col):
    seats[row][col] = 1
    st.success(f"Seat {row+1}-{col+1} booked successfully!")

# Display the seats
display_seats()

# Reset Button
if st.button("Reset Seats"):
    for i in range(ROWS):
        for j in range(COLUMNS):
            seats[i][j] = 0
    st.experimental_rerun()
