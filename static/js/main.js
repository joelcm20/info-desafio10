document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".btn-edit-categoria");

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const categoriaId = btn.getAttribute("data-id");
      const nombre = prompt(
        "Editar categoria:",
        btn.previousElementSibling.value
      );
      editarCategoria(categoriaId, nombre);
    });
  });
});

function editarCategoria(categoriaId, nombre) {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  console.log(csrfToken);

  const data = {
    nombre,
    csrfmiddlewaretoken: csrfToken,
  };

  fetch(`/editar-categoria/${categoriaId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.msg);
      document.location.reload()
    })
    .catch((error) => console.log(error));
}
