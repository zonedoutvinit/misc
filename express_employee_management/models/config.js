const mongoose = require("mongoose");

const DB =
  "mongodb+srv://vinit9:vinit4545@cluster0.qjm1x.mongodb.net/EMP_Auth?retryWrites=true&w=majority";

const connectDB = async () => {
  await mongoose.connect(DB);
  console.log("db connected");
};
module.exports = connectDB;
