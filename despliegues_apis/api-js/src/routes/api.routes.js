const express = require('express');
const router = express.Router();

const {
    checkStatus,
    getInfo
} = require('../controllers/api.controller');

// GET /check -> devuelve un estado OK.
router.get('/check', checkStatus);
// GET /info -> devuelve metadatos de la instancia en JSON.
router.get('/info', getInfo);

module.exports = router;
