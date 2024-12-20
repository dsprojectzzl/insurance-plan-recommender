const plans = [
    { UID: 1, Plan: "Standard", Premium: "$50-$100", Deductible: "$1500-$3000", Coverage: "Basic coverage", AdditionalBenefits: "Wellness discounts" },
    { UID: 2, Plan: "Standard Plus", Premium: "$150-$250", Deductible: "$750-$1500", Coverage: "Routine care", AdditionalBenefits: "Health coaching" },
    { UID: 3, Plan: "Enhanced", Premium: "$300-$500", Deductible: "$250-$500", Coverage: "Comprehensive care", AdditionalBenefits: "Free wellness programs" }
];

function renderPlans() {
    const loadingDiv = document.getElementById("loading");
    const plansContainer = document.getElementById("plans-container");

    setTimeout(() => {
        const recommendedIndex = Math.floor(Math.random() * plans.length);

        plans.forEach((plan, index) => {
            const planDiv = document.createElement("div");
            planDiv.classList.add("plan");

            // Add plan content
            planDiv.innerHTML = `
                <h2>${plan.Plan}</h2>
                <p><strong>Premium:</strong> ${plan.Premium}</p>
                <p><strong>Deductible:</strong> ${plan.Deductible}</p>
                <p><strong>Coverage:</strong> ${plan.Coverage}</p>
                <p><strong>Benefits:</strong> ${plan.AdditionalBenefits}</p>
                <button class="details-btn" data-uid="${plan.UID}">View Details</button>
            `;

            // Highlight the recommended plan
            if (index === recommendedIndex) {
                const badge = document.createElement("div");
                badge.classList.add("recommended");
                badge.textContent = "Recommended";
                planDiv.prepend(badge);
            }

            plansContainer.appendChild(planDiv);
        });

        // Attach click event to "View Details" buttons
        attachDetailsEvent();

        // Hide loading animation and display plans
        loadingDiv.classList.add("hidden");
        plansContainer.classList.remove("hidden");
    }, 3000);
}

function attachDetailsEvent() {
    const detailButtons = document.querySelectorAll(".details-btn");
    detailButtons.forEach(button => {
        button.addEventListener("click", (event) => {
            const uid = event.target.dataset.uid; // Get UID from the button's data attribute
            alert(`You clicked View Details for Plan UID: ${uid}`);
            // Additional logic to show detailed information can go here
        });
    });
}

document.addEventListener("DOMContentLoaded", renderPlans);

