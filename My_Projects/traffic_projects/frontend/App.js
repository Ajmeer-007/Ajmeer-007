import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

export default function App() {
  const directions = ['North', 'East', 'West', 'South']; // order is just for display
  const [files, setFiles] = useState({
    North: null,
    South: null,
    East: null,
    West: null,
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const onPick = (dir) => document.getElementById(`tmx-file-${dir}`).click();

  const onChange = (e, dir) => {
    const file = e.target.files?.[0] || null;
    setFiles((prev) => ({ ...prev, [dir]: file }));
  };

  const onRemove = (dir) =>
    setFiles((prev) => ({ ...prev, [dir]: null }));

  const allSelected =
    files.North && files.South && files.East && files.West;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!allSelected) return;
    setLoading(true);
    setResult(null);

    // Append videos in fixed order N,S,E,W to match backend expectation
    const form = new FormData();
    form.append('videos', files.North);
    form.append('videos', files.South);
    form.append('videos', files.West);
    form.append('videos', files.East);

    try {
      const { data } = await axios.post('http://localhost:5000/upload', form, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResult(data);
    } catch (err) {
      console.error(err);
      setResult({ error: 'Failed to process traffic feeds. Please try again.' });
    } finally {
      setLoading(false);
    }
  };

  const Tile = ({ dir }) => (
    <div className="tmx-card">
      <div className="tmx-card-header">
        <span className="tmx-dir">{dir} Feed</span>
        {files[dir] ? (
          <button type="button" className="tmx-text-btn" onClick={() => onRemove(dir)}>
            Remove
          </button>
        ) : (
          <button type="button" className="tmx-text-btn" onClick={() => onPick(dir)}>
            Select
          </button>
        )}
      </div>

      <div className="tmx-card-body">
        {!files[dir] ? (
          <button type="button" className="tmx-choose-btn" onClick={() => onPick(dir)}>
            Choose {dir} camera file
          </button>
        ) : (
          <video
            className="tmx-video"
            src={URL.createObjectURL(files[dir])}
            controls
            muted
          />
        )}
        <input
          id={`tmx-file-${dir}`}
          type="file"
          accept="video/*"
          onChange={(e) => onChange(e, dir)}
          style={{ display: 'none' }}
        />
      </div>

      <div className="tmx-card-footer">
        <span className="tmx-filename">
          {files[dir]?.name || 'No file selected'}
        </span>
      </div>
    </div>
  );

  return (
    <div className="tmx-app">
      <h1>🚗 AI-Based Traffic Management</h1>
      <p className="tmx-sub">
        Select four traffic camera feeds from the intersection. The system will analyze them and
        recommend optimized green times.
      </p>

      <form onSubmit={handleSubmit} className="tmx-form">
        <div className="tmx-intersection">
          <Tile dir="North" />
          <Tile dir="East" />
          <Tile dir="West" />
          <Tile dir="South" />
        </div>

        <div className="tmx-actions">
          <button
            type="submit"
            className="tmx-run"
            disabled={!allSelected || loading}
          >
            {loading ? 'Analyzing…' : '▶️ Run Real-Time Analysis'}
          </button>
        </div>
      </form>

      <div className="tmx-result">
        {!loading && !result && (
          <p className="tmx-placeholder">
            Results will appear here. <span>🚦🚦🚦🚦</span>
          </p>
        )}

        {result && !result.error && (
          <>
            <h2>✅ Optimization Results</h2>
            <ul className="tmx-list">
              <li>🚦 North: <b>{result.north}</b> seconds</li>
              <li>🚦 South: <b>{result.south}</b> seconds</li>
              <li>🚦 West: <b>{result.west}</b> seconds</li>
              <li>🚦 East: <b>{result.east}</b> seconds</li>
            </ul>
          </>
        )}

        {result && result.error && (
          <div className="tmx-error">{result.error}</div>
        )}
      </div>
    </div>
  );
}

