import React, { useState } from "react";

const VirtualizedList = () => {
  const totalItems = 10000;
  const itemHeight = 40;
  const containerHeight = 400;

  const [scrollTop, setScrollTop] = useState(0);

  // Calculate visible range
  const startIndex = Math.floor(scrollTop / itemHeight);
  const visibleCount = Math.ceil(containerHeight / itemHeight);
  const endIndex = startIndex + visibleCount;

  // Generate data
  const data = Array.from({ length: totalItems }, (_, i) => `Item ${i}`);

  // Slice visible items
  const visibleItems = data.slice(startIndex, endIndex);

  const handleScroll = (e) => {
    setScrollTop(e.target.scrollTop);
  };

  return (
    <div
      onScroll={handleScroll}
      style={{
        height: containerHeight,
        overflowY: "auto",
        border: "1px solid black",
        position: "relative",
      }}
    >
      {/* Full height spacer */}
      <div
        style={{
          height: totalItems * itemHeight,
          position: "relative",
        }}
      >
        {visibleItems.map((item, index) => {
          const actualIndex = startIndex + index;

          return (
            <div
              key={actualIndex}
              style={{
                position: "absolute",
                top: actualIndex * itemHeight,
                height: itemHeight,
                width: "100%",
                borderBottom: "1px solid #ccc",
                padding: "8px",
                boxSizing: "border-box",
              }}
            >
              {item}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default VirtualizedList;