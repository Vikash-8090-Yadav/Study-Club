// nav.jsx
import React from 'react';

import './nav.css';

const Nv = () => {
  return (
<nav className="nav">
  <div className="container nav-wrapper">
    <div className="brand">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
        <path
          d="M10.5 10a2.5 2.5 0 1 1-5.001-.001A2.5 2.5 0 0 1 10.5 10zM16 4v12c0 1.1-.9 2-2 2H2c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h12c1.1 0 2 .9 2 2zm-3.5 6a4.5 4.5 0 1 0-9 0 4.5 4.5 0 0 0 9 0zm6.715-4.914L17 6.562v7l2.215 1.477a.505.505 0 0 0 .785-.42V5.506a.505.505 0 0 0-.785-.42z"
        />
      </svg>
      <span>
        <strong>STUDY CLUB</strong>
      </span>
    </div>

    <ul className="nav-list">
      <li className="active">
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Services</a>
      </li>
      <li>
        <a href="#">Q&A</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
      <li>
      <a href="http://localhost:8000/">
      
        <button className="btn">GO BACK</button>
        </a>
      </li>
    </ul>
  </div>
</nav>

  );
};

export default Nv;
