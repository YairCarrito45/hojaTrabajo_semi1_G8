// Endpoint de salud para validar disponibilidad de la API.
exports.checkStatus = (req, res) => {
    res.status(200).send("OK");
};

// Devuelve metadatos de la instancia usados en el laboratorio.
exports.getInfo = (req, res) => {
    res.status(200).json({
        Instancia: "Instancia-1 - API JS",
        Curso: "Seminario de Sistemas 1 A",
        Grupo: "Grupo #8"
    });
};
