import React, { useState } from "react";
import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";
import {
  SortableContext,
  verticalListSortingStrategy,
  arrayMove,
} from "@dnd-kit/sortable";
import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";

// ---------------- Sortable Card ----------------
const Card = ({ id, content }) => {
  const { attributes, listeners, setNodeRef, transform, transition } =
    useSortable({ id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    padding: "10px",
    marginBottom: "8px",
    background: "#fff",
    borderRadius: "6px",
    border: "1px solid #ddd",
    cursor: "grab",
  };

  return (
    <div ref={setNodeRef} style={style} {...attributes} {...listeners}>
      {content}
    </div>
  );
};

// ---------------- Column ----------------
const Column = ({ title, items, addTask }) => {
  const [input, setInput] = useState("");

  return (
    <div style={styles.column}>
      <h3>{title}</h3>

      <SortableContext items={items} strategy={verticalListSortingStrategy}>
        {items.map((item) => (
          <Card key={item.id} id={item.id} content={item.content} />
        ))}
      </SortableContext>

      {/* Add Task */}
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Add task..."
        style={styles.input}
      />
      <button
        onClick={() => {
          if (!input.trim()) return;
          addTask(input);
          setInput("");
        }}
      >
        Add
      </button>
    </div>
  );
};

// ---------------- Main Board ----------------
const KanbanBoard = () => {
  const [columns, setColumns] = useState({
    todo: [
      { id: "1", content: "Task 1" },
      { id: "2", content: "Task 2" },
    ],
    inProgress: [{ id: "3", content: "Task 3" }],
    done: [{ id: "4", content: "Task 4" }],
  });

  // ---------------- Add Task ----------------
  const addTask = (columnKey, content) => {
    setColumns((prev) => ({
      ...prev,
      [columnKey]: [
        ...prev[columnKey],
        { id: Date.now().toString(), content },
      ],
    }));
  };

  // ---------------- Drag End ----------------
  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (!over) return;

    let sourceCol, targetCol;
    let sourceIndex, targetIndex;

    Object.keys(columns).forEach((col) => {
      columns[col].forEach((item, index) => {
        if (item.id === active.id) {
          sourceCol = col;
          sourceIndex = index;
        }
        if (item.id === over.id) {
          targetCol = col;
          targetIndex = index;
        }
      });
    });

    if (!sourceCol || !targetCol) return;

    // Same column reorder
    if (sourceCol === targetCol) {
      const updated = arrayMove(
        columns[sourceCol],
        sourceIndex,
        targetIndex
      );

      setColumns({
        ...columns,
        [sourceCol]: updated,
      });
    } else {
      // Move between columns
      const sourceItems = [...columns[sourceCol]];
      const targetItems = [...columns[targetCol]];

      const [movedItem] = sourceItems.splice(sourceIndex, 1);
      targetItems.splice(targetIndex, 0, movedItem);

      setColumns({
        ...columns,
        [sourceCol]: sourceItems,
        [targetCol]: targetItems,
      });
    }
  };

  return (
    <div>
      <h2>Kanban Board</h2>

      <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
        <div style={styles.board}>
          <Column
            title="To Do"
            items={columns.todo}
            addTask={(content) => addTask("todo", content)}
          />
          <Column
            title="In Progress"
            items={columns.inProgress}
            addTask={(content) => addTask("inProgress", content)}
          />
          <Column
            title="Done"
            items={columns.done}
            addTask={(content) => addTask("done", content)}
          />
        </div>
      </DndContext>
    </div>
  );
};

// ---------------- Styles ----------------
const styles = {
  board: {
    display: "flex",
    gap: "20px",
    padding: "20px",
  },
  column: {
    width: "250px",
    background: "#f4f5f7",
    padding: "10px",
    borderRadius: "8px",
  },
  input: {
    width: "100%",
    marginTop: "10px",
    padding: "5px",
  },
};

export default KanbanBoard;