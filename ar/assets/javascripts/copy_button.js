const codeblocks = document.querySelectorAll("div.highlight pre code");

codeblocks.forEach((pre) => {
    const template = document.createElement("template");
    template.innerHTML = `
    <div class="copy-button">
        <svg class="copy-icon" viewBox="0 0 448 512">
            <path d="M208 0H332.1c12.7 0 24.9 5.1 33.9 14.1l67.9 67.9c9 9 14.1 21.2 14.1 33.9V336c0 26.5-21.5 48-48 48H208c-26.5 0-48-21.5-48-48V48c0-26.5 21.5-48 48-48zM48 128h80v64H64V448H256V416h64v48c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V176c0-26.5 21.5-48 48-48z" />
        </svg>
    </div>
    `.replace(/^\s+/gm, '');
    const copyButton = template.content.firstElementChild;
    copyButton.addEventListener("click", handleCopyClick);
    pre.prepend(copyButton);
    });

// Excludes the button div, and the Pygments-tagged spans that are the console/doscon
// shell prompt and the code output of a given command.
const exclude = ["div.copy-button", "div.copy-button-copied", "span.gp", "span.go"]

function filterText(target, exclusions) {
    // Clone as to not modify the live DOM.
    const clone = target.cloneNode(true);
    clone.querySelectorAll(exclusions).forEach(node => node.remove());
    // The space between the venv name and the prompt is not tagged, so it is included
    // in the copied content. The newlines present in code output in codeblocks also
    // isn't tagged, and therefore is also included in the copied content. Managing
    // both of these issues is the purpose of the following.
    return clone.innerText.replace(/^ /gm, "").trim();
}

function handleCopyClick(event) {
    // Target is walked back to the code tag.
    const code_node = event.target.parentElement.parentElement.parentElement
    navigator.clipboard.writeText(filterText(code_node, exclude));
    this.classList.add("copy-button-copied")
    this.classList.remove("copy-button")
    this.firstChild.textContent = "Copied!"
    setTimeout(() => {
        this.classList.remove("copy-button-copied")
        this.classList.add("copy-button")
        this.firstChild.textContent = ""
    }, 2000);
}
