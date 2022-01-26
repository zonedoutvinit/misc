const express = require("express");
const router = express.Router();
const admin = require("../models/admin");
const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");
dotenv.config();

router.get("/", (req, res) => {
  res.render("users/login");
});

router.post("/auth", async (req, res) => {
  // res.set({
  //   "Access-Control-Allow-Headers":
  //     "X-Requested-With,content-type, Authorization, authorization",
  //   "Access-Control-Expose-Headers":
  //     "X-Requested-With,content-type, Authorization, authorization",
  // });
  admin
    .find({ uname: req.body.uname, passw: req.body.passw })
    //.find({ uname: req.body.uname } && { passw: req.body.passw })
    .exec()
    .then((user) => {
      if (user.length < 1) {
        res.json({ message: "no user found" });
      } else {
        const token = generateAccessToken(req.body.uname, user[0]._id);
        console.log(token);
        // res.header.token = token;
        res.append("authorization", token);
        //res.send(token);
        res.redirect(`/profile`);
      }
    });
});

function generateAccessToken(username, adminID) {
  return jwt.sign({ username, adminID }, process.env.SECRET_KEY, {
    expiresIn: "10hr",
  });
}

module.exports = router;
