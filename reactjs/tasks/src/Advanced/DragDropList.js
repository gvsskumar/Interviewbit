// npm install @dnd-kit/dom
import { useState } from "react";

const DragList = () => {
  const [list, setList] = useState(["A", "B", "C", "D"]);
  const [dragIndex, setDragIndex] = useState(null);

   const handleDragStart = (index) => {
    setDragIndex(index);
  };

  const handleDrop = (index) => {
    const updated = [...list];
    const draggedItem = updated[dragIndex];

    // remove dragged item
    updated.splice(dragIndex, 1);

    // insert at new position
    updated.splice(index, 0, draggedItem);

    setList(updated);
  }; 

    return (
    <div>
      {list.map((item, index) => (
        <div
          key={index}
          draggable={true}
          onDragStart={() => handleDragStart(index)}
          onDragOver={(e) => e.preventDefault()}
          onDrop={() => handleDrop(index)}

          style={{
            padding: "10px",
            margin: "5px",
            border: "1px solid black",
          }}
        >
          {item}
        </div>
      ))}
    </div>
  );
}

export default DragList;