const analyzeBtn = document.getElementById("analyzeBtn");

if (analyzeBtn) {

    analyzeBtn.addEventListener("click", () => {

        document.getElementById("resultBox").innerHTML = `

        <div class="task">

            <div class="task-title">
                ✓ Complete AI Project
            </div>

            <div class="task-meta">
                Work • High Priority
            </div>

        </div>

        <div class="task">

            <div class="task-title">
                ✓ Prepare Java Interview
            </div>

            <div class="task-meta">
                Study • Medium Priority
            </div>

        </div>

        <div class="task">

            <div class="task-title">
                ✓ Buy Groceries
            </div>

            <div class="task-meta">
                Personal • Low Priority
            </div>

        </div>

        <br>

        <p style="color:#6B7280;">

        Summary:

        Three tasks were detected and categorized successfully.

        </p>

        `;

    });

}