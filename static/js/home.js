console.log("%c home.js loaded", "color:blue");

const form_object = document.getElementById("create-form");
console.log("form_object:", form_object);

function generateTemplate(new_plan) {
    return `  <li
            class="plan list-group-item bg-light d-flex align-items-center justify-content-between custom-list"
          >
            <span style="color:green" class="item-text">${new_plan.content}</span>
            <div>
              <button
                data-id="{{ new_plan.id }}"
                class="edit-me btn btn-success btn-sm mr-1 custom-radius"
              >
                <i style="margin-right: 5px" class="bi bi-pencil-square"></i
                >Edit
              </button>
              <button
                data-id="{{ new_plan.id }}"
                class="delete-me btn btn-danger btn-sm custom-radius"
              >
                <i style="margin-right: 5px" class="bi bi-trash"></i> Delete
              </button>
            </div>
          </li>`;
}

form_object.addEventListener("submit", function (event) {
    // stop Traditional API
    event.preventDefault();

    const input_value = document.getElementById("create-field").value;

    console.log("STEP1: Frontend > Rest API REQUEST > Backend");
    axios
        .post("/create_plan", { content: input_value })
        .then((response) => {
            console.log("STEP6: Frontend recieved back API Response");
            console.log("AXIOS Response:", response);
            const { status, result } = response.data;
            const new_plan = {
                id: result,
                content: input_value,
            }
            console.log("STEP7: Frontend Javascript mutates above page");
            document
                .getElementById("item-list")
                .insertAdjacentHTML("beforeend", generateTemplate(new_plan))
            document.getElementById("create-field").value = "";
            document.getElementById("create-field").focus();

            console.log("Created plan:", result, input_value);
        })
        .catch((err) => {
            console.log("Creating plan, Error:", err)
        });
});