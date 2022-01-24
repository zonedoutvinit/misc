const mongoose = require("mongoose");
const admin = require("./admin");
let Schema = mongoose.Schema;

let empSchema = new Schema({
  name: {
    type: String,
    required: true,
  },
  age: {
    type: Number,
    required: true,
  },
  adminID: {
    type: Schema.Types.ObjectId,
    ref: "user",
  },
});

let emp = mongoose.model("emp", empSchema);
module.exports = emp;
