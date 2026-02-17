const express = require('express');
require('dotenv').config();

const apiRoutes = require('./routes/api.routes');

const app = express();
const PORT = process.env.PORT || 3000;

// Parsea cuerpos JSON en las solicitudes.
app.use(express.json());
// Monta las rutas de la API en la raiz.
app.use('/', apiRoutes);

app.listen(PORT, () => {
    console.log(`API JS corriendo en puerto ${PORT}`);
});
