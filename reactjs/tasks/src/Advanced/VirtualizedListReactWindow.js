import { List } from "react-window";

const VirtualizedListReactWindow = () => {
  const totalItems = 10000;

const Row = ({ index, style }) => {
    return (
      <div
        style={{
          ...style,
          borderBottom: "1px solid #ccc",
          padding: "10px",
          boxSizing: "border-box",
        }}
      >
        Item {index}
      </div>
    );
  };

  return (
    <List
      height={400}
      rowCount={totalItems}   // ✅ changed
      rowHeight={40}          // ✅ changed
      width={"100%"}
      rowComponent={Row}      // ✅ changed
    />
  );
};

export default VirtualizedListReactWindow;