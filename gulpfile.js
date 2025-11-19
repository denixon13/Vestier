import {src, dest, watch } from 'gulp' 
import * as dartSass from 'sass' 
import gulpSass from 'gulp-sass'
import GulpUglify from 'gulp-uglify'
import GulpConcat from 'gulp-concat'
import babel from 'gulp-babel' 
import imagemin from 'gulp-imagemin'
import imageminMozjpeg from 'imagemin-mozjpeg'
import pngquant from 'imagemin-pngquant';
import debug from 'gulp-debug'
import webp from 'gulp-webp'
import cleanCSS from 'gulp-clean-css';
import autoprefixer from 'gulp-autoprefixer';
import concat from 'gulp-concat';

const sass = gulpSass(dartSass) // inicializar gulp-sass

// tareas

// tarea para compilar JS
export function js(done){
    src('appvestier/static/js/app.js') // archivos fuentes
        .pipe(babel({presets: ['@babel/preset-env']})) // convertir a ES5
        .pipe(GulpConcat('app.js')) // nombre del archivo final
        .pipe(GulpUglify()) // minificar
        .pipe(dest('appvestier/static/build/js')) // carpeta destino
    done()
}

// tarea para compilar SASS
export function css(done){
    src('appvestier/static/scss/app.scss') // archivo fuente
        .pipe(sass()) // compilar
        .pipe(dest('appvestier/static/build/css')) // carpeta destino
    done()
}

// tarea para optimizar CSS
export function cssMin(done){
    src('appvestier/static/build/css/app.css') // archivo fuente
        .pipe(debug({title: 'CSS:'})) // ver en consola el archivo que se está optimizando
        .pipe(autoprefixer({cascade: false})) // agregar prefijos
        .pipe(cleanCSS({level: 2})) // minificar CSS
        .pipe(dest('appvestier/static/build/css')) // carpeta destino
    done()
}

// tarea para optimizar imágenes
export function img(done){
    src('appvestier/static/img/**/*.{png,jpg,jpeg}', {encoding:false}) // archivos fuente
        .pipe(debug({title: 'Imagenes:'})) // ver en consola los archivos que se están optimizando
        .pipe(imagemin([
            imageminMozjpeg({quality: 75}), // optimizar JPEG
            pngquant({quality: [0.6, 0.8]}) // optimizar PNG
        ])) // optimizar imágenes
        .pipe(dest('appvestier/static/build/img')) // carpeta destino
    done()
}

// tarea para convertir imágenes a WebP
export function imgWebp(done){
    src('appvestier/static/img/**/*.{png,jpg,jpeg}', {encoding:false}) // archivos fuente
        .pipe(debug({title: 'Convertiendo a WebP:'})) // ver en consola los archivos que se están convirtiendo
        .pipe(webp({quality: 75})) // convertir a WebP
        .pipe(dest('appvestier/static/build/img')) // carpeta destino
    done()
}

// tarea para observar cambios en archivos
export function dev(){
    watch('appvestier/static/scss/app.scss', css) // observar cambios en el archivo SASS
    watch('appvestier/static/js/app.js', js) // observar cambios en el archivo JS
    watch('appvestier/static/img/**/*', img) // observar cambios en las imágenes
    watch('appvestier/static/img/**/*', imgWebp) // observar cambios en las imágenes para convertir a WebP
    //watch('appvestier/static/scss/**/*.scss', cssMin) // observar cambios en los archivos SASS para optimizar CSS
}