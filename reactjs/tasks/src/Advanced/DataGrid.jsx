import React, { useState, useMemo } from "react";

// ---------------- Sample Data ----------------
const initialData = [
  { id: 1, name: "Alice", age: 25, role: "Developer" },
  { id: 2, name: "Bob", age: 30, role: "Designer" },
  { id: 3, name: "Charlie", age: 28, role: "Manager" },
  { id: 4, name: "David", age: 35, role: "Developer" },
];

// ---------------- Columns Config ----------------
const columns = [
  { key: "name", label: "Name" },
  { key: "age", label: "Age" },
  { key: "role", label: "Role" },
];

// ---------------- DataGrid ----------------
const DataGrid = () => {
  const [data] = useState(initialData);
  const [sortConfig, setSortConfig] = useState(null);
  const [filters, setFilters] = useState({});

  // ---------------- Sorting ----------------
  const handleSort = (key) => {
    let direction = "asc";
    if (sortConfig?.key === key && sortConfig.direction === "asc") {
      direction = "desc";
    }
    setSortConfig({ key, direction });
  };

  // ---------------- Filtering ----------------
  const handleFilterChange = (key, value) => {
    setFilters((prev) => ({
      ...prev,
      [key]: value.toLowerCase(),
    }));
  };

  // ---------------- Process Data ----------------
  const processedData = useMemo(() => {
    let filtered = [...data];

    // Apply filters
    filtered = filtered.filter((row) =>
      Object.keys(filters).every((key) =>
        row[key]
          ?.toString()
          .toLowerCase()
          .includes(filters[key] || "")
      )
    );

    // Apply sorting
    if (sortConfig) {
      filtered.sort((a, b) => {
        const aVal = a[sortConfig.key];
        const bVal = b[sortConfig.key];

        if (aVal < bVal) return sortConfig.direction === "asc" ? -1 : 1;
        if (aVal > bVal) return sortConfig.direction === "asc" ? 1 : -1;
        return 0;
      });
    }

    return filtered;
  }, [data, sortConfig, filters]);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Data Grid</h2>

      <table border="1" cellPadding="8" style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            {columns.map((col) => (
              <th
                key={col.key}
                onClick={() => handleSort(col.key)}
                style={{ cursor: "pointer" }}
              >
                {col.label}
                {sortConfig?.key === col.key &&
                  (sortConfig.direction === "asc" ? " 🔼" : " 🔽")}
              </th>
            ))}
          </tr>

          {/* Filter Row */}
          <tr>
            {columns.map((col) => (
              <th key={col.key}>
                <input
                  type="text"
                  placeholder="Filter..."
                  onChange={(e) =>
                    handleFilterChange(col.key, e.target.value)
                  }
                  style={{ width: "90%" }}
                />
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {processedData.map((row) => (
            <tr key={row.id}>
              {columns.map((col) => (
                <td key={col.key}>{row[col.key]}</td>
              ))}
            </tr>
          ))}

          {processedData.length === 0 && (
            <tr>
              <td colSpan={columns.length} align="center">
                No Data Found
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default DataGrid;