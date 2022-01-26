const express = require("express");
const app = express();
const connectDB = require("./models/config");

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

connectDB();

app.get("/", (req, res) => {
  res.render("index");
});

//api register new user & login
const regRouter = require("./routes/register");
app.use("/register", regRouter);
const loginRouter = require("./routes/login");
app.use("/login", loginRouter);
const profRouter = require("./routes/profile");
app.use("/profile", profRouter);

app.listen(4000);
