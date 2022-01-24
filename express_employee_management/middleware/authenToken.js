const dotenv = require("dotenv");
const config = process.env;
const jwt = require("jsonwebtoken");

function authenticateToken(req, res, next) {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1];

  if (token == null) return res.sendStatus(401);
  try {
    const decode = jwt.verify(token, config.SECRET_KEY);
    req.user = decode;
  } catch (err) {
    return res.status(401).send("invalid token");
  }
  return next();
}

module.exports = authenticateToken;
