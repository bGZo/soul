const addCopyButtonToCodeBlock = (block) => {
  if (block.querySelector(".copy-code-button")) return;
  const copyButton = document.createElement("button");
  copyButton.className = "copy-code-button";
  copyButton.textContent = "Copy";
  copyButton.style.cssText = `
    position: absolute;
    bottom: 5px;
    right: 5px;
    z-index: 10;
    padding: 2px 5px;
    cursor: pointer;
    font-size: 70%;
  `;
  copyButton.addEventListener("click", () => {
    copyCodeContent(block);
  });
  block.style.position = "relative";
  block.appendChild(copyButton);
};
const copyCodeContent = (block) => {
  const codeMirror = block.querySelector(".CodeMirror");
  let content = "";
  if (codeMirror && codeMirror.CodeMirror) {
    content = codeMirror.CodeMirror.getValue();
  } else {
    const codeElement =
      block.querySelector("textarea") || block.querySelector("pre");
    if (codeElement) {
      content = codeElement.value || codeElement.textContent;
    } else {
      console.error("No code content found");
      return;
    }
  }
  navigator.clipboard
    .writeText(content)
    .then(() => {
      logseq.api.show_msg("Copied to clipboard");
    })
    .catch((err) => {
      console.error("Could not copy text: ", err);
      logseq.api.show_msg("Could not copy to clipboard");
    });
};
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === "childList") {
      mutation.addedNodes.forEach(function (node) {
        if (node.nodeType === Node.ELEMENT_NODE) {
          if (node.classList.contains("cp__fenced-code-block")) {
            addCopyButtonToCodeBlock(node);
          } else {
            const codeBlocks = node.querySelectorAll(".cp__fenced-code-block");
            codeBlocks.forEach(addCopyButtonToCodeBlock);
          }
        }
      });
    }
  });
});
observer.observe(document.body, { childList: true, subtree: true });
document
  .querySelectorAll(".cp__fenced-code-block")
  .forEach(addCopyButtonToCodeBlock);