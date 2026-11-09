* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #0b1020;
  color: #edf2ff;
}
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 48px 20px 80px;
}
header {
  margin-bottom: 24px;
}
header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}
.panel {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
.field {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 18px;
}
.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.small { width: 100%; }
input, button {
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.15);
  padding: 12px 14px;
  font-size: 1rem;
}
input {
  background: rgba(13, 19, 35, 0.9);
  color: #edf2ff;
}
.checkbox-row {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-direction: row;
}
button {
  width: 100%;
  background: linear-gradient(135deg, #7c3aed, #2563eb);
  border: none;
  color: white;
  font-weight: 600;
  cursor: pointer;
}
.hidden { display: none; }
pre {
  white-space: pre-wrap;
  word-break: break-word;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 16px;
}
