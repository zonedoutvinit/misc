const express = require("express");
const router = express.Router();
const emp = require("../models/emp");
const auth = require("../middleware/authenToken");

router.get("/:id",  (req, res) => {
  // let token = req.headers;
  // console.log(token);
  res.render("users/profile", { id: req.params.id });
});

// insert employee
router.post("/new", (req, res) => {
  const newEmp = new emp({
    name: req.body.name,
    age: req.body.age,
    adminID: req.body.id,
  });
  newEmp.save().then((result) => {
    res.send(`emp inserted`);
  });
});

// search employee
router.post("/view", (req, res) => {
  var name = req.body.name;
  var age = req.body.age;
  emp
    .where("name")
    .equals(name)
    .exec()
    .then((result) => {
      console.log({ result });
      // if (Object.values(result).includes(null)) {
      //   res.send("employee not found");
      // }
      // if (result.includes(null) == true) {
      //   res.send("employee not found");
      // }
      if (!result.length) {
        res.send("employee not found");
      } else {
        res.send(`employ is/are : ${result}`);
      }
    });
});

//update employee
router.post("/update", (req, res) => {
  var adminID = req.body.id;
  const Name = req.body.name;
  // var newName = req.nody.newname
  const update = req.body.newName; 
  console.log(update)
  emp
    .findOneAndUpdate({Name},{update},{new:true})
    .exec()
    .then((result)=>{ 
      console.log(result);
    });
  // emp.updateOne({Name},{update}).exec().then((result)=>{
  //   console.log(result)
  // });
});

// delete employee
router.delete("/delete", (req, res) => {
  res.send(`delete Id ${req.body.id}`);
});
/*
router.param("id", (req, res, next, id) => {
  console.log(id);
  next();
});*/

module.exports = router;
