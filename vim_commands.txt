Certainly! Here's a list of some fundamental Vim commands categorized by mode:

**Normal Mode Commands:**

1. **Navigation:**
   - `h`: Move left.
   - `j`: Move down.
   - `k`: Move up.
   - `l`: Move right.
   - `w`: Move forward by word.
   - `b`: Move backward by word.
   - `0`: Move to the beginning of the line.
   - `$`: Move to the end of the line.
   - `gg`: Move to the beginning of the document.
   - `G`: Move to the end of the document.
   - `<line_number>G`: Move to a specific line number.

2. **Editing:**
   - `i`: Enter Insert Mode before the cursor.
   - `I`: Enter Insert Mode at the beginning of the line.
   - `a`: Enter Insert Mode after the cursor.
   - `A`: Enter Insert Mode at the end of the line.
   - `o`: Open a new line below the current line and enter Insert Mode.
   - `O`: Open a new line above the current line and enter Insert Mode.
   - `x`: Delete the character under the cursor.
   - `dd`: Delete the current line.
   - `yy`: Copy (yank) the current line.
   - `p`: Paste after the cursor.
   - `P`: Paste before the cursor.
   - `u`: Undo the last change.
   - `Ctrl-r`: Redo the last undone change.
   - `.`: Repeat the last change.

3. **Searching and Replacing:**
   - `/`: Search forward.
   - `?`: Search backward.
   - `:s/old/new/g`: Replace "old" with "new" in the current line.
   - `:%s/old/new/g`: Replace "old" with "new" in the entire document.
   - `:n`: Go to the next search result.
   - `:N`: Go to the previous search result.

4. **File Operations:**
   - `:w`: Save the file.
   - `:q`: Quit Vim.
   - `:q!`: Quit Vim without saving changes.
   - `:wq` or `:x`: Save and quit Vim.

**Insert Mode Commands:**

1. **Text Entry:**
   - Normal typing keys insert text as usual.
   - `Esc`: Return to Normal Mode.

**Visual Mode Commands:**

1. **Text Selection:**
   - `v`: Enter Visual Mode to select text character by character.
   - `V`: Enter Visual Line Mode to select entire lines.
   - `Ctrl-v`: Enter Visual Block Mode to select a block of text.
   - Once text is selected, you can copy with `y` and cut with `x`, and paste with `p`.

These are some of the basic commands to get you started with Vim. Vim has many more advanced features and commands, so as you become more comfortable, you can explore additional functionality and customize your Vim setup to suit your needs.
