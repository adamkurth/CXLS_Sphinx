Buttons
=========



.. CXLS/CXFEL Buttons AND Person of Contact Button

.. CENTER POC 
.. raw:: html 

    <div class="contact-section">
        <button onclick="toggleContactInfo()" class="contact-button">Person of Contact</button>
        <div id="contactInfo" class="contact-info" style="display:none;">
            <p>Phone: 123-456-7890</p>
            <p>Email: <a href="mailto:contact@example.com">contact@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>

    <script>
    function toggleContactInfo() {
        var info = document.getElementById("contactInfo");
        if (info.style.display === "none" || !info.style.display) {
            info.style.display = "block";
        } else {
            info.style.display = "none";
        }
    }
    </script>

    <style>
    .contact-section {
        text-align: center;
        padding-top: 20px;
        position: relative;  /* Establishes a positioning context for dropdown */
    }

    .contact-button {
        background-color: #007bff;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        display: inline-block;
    }

    .contact-info {
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        position: absolute;
        top: 100%;  /* Position directly below the button */
        left: 50%;  /* Center horizontally */
        transform: translateX(-50%);  /* Adjust horizontal position */
        width: 80%;  /* Adjust width as needed */
        max-width: 600px;  /* Maximum width */
        text-align: left;
        z-index: 1000;  /* Ensure it's on top of other content */
    }
    </style>
















    