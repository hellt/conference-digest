// Conference and employer trackers: the name-filter box above the table.
// Typing keeps only rows whose first-column name contains the text
// (case-insensitive). With instant navigation the page is swapped without a
// reload, so wire on every visit, exactly like video.js does.
const wireConfFilter = () => {
  const input = document.querySelector(".conf-filter input[type='search']");
  if (!input || input.dataset.wired) return;
  const scope = input.closest(".md-content") || document;
  const table = scope.querySelector("table");
  if (!table) return;
  input.dataset.wired = "1";
  const rows = table.tBodies.length ? Array.from(table.tBodies[0].rows) : [];
  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    for (const row of rows) {
      const name = row.cells[0] ? row.cells[0].textContent : "";
      row.style.display = name.toLowerCase().includes(q) ? "" : "none";
    }
  });
};
if (typeof document$ !== "undefined") document$.subscribe(wireConfFilter);
else document.addEventListener("DOMContentLoaded", wireConfFilter);
