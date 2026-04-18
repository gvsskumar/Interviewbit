import React, { useState, useRef, useEffect } from "react";

// ---------------- Main Component ----------------
const MultiSelectDropdown = ({ options }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selected, setSelected] = useState([]);
  const [search, setSearch] = useState("");
  const dropdownRef = useRef(null);

  // ---------------- Toggle Dropdown ----------------
  const toggleDropdown = () => setIsOpen((prev) => !prev);

  // ---------------- Select / Deselect ----------------
  const handleSelect = (option) => {
    if (selected.includes(option)) {
      setSelected(selected.filter((item) => item !== option));
    } else {
      setSelected([...selected, option]);
    }
  };

  // ---------------- Remove Tag ----------------
  const removeTag = (option) => {
    setSelected(selected.filter((item) => item !== option));
  };

  // ---------------- Click Outside ----------------
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setIsOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // ---------------- Filter Options ----------------
  const filteredOptions = options.filter((opt) =>
    opt.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div style={{ width: "300px" }} ref={dropdownRef}>
      <div
        onClick={toggleDropdown}
        style={{
          border: "1px solid #ccc",
          padding: "8px",
          borderRadius: "6px",
          cursor: "pointer",
          minHeight: "40px",
        }}
      >
        {selected.length === 0 ? (
          <span>Select options...</span>
        ) : (
          selected.map((item) => (
            <span key={item} style={styles.tag}>
              {item}
              <span
                style={styles.remove}
                onClick={(e) => {
                  e.stopPropagation();
                  removeTag(item);
                }}
              >
                ✖
              </span>
            </span>
          ))
        )}
      </div>

      {isOpen && (
        <div style={styles.dropdown}>
          {/* Search */}
          <input
            type="text"
            placeholder="Search..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={styles.search}
          />

          {/* Options */}
          {filteredOptions.map((option) => (
            <div
              key={option}
              onClick={() => handleSelect(option)}
              style={{
                ...styles.option,
                background: selected.includes(option) ? "#e6f7ff" : "#fff",
              }}
            >
              <input
                type="checkbox"
                checked={selected.includes(option)}
                readOnly
              />
              {option}
            </div>
          ))}

          {filteredOptions.length === 0 && (
            <div style={{ padding: "10px" }}>No results</div>
          )}
        </div>
      )}
    </div>
  );
};

// ---------------- Styles ----------------
const styles = {
  dropdown: {
    border: "1px solid #ccc",
    marginTop: "5px",
    borderRadius: "6px",
    maxHeight: "200px",
    overflowY: "auto",
    background: "#fff",
  },
  option: {
    padding: "8px",
    cursor: "pointer",
    display: "flex",
    gap: "8px",
  },
  search: {
    width: "95%",
    margin: "5px",
    padding: "5px",
  },
  tag: {
    display: "inline-block",
    background: "#007bff",
    color: "#fff",
    padding: "3px 6px",
    borderRadius: "4px",
    margin: "2px",
  },
  remove: {
    marginLeft: "5px",
    cursor: "pointer",
  },
};

export default MultiSelectDropdown;