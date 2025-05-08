function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// Usage:
const userInput = '<img src=x onerror=alert(1)//>';
document.getElementById('output').innerHTML = escapeHtml(userInput);