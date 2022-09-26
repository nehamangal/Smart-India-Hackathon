document.addEventListener("DOMContentLoaded", function () {
  const separator = ",";

  const input = document
    .getElementsByClassName("field")[0]
    .querySelector("input");
  if (input.multiple) {
    if (input.list instanceof HTMLDataListElement) {
      const optionsValues = Array.from(input.list.options).map(
        (opt) => opt.value
      );
      let valueCount = input.value.split(separator).length;

      input.addEventListener("input", () => {
        const currentValueCount = input.value.split(separator).length;

        // Do not update list if the user doesn't add/remove a separator
        // Current value: "a, b, c"; New value: "a, b, cd" => Do not change the list
        // Current value: "a, b, c"; New value: "a, b, c," => Update the list
        // Current value: "a, b, c"; New value: "a, b" => Update the list
        if (valueCount !== currentValueCount) {
          const lsIndex = input.value.lastIndexOf(separator);
          const str =
            lsIndex !== -1 ? input.value.substr(0, lsIndex) + separator : "";
          filldatalist(input, optionsValues, str);
          valueCount = currentValueCount;
        }
      });
    }
  }

  function filldatalist(input, optionValues, optionPrefix) {
    const list = input.list;
    if (list && optionValues.length > 0) {
      list.innerHTML = "";

      const usedOptions = optionPrefix
        .split(separator)
        .map((value) => value.trim());

      for (const optionsValue of optionValues) {
        if (usedOptions.indexOf(optionsValue) < 0) {
          // Skip used values
          const option = document.createElement("option");
          option.value = optionPrefix + optionsValue;
          list.append(option);
        }
      }
    }
  }
});

let ideaDetails = document.querySelectorAll(".ideaDetails");

// ideaDetails.forEach((element) => {
//   let fields = element.querySelector(".fields");
//   let timesIcon = element.querySelector(".timesIcon");
//   let desc = element.querySelector(".desc");
//   let bottom = element.querySelector(".bottom");
//   element.addEventListener("mouseenter", () => {
//     fields.classList.remove("d_none");
//     desc.classList.remove("d_none");
//     bottom.classList.remove("d_none");
//     timesIcon.classList.remove("d_none");
//   });
//   timesIcon.addEventListener("click", () => {
//     fields.classList.add("d_none");
//     desc.classList.add("d_none");
//     bottom.classList.add("d_none");
//     timesIcon.classList.add("d_none");
//   });
// });

let addBtn = document.querySelector(".addBtn");
let popUpBg = document.getElementById("popUpBg");

addBtn.addEventListener("click", () => {
  popUpBg.classList.remove("d_none");
});

let closePopUp = document.getElementById("closePopUp");
closePopUp.addEventListener("click", () => {
  popUpBg.classList.add("d_none");

  //make default value
  popUpWindow.querySelector("#nameInput").value = "";
  popUpWindow.querySelector("#desc").value = "";
  popUpWindow.querySelector("#fieldInput").value = "";
  popUpWindow.querySelector("#file").value = "";
  popUpWindow.querySelector("#marketSize").value = "";
  popUpWindow.querySelector(
    'input[name="targetMarket"]:checked'
  ).checked = false;
});

let popUpWindow = document.getElementById("popUpWindow");

popUpBg.addEventListener("click", (e) => {
  if (!popUpWindow.contains(e.target)) {
    popUpBg.classList.add("d_none");
  }
});

let submitBtn = popUpWindow.querySelector("#submitBtn");

// Inputs data value
let nameValue = popUpWindow.querySelector("#nameInput").value || "UnKnown";
let desc = popUpWindow.querySelector("#desc").value || "UnKnown";
let fieldInput =
  popUpWindow.querySelector("#fieldInput").value.replaceAll(",", ", ") ||
  "UnKnown";
let file = popUpWindow.querySelector("#file").value || "UnKnown";
let marketSize = popUpWindow.querySelector("#marketSize").value || "UnKnown";
let targetMarket =
  popUpWindow.querySelector('input[name="targetMarket"]:checked').value ||
  "UnKnown";

submitBtn.addEventListener("click", (e) => {
  e.preventDefault();
  let nameValue = popUpWindow.querySelector("#nameInput").value || "UnKnown";
  let desc = popUpWindow.querySelector("#desc").value || "UnKnown";
  let fieldInput =
    popUpWindow.querySelector("#fieldInput").value.replaceAll(",", ", ") ||
    "UnKnown";
  let file = popUpWindow.querySelector("#file").value || "UnKnown";
  let marketSize = popUpWindow.querySelector("#marketSize").value || "UnKnown";
  let targetMarket =
    popUpWindow.querySelector('input[name="targetMarket"]:checked').value ||
    "UnKnown";

  let node = document.createElement("div");
  node.className = "ideaDetails";
  node.innerHTML = `<div class="ideaDetailsTop">
                      <h3 class="nameOfIdea">${nameValue}</h3>
                    </div>
                    <span class="fields d_none">${fieldInput}</span>
                    <br>
                    <span class="maeketSize">${marketSize}</span>
                    <h6 class="targetMarket">${targetMarket}</h6>
                    <p class="desc d_none">${desc}</p>
                    <div class="bottom d_none">
                      <div class="files">
                          <span>Download File</span>
                          <img src="./dashboard-fileIcon.svg" alt="">
                      </div>
                      <div class="btns">
                          <img src="./dashboard-edit-40.png" alt="" width="25px">
                          <img src="./dashboard-delete-32.png" alt="" width="30px">
                      </div>
                    </div>`;
  document.querySelector(".right").appendChild(node);

  popUpWindow.querySelector("#nameInput").value = "";
  popUpWindow.querySelector("#desc").value = "";
  popUpWindow.querySelector("#fieldInput").value = "";
  popUpWindow.querySelector("#file").value = "";
  popUpWindow.querySelector("#marketSize").value = "";
  popUpWindow.querySelector(
    'input[name="targetMarket"]:checked'
  ).checked = false;
});

let dashBoardRight = document.querySelector("right");
dashBoardRight;
