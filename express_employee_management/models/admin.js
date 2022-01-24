const mongoose = require("mongoose");
let Schema = mongoose.Schema;

let adminSchema = new Schema({
  email: {
    type: String,
    required: true,
    unique: true,
  },
  uname: {
    type: String,
    unique: true,
    required: true,
  },
  passw: {
    type: Number,
    required: true,
  },
});

let admin = mongoose.model("user", adminSchema);

module.exports = admin;
