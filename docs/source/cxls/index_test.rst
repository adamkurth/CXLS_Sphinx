Homepage for TEST index
========================

.. Simple CXLS/CXFEL buttons.
.. raw:: html

    <div class="custom-buttons">
        <a href="../cxls/index.html" class="button">Access CXLS Docs</a>
        <a href="../cxfel/index.html" class="button">Access CXFEL Docs</a>
    </div>

.. Accelerator/POC 1

.. toctree::
   :maxdepth: 3
   :caption: Accelerator:
   
   accelerator/accelerator
   accelerator/overview


.. Accelerator/POC 1
.. raw:: html 

    <div class="contact-section" style="position: relative; text-align: right;">
        <button onclick="toggleContactInfo('contactInfo1')" class="contact-button">Person of Contact 1</button>
        <div id="contactInfo1" class="contact-info" style="display:none; position: absolute; right: 0; top: 100%;">
            <p>Phone: 123-456-7890</p>
            <p>Email: <a href="mailto:contact1@example.com">contact1@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>



.. Endstations/POC 2
.. toctree::
   :maxdepth: 3
   :caption: Endstations:

   endstations/endstations
   endstations/area_detector
   endstations/cxls_eiger_4m


.. Endstations/POC 2
.. raw:: html 

    <div class="contact-section" style="position: relative; text-align: right;">
        <button onclick="toggleContactInfo('contactInfo2')" class="contact-button">Person of Contact 2</button>
        <div id="contactInfo2" class="contact-info" style="display:none; position: absolute; right: 0; top: 100%;">
            <p>Phone: 987-654-3210</p>
            <p>Email: <a href="mailto:contact2@example.com">contact2@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>



.. Sample Delivery/POC 3
.. toctree::
   :maxdepth: 3
   :caption: Sample Delivery:

   sample_delivery/sample_delivery


.. Data Analysis/POC 3
.. raw:: html 

    <div class="contact-section" style="position: relative; text-align: right;">
        <button onclick="toggleContactInfo('contactInfo3')" class="contact-button">Person of Contact 3</button>
        <div id="contactInfo3" class="contact-info" style="display:none; position: absolute; right: 0; top: 100%;">
            <p>Phone: 111-222-3333</p>
            <p>Email: <a href="mailto:contact3@example.com">contact3@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>


.. Data Analysis/POC 3
.. toctree::
   :maxdepth: 3
   :caption: Data Analysis:
   
   data_analysis/data_analysis
   data_analysis/access/agave
   data_analysis/access/sol
   data_analysis/access/globus
   data_analysis/slurm_script
   data_analysis/external_software
   data_analysis/custom_software/custom_software
   data_analysis/custom_software/rcsb_search_api
   data_analysis/online_analysis
   data_analysis/offline_analysis
   data_analysis/projects
   data_analysis/projects/background_subtraction
   data_analysis/projects/stream_background_subtraction
   data_analysis/projects/overwrite_background_subtraction

.. Endstations POC 4
.. raw:: html 

    <div class="contact-section" style="position: relative; text-align: right;">
        <button onclick="toggleContactInfo('contactInfo4')" class="contact-button">Person of Contact 4</button>
        <div id="contactInfo4" class="contact-info" style="display:none; position: absolute; right: 0; top: 100%;">
            <p>Phone: 444-555-6666</p>
            <p>Email: <a href="mailto:contact4@example.com">contact4@example.com</a></p>
            <p>More info: <a href="https://www.example.com" target="_blank">Visit our website</a></p>
        </div>
    </div>

.. raw:: html

    <script>
    function toggleContactInfo(id) {
        var info = document.getElementById(id);
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
    }

    .contact-info {
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        width: 80%;
        max-width: 600px;
        text-align: left;
        z-index: 1000;
        display: none;
    }
    </style>
