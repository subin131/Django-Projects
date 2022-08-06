import React from "react";
import "./style.css";
function Formss() {
  return (
    <form>
      <label>Email</label>
      <input type="email" placeholder="Enter the email" name="email" />
      <label>Password</label>
      <input type="password" placeholder="Enter the password" name="password" />
    </form>
  );
}

export default Formss;
