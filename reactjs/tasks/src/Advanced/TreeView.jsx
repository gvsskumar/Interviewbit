import React, { useState } from "react";

// ---------------- Tree Node ----------------
const TreeNode = ({ node }) => {
  const [expanded, setExpanded] = useState(false);

  const hasChildren = node.children && node.children.length > 0;

  return (
    <div style={{ marginLeft: "20px" }}>
      <div
        style={{ cursor: hasChildren ? "pointer" : "default" }}
        onClick={() => hasChildren && setExpanded(!expanded)}
      >
        {hasChildren && (expanded ? "📂" : "📁")} {node.label}
      </div>

      {expanded &&
        hasChildren &&
        node.children.map((child) => (
          <TreeNode key={child.id} node={child} />
        ))}
    </div>
  );
};

// ---------------- Tree View ----------------
const TreeView = ({ data }) => {
  return (
    <div>
      <h2>Tree View</h2>
      {data.map((node) => (
        <TreeNode key={node.id} node={node} />
      ))}
    </div>
  );
};

export default TreeView;