// GitHub and Kaltura URLs allow CORS but serve PDFs as unembeddable downloads.
// Give the browser's native PDF viewer a correctly typed, same-origin blob.
const pdfBlobs = new Map();
const loadPdfDownloads = () => {
  for (const [frame, url] of pdfBlobs) {
    if (!frame.isConnected) {
      URL.revokeObjectURL(url);
      pdfBlobs.delete(frame);
    }
  }
  document.querySelectorAll("iframe[data-pdf-src]").forEach(async (frame) => {
    const source = frame.dataset.pdfSrc;
    frame.removeAttribute("data-pdf-src");
    frame.setAttribute("aria-busy", "true");
    try {
      const response = await fetch(source);
      if (!response.ok) throw new Error(`PDF download: ${response.status}`);
      const data = await response.arrayBuffer();
      if (!frame.isConnected) return;
      const url = URL.createObjectURL(new Blob([data], { type: "application/pdf" }));
      pdfBlobs.set(frame, url);
      frame.src = url;
    } catch {
      if (!frame.isConnected) return;
      const link = document.createElement("a");
      link.href = source;
      link.textContent = "PDF preview unavailable — open the slides directly";
      frame.replaceWith(link);
    } finally {
      frame.removeAttribute("aria-busy");
    }
  });
};
// Run after each instant-navigation page swap as well as on the first load.
if (typeof document$ !== "undefined") document$.subscribe(loadPdfDownloads);
else document.addEventListener("DOMContentLoaded", loadPdfDownloads);
