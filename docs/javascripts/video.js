// Click-to-play recordings: a pick shows a YouTube thumbnail, and only a click
// loads the player (youtube-nocookie), so a page of 25 picks stays light.
// Modifier clicks and no-JS visitors follow the link to YouTube instead.
document.addEventListener("click", (event) => {
  const thumb = event.target.closest(".pick-video__thumb[data-yt]");
  if (!thumb || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const id = thumb.dataset.yt;
  if (!/^[A-Za-z0-9_-]{11}$/.test(id)) return;
  event.preventDefault();
  const frame = document.createElement("iframe");
  const start = Number.parseInt(thumb.dataset.start || "0", 10);
  frame.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0${start > 0 ? `&start=${start}` : ""}`;
  frame.title = thumb.querySelector("img")?.alt || "Recording";
  frame.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
  frame.allowFullscreen = true;
  frame.className = "pick-video__frame";
  thumb.replaceWith(frame);
});

// Full-width thumbnails: hqdefault (480 px, always present) is the default;
// near the viewport, swap in maxresdefault (1280 px) if the video has one
// (YouTube answers a missing one with a 120 px placeholder).
const sharpen = () => {
  const imgs = document.querySelectorAll(".pick-video__thumb img[data-hd]");
  const upgrade = (img) => {
    const hd = new Image();
    hd.onload = () => { if (hd.naturalWidth > 120) img.src = hd.src; };
    hd.src = img.dataset.hd;
    img.removeAttribute("data-hd");
  };
  if (!("IntersectionObserver" in window)) return imgs.forEach(upgrade);
  const seen = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { seen.unobserve(e.target); upgrade(e.target); }
  }, { rootMargin: "400px 0px" });
  imgs.forEach((img) => seen.observe(img));
};
// Instant navigation swaps pages without a reload: run on every page.
if (typeof document$ !== "undefined") document$.subscribe(sharpen);
else document.addEventListener("DOMContentLoaded", sharpen);
