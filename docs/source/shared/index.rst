Homepage for Shared Directory
=============================

.. Simple CXLS/CXFEL buttons.
.. raw:: html

    <div class="custom-buttons">
        <a href="../cxls/index.html" class="button">Access CXLS Docs</a>
        <a href="../cxfel/index.html" class="button">Access CXFEL Docs</a>
    </div>


.. Accelerator/POC 1
.. toctree::
   :maxdepth: 2

    accelerator

.. Accelerator POC 1
.. raw:: html

    <div class="contact-section" style="text-align: right;">
        <button onclick="toggleContactInfo1(event)" class="contact-button">Person of Contact 1</button>
        <div id="contactInfo1" class="contact-info" style="display:none;">
            <p>Phone: 123-456-7890</p>
            <p>Email: <a href="mailto:contact1@example.com">contact1@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>


.. Sample Delivery/POC 2
.. toctree::
   :maxdepth: 2
   :caption: Sample Delivery:

   sample_delivery


.. raw:: html

    <div class="contact-section" style="text-align: right;">
        <button onclick="toggleContactInfo2(event)" class="contact-button">Person of Contact 2</button>
        <div id="contactInfo2" class="contact-info" style="display:none;">
            <p>Phone: 987-654-3210</p>
            <p>Email: <a href="mailto:contact2@example.com">contact2@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>

.. raw:: html

    <script>
    function toggleContactInfo1(event) {
        event.preventDefault();
        var info = document.getElementById("contactInfo1");
        if (info.style.display === "none" || !info.style.display) {
            info.style.display = "block";
        } else {
            info.style.display = "none";
        }
    }

    function toggleContactInfo2(event) {
        event.preventDefault();
        var info = document.getElementById("contactInfo2");
        if (info.style.display === "none" || !info.style.display) {
            info.style.display = "block";
        } else {
            info.style.display = "none";
        }
    }
    </script>

    <style>
    .contact-button {
        background-color: #007bff;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        display: inline-block;
        margin-bottom: 10px;
    }

    .contact-info {
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        position: absolute;
        top: 100%;
        right: 0;
        width: 300px; /* Adjust as needed */
        text-align: left;
        z-index: 1000;
        display: none;
    }
    </style>