import React, { useState } from "react";

// ---------------- Helper Functions ----------------

// Get days in month
const getDaysInMonth = (year, month) => {
  return new Date(year, month + 1, 0).getDate();
};

// Get first day index (0 = Sunday)
const getFirstDay = (year, month) => {
  return new Date(year, month, 1).getDay();
};

// Month names
const months = [
  "January","February","March","April","May","June",
  "July","August","September","October","November","December"
];

// ---------------- Calendar ----------------
const Calendar = () => {
  const today = new Date();

  const [currentDate, setCurrentDate] = useState(today);
  const [selectedDate, setSelectedDate] = useState(null);

  const year = currentDate.getFullYear();
  const month = currentDate.getMonth();

  const daysInMonth = getDaysInMonth(year, month);
  const firstDay = getFirstDay(year, month);

  // ---------------- Navigation ----------------
  const prevMonth = () => {
    setCurrentDate(new Date(year, month - 1, 1));
  };

  const nextMonth = () => {
    setCurrentDate(new Date(year, month + 1, 1));
  };

  // ---------------- Generate Calendar Grid ----------------
  const dates = [];

  // Empty cells before first day
  for (let i = 0; i < firstDay; i++) {
    dates.push(null);
  }

  // Actual days
  for (let d = 1; d <= daysInMonth; d++) {
    dates.push(new Date(year, month, d));
  }

  return (
    <div style={styles.container}>
      {/* Header */}
      <div style={styles.header}>
        <button onClick={prevMonth}>◀</button>
        <h3>{months[month]} {year}</h3>
        <button onClick={nextMonth}>▶</button>
      </div>

      {/* Week Days */}
      <div style={styles.grid}>
        {["Sun","Mon","Tue","Wed","Thu","Fri","Sat"].map((day) => (
          <div key={day} style={styles.dayHeader}>{day}</div>
        ))}

        {/* Dates */}
        {dates.map((date, index) => {
          const isToday =
            date &&
            date.toDateString() === today.toDateString();

          const isSelected =
            date &&
            selectedDate &&
            date.toDateString() === selectedDate.toDateString();

          return (
            <div
              key={index}
              onClick={() => date && setSelectedDate(date)}
              style={{
                ...styles.cell,
                background: isSelected
                  ? "#007bff"
                  : isToday
                  ? "#e6f7ff"
                  : "#fff",
                color: isSelected ? "#fff" : "#000",
                cursor: date ? "pointer" : "default",
              }}
            >
              {date ? date.getDate() : ""}
            </div>
          );
        })}
      </div>
    </div>
  );
};

// ---------------- Styles ----------------
const styles = {
  container: {
    width: "300px",
    border: "1px solid #ccc",
    borderRadius: "8px",
    padding: "10px",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(7, 1fr)",
    gap: "5px",
    marginTop: "10px",
  },
  dayHeader: {
    fontWeight: "bold",
    textAlign: "center",
  },
  cell: {
    height: "40px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: "4px",
  },
};

export default Calendar;