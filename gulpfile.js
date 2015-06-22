var STICKER_ROOT = "https://d33e9um4nuyldw.cloudfront.net/stickers"
// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var jshint = require('gulp-jshint');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var download = require("gulp-download");
var minimatch = require('minimatch');
var unzip = require("gulp-unzip");
var shell = require('gulp-shell');

// Lint Task
gulp.task('lint', function() {
    return gulp.src('src/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// Concatenate & Minify JS
gulp.task('scripts', function() {
    return gulp.src('src/*.js')
        .pipe(concat('index.js'))
        .pipe(gulp.dest('dist'))
        .pipe(rename('index.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('dist'));
});

// Download the first metadata file
gulp.task('downloadmeta', function() {
    var metadataUrl = STICKER_ROOT + "/metadata";
    return download(metadataUrl)
        .pipe(gulp.dest("downloads/"));
});

// Download the catalog file
gulp.task('downloadcatalog', function() {
    var categoryZipFileUrl = STICKER_ROOT + "/catalog.zip";
    return download(categoryZipFileUrl)
        .pipe(gulp.dest("downloads/"));
});

// Extract the catalog zip file
gulp.task('extractcatalog', function(){
  gulp.src("downloads/catalog.zip")
    .pipe(unzip())
    .pipe(gulp.dest('downloads/'));
});

// Parse the metadata files and create the index.js file
gulp.task('createjs', shell.task([
  'python bin/metadata_to_js.py'
]));


// Download the metadata and category files
gulp.task('default', ['downloadmeta', 'downloadcatalog', 'extractcatalog', 'createjs', 'scripts']);



