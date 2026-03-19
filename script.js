function verTelefone(nome, telefone) {
    if (telefone && telefone !== 'None' && telefone.trim() !== '') {
        alert("📞 Contato de " + nome + ": " + telefone);
    } else {
        alert("🌴 Ops! " + nome + " não deixou um telefone.");
    }
}
console.log("Ilha Tropical carregada! 🥥");