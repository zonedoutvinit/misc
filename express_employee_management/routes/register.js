const express = require("express");
const admin = require("../models/admin");
const router = express.Router();

router.get("/", (req, res) => {
  res.render("users/register");
});

//sends user to their intended page via id
router.post("/", (req, res) => {
  const newUser = new admin({
    email: req.body.email,
    uname: req.body.uname,
    passw: req.body.passw,
  });
  newUser
    .save()
    .then((result) => {
      //res.json({ new: "user" });
      res.redirect(`profile`);
    })
    .catch((error) => {
      res.json(error);
    });
});

module.exports = router;
