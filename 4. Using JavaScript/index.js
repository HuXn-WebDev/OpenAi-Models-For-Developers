// ---------------------------------------
// 1. npm i dotenv
// import dotenv from "dotenv";
// dotenv.config();
// const API_KEY = process.env.API_KEY;
// console.log(API_KEY);

// async function fetchData() {
//   const response = await fetch("https://api.openai.com/v1/chat/completions", {
//     method: "POST",
//     headers: {
//       Authorization: `Bearer ${API_KEY}`,
//       "Content-Type": "application/json",
//     },

//     body: JSON.stringify({
//       model: "gpt-3.5-turbo",
//       messages: [{ role: "user", content: "Hello!" }],
//     }),
//   });

//   const data = await response.json();
//   // console.log(data);
//   console.log(data.choices[0].message);
// }

// fetchData();
// ---------------------------------------

// ---------------------------------------
// DALL-E
// import dotenv from "dotenv";
// dotenv.config();
// const API_KEY = process.env.API_KEY;

// async function fetchImages() {
//   const response = await fetch("https://api.openai.com/v1/images/generations", {
//     method: "POST",
//     headers: {
//       Authorization: `Bearer ${API_KEY}`,
//       "Content-Type": "application/json",
//     },

//     body: JSON.stringify({
//       prompt: "A cat staring at computer",
//       n: 2,
//       size: "1024x1024",
//     }),
//   });

//   const data = await response.json();
//   console.log(data);
// }

// fetchImages();
// ---------------------------------------
