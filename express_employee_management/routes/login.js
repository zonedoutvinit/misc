const express = require("express");
const router = express.Router();
const admin = require("../models/admin");
const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");
dotenv.config();
const auth = require("../middleware/authenToken");

router.get("/", (req, res) => {
  res.render("users/login");
});

router.post("/auth", async (req, res) => {
  admin
    .find({ uname: req.body.uname, passw: req.body.passw })
    //.find({ uname: req.body.uname } && { passw: req.body.passw })
    .exec()
    .then((user) => {
      if (user.length < 1) {
        res.json({ message: "no user found" });
      } else {
        const token = generateAccessToken({ uname: req.body.uname });
        //console.log(token);
        //res.json(token);

        console.log({ token });
        //res.send(token);
      }
      res.redirect(`/profile/${user[0]._id}`);
    });
});

// router.get("/protect/:id", auth, (req, res) => {
//   // const token = req.headers;
//   // console.log(token);
//   res.json({ mesage: "hidden message" });
//   //res.redirect(`profile/${user[0]._id}`);
// });

function generateAccessToken(username) {
  return jwt.sign(username, process.env.SECRET_KEY, { expiresIn: "1800s" });
}

module.exports = router;
