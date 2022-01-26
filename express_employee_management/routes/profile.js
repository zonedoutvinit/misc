const express = require("express");
const router = express.Router();
const emp = require("../models/emp");
const auth = require("../middleware/authenToken");

router.get("/", auth, (req, res) => {
  res.render("users/profile");
});

// insert employee
router.post("/new", auth, async (req, res) => {
  try {
    //console.log(req.user);
    const newEmp = await new emp({
      name: req.body.name,
      age: req.body.age,
      adminID: req.user.adminID, // use from token(req.decoded.userId)
    });
    newEmp.save().then((result) => {
      res.send(`emp inserted`);
    });
  } catch (error) {
    res.send("error");
  }
});

// search employee
router.post("/view", auth, (req, res) => {
  var name = req.body.name;
  var ID = req.user.adminID;
  emp
    .where("name")
    .equals(name)
    .where("adminID")
    .equals(ID)
    .exec()
    .then((result) => {
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
router.put("/update", auth, async (req, res) => {
  const filter = req.body.name;
  const changes = req.body.newname;
  const ID = req.user.adminID;
  try {
    const newEmp = await emp
      .where("name")
      .equals(filter)
      .where("adminID")
      .equals(ID)
      .select("_id");
    //console.log(newEmp);
    const postUpdate = await update(newEmp, changes);
    res.send(postUpdate);
  } catch {
    res.send(error);
  }
});

// delete employee
router.delete("/delete", auth, async (req, res) => {
  const deleteEmp = req.body.name;
  const adminID = req.user.adminID;
  //console.log(deleteEmp);
  try {
    const ID = await emp
      .where("name")
      .equals(deleteEmp)
      .where("adminID")
      .equals(adminID)
      .select("_id");
    //console.log(ID);
    const postDelete = await del(ID);
    res.send(postDelete);
  } catch {
    res.send(error);
  }
});

//update function
const update = async (_id, changes) => {
  try {
    const result = await emp.updateOne(
      { _id },
      {
        name: changes,
      }
    );
    return { result };
  } catch (err) {
    console.log("error");
  }
};

//delete function
const del = async (_id) => {
  try {
    const result = await emp.deleteOne({ _id });
    return { result };
  } catch (err) {
    console.log("error");
  }
};

module.exports = router;
