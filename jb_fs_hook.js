const fs = require('fs');

const originalRead = fs.readFileSync.bind(fs);

fs.readFileSync = function(file, ...args) {
  try {
    const st = fs.statSync(file);
    if (st && typeof st.isDirectory === 'function' && st.isDirectory()) {
      console.error('JBOOK-FS-HOOK: readFileSync called on directory:', file);
    }
  } catch (e) {
    // ignore stat errors
  }
  return originalRead(file, ...args);
};

console.error('JBOOK-FS-HOOK: hook installed');
