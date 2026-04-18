import React, { useRef, useState } from "react";

// ---------------- Toolbar Button ----------------
const Button = ({ label, onClick }) => (
  <button
    onMouseDown={(e) => e.preventDefault()} // prevent focus loss
    onClick={onClick}
    style={{
      marginRight: "5px",
      padding: "5px 10px",
      cursor: "pointer",
    }}
  >
    {label}
  </button>
);

// ---------------- Main Editor ----------------
const RichTextEditor = () => {
  const editorRef = useRef(null);
  const [html, setHtml] = useState("");

  // Execute formatting command
  const exec = (command, value = null) => {
    document.execCommand(command, false, value);
  };

  // Save content
  const handleInput = () => {
    setHtml(editorRef.current.innerHTML);
  };

  // Insert Link
  const addLink = () => {
    const url = prompt("Enter URL:");
    if (url) exec("createLink", url);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Basic Rich Text Editor</h2>

      {/* Toolbar */}
      <div style={{ marginBottom: "10px" }}>
        <Button label="B" onClick={() => exec("bold")} />
        <Button label="I" onClick={() => exec("italic")} />
        <Button label="U" onClick={() => exec("underline")} />

        <Button label="H1" onClick={() => exec("formatBlock", "H1")} />
        <Button label="H2" onClick={() => exec("formatBlock", "H2")} />

        <Button label="UL" onClick={() => exec("insertUnorderedList")} />
        <Button label="OL" onClick={() => exec("insertOrderedList")} />

        <Button label="Link" onClick={addLink} />
        <Button label="Clear" onClick={() => exec("removeFormat")} />
      </div>

      {/* Editable Area */}
      <div
        ref={editorRef}
        contentEditable
        onInput={handleInput}
        suppressContentEditableWarning={true}
        style={{
          minHeight: "200px",
          border: "1px solid #ccc",
          padding: "10px",
          borderRadius: "6px",
        }}
      />

      {/* Output Preview */}
      <div style={{ marginTop: "20px" }}>
        <h3>HTML Output:</h3>
        <pre
          style={{
            background: "#f4f4f4",
            padding: "10px",
            borderRadius: "6px",
          }}
        >
          {html}
        </pre>
      </div>
    </div>
  );
};

export default RichTextEditor;