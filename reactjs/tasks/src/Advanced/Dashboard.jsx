import React, { useState, useEffect } from "react";
import GridLayout from "react-grid-layout";
import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";

// ------------------- Widgets -------------------

const ChartWidget = ({ config }) => (
  <div style={styles.widget}>
    📊 Chart Widget
    <div>{config.title}</div>
  </div>
);

const TableWidget = ({ config }) => (
  <div style={styles.widget}>
    📋 Table Widget
    <div>{config.title}</div>
  </div>
);

const StatsWidget = ({ config }) => (
  <div style={styles.widget}>
    📈 Stats Widget
    <div>{config.title}</div>
  </div>
);

// ------------------- Widget Factory -------------------

const widgetMap = {
  chart: ChartWidget,
  table: TableWidget,
  stats: StatsWidget,
};

// ------------------- Main Dashboard -------------------

const Dashboard = () => {
  const [widgets, setWidgets] = useState([]);

  // Load from localStorage
  useEffect(() => {
    const saved = localStorage.getItem("dashboard");
    if (saved) setWidgets(JSON.parse(saved));
  }, []);

  // Save to localStorage
  useEffect(() => {
    localStorage.setItem("dashboard", JSON.stringify(widgets));
  }, [widgets]);

  // Add widget
  const addWidget = (type) => {
    const newWidget = {
      id: Date.now().toString(),
      type,
      layout: {
        i: Date.now().toString(),
        x: (widgets.length * 2) % 12,
        y: Infinity,
        w: 3,
        h: 3,
      },
      config: {
        title: `${type.toUpperCase()} Widget`,
      },
    };

    setWidgets([...widgets, newWidget]);
  };

  // Remove widget
  const removeWidget = (id) => {
    setWidgets(widgets.filter((w) => w.id !== id));
  };

  // Handle layout change
  const onLayoutChange = (layout) => {
    const updated = widgets.map((w) => {
      const l = layout.find((item) => item.i === w.id);
      return { ...w, layout: l };
    });
    setWidgets(updated);
  };

  return (
    <div>
      <h2>Dynamic Dashboard</h2>

      {/* Add Buttons */}
      <div style={{ marginBottom: "10px" }}>
        <button onClick={() => addWidget("chart")}>Add Chart</button>
        <button onClick={() => addWidget("table")}>Add Table</button>
        <button onClick={() => addWidget("stats")}>Add Stats</button>
      </div>

      {/* Grid Layout */}
      <GridLayout
        className="layout"
        layout={widgets.map((w) => ({ ...w.layout, i: w.id }))}
        cols={12}
        rowHeight={100}
        width={1200}
        onLayoutChange={onLayoutChange}
      >
        {widgets.map((widget) => {
          const Component = widgetMap[widget.type];

          return (
            <div key={widget.id} style={styles.card}>
              <button
                style={styles.closeBtn}
                onClick={() => removeWidget(widget.id)}
              >
                ✖
              </button>
              <Component config={widget.config} />
            </div>
          );
        })}
      </GridLayout>
    </div>
  );
};

// ------------------- Styles -------------------

const styles = {
  card: {
    background: "#fff",
    border: "1px solid #ddd",
    borderRadius: "8px",
    padding: "10px",
    position: "relative",
    overflow: "hidden",
  },
  widget: {
    textAlign: "center",
    marginTop: "20px",
  },
  closeBtn: {
    position: "absolute",
    top: "5px",
    right: "5px",
    border: "none",
    background: "red",
    color: "#fff",
    cursor: "pointer",
    padding: "2px 6px",
    borderRadius: "4px",
  },
};

export default Dashboard;