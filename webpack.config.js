const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require("path");

module.exports = {
    mode: "development",
    entry: "./js/src/index.js",
    output: {
        filename: '[name].js',
        path: __dirname + '/public',
    },
    module: {
      rules: [
        {
            test: /\.vue$/,
            use: [
                'vue-loader',
            ]
        },
        {
          test: /\.js$/,
          use: [
            {
              loader: "babel-loader",
              options: {
                presets: [
                  "@babel/preset-env"
                ]
              }
            }
          ]
        },
        {
            test: /\.scss$/,
            use: [
                'style-loader',
                {
                    loader: 'css-loader',
                    options: {
                        url: false,
                        sourceMap: true,
                        minimize: true,
                        importLoaders: 2
                    }
                },
                {
                    loader: 'postcss-loader',
                    options: {
                        sourceMap: true,
                        plugins: [
                            require('autoprefixer')({grid: true})
                        ]
                    }
                },
                {
                    loader: 'sass-loader',
                    options: {
                        sourceMap: true,
                    }
                }
            ]
        },
        {
            test: /\.css$/,
            use: [
                'vue-style-loader',
                'css-loader'
            ]
        },
      ]
    },
    resolve: {
      extensions: ['.js', '.vue'],
      alias: {
        vue$: 'vue/dist/vue.esm.js',
      },
    },
    plugins: [new VueLoaderPlugin()],
    devServer: {
        open: true,
        openPage: "index.html",
        contentBase: path.join(__dirname, 'public'),
        watchContentBase: true,
        port: 8799,
    },
};