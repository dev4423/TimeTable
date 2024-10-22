import streamlit as st
import time

# Initialize the session state for seat availability and prices
if "seats" not in st.session_state:
    ROWS = 5
    COLUMNS = 8
    st.session_state.seats = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]  # 0 means seat available, 1 means booked

# Set pricing for different rows
seat_prices = {
    1: 10,  # Row 1 price = $10
    2: 15,  # Row 2 price = $15
    3: 20,  # Row 3 price = $20
    4: 25,  # Row 4 price = $25
    5: 30   # Row 5 price = $30
}

# Title of the app
st.title("Cinema Seat Booking System")

# Function to display an LED-like screen
def show_led_screen(seat_number, price):
    st.markdown("<h1 style='text-align: center; color: green;'>BOOKED</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: orange;'>Seat {seat_number} Successfully Booked!</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: red;'>Price: ${price}</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: red;'>Enjoy the Show!</h3>", unsafe_allow_html=True)
    time.sleep(2)  # Pause for 2 seconds before returning to seat layout

# Display the seating layout
def display_seats():
    for i in range(5):
        cols = st.columns(8)
        for j in range(8):
            seat_price = seat_prices[i + 1]  # Price based on the row
            if st.session_state.seats[i][j] == 0:
                cols[j].button(f"Seat {i+1}-{j+1} (${seat_price})", key=f"{i}-{j}", on_click=book_seat, args=(i, j, seat_price))
            else:
                cols[j].button(f"Booked", key=f"booked-{i}-{j}", disabled=True)

# Function to book a seat
def book_seat(row, col, price):
    st.session_state.seats[row][col] = 1
    seat_number = f"{row+1}-{col+1}"
    st.success(f"Seat {seat_number} booked successfully!")
    # Show the LED-like screen
    st.session_state.led_screen = True
    st.session_state.last_booked_seat = seat_number
    st.session_state.last_booked_price = price

# Check if LED screen needs to be displayed
if "led_screen" in st.session_state and st.session_state.led_screen:
    show_led_screen(st.session_state.last_booked_seat, st.session_state.last_booked_price)
    st.session_state.led_screen = False  # Turn off the LED screen after showing it
else:
    # Display the seats
    display_seats()

# Reset Button
if st.button("Reset Seats"):
    ROWS = 5
    COLUMNS = 8
    st.session_state.seats = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
    st.experimental_set_query_params()  # Optional to refresh the UI, but not mandatory
