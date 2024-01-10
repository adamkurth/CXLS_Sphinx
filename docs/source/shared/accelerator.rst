Accelerator
============

.. This button below works !!
.. raw:: html

    <div class="contact-section">
        <button onclick="toggleContactInfo()" class="contact-button">Person of Contact</button>
        <div id="contactInfo" class="contact-info">
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
            info.classList.add("expanded");
        } else {
            info.style.display = "none";
            info.classList.remove("expanded");
        }
    }
    </script>

    <style>
    .contact-section {
        text-align: right;
        position: relative; /* For absolute positioning of the dropdown */
        padding-top: 20px; /* Space above the button */
        padding-right: 20px; /* Space on the right */
    }

    .contact-button {
        background-color: #007bff; /* Blue background */
        color: white; /* White text */
        padding: 10px 15px; /* Some padding */
        border: none; /* No border */
        border-radius: 5px; /* Rounded corners */
        cursor: pointer; /* Pointer/hand icon */
        transition: background-color 0.3s; /* Smooth transition for hover effect */
        text-align: left; /* Align text to the left */
        display: inline-block; /* Inline block element */
    }

    .contact-info {
        background-color: #f8f9fa; /* Light background */
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        position: absolute; /* Positioned relative to the contact-section */
        top: 100%; /* Directly below the button */
        right: 0; /* Aligned with the left side of the button */
        width: auto; /* Auto width based on content */
        display: none; /* Hidden by default */
        text-align: left; /* Align text to the left */
    }
    </style>




Introduction
------------

The CXLS Compact X-ray Light Source is a state-of-the-art facility dedicated to cutting-edge research in compact X-ray technology and its applications in various fields. Our laboratory is equipped with advanced X-ray systems and experimental setups, allowing researchers to explore new frontiers in compact X-ray-based research.

Research Areas
--------------

Our laboratory focuses on the following research areas:

1. Compact X-ray imaging techniques for biomedical applications.
2. Compact X-ray-assisted fabrication of micro and nanostructures for advanced devices.
3. Compact X-ray-based materials analysis and characterization.
4. Compact X-ray diagnostics and therapeutics for various industries.
5. Compact X-ray safety and optimization of X-ray parameters for different applications.

Facilities and Equipment
------------------------

Our laboratory is equipped with the latest compact X-ray systems and experimental setups, including:

- High-power compact X-ray sources for precision imaging and analysis.
- Ultrafast compact X-ray systems for high-resolution imaging.
- Compact X-ray microscopy systems for detailed analysis.
- X-ray safety equipment and protocols to ensure a safe working environment.

Collaboration and Partnerships
-------------------------------

We actively collaborate with researchers, scientists, and industry partners to foster innovation and advance compact X-ray-based research. Our laboratory welcomes collaborations and partnerships from academia, industry, and other research institutions.

Contact Us
----------

For more information about the CXLS Compact X-ray Light Source and our research activities, please contact:

- Contact Name Goes Here
    Email: contact@asu.edu
    Phone: +1 (123) 456-7890

- Contact Name Goes Here
    Email: contact@asu.edu
    Phone: +1 (123) 456-7890

We look forward to hearing from you and exploring opportunities for collaboration!




