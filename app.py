import streamlit as st

# Initialize the session state for seat availability
if "seats" not in st.session_state:
    ROWS = 5
    COLUMNS = 8
    st.session_state.seats = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]  # 0 means seat available, 1 means booked

# Title of the app
st.title("Cinema Seat Booking System")

# Display the seating layout
def display_seats():
    for i in range(5):
        cols = st.columns(8)
        for j in range(8):
            if st.session_state.seats[i][j] == 0:
                cols[j].button(f"Seat {i+1}-{j+1}", key=f"{i}-{j}", on_click=book_seat, args=(i, j))
            else:
                cols[j].button(f"Booked", key=f"booked-{i}-{j}", disabled=True)

# Function to book a seat
def book_seat(row, col):
    st.session_state.seats[row][col] = 1
    st.success(f"Seat {row+1}-{col+1} booked successfully!")

# Display the seats
display_seats()

# Reset Button
if st.button("Reset Seats"):
    ROWS = 5
    COLUMNS = 8
    st.session_state.seats = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
    st.experimental_set_query_params()  # Optionally refresh the query parameters to update the UI
    st.experimental_rerun()  # This line might work for older Streamlit versions; if it doesn't, you can skip it
