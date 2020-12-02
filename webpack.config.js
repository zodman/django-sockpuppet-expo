const webpack = require("webpack");
const glob = require("glob");
var BundleTracker = require('webpack-bundle-tracker')

let globOptions = {
  ignore: ["node_modules/**", "venv/**"]
};

let entryFiles = glob.sync("**/javascript/*.js", globOptions);
let entryObj = {};
entryFiles.forEach(function(file) {
  if (file.includes(".")) {
    let parts = file.split("/");
    let path = parts.pop();
    let fileName = path.split(".")[0];
    entryObj[fileName] = `./${file}`;
  }
});
const config = {
  mode: process.env.NODE_ENV,
  entry: entryObj,
  output: {
    path: __dirname + "/core/static/dist/js",
    filename: "[name].[fullhash].js"
  },
  optimization: {
    minimize: true
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: "./webpack-stats.json"
    })
  ]
};
//console.log(config);
module.exports = config;
