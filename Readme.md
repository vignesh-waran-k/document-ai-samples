# Preliminary Processor Management API Documentation
<div style="padding-bottom:30px"></div>
* Author: docai-incubator@google.com
<div style="padding-bottom:30px"></div>
<h3> Disclaimer</h3>

This tool is not supported by the Google engineering team or product team. It is provided and supported on a best-effort basis by the DocAI Incubator Team. No guarantees of performance are implied.
<div style="padding-bottom:30px"></div>
<h3> Introduction and Notes</h3>
<div>This is preliminary documentation of internal API’s before they are readied for external use.
There is <b>no guarantee that the API’s will not change</b>, though those are typically minimized.
The necessary steps for training a CDE processor are all available in Python (as shown in Section 4) not fully documented here.
<span style="color:red">  These are experimental, subject to change and generally not recommended unless prior arrangements are specifically made in advance. </span></div>
<br>
<p ><span >NOTE 1: </span></p><p><span>The prediction / process document calls for CDE processors are the same as other processors,
so these are not documented here. Refer to online </span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors&amp;sa=D&amp;source=editors&amp;
ust=1704207105405744&amp;usg=AOvVaw2Qm4vh7sJhziy7EzPgmUfm">DocAI Documentation</a>
</span><span>. &nbsp;Either V1 or V1Beta3 may be used - they behave the same (For Java - V1 &amp; V1Beta3 differ significantly,
It is advised to use V1beta3). </span></p>

<ul>
    <li><span>Python for v1beta3 </span><span ><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.                                             document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document
_processor_service_DocumentProcessorServiceClient_process_document&amp;sa=D&amp;source=editors&amp;
ust=1704207105406068&amp;usg=AOvVaw07LfbSclRqCFaVJxf_mf91">here</a></span><span >. </span></li>
    <li ><span>For JAVA Client , use v1beta3 </span><span ><a  href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3&amp;sa=D&amp;source=editors&amp;ust=1704207105406321&amp;usg=AOvVaw3jqZFEiCpKrQcdiCgWrGDd">here</a></span></li>

</ul>
<p ><span></span></p>


<p><span>NOTE 2: Some API aspects (esp. Processor Mgmt) </span><span>are exposed</span><span >&nbsp;through </span></p>
<ul>
    <li><span>Python v1beta3 client libraries, documented online </span><span ><a  href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service&amp;sa=D&amp;source=editors&amp;ust=1704207105406621&amp;usg=AOvVaw2PCAuf77nTG4q1XQh5VBIY">here</a></span><span >. &nbsp;</span></li>
</ul>
<p><span></span></p>

<p><span >NOTE 3: </span></p><p ><span>You may wish to FIRST review section</span><span >&nbsp;Part 1, section 4)
Example Python Notebook Code</span><span>&nbsp;to see the Python code involved in training a CDE Parser. &nbsp;
As noted, this example leverages Google&rsquo;s HITL (Human Review) for annotation. Training datasets, properly prepared, may be imported from other sources.</span></p><p><span ></span></p>

<p><span>NOTE 4: </span></p>

<ul>
    <li ><span >RPC argument names should be translated to camelCase for HTTP REST calls (ex: display_name to displayName).</span></li>
    <li ><span>RPC references needs to be translated into URI&rsquo;s for HTTP REST Calls. See the first API call, </span><span >Create Processor</span><span >&nbsp;below for an example.</span></li>
</ul>

<p ><span ></span></p><p ><span class="c2">NOTE 5: Some minor RPC flags &nbsp;(esp. &ndash;-proto2) are excluded for brevity.
<div style="padding-bottom:30px"></div>
<h2> Summary</h2>
<table>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span>Language</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Function Name</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="13">
               <p><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px;
                border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px);
                -webkit-transform: rotate(0.00rad) translateZ(0px); width: 49.00px;
                height: 208.00px;"><img alt="" src="images/image2.png" style="width: 49.00px;
                height: 208.00px; margin-left: 0.00px; margin-top: 0.00px;
                transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);
                " title=""></span></p>
            </td>
            <td colspan="1" rowspan="6">
               <p><span>Processor Management</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_create_processor&amp;sa=D&amp;source=editors&amp;ust=1704207105409639&amp;usg=AOvVaw0gViCqhbX5HAj61b-UJBpS">create_processor</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Creates a processor from the type processor that the user chose. The processor is &nbsp;&quot;ENABLED&quot; state by default after its creation.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_list_processors&amp;sa=D&amp;source=editors&amp;ust=1704207105411071&amp;usg=AOvVaw0RiQIS3e6DS_jZnvtwLyG4">list_processors</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Lists all processors which belong to this project.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_get_processor&amp;sa=D&amp;source=editors&amp;ust=1704207105411873&amp;usg=AOvVaw0bh0JS8JIVnYL2RuexFYrV">get_processor</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Gets a processor detail.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.
services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_            services_document_processor_service_DocumentProcessorServiceClient_delete_processor&amp;sa=D&amp;
source=editors&amp;ust=1704207105412605&amp;usg=AOvVaw17H4jhFPvGod_F9DoxTZ6P">
delete_processor</a></span><span>(request) </span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.
document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_                        document_processor_service_DocumentProcessorServiceClient_enable_processor&amp;sa=D&amp;source=editors&amp;
ust=1704207105413597&amp;usg=AOvVaw1sxCK23j0V9VhWnqwiF7cv">enable_processor</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>It enables a processor</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_disable_processor&amp;sa=D&amp;source=editors&amp;ust=1704207105414381&amp;usg=AOvVaw2w6U834xIo4bJrDKIyXpfp">disable_processor</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>It disables a processor</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="5">
               <p><span>Processor Building</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_deploy_processor_version&amp;sa=D&amp;source=editors&amp;ust=1704207105415186&amp;usg=AOvVaw0P1irF7O0T0YwETU_lwm0G">deploy_processor_version</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Deploys the processor version.</span></p>
               <p><span>NOTE: It is not required for pre-trained processors</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_undeploy_processor_version&amp;sa=D&amp;source=editors&amp;ust=1704207105415965&amp;usg=AOvVaw3MGMuUKsJi3u3rrPlEUdM6">undeploy_processor_version</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Undeploys the processor version.</span></p>
               <p><span>NOTE: It is not required for pre-trained processors</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_get_processor_version&amp;sa=D&amp;source=editors&amp;ust=1704207105416779&amp;usg=AOvVaw1-lF7vBIpCFxOaeLX96VAM">get_processor_version</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Gets a processor version detail.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_process_document&amp;sa=D&amp;source=editors&amp;ust=1704207105417466&amp;usg=AOvVaw0klSmUuKurx3e25a_6jfDb">process_document</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Processes a single document.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_batch_process_documents&amp;sa=D&amp;source=editors&amp;ust=1704207105418133&amp;usg=AOvVaw0yQORUSrHFSEhCT07CI7hD">batch_process_documents</a></span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="2">
               <p><span>Operation (Async) Management</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.Document        ProcessorServiceAsyncClient%23google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsync
Client_get_operation&amp;sa=D&amp;source=editors&amp;ust=1704207105418845&amp;usg=AOvVaw3sfZ_z_NGbDznJ-d3a1ctY">get_operation</a>
</span><span>(request)</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Gets the latest state of a long-running operation.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_
processor_service.DocumentProcessorServiceAsyncClient%23google_cloud_documentai_v1beta3_services_document_processor_service_Document  ProcessorServiceAsyncClient_cancel_operation&amp;sa=D&amp;source=editors&amp;ust=1704207105419622&amp;usg=AOvVaw1fUDR2CEler3LBmpzwal3D">
cancel_operation</a></span><span>(request)</span></p>
               <h3 id="h.x3sper4sur7g"><span></span></h3>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Starts asynchronous cancellation on a long-running operation.</span></p>
               <p><span>The server makes a best effort to cancel the operation, but success is not guaranteed.
                If the server doesn&#39;t support this method, it returns google.rpc.Code.UNIMPLEMENTED.</span></p>
               <p><span></span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="7">
               <p><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px;
                border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);
                width: 49.00px; height: 208.46px;"><img alt="" src="images/image1.png" style="width: 49.00px;
                height: 208.46px; margin-left: 0.00px; margin-top: 0.00px;
                transform: rotate(0.00rad) translateZ(0px);
                -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p>
            </td>
            <td colspan="1" rowspan="5">
               <p><span>Processor Management</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_createProcessor_com_google_cloud_documentai_v1beta3_LocationName_com_
google_cloud_documentai_v1beta3_Processor_&amp;sa=D&amp;source=editors&amp;ust=1704207105420731&amp;
usg=AOvVaw3u2836Zh40dyD-mz3Vj26F">createProcessor</a></span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_
v1beta3_DocumentProcessorServiceClient_createProcessor_com_google_cloud_documentai_v1beta3_LocationName_com_                                             google_cloud_documentai_v1beta3_Processor_&amp;sa=D&amp;source=editors&amp;ust=1704207105420965&amp;
usg=AOvVaw3Ml1m9xinmPhy3PrkM8aBx">(LocationName parent, Processor processor)</a></span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Creates a processor from the type processor that the user chose. The processor are &quot;ENABLED&quot; state by default after its creation.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_Document
ProcessorServiceClient_listProcessors_com_google_cloud_documentai_v1beta3_LocationName_&amp;sa=D&amp;
source=editors&amp;ust=1704207105421648&amp;usg=AOvVaw0_ZHAlFUf8_nund9a9y1LC">listProcessors</a></span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_listProcessors_com_google_cloud_documentai_v1beta3_LocationName_&amp;sa=D&amp;
source=editors&amp;ust=1704207105421818&amp;usg=AOvVaw1lPrEqcM6vKols8g8R3_Cd">(LocationName parent)</a></span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Lists all processors which belong to this project.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_deleteProcessorAsync_com_google_cloud_documentai_v1beta3_ProcessorName_&amp;sa=D&amp;
source=editors&amp;ust=1704207105422495&amp;usg=AOvVaw2Mnw7xuKuwYqluuucLyw02">delete Processor Async</a></span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_deleteProcessorAsync_com_google_cloud_documentai_v1beta3_ProcessorName_&amp;sa=D&amp;
source=editors&amp;ust=1704207105422659&amp;usg=AOvVaw1JE_szJ5AD30TPFsk6kE83">(ProcessorName name)</a></span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_Document
ProcessorServiceClient_enableProcessorAsync_com_google_cloud_documentai_v1beta3_EnableProcessorRequest_&amp;
sa=D&amp;source=editors&amp;ust=1704207105423323&amp;usg=AOvVaw2xPBmB3sHSRkOqBHDWiimj">enableProcessorAsync</a></span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_    DocumentProcessorServiceClient_enableProcessorAsync_com_google_cloud_documentai_v1beta3_EnableProcessorRequest_&amp;
sa=D&amp;source=editors&amp;ust=1704207105423501&amp;usg=AOvVaw2Xy6lojAz8t9TQt1rhpbWl">(EnableProcessorRequest request)</a></span>
</p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Enables a processor.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_disableProcessorAsync_com_google_cloud_documentai_v1beta3_DisableProcessorRequest_&amp;
sa=D&amp;source=editors&amp;ust=1704207105424266&amp;usg=AOvVaw0Pm3ymD4-bXWFd06SoFX48">disableProcessorAsync</a></span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_disableProcessorAsync_com_google_cloud_documentai_v1beta3_DisableProcessorRequest_&amp;
sa=D&amp;source=editors&amp;ust=1704207105424461&amp;usg=AOvVaw0mE4DHrr6f2RPaEVYBKWVq">(DisableProcessorRequest request)</a>
</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Disables a processor.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="2">
               <p><span>Processor Building</span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_Document
ProcessorServiceClient_processDocument_com_google_cloud_documentai_v1beta3_ProcessRequest_&amp;sa=D&amp;
source=editors&amp;ust=1704207105425165&amp;usg=AOvVaw0dUQnGUeDiY-EoDzSxFqt2">processDocument</a></span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_
DocumentProcessorServiceClient_processDocument_com_google_cloud_documentai_v1beta3_ProcessRequest_&amp;sa=D&amp;
source=editors&amp;ust=1704207105425330&amp;usg=AOvVaw0JI_T85q8_QWfe4E1aN7k6">(ProcessRequest request)</a></span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>Processes a single document</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_                            DocumentProcessorServiceClient_batchProcessDocumentsAsync_com_google_cloud_documentai_v1beta3_BatchProcessRequest_&amp;
sa=D&amp;source=editors&amp;ust=1704207105426004&amp;usg=AOvVaw15IPpo1oavx6w3BG-R0QwZ">batchProcessDocumentsAsync</a></span><span>
<a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_Document
ProcessorServiceClient_batchProcessDocumentsAsync_com_google_cloud_documentai_v1beta3_BatchProcessRequest_&amp;sa=D&amp;
source=editors&amp;ust=1704207105426219&amp;usg=AOvVaw1ZknCJK58YOKLdzB2vmWPq">(BatchProcessRequest request)</a></span></p>
            </td>
            <td colspan="1" rowspan="1">
               <p><span>LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<br><br>
<h3> Part 1: Document AI Client for RPC and Python</h3>

## Create Processor

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3 DocumentProcessorServiceUIV1Beta3.CreateProcessor

<hr>
 <b>Example RPC payload:</b>
<code>parent:"projects/${GCP_PROJECT?}/locations/us"
processor {
  type: "SAMPLE_PROCESSOR"
  display_name: "TEST_STUBBY"
}</code>

<b>Example payload (JSON):</b>
<br>
<code>{
  "parent": "projects/${GCP_PROJECT?}/locations/us",
  "processor": {
    "type": "SAMPLE_PROCESSOR"
    "displayName": "TEST_STUBBY"
  },
}
</code>
<hr>

<h2 style="">Python:</h2><h3><a href="https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_create_processor">create_processor</a></h3>
<h5>
(request: Optioncreate_processoral[Union[google.cloud.documentai_v1beta3.types.document_processor_service.CreateProcessorRequest, dict]] = None, *, parent: Optional[str] = None, processor: Optional[google.cloud.documentai_v1beta3.types.processor.Processor] = None, retry: Union[google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault] = <_MethodDefault._DEFAULT_VALUE: <object object>>, timeout: Optional[float] = None, metadata: Sequence[Tuple[str, str]] = ())</h5>
<h4>Creates a processor from the type processor that the user chose. The processor is "ENABLED" state by default after its creation.</h4>

<h3>Parameters</h3>
<table style="border: 1px solid black">
         <tr style="border: 1px solid black; font-weight:700">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Name</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>request</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Union[</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.CreateProcessorRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105429624&amp;usg=AOvVaw2vWNEy5rx6QCFxa4Eqy_j3">google.cloud.documentai_v1beta3.types.CreateProcessorRequest</a></span><span>, dict]</span></p>
               <p><span>The request object. Request message for create a processor. Notice this request is sent to a regionalized backend service, and if the processor type is not available on that region, the creation fails.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>parent</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
               <p><span>Required. The parent (project and location) under which to create the processor. Format: projects/{project}/locations/{location} This corresponds to the parent field on the request instance; if request is provided, this should not be set.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>processor</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor&amp;sa=D&amp;source=editors&amp;ust=1704207105430517&amp;usg=AOvVaw2YcT3pWJfH3gL4pyk9ZfaM">google.cloud.documentai_v1beta3.types.Processor</a></span></p>
               <p><span>Required. The processor to be created,</span><span>&nbsp;requires [processor_type] and [display_name] </span><span>to be set. Also, the processor is under CMEK if CMEK fields are set. This corresponds to the processor field on the request instance; if request is provided, this should not be set.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>retry</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>google.api_core.retry.Retry</span></p>
               <p><span>Designation of what errors, if any, should be retried.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>timeout</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>float</span></p>
               <p><span>The timeout for this request.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>metadata</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Sequence[Tuple[str, str]]</span></p>
               <p><span>Strings which should be sent along with the request as metadata.</span></p>
               <p><span></span></p>
            </td>
         </tr>
      </table>
<h3>Returns</h3>

<table style="border: 1px solid black; float:left">
         <tr style="border: 1px solid black; font-weight:700">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Type</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor&amp;sa=D&amp;source=editors&amp;ust=1704207105432736&amp;usg=AOvVaw0jXt0AFKM5jh3vq4va36kl">google.cloud.documentai_v1beta3.types.Processor</a></span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>The first-class citizen for DocumentAI. Each processor defines how to extract structural information from a document.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<br><br><h3> List Processors</h3>

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3 DocumentProcessorServiceUIV1Beta3.ListProcessors


<h2 style="">Python:</h2><h3><ahref="https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_list_processors">List_processor</a></h3>
<h5>list_processors(request: Optional[Union[google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorsRequest, dict]] = None, *, parent: Optional[str] = None, retry: Union[google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault] = <_MethodDefault._DEFAULT_VALUE: <object object>>, timeout: Optional[float] = None, metadata: Sequence[Tuple[str, str]] = ())</h5>
<h4>Lists all processors which belong to this project.</h4>

<h3>Parameters</h3>
<table style="border: 1px solid black">
         <tr style="border: 1px solid black; font-weight:700">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Name</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>request</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Union[</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorsRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105435170&amp;usg=AOvVaw35nEC2HMT53vIg5xmghQ3N">google.cloud.documentai_v1beta3.types.ListProcessorsRequest</a></span><span>, dict]</span></p>
               <p><span>The request object. Request message for list all processors belongs to a project.</span></p>
            </td>
         </tr >
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>parent</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
               <p><span>Required. The parent (project and location) which owns this collection of Processors. Format: projects/{project}/locations/{location} This corresponds to the parent field on the request instance; if request is provided, this should not be set.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>retry</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>google.api_core.retry.Retry</span></p>
               <p><span>Designation of what errors, if any, should be retried.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>timeout</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>float</span></p>
               <p><span>The timeout for this request.</span></p>
            </td>
         </tr >
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>metadata</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Sequence[Tuple[str, str]]</span></p>
               <p><span>Strings which should be sent along with the request as metadata.</span></p>
            </td>
         </tr>
      </table>

<h3>Returns</h3>

<table style="border: 1px solid black; float:left">
         <tr style="border: 1px solid black; font-weight:700">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Type</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span><a href="https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorsPager">google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorsPager</a></span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Response message for list processors. Iterating over this object yields results and resolve additional pages automatically.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<h2><span style="color:#646b67;font-weight:800">Class ListProcessorsPager</span><span>&nbsp;</span></h2>
      <p><span>A pager for iterating through list_processors requests.</span></p>
      <p><span>This class thinly wraps an initial </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorsResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105438061&amp;usg=AOvVaw0gC0MV-RECzjCjVQAZa4K3">ListProcessorsResponse</a></span><span>&nbsp;object, and provides an __iter__ method to iterate through its processors field.</span></p>
      <p><span>If there are more pages, the __iter__ method makes additional ListProcessors requests and continue to iterate through the processors field on the corresponding responses.</span></p>
      <p><span>All the usual </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorsResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105438353&amp;usg=AOvVaw3F1a4J7smdccnjQ8SgfeFa">ListProcessorsResponse</a></span><span>&nbsp;attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.</span></p>
<br>

<h2><span style="color:#646b67;font-weight:800">Class ListProcessorsResponse</span><span>&nbsp;</span></h2>
<h4>Response message for list processors.</h4>
<p><span><b>Attributes</b></span></p>
      <table style="border: 1px solid black; padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Name</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Sequence[</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor&amp;sa=D&amp;source=editors&amp;ust=1704207105439208&amp;usg=AOvVaw2DLyx2K4b2SFqYpMdO287c">google.cloud.documentai_v1beta3.types.Processor</a></span><span>]</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>processors</span></p>
               <p><span>The list of processors.</span></p>
            </td>
         </tr>
         <tr>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>next_page_token</span></p>
               <p><span>Points to the next processor, otherwise empty.</span></p>
            </td>
         </tr>
      </table>

<br>

<h2><span style="color:#646b67;font-weight:800;">Class Processor</span><span>&nbsp;</span></h2>
<h4>The first-class citizen for DocumentAI. Each processor defines how to extract structural information from a document.</h4>
<p><span><b>Attributes</b></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Name</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>Description</span></p>
            </td>
         </tr >
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>name</span></p>
               <p><span>Output only. Immutable. The resource name of the processor. Format: projects/{project}/locations/{location}/processors/{processor}</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>type_</span></p>
               <p><span>The processor type.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>display_name</span></p>
               <p><span>The display name of the processor.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor.State&amp;sa=D&amp;source=editors&amp;ust=1704207105441945&amp;usg=AOvVaw0ftY5jqhZOiNaRIZl_g_Cq">google.cloud.documentai_v1beta3.types.Processor.State</a></span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>state</span></p>
               <p><span>Output only. The state of the processor.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>default_processor_version</span></p>
               <p><span>The default processor version.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>process_endpoint</span></p>
               <p><span>Output only. Immutable. The http endpoint that can be called to invoke processing.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>google.protobuf.timestamp_pb2.Timestamp</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>create_time</span></p>
               <p><span>The time the processor was created.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black">
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>str</span></p>
            </td>
            <td colspan="1" rowspan="1" style="border: 1px solid black">
               <p><span>kms_key_name</span></p>
               <p><span>The KMS key used for encryption/decryption in CMEK scenarios. See https://cloud.google.com/security-key- management.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<h2> Get Processor </h2>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3<br> <code>DocumentProcessorServiceUIV1Beta3.GetProcessor <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}"'<code>

<h2>Delete Processor </h2>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3 <br> <code>DocumentProcessorServiceUIV1Beta3.DeleteProcessor <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}"'</code>

## Python: <a href="https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_delete_processor">delete_processor </a><br>
delete_processor(request: Optional[Union[google.cloud.documentai_v1beta3.types.document_processor_service.DeleteProcessorRequest, dict]] = None, *, name: Optional[str] = None, retry: Union[google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault] = <_MethodDefault._DEFAULT_VALUE: <object object>>, timeout: Optional[float] = None, metadata: Sequence[Tuple[str, str]] = ())
<h4>Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.</h4><br>
<p><span><b>Parameters</b></span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Union[</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeleteProcessorRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105445638&amp;usg=AOvVaw3RRukULfS_hHWlTteoaZQw">google.cloud.documentai_v1beta3.types.DeleteProcessorRequest</a></span><span>, dict]</span></p>
               <p><span>The request object. Request message for the delete processor method.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>str</span></p>
               <p><span>Required. The processor resource name to be deleted. This corresponds to the name field on the request instance; if request is provided, this should not be set.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>retry</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>google.api_core.retry.Retry</span></p>
               <p><span>Designation of what errors, if any, should be retried.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>timeout</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>float</span></p>
               <p><span>The timeout for this request.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>metadata</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Sequence[Tuple[str, str]]</span></p>
               <p><span>Strings which should be sent along with the request as metadata.</span></p>
            </td>
         </tr>
      </table>
    <br>
 <p><span><b>Returns</b></span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>google.api_core.operation.Operation</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>An object representing a long-running operation. The result type for the operation is &nbsp;`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON representation for Empty is empty JSON object {}.</span></p>
               <p><span></span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<h2> Enable Processor</h2>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3 <br> <code>DocumentProcessorServiceUIV1Beta3.EnableProcessor <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}"'<code>

## Python: <a href="https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_enable_processor">enable_processor </a><br>
enable_processor(request: Optional[Union[google.cloud.documentai_v1beta3.types.document_processor_service.EnableProcessorRequest, dict]] = None, *, retry: Union[google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault] = <_MethodDefault._DEFAULT_VALUE: <object object>>, timeout: Optional[float] = None, metadata: Sequence[Tuple[str, str]] = ())
<h4>It enables a processor</h4><br>
<p><span><b>Parameters</b></span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Union[</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EnableProcessorRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105450088&amp;usg=AOvVaw1ZmTrjkCeGfH64rrauDDky">google.cloud.documentai_v1beta3.types.EnableProcessorRequest</a></span><span>, dict]</span></p>
               <p><span>The request object. Request message for the enable processor method.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>retry</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>google.api_core.retry.Retry</span></p>
               <p><span>Designation of what errors, if any, should be retried.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>timeout</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>float</span></p>
               <p><span>The timeout for this request.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>metadata</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Sequence[Tuple[str, str]]</span></p>
               <p><span>Strings which should be sent along with the request as metadata.</span></p>
            </td>
         </tr>
      </table>
<br>
<p><span><b>Returns</b></span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>google.api_core.operation.Operation</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>An object representing a long-running operation. The result type for the operation is &nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EnableProcessorResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105452268&amp;usg=AOvVaw1mDk_XARZbZuP6thWdKEgw">EnableProcessorResponse</a></span><span>&nbsp;Response message for the enable processor method. Intentionally empty proto for adding fields in future.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<p><span>Class<a href="https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3#enableprocessorrequest">EnableProcessorRequest</a></span></p>
<div><span style="background-color:#c9d1cf">public final class EnableProcessorRequest extends GeneratedMessageV3 implements EnableProcessorRequestOrBuilder</span></div>
<p><span>Request message for the enable processor method.</span></p>
      <p><span>Protobuf type google.cloud.documentai.v1beta3.EnableProcessorRequest</span></p>
      <p><span>Please Check </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.EnableProcessorRequest%23com_google_cloud_documentai_v1beta3_EnableProcessorRequest_NAME_FIELD_NUMBER&amp;sa=D&amp;source=editors&amp;ust=1704207105453680&amp;usg=AOvVaw3DN6i-QSE3bwepfWPs1ikm">Static Methods</a></span><span>&nbsp;and </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.EnableProcessorRequest%23com_google_cloud_documentai_v1beta3_EnableProcessorRequest_equals_java_lang_Object_&amp;sa=D&amp;source=editors&amp;ust=1704207105453852&amp;usg=AOvVaw3dxKQGcAjMv5po1Smi5J6Z">Non-Static Methods</a></span><span>&nbsp;Descriptions. </span></p>

## Disable Processor
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3  <br> <code>DocumentProcessorServiceUIV1Beta3.DisableProcessor <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}"'<code>

## Python: <a href="https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceClient#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceClient_disable_processor">disable_processor </a><br>
disable_processor(request: Optional[Union[google.cloud.documentai_v1beta3.types.document_processor_service.DisableProcessorRequest, dict]] = None, *, retry: Union[google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault] = <_MethodDefault._DEFAULT_VALUE: <object object>>, timeout: Optional[float] = None, metadata: Sequence[Tuple[str, str]] = ())
<h4>It disables a processor</h4><br>
<p><span><b>Parameters</b></span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Union[</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DisableProcessorRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105455722&amp;usg=AOvVaw0ZvqW72Usaz1_FKfga0nGI">google.cloud.documentai_v1beta3.types.DisableProcessorRequest</a></span><span>, dict]</span></p>
               <p><span>The request object. Request message for the disable processor method.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>retry</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>google.api_core.retry.Retry</span></p>
               <p><span>Designation of what errors, if any, should be retried.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>timeout</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>float</span></p>
               <p><span>The timeout for this request.</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>metadata</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Sequence[Tuple[str, str]]</span></p>
               <p><span>Strings which should be sent along with the request as metadata.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>
<p><span><b>Returns</b></span></p>
 <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>google.api_core.operation.Operation</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>An object representing a long-running operation. The result type for the operation is </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DisableProcessorResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105457757&amp;usg=AOvVaw1DSc8BDhLDfU0q-sCGAos9">DisableProcessorResponse</a></span><span>&nbsp;Response message for the disable processor method. Intentionally empty proto for adding fields in future.</span></p>
            </td>
         </tr>
      </table>
<div style="padding-bottom:30px"></div>

<p><span>Class<a href="https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3#disableprocessorrequest">DisableProcessorRequest</a></span></p>
<div><span style="background-color:#c9d1cf">public final class DisableProcessorRequest extends
GeneratedMessageV3 implements DisableProcessorRequestOrBuilder</span></div>
<p><span>Request message for the disable processor method.</span></p>
      <p><span>Protobuf type google.cloud.documentai.v1beta3.DisableProcessorRequest</span></p>
      <p><span>Please Check </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DisableProcessorRequest%23com_google_cloud_documentai_v1beta3_DisableProcessorRequest_NAME_FIELD_NUMBER&amp;sa=D&amp;source=editors&amp;ust=1704207105459634&amp;usg=AOvVaw2Jh8NvXY1f07ocWPOqZijc">Static Methods</a></span><span>&nbsp;and </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DisableProcessorRequest%23com_google_cloud_documentai_v1beta3_DisableProcessorRequest_equals_java_lang_Object_&amp;sa=D&amp;source=editors&amp;ust=1704207105459918&amp;usg=AOvVaw0moPU8_ZxaqNYxmklOOf03">Non-Static Methods</a></span><span>&nbsp;Descriptions. </span></p>
<div style="padding-bottom:30px"></div>
<div style="padding-bottom:30px"></div>
<h2> 2) Processor Building </h2>
<h3> Train Processor Version</h3>

<div style="color:#1a6ebb; background-color:#b2d6f7">NOTE: Supported only for custom or up-trainable processors.<br>
NOTE: Only flat schemas are currently supported (no EntityType.properties).</div>

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3 <br> <code>DocumentProcessorServiceUIV1Beta3.TrainProcessorVersion <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}"'<code>
<div>
<b>RETURNS:</b>longrunning.Operation<br>
<b>HTTP ARGUMENTS:</b>
    <ol>
    <li><b>parent:</b> Resource name of the document processor in  "projects/*/locations/*/processors/*" format.</li>
    <li><b>display_name:</b> Display name of the new processor version.</li>
    <li><b>schema:</b> Processor schema.
 display_name: "custom_schema_name"
  entity_types {
    type: "custom_field_name"
    base_type: "string"
    occurrence_type: REQUIRED_ONCE
}
schema.base_type’s: string, datetime, money, number date, address
occurrence_type: optional once, optional multiple, required once, required multiple</li>
    <li><b>training_data_path:</b> Path to the training data directory.</li>
    <li><b>test_data_path:</b> Path to the test data directory.</li>
<span style="color:red">INTERNAL OPTIONS:</span>
     <li><b>extraction_options:</b> Options for training extraction processors.</li>
     <li><b>classification_options:</b> Options for training classification processors.</li>
    </ol>
</div>
<b><i>Example:</i></b>
<code>
parent:
"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}"
processor_version { display_name: "my-custom-processor-v01" }
input_data {
  training_documents {
    gcs_prefix {
      gcs_uri_prefix: "gs://my-bucket/my_train_dir_json/"
    }
  }
  test_documents {
    gcs_prefix {
      gcs_uri_prefix: "gs://my-bucket/my_test_dir_json/"
    }
  }
}
schema {
  display_name: "my_schema"
  entity_types {
    type: "invoice_id"
    base_type: "string"
    occurrence_type: REQUIRED_ONCE
  }
  entity_types {
    type: "invoice_date"
    base_type: "datetime"
    occurrence_type: REQUIRED_ONCE
  }
  entity_types {
    type: "line_item/amount"
    base_type: "money"
    occurrence_type: OPTIONAL_MULTIPLE
  }
  entity_types {
    type: "line_item/description"
    base_type: "string"
    occurrence_type: OPTIONAL_MULTIPLE
  }
}
};

</code>

## Deploy Processor Version

<div style="color:#1a6ebb; background-color:#b2d6f7">NOTE: This step is not required for pre-trained processors.
</div>
<br>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3  <br>
 <code> DocumentProcessorServiceUIV1Beta3.DeployProcessorVersion
 <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/processorVersions/${PROCESSOR_VERSION_ID?}" ' </code>

## Undeploy Processor Version

<div style="color:#1a6ebb; background-color:#b2d6f7">NOTE: This step is not required for pre-trained processors.
</div>
<br>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3  <br>

 <code> DocumentProcessorServiceUIV1Beta3.UndeployProcessorVersion
 <br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/processorVersions/${PROCESSOR_VERSION_ID?}" ' </code>
## Get Processor Version
<br>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3<br>
<code>DocumentProcessorServiceUIV1Beta3.GetProcessorVersion
<br>'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/processorVersions/${PROCESSOR_VERSION_ID?}"'
</code>

## Process Document (UI preview)
## Using the default version
<br>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3<br>
 <code>DocumentProcessorServiceUIV1Beta3.ProcessDocument
 <br>'document.content=readfile(/my-dir/taulia_1.pdf)'
  'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}" document mime_type: "application/pdf" '
 </code>

## Using the specific version
<br>
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentprocessorserviceuiv1beta3<br>

 <code>DocumentProcessorServiceUIV1Beta3.ProcessDocument
 <br>'document.content=readfile(/my-dir/taulia_1.pdf) '
  'name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/processorVersions/${PROCESSOR_VERSION_ID?}" document mime_type: "application/pdf"'
 </code>
<div style="padding-bottom:30px"></div>
<h2> 3) Operation (Async) Management</h2>
<h3> Get Operation</h3>

<b>RPC:</b>
google.longrunning.clouddocumentaicoreoperations
<br>
<code>CloudDocumentAICoreOperations.GetOperation
 <br>'name: "projects/${GCP_PROJECT?}/locations/us/operations/${OPERATION_ID?}"’
<code>

## Cancel Operation
<b>RPC:</b>
google.longrunning.clouddocumentaicoreoperations
<br>
<code>CloudDocumentAICoreOperations.CancelOperation
 <br>'name: "projects/${GCP_PROJECT?}/locations/us/operations/${OPERATION_ID?}"’
<code>
<div style="padding-bottom:30px"></div>
# 4) Document Service Sample Calls
 These involve:
<ul>

<li>GCP project</li>
<li>Location </li>
<li>Processor ID</li>
</ul>

## Get Dataset

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3  
<br>
<code>DocumentServiceUIV1Beta3.GetDataset
 <br>name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
<code>

## Import Documents
## Use GCS prefix to import a set of documents
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.ImportDocuments
    <b><i>Example Payload:</i></b>
 <br>dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
batch_documents_import_configs {
  batch_input_config {
    gcs_prefix {
      gcs_uri_prefix: "${GCS_URI?}"
    }
  }
}

</code>

## Use a list of individual GCS documents

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.ImportDocuments
    <b><i>Example Payload:</i></b>
 <br>dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
batch_documents_import_configs {
  batch_input_config {
    gcs_documents {
      documents{
        gcs_uri: "${GCS_URI?}"
        mime_type: "application/pdf"
      }
      documents{
        gcs_uri: "${GCS_URI?}"
        mime_type: "application/pdf"
      }
    }
  }
}
'
</code>

## Get Documents
## Use GCS prefix to import a set of documents as follows
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.GetDocument
    <b><i>Example Payload:</i></b>
 <br>dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
document_id {
  gcs_managed_doc_id {
    gcs_uri:"${GCS_URI?}"
  }
}
page_range {
  start: 1
  end: -1
}
</code>

## Get Documents Thumbnails
## Use GCS prefix to import a set of documents follows
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.GetThumbnails
    <b><i>Example Payload:</i></b>
 <br>dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
document_id {
  gcs_managed_doc_id {
    gcs_uri:"${GCS_URI?}"
  }
}
thumbnail_size: THUMBNAIL_SIZE_SMALL
page_range {
  start:1
  end:1
}
</code>

## List Documents
## Use GCS prefix to import a set of documents for processors
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.ListDocuments

 <br>dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
'
</code>

## Update Documents
## Use GCS prefix to import a set of documents for locations
<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.UpdateDocument
    <b><i>Example Payload:</i></b>
 <br>dataset:"projects/${GCP_PROJECT?}/locations/__LOCATIONS__/processors/${PROCESSOR_ID?}/dataset"
document_update {
  document_id {
    gcs_managed_doc_id {
      gcs_uri: "${GCS_URI?}"
      cw_doc_id: "fake-cw-doc-id"
    }
  }
  document {
    text: "fake document"
    revisions: {
      id: "parent revision"
      parent: 0
    }
    entities: {type: "address"}
    entities: {type: "first_name"}
  }
}

</code>

## Batch Move Documents

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.BatchMoveDocuments
    <b><i>Example Payload:</i></b>
 <br>dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
document_ids {
  gcs_managed_doc_id {
    gcs_uri:"${GCS_URI?}"
  }
}
dataset_type: DATASET_SPLIT_TEST

</code>

## Get All Dataset Split Stats

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.GetAllDatasetSplitStats

 <br>‘dataset:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset"
'
</code>

## Get Dataset Schema

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3
<br>
<code>DocumentServiceUIV1Beta3.GetDatasetSchema

 <br>‘name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset/datasetSchema"
'
</code>

## Update Dataset Schema
## Updatable items include

<ul>

<li>Dataset Schema Display Name</li>
<li>Dataset Schema Description</li>
<li>Base Type</li>
<li>Occurrence Type</li>
<li>Source</li>
<li>Type</li>

</ul>

<b>RPC:</b>
google.cloud.documentai.uiv1beta3.documentserviceuiv1beta3  
<br>
<code>DocumentServiceUIV1Beta3.UpdateDatasetSchema  
    <b><i>Example Payload:</i></b>
 <br>dataset_schema {
name:"projects/${GCP_PROJECT?}/locations/us/processors/${PROCESSOR_ID?}/dataset/datasetSchema"
  schema {
          display_name:"${SCHEMA_DISPLAY_NAME}"
          description:"${SCHEMA_DESCRIPTION}"
          entity_types {
                  base_type:"${BASE_TYPE?}"
                  occurrence_type:${OCCURRENCE_TYPE_ENUM?}
                  source:${SOURCE_ENUM?}
                  type:"${TYPE?}"
          }
  }
}
</code>
 <div style="color:#1a6ebb; background-color:#b2d6f7">NOTE: display_name and description can be empty string if not explicitly set

</div>


<div style="padding-bottom:30px"></div>
<h2> Part 2: Document AI Client for Java</h2>
<h3> Quickstart</h3>
If you are using Maven with "libraries-bom", add this to your pom.xml file:

<div style="padding-bottom:30px"></div>
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>libraries-bom</artifactId>
      <version>26.30.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>com.google.cloud</groupId>
    <artifactId>google-cloud-storage</artifactId>
  </dependency>
<div style="padding-bottom:30px"></div>
If you are using Maven without BOM, add this to your dependencies:
<div style="padding-bottom:30px"></div>
<dependency>
  <groupId>com.google.cloud</groupId>
  <artifactId>google-cloud-document-ai</artifactId>
  <version>26.30.0</version>
</dependency>
<div style="padding-bottom:30px"></div>
If you are using Gradle 5.x or later, add this to your dependencies:
<div style="padding-bottom:30px"></div>
implementation platform('com.google.cloud:libraries-bom:26.30.0')

implementation 'com.google.cloud:google-cloud-storage'
<div style="padding-bottom:30px"></div>

If you are using Gradle without BOM, add this to your dependencies:

<div style="padding-bottom:30px"></div>
implementation 'com.google.cloud:google-cloud-document-ai:26.30.0'
<div style="padding-bottom:30px"></div>
If you are using SBT, add this to your dependencies:
<div style="padding-bottom:30px"></div>
libraryDependencies += "com.google.cloud" % "google-cloud-document-ai" % "26.30.0"
<div style="padding-bottom:30px"></div>
Authentication
See the <a href="https://github.com/googleapis/google-cloud-java#authentication">Authentication</a> section in the base directory's README.

Authorization
The client application making API calls must be granted <a href="https://developers.google.com/identity/protocols/oauth2/scopes">authorization scopes</a> required for the desired Document AI APIs, and the authenticated principal must have the <a href="https://cloud.google.com/iam/docs/understanding-roles#predefined_roles">IAM role(s)</a> required to access GCP resources using the Document AI API calls.
<div style="padding-bottom:30px"></div>
  <h2 ><span>Getting Started - Procedure</span></h2>
      <h4 ><span>Prerequisites</span></h4>
      <p><span>You need a </span><span><a href="https://www.google.com/url?q=https://console.developers.google.com/&amp;sa=D&amp;source=editors&amp;ust=1704207105489935&amp;usg=AOvVaw0sCfwjsP6xrFl8WUbmTw4H">Google Cloud Platform Console</a></span><span>&nbsp;project with the Document AI </span><span><a href="https://www.google.com/url?q=https://console.cloud.google.com/flows/enableapi?apiid%3Ddocumentai.googleapis.com&amp;sa=D&amp;source=editors&amp;ust=1704207105490042&amp;usg=AOvVaw0uKl4iX3KQvb28dd2-qIfL">API enabled</a></span><span>.</span></p>
      <p><span>You need to </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/apis/docs/getting-started%23enabling_billing&amp;sa=D&amp;source=editors&amp;ust=1704207105490169&amp;usg=AOvVaw2-2oEkB1vkMsK5nwc19U4S">enable billing</a></span><span>&nbsp;to use Google Document AI.</span></p>
      <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/resource-manager/docs/creating-managing-projects&amp;sa=D&amp;source=editors&amp;ust=1704207105490301&amp;usg=AOvVaw14EPtrktONX4l2rfmI9UM6">Follow these instructions</a></span><span>&nbsp;to get your project set up. You also need to set up the local development environment by</span></p>
      <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/sdk/&amp;sa=D&amp;source=editors&amp;ust=1704207105490427&amp;usg=AOvVaw2IMs4i44l_a_rSxghOwDjd">installing the Google Cloud SDK</a></span><span>&nbsp;and running the following commands in command line:</span></p>
<div style="padding-bottom:30px"></div>
<div style="padding-bottom:30px"></div>
gcloud auth login and gcloud config set project [YOUR PROJECT ID]
<div style="padding-bottom:30px"></div>
## Installation and setup

<p><span>You&#39;ll need to obtain the </span><span>google-cloud-document-ai</span><span>&nbsp;library. &nbsp;See the </span>>Quickstart<span>&nbsp;section</span></p>
<p><span>to add </span><span>google-cloud-document-ai</span><span>&nbsp;as a dependency in your code.</span></p>
<p><span></span></p>
<p><span>Also, Check the</span> QuickStart.java<span>&nbsp;file available at the end of this document to get a better understanding of various function calls. </span></p>
<div style="padding-bottom:30px"></div>
<div style="padding-bottom:30px"></div>
<h2>1. Processor Management</h2>
<h3><span>Create Processor</span></h3>
<p><span>Function</span><span>&nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_createProcessor_com_google_cloud_documentai_v1beta3_LocationName_com_google_cloud_documentai_v1beta3_Processor_&amp;sa=D&amp;source=editors&amp;ust=1704207105493477&amp;usg=AOvVaw3-Q3kydHo1Ao5e-dO0rjg7">createProcessor(LocationName parent, Processor processor)</a></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;Processor </span><span>createProcessor</span><span>(LocationName parent, Processor processor)</span></p>
            </td>
         </tr>
      </table>
      <p><span>Creates a processor from the type processor that the user chose. The processor is &quot;ENABLED&quot; state by default after its creation.</span></p>
      <p><span>Parameters</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>parent</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.LocationName&amp;sa=D&amp;source=editors&amp;ust=1704207105494725&amp;usg=AOvVaw1ZFN-c-MjTWKXBpLxMrSxb">LocationName</a></span></p>
               <p><span>Required. The parent (project and location) under which to create the processor. Format: projects/{project}/locations/{location}</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>processor</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Processor&amp;sa=D&amp;source=editors&amp;ust=1704207105495215&amp;usg=AOvVaw2Dkt7kCoKSC6KskMF44DZM">Processor</a></span></p>
               <p><span>Required. The processor to be created, requires [processor_type] and [display_name] to be set. Also, the processor is under CMEK if CMEK fields are set.</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Processor&amp;sa=D&amp;source=editors&amp;ust=1704207105496230&amp;usg=AOvVaw11wsksWqG8pMT5g9G06v5K">Processor</a></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span>Sample Implementation:</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>// This snippet has been automatically generated for illustrative purposes only.</span><span><br> </span><span>// It may require modifications to work in your environment.</span><span><br> </span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; LocationName parent = LocationName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>);<br> &nbsp; Processor processor = Processor.newBuilder().build();<br> &nbsp; Processor response = documentProcessorServiceClient.createProcessor(parent, processor);<br> }</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <h3 ><span>List Processors</span></h3>
      <p><span>Function </span><span>&nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_listProcessors_com_google_cloud_documentai_v1beta3_LocationName_&amp;sa=D&amp;source=editors&amp;ust=1704207105497607&amp;usg=AOvVaw15sX68Nym28GDdU6vhoHZl">listProcessors(LocationName parent)</a></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;DocumentProcessorServiceClient.ListProcessorsPagedResponse </span><span>listProcessors</span><span>(LocationName parent)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Lists the processor types that exist.</span></p>
      <p><span>Parameters</span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>parent</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.LocationName&amp;sa=D&amp;source=editors&amp;ust=1704207105498970&amp;usg=AOvVaw1A-mO8TJlDtNPp4BQH8XzX">LocationName</a></span></p>
               <p><span>Required. The parent (project and location) which owns this collection of Processors. Format: projects/{project}/locations/{location}</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient.ListProcessorsPagedResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105499948&amp;usg=AOvVaw1bxbFf1pHge4XVhqj4UhZu">DocumentProcessorServiceClient.ListProcessorsPagedResponse</a></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span><br></span><span>Sample Implementation:</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>// This snippet has been automatically generated for illustrative purposes only.</span><span><br> </span><span>// It may require modifications to work in your environment.</span><span><br> </span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; LocationName parent = LocationName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>);<br> &nbsp; </span><span>for</span><span>&nbsp;(Processor element : documentProcessorServiceClient.listProcessors(parent).iterateAll()) {<br> &nbsp; &nbsp; </span><span>// doThingsWith(element);</span><span><br> &nbsp; }<br> }</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Function </span><span>&nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_deleteProcessorAsync_com_google_cloud_documentai_v1beta3_ProcessorName_&amp;sa=D&amp;source=editors&amp;ust=1704207105501370&amp;usg=AOvVaw2Pu1YR43CvA9z9dh5DKIzR">deleteProcessorAsync(ProcessorName name)</a></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;"></tr>
      </table>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;Empty,DeleteProcessorMetadata&gt; </span><span>deleteProcessorAsync</span><span>(ProcessorName name)</span></p>
            </td>
         </tr>
      </table>
      <p><span>Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.</span></p>
      <p><span>Parameters</span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ProcessorName&amp;sa=D&amp;source=editors&amp;ust=1704207105502695&amp;usg=AOvVaw2ErjsxPUoVWJGNs-lJTHTz">ProcessorName</a></span></p>
               <p><span>Required. The processor resource name to be deleted.</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html&amp;sa=D&amp;source=editors&amp;ust=1704207105503477&amp;usg=AOvVaw3um3qZY6ZXie-A903_VCAi">OperationFuture</a></span><span>&lt;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html&amp;sa=D&amp;source=editors&amp;ust=1704207105503603&amp;usg=AOvVaw2ksyvpFJhA2666j77TcheP">Empty</a></span><span>,</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DeleteProcessorMetadata&amp;sa=D&amp;source=editors&amp;ust=1704207105503737&amp;usg=AOvVaw2o0goFbJ99SAZTVyF4CCgX">DeleteProcessorMetadata</a></span><span>&gt;</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span><br></span><span>Sample Implementation:</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>// This snippet has been automatically generated for illustrative purposes only.</span><span><br> </span><span>// It may require modifications to work in your environment.</span><span><br> </span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; ProcessorName name = ProcessorName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>);<br> &nbsp; documentProcessorServiceClient.deleteProcessorAsync(name).get();<br> }<br> </span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <h3 ><span>Enable Processor</span></h3>
      <p><span>Function</span><span>&nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_enableProcessorAsync_com_google_cloud_documentai_v1beta3_EnableProcessorRequest_&amp;sa=D&amp;source=editors&amp;ust=1704207105505138&amp;usg=AOvVaw1-6O2RDMHl_nFbc4XOHKEh">enableProcessorAsync(EnableProcessorRequest request)</a></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;EnableProcessorResponse,EnableProcessorMetadata&gt; </span><span>enableProcessorAsync</span><span>(EnableProcessorRequest request)</span></p>
            </td>
         </tr>
      </table>
      <p><span>Enables a processor</span></p>
      <p><span></span></p>
      <p><span>Parameters</span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.EnableProcessorRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105506702&amp;usg=AOvVaw2q269KFh4lb2wOuKdpKP1H">EnableProcessorRequest</a></span></p>
               <p><span>The request object containing all of the parameters for the API call.</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html&amp;sa=D&amp;source=editors&amp;ust=1704207105508078&amp;usg=AOvVaw04h0CorwF-w-czRSmSAsc-">OperationFuture</a></span><span>&lt;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.EnableProcessorResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105508260&amp;usg=AOvVaw3RRpkUqlX_UDtq4YIkOUkh">EnableProcessorResponse</a></span><span>,</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.EnableProcessorMetadata&amp;sa=D&amp;source=editors&amp;ust=1704207105508414&amp;usg=AOvVaw3yynf0ulMohzwRxQtjbSDS">EnableProcessorMetadata</a></span><span>&gt;</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span><br></span><span>Sample Implementation</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; EnableProcessorRequest request =<br> &nbsp; &nbsp; &nbsp; &nbsp; EnableProcessorRequest.newBuilder()<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setName(ProcessorName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>).toString())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .build();<br> &nbsp; &nbsp; EnableProcessorResponse response = documentProcessorServiceClient.enableProcessorAsync(request).get();<br> &nbsp; &nbsp;}<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <h3 ><span>Disable Processor</span></h3>
      <p><span>Function</span><span>&nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_disableProcessorAsync_com_google_cloud_documentai_v1beta3_DisableProcessorRequest_&amp;sa=D&amp;source=editors&amp;ust=1704207105509743&amp;usg=AOvVaw2FVytAK6Wm2NW8myGsZKzp">disableProcessorAsync(DisableProcessorRequest request)</a></span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;DisableProcessorResponse,DisableProcessorMetadata&gt; </span><span>disableProcessorAsync</span><span>(DisableProcessorRequest request)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Disables a processor.</span></p>
      <p><span></span></p>
      <p><span>Parameters</span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DisableProcessorRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105511095&amp;usg=AOvVaw2pFV2uM8EXNMt6X1Fz6mqR">DisableProcessorRequest</a></span></p>
               <p><span>The request object containing all of the parameters for the API call.</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html&amp;sa=D&amp;source=editors&amp;ust=1704207105512045&amp;usg=AOvVaw1-Raj1m_1DMPDRlHImNs7O">OperationFuture</a></span><span>&lt;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DisableProcessorResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105512187&amp;usg=AOvVaw13ppleR2Dq1aEPDCiZU2eP">DisableProcessorResponse</a></span><span>,</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DisableProcessorMetadata&amp;sa=D&amp;source=editors&amp;ust=1704207105512322&amp;usg=AOvVaw16615JdMmwNWz2G40TEQB1">DisableProcessorMetadata</a></span><span>&gt;</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <p><span>Sample Implementation</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>// This snippet has been automatically generated for illustrative purposes only.</span><span><br> </span><span>// It may require modifications to work in your environment.</span><span><br> </span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; DisableProcessorRequest request =<br> &nbsp; &nbsp; &nbsp; DisableProcessorRequest.newBuilder()<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setName(ProcessorName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>).toString())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .build();<br> &nbsp; DisableProcessorResponse response =<br> &nbsp; &nbsp; &nbsp; documentProcessorServiceClient.disableProcessorAsync(request).get();<br> }<br> </span></p>
            </td>
         </tr>
      </table>
      <hr style="page-break-before:always;display:none;">
<div style="padding-bottom:30px"></div>
<h2> 2. Processor Building</h2>

<p><span>Note: For calling these APIs, you need a local .zip file of DocumentAI API. As these functions are not available in GA/Preview , there is no git repository for these.</span><span>&nbsp;</span></p>
      <p><span></span></p>
      <h3 ><span>Train Processor Version</span></h3>
      <p><span>Function</span><span>&nbsp;</span><span>trainProcessorVersionAsync(TrainProcessorVersionRequest request)</span></p>
      <p><span></span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;TrainProcessorVersionResponse, TrainProcessorVersionMetadata&gt;<br> &nbsp; &nbsp; &nbsp;</span><span>trainProcessorVersionAsync</span><span>(TrainProcessorVersionRequest request)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Trains a new processor version. Operation metadata is returned as &nbsp;cloud_documentai_core.TrainProcessorVersionMetadata</span></p>
      <p><span>Sample Implementation</span></p>
<table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; &nbsp;DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; &nbsp;TrainProcessorVersionRequest request =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;TrainProcessorVersionRequest.newBuilder()<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setParent(ProcessorName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>).toString())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setProcessorVersion(ProcessorVersion.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setSchema(Schema.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setDocumentSchema(DocumentSchema.newBuilder().build()) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setInputData(TrainProcessorVersionRequestTrainProcessorVersionRequest.InputData.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setEvaluationOutput(DocumentOutputConfig.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setBaseProcessorVersion(</span><span>&quot;baseProcessorVersion337709271&quot;</span><span>)<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.build();<br> &nbsp; &nbsp; &nbsp;TrainProcessorVersionResponse response =<br> &nbsp; &nbsp; &nbsp; &nbsp; documentProcessorServiceClient.trainProcessorVersionAsync(request).get();<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span>Parameters</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>TrainProcessorVersionRequest</span></p>
               <p><span>The request object containing all of the parameters for the API call such as (Schema, Input Dataset, Evaluation configuration etc. )</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>TrainProcessorVersionResponse</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <h3 ><span>Deploy Processor Version</span></h3>
      <p><span>Function</span><span>&nbsp;</span><span>deployProcessorVersionAsync</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;DeployProcessorVersionResponse, DeployProcessorVersionMetadata&gt;<br> &nbsp; &nbsp; &nbsp;</span><span>deployProcessorVersionAsync</span><span>(ProcessorVersionName name)</span></p>
            </td>
         </tr>
      </table>
      <p><span>Deploys the processor version</span></p>
      <p><span></span></p>
      <p><span>Sample Implementation</span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; &nbsp;DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; &nbsp;ProcessorVersionName name =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ProcessorVersionName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>, </span><span>&quot;[PROCESSOR_VERSION]&quot;</span><span>);<br> &nbsp; &nbsp; &nbsp;DeployProcessorVersionResponse response =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;documentProcessorServiceClient.deployProcessorVersionAsync(name).get();<br> &nbsp; }</span></p>
            </td>
         </tr>
      </table>
      <p><span>Parameters</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>ProcessorVersionName</span></p>
               <p><span>The request object containing all of the parameters for the API call such as (Project ID, Location, ProcessorID, ProccessorVersionID)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>DeployProcessorVersionResponse</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <h3><span>Undeploy Processor Version</span></h3>
      <p><span>Function </span><span>undeployProcessorVersionAsync</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;UndeployProcessorVersionResponse, UndeployProcessorVersionMetadata&gt;<br> &nbsp; &nbsp; &nbsp;</span><span>undeployProcessorVersionAsync</span><span>(ProcessorVersionName name)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Undeploys the processor version</span></p>
      <p><span></span></p>
      <p><span>Sample Implementation</span></p>
       <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; &nbsp;DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; &nbsp;ProcessorVersionName name =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ProcessorVersionName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>, </span><span>&quot;[PROCESSOR_VERSION]&quot;</span><span>);<br> &nbsp; &nbsp; &nbsp;UndeployProcessorVersionResponse response =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;documentProcessorServiceClient.undeployProcessorVersionAsync(name).get();<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Parameters</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>ProcessorVersionName</span></p>
               <p><span>The request object containing all of the parameters for the API call (i.e. ProjectID, Location, ProcessorID, ProcessorVersionID)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>UndeployProcessorVersionResponse</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <h3 ><span>Evaluate Processor</span></h3>
      <p><span>Function</span><span>&nbsp;</span><span>evaluateProcessorVersionAsync(EvaluateProcessorVersionRequest request)</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;EvaluateProcessorVersionResponse, EvaluateProcessorVersionMetadata&gt;<br> &nbsp; &nbsp; &nbsp;</span><span>evaluateProcessorVersionAsync</span><span>(EvaluateProcessorVersionRequest request)</span></p>
            </td>
         </tr>
      </table>
      <p><span>Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.</span></p>
      <p><span>Sample Implementation</span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; EvaluateProcessorVersionRequest request =<br> &nbsp; &nbsp; &nbsp; &nbsp; EvaluateProcessorVersionRequest.newBuilder()<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setProcessorVersion(<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ProcessorVersionName.of(<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>, </span><span>&quot;[PROCESSOR_VERSION]&quot;</span><span>)<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.toString())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setEvaluationDocuments(BatchDocumentsInputConfig.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.setEvaluationOutput(DocumentOutputConfig.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;.build();<br> &nbsp; &nbsp; &nbsp;EvaluateProcessorVersionResponse response =<br> &nbsp; &nbsp; &nbsp; &nbsp; documentProcessorServiceClient.evaluateProcessorVersionAsync(request).get();<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span>Parameters</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>EvaluateProcessorVersionRequest</span></p>
               <p><span>The request object containing all of the parameters for the API call. (ProjectID, Location, ProcessorID, ProcessorVersionID)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>EvaluateProcessorVersionResponse</span></p>
               <p><span></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <p><span></span></p>
      <h3 ><span>Get Processor</span></h3>
      <p><span>Function </span><span>getProcessorVersion(name)</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;ProcessorVersion </span><span>getProcessorVersion</span><span>(ProcessorVersionName name)</span><span>&nbsp;</span></p>
            </td>
         </tr>
      </table>
      <p><span>Gets a processor version detail.</span></p>
      <p><span>Sample Implementation</span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; &nbsp;DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; &nbsp;ProcessorVersionName name =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ProcessorVersionName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>, </span><span>&quot;[PROCESSOR_VERSION]&quot;</span><span>);<br> &nbsp; &nbsp; &nbsp;ProcessorVersion response = documentProcessorServiceClient.getProcessorVersion(name);<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span>Parameters</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>ProcessorVersionName</span></p>
               <p><span>The processor resource name. (ProjectID, Location, ProcessorID, ProcessorVersionID)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns </span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>ProcessorVersion</span></p>
               <p><span></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Contain all the details about a processor Version. </span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <h3 <span>Get Evaluation</span></h3>
      <p><span>Function </span><span>getEvaluation(name)</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;Evaluation </span><span>getEvaluation</span><span>(EvaluationName name)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Sample Implementation &nbsp; </span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; EvaluationName name =<br> &nbsp; &nbsp; &nbsp; &nbsp; EvaluationName.of(<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>, </span><span>&quot;[PROCESSOR_VERSION]&quot;</span><span>, </span><span>&quot;[EVALUATION]&quot;</span><span>);<br> &nbsp; &nbsp; Evaluation response = documentProcessorServiceClient.getEvaluation(name);<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Parameters</span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>EvaluationName</span></p>
               <p><span>The resource name of the &nbsp; &nbsp;"google.cloud.documentai.uiv1beta3.Evaluation"&nbsp; &nbsp;</span><span>projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}/evaluations/{evaluation}</span></p>
               <p><span>Note: You can evaluationID from the getProcessor(name) method. </span></p>
            </td>
         </tr>
      </table>
      <p><span>Returns </span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Evaluation</span></p>
               <p><span></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Contains Evaluation metrics of the corresponding evaluationID</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <h3 ><span>Get List of Evaluations</span></h3>
      <p><span>Function </span><span>listEvaluations(String parent)</span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;ListEvaluationsPagedResponse </span><span>listEvaluations</span><span>(String parent)</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Sample Implementation</span></p>
    <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; &nbsp; String parent =<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ProcessorVersionName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>, </span><span>&quot;[PROCESSOR_VERSION]&quot;</span><span>)<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .toString();<br> &nbsp; &nbsp; &nbsp;</span><span>for</span><span>&nbsp;(Evaluation element : documentProcessorServiceClient.listEvaluations(parent).iterateAll()) {<br> &nbsp; &nbsp; &nbsp; &nbsp;</span><span>// doThingsWith(element);</span><span><br> &nbsp; &nbsp; &nbsp;}<br> &nbsp; &nbsp;}</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Parameters </span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>parent</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>parent</span></p>
               <p><span>"google.cloud.documentai.uiv1beta3.ProcessorVersion" to list evaluations for &nbsp; &nbsp; </span><span>projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}</span></p>
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
    <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>ListEvaluationsPagedResponse</span></p>
               <p><span></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Iterator with list of Evaluations</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
<div style="padding-bottom:30px"></div>
<h2> 3. Processing Documents</h2>
<h3 ><span>Process Single Document</span></h3>
      <p><span>Function </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_processDocument_com_google_cloud_documentai_v1beta3_ProcessRequest_&amp;sa=D&amp;source=editors&amp;ust=1704207105538146&amp;usg=AOvVaw23dBDZ48Z9w3XdFmc-gn7Q">processDocument(ProcessRequest request)</a></span></p>
      <p><span></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black; font-weight:700;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;ProcessResponse </span><span>processDocument</span><span>(ProcessRequest request)</span></p>
            </td>
         </tr>
      </table>
      <p><span>Processes a single document</span></p>
      <p><span>Sample Implementation</span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>// This snippet has been automatically generated for illustrative purposes only.</span><span><br> </span><span>// It may require modifications to work in your environment.</span><span><br> </span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; ProcessRequest request =<br> &nbsp; &nbsp; &nbsp; ProcessRequest.newBuilder()<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setName(ProcessorName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>).toString())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setDocument(Document.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setSkipHumanReview(</span><span>true</span><span>)<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .build();<br> &nbsp; ProcessResponse response = documentProcessorServiceClient.processDocument(request);<br> }</span></p>
            </td>
         </tr>
      </table>
      <p><span>Parameters</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ProcessRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105540116&amp;usg=AOvVaw0lUue2ZyUcaQLlCupRArwM">ProcessRequest</a></span></p>
               <p><span>The request object containing all of the parameters for the API call.</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
      <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ProcessResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105541052&amp;usg=AOvVaw2VP6vWjk9fyMONE6sR47oB">ProcessResponse</a></span></p>
               <p><span></span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span></span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <p><span></span></p>
      <h3 ><span>Batch Process Document </span></h3>
      <p><span>Function</span><span>&nbsp;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient%23com_google_cloud_documentai_v1beta3_DocumentProcessorServiceClient_batchProcessDocumentsAsync_com_google_cloud_documentai_v1beta3_BatchProcessRequest_&amp;sa=D&amp;source=editors&amp;ust=1704207105541898&amp;usg=AOvVaw0FrT2jBoz1Doh0rjq8PeeA">batchProcessDocumentsAsync(BatchProcessRequest request)</a></span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>public</span><span>&nbsp;</span><span>final</span><span>&nbsp;OperationFuture&lt;BatchProcessResponse,BatchProcessMetadata&gt; </span><span>batchProcessDocumentsAsync</span><span>(BatchProcessRequest request)</span></p>
            </td>
         </tr>
      </table>
      <p><span>LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.</span></p>
      <p><span>Sample Implementation</span></p>
     <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>&nbsp;</span><span>// This snippet has been automatically generated for illustrative purposes only.</span><span><br> </span><span>// It may require modifications to work in your environment.</span><span><br> </span><span>try</span><span>&nbsp;(DocumentProcessorServiceClient documentProcessorServiceClient =<br> &nbsp; &nbsp; DocumentProcessorServiceClient.create()) {<br> &nbsp; BatchProcessRequest request =<br> &nbsp; &nbsp; &nbsp; BatchProcessRequest.newBuilder()<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setName(ProcessorName.of(</span><span>&quot;[PROJECT]&quot;</span><span>, </span><span>&quot;[LOCATION]&quot;</span><span>, </span><span>&quot;[PROCESSOR]&quot;</span><span>).toString())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .addAllInputConfigs(</span><span>new</span><span>&nbsp;ArrayList&lt;BatchProcessRequest.BatchInputConfig&gt;())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setOutputConfig(BatchProcessRequest.BatchOutputConfig.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setInputDocuments(BatchDocumentsInputConfig.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setDocumentOutputConfig(DocumentOutputConfig.newBuilder().build())<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .setSkipHumanReview(</span><span>true</span><span>)<br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .build();<br> &nbsp; BatchProcessResponse response =<br> &nbsp; &nbsp; &nbsp; documentProcessorServiceClient.batchProcessDocumentsAsync(request).get();<br> }</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span></span></p>
      <p><span>Parameters</span></p>
      <p><span></span></p>
    <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Name</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>request</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.BatchProcessRequest&amp;sa=D&amp;source=editors&amp;ust=1704207105543762&amp;usg=AOvVaw0nau0KvRCrTsyndF_oVOAO">BatchProcessRequest</a></span></p>
               <p><span>The request object containing all of the parameters for the API call.</span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Returns</span></p>
      <p><span></span></p>
    <table style="border: 1px solid black;padding:0px; margin:0px">
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Type</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span>Description</span></p>
            </td>
         </tr>
         <tr style="border: 1px solid black;">
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html&amp;sa=D&amp;source=editors&amp;ust=1704207105544708&amp;usg=AOvVaw0IPLYGLlYjhlDihgtNMA4N">OperationFuture</a></span><span>&lt;</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.BatchProcessResponse&amp;sa=D&amp;source=editors&amp;ust=1704207105544849&amp;usg=AOvVaw25rdisxhcnGpjuTMzYtqAL">BatchProcessResponse</a></span><span>,</span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.BatchProcessMetadata&amp;sa=D&amp;source=editors&amp;ust=1704207105544986&amp;usg=AOvVaw2_i72IZRuA-SxFPk5OcVTA">BatchProcessMetadata</a></span><span>&gt;</span></p>
            </td>
            <td  style="border: 1px solid black;" colspan="1" rowspan="1">
               <p><span></span></p>
            </td>
         </tr>
      </table>
      <p><span></span></p>
      <p><span>Exceptions</span></p>
      <p><span></span></p>
      <p><span>throws</span><span>&nbsp;com.google.api.gax.rpc.ApiException</span><span>&nbsp;if the remote call fails</span></p>
      <hr style="page-break-before:always;display:none;">
<div style="padding-bottom:30px"></div>
<h2> 4. Example Java Files</h2>
<p><span>These examples are intended to give a holistic idea on how to implement and use the functions available in DocumentProcessorServiceClient. </span></p>
      <h3 ><span>Prerequisites</span><span>&nbsp;</span></h3>
      <ul >
         <li ><span>Create a Java Project and add all the Dependencies as mentioned in </span>Quickstart</li>
         <li><span>Having a Google Cloud Project , with all the required APIs Enabled &amp; Granted Permissions [Quickstart]</span></li>
         <li><span>For Batch Processing Documents, Please add </span><span><a href="https://www.google.com/url?q=https://github.com/googleapis/java-storage%23quickstart&amp;sa=D&amp;source=editors&amp;ust=1704207105546282&amp;usg=AOvVaw0QW1RhLdVO2WAD_mkijUAe">Google Cloud Storage</a></span><span>&nbsp;Dependencies in your Java Project </span></li>
      </ul>
      <ul >
         <li ><span>For QuickStart.java, Create a class with name </span><span>QuickStart</span><span>&nbsp;and copy the given code.</span></li>
         <li ><span>For BatchProcessDocument.java , Create a class with name </span><span>Batch Process Document</span><span>&nbsp;and</span><span>&nbsp;</span><span>copy the given program</span></li>
      </ul>
      <h3><span>QuickStart.java</span></h3>
      <p><span>The QuickStart.java file describes the function call of the above mentioned methods. For more info follow </span><span><a href="https://www.google.com/url?q=https://cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient&amp;sa=D&amp;source=editors&amp;ust=1704207105546838&amp;usg=AOvVaw1XdnlM6_EyCCWAehYoIEAd">DocumentProcessorServiceClient</a></span><span>&nbsp;</span><span>class and the </span><span><a href="https://www.google.com/url?q=https://github.com/googleapis/java-document-ai/tree/76fa19e5f8eb2b8e563bcc72139b5b33350232a5&amp;sa=D&amp;source=editors&amp;ust=1704207105546969&amp;usg=AOvVaw1LDWRaxkWpoTIw1QNGdw2o">Github Repo</a></span><span>&nbsp;</span></p>
<div style="padding-bottom:30px"></div>
<div style="padding-bottom:30px"></div>
package com.google.cloud.documentai.uiv1beta3;

import com.google.api.client.util.Strings;
import com.google.api.gax.longrunning.OperationFuture;
import com.google.cloud.documentai.uiv1beta3.DocumentOutputConfig.GcsOutputConfig;
import com.google.cloud.documentai.uiv1beta3.Schema.EntityType;
import com.google.cloud.documentai.uiv1beta3.Schema.EntityType.OccurrenceType;
import com.google.cloud.documentai.uiv1beta3.TrainProcessorVersionRequest.InputData;
import com.google.protobuf.ByteString;
import com.google.protobuf.Empty;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

//import com.google.cloud.documentai.v1beta3.Processor;
public class QuickStart {

  public static void main(String[] args)
      throws IOException, InterruptedException, ExecutionException, TimeoutException {
    // TODO(developer): Replace these variables before running the sample.
    String projectId = "xxxxxxxxxxxxx"; // ProjectID
    String location = "us"; // Format is "us" or "eu".
    String processorType = "CUSTOM_DOCUMENT_EXTRACTOR"; // Mention the Processor Type Name , e.g. INVOICE_PARSER etc.
    String displayName = ""; // Mention the displayName
    // createProcessor(projectId, location, processorType, displayName); // Creates a new Processor and prints the processor metadata
    String processorId = "xxxxxxxxxxx"; // If you already have the processor, Or Else first Create the processor amd then Write the ProcessorID
    String processorVersionID = "xxxxxxxxxxxxx";
    // String filePath = "FILE PATH";// For Parsing Single pdf Document, give local file path. [Uncomment while calling processDocument()]
    // deleteProcessor(projectId, location, processorId);// Deletes the Processor
    // listProcessors(projectId, location); // List all the processor in the Project
    // disableProcessor(projectId, location, processorId); // Disable the processor
    // enableProcessor(projectId, location, processorId); // Enable the processor
    // processDocument(projectId, location, processorId, filePath); // Process Single Document
    // fetchProcessorType(projectId, location); // Fetch all the available ProcessorType Available
    // train(projectId, location, processorId); // Train a new processor
    // eval(projectId, location, processorId, processorVersionID); // Evaluates the processor Version
    // undeployProcessor(projectId,location,processorId,processorVersionID); // Undeploy the processor Version
    // deployProcessor(projectId,location,processorId,processorVersionID); // Deploy the processor Version
    // ProcessorVersion processorVersion=getProcessor(projectId,location,processorId,processorVersionID); // Get the details of the processor Version
    // System.out.println("--------------------------------");
    // String evaluation =processorVersion.getLatestEvaluation().getEvaluation();
    // String [] evaluationPath=evaluation.split("/");
    // getEvaluation(projectId,location,processorId,processorVersionID,evaluationPath[evaluationPath.length-1]); // Get the details of evaluation.
    // getEvaluations(projectId,location,processorId,processorVersionID); // Get EvaluationList
    // getEvaluationDocumentList(projectId,location,processorId,processorVersionID,evaluationPath[evaluationPath.length-1]); //Retrieves the documents that were evaluated.
    // getEvaluationDocument(projectId,location,processorId,processorVersionID,evaluationPath[evaluationPath.length-1]); // Retrieves a specific document that was evaluated.
    // evaluateProcessorVersion(projectId,location,processorId,processorVersionID); // Evaluate a Processor version with documents in gs:// bucket
  }

  public static void createProcessor(String projectId, String location, String processorType,
      String displayName) throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      String parent = LocationName.of(projectId, location).toString();
      Processor processor = Processor.newBuilder().setType(processorType)
          .setDisplayName(displayName).build();
      Processor response = documentProcessorServiceClient.createProcessor(parent, processor);
      System.out.println(response);

    }

  }

  public static void deleteProcessor(String projectId, String location, String processorId)
      throws IOException, ExecutionException, InterruptedException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      DeleteProcessorRequest request =
          DeleteProcessorRequest.newBuilder()
              .setName(ProcessorName.of(projectId, location, processorId).toString())
              .build();
      OperationFuture<Empty, DeleteProcessorMetadata> future =
          documentProcessorServiceClient.deleteProcessorOperationCallable()
              .futureCall(request);
      // Do something.
      System.out.println(future.get());
    }
  }

  public static void fetchProcessorType(String projectID, String location) throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      FetchProcessorTypesRequest request =
          FetchProcessorTypesRequest.newBuilder()
              .setParent(LocationName.of(projectID, location).toString())
              .build();
      FetchProcessorTypesResponse response =
          documentProcessorServiceClient.fetchProcessorTypes(request);
      System.out.println(response);
    }
  }

  public static void listProcessors(String projectID, String location) throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      String parent = LocationName.of(projectID, location).toString();
      for (Processor element : documentProcessorServiceClient.listProcessors(parent)
          .iterateAll()) {
        // doThingsWith(element);
        System.out.println(element.getDisplayName());
      }
    }
  }

  public static void enableProcessor(String projectID, String location, String processorID)
      throws IOException, ExecutionException, InterruptedException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      EnableProcessorRequest request =
          EnableProcessorRequest.newBuilder()
              .setName(ProcessorName.of(projectID, location, processorID).toString())
              .build();
      EnableProcessorResponse response =
          documentProcessorServiceClient.enableProcessorAsync(request).get();
      System.out.println(response);
    }

  }

  public static void disableProcessor(String projectID, String location, String processorID)
      throws IOException, ExecutionException, InterruptedException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {

      DisableProcessorRequest request =
          DisableProcessorRequest.newBuilder()
              .setName(ProcessorName.of(projectID, location, processorID).toString())
              .build();
      DisableProcessorResponse response =
          documentProcessorServiceClient.disableProcessorAsync(request).get();
      System.out.println(response);
    }
  }

  public static void processDocument(
      String projectId, String location, String processorId, String filePath)
      throws IOException, InterruptedException, ExecutionException, TimeoutException {
    // Initialize client that is be used to send requests. This client only needs to be created
    // once, and can be reused for multiple requests. After completing all of your requests, call
    // the "close" method on the client to safely clean up any remaining background resources.
    try (DocumentProcessorServiceClient client = DocumentProcessorServiceClient.create()) {
      // The full resource name of the processor, e.g.:
      // projects/project-id/locations/location/processor/processor-id
      // You must create new processors in the Cloud Console first
      String name =
          String.format("projects/%s/locations/%s/processors/%s", projectId, location,
              processorId);

      // Read the file.
      byte[] imageFileData = Files.readAllBytes(Paths.get(filePath));

      // Convert the image data to a Buffer and base64 encode it.
      ByteString content = ByteString.copyFrom(imageFileData);

      RawDocument document =
          RawDocument.newBuilder().setContent(content).setMimeType("application/pdf").build();

      // Configure the process request.
      ProcessRequest request =
          ProcessRequest.newBuilder().setName(name).setRawDocument(document).build();

      // Recognizes text entities in the PDF document
      ProcessResponse result = client.processDocument(request);
      Document documentResponse = result.getDocument();

      // Get all of the document text as one big string
      String text = documentResponse.getText();

      // Read the text recognition output from the processor
      System.out.println("The document contains the following paragraphs:");
      Document.Page firstPage = documentResponse.getPages(0);
      List<Document.Page.Paragraph> paragraphs = firstPage.getParagraphsList();

      for (Document.Page.Paragraph paragraph : paragraphs) {
        String paragraphText = getText(paragraph.getLayout().getTextAnchor(), text);
        System.out.printf("Paragraph text:\n%s\n", paragraphText);
      }

      // Form parsing provides additional output about
      // form-formatted PDFs. You  must create a form
      // processor in the Cloud Console to see full field details.
      System.out.println("The following form key/value pairs were detected:");

      for (Document.Page.FormField field : firstPage.getFormFieldsList()) {
        String fieldName = getText(field.getFieldName().getTextAnchor(), text);
        String fieldValue = getText(field.getFieldValue().getTextAnchor(), text);

        System.out.println("Extracted form fields pair:");
        System.out.printf("\t(%s, %s))\n", fieldName, fieldValue);
      }
    }
  }

  public static void train(String projectID, String location, String processorID)
      throws IOException, ExecutionException, InterruptedException {
    // If you are using UI for labeling then use this Try - Catch Block.
    try (DocumentProcessorServiceClient documentProcessorServiceClient = DocumentProcessorServiceClient.create()) {
        ProcessorName parent = ProcessorName.of(projectID, location, processorID);
        ProcessorVersion processorVersion = ProcessorVersion.newBuilder()
            .setDisplayName("java_sdk_test").build();

        TrainProcessorVersionResponse response =
            documentProcessorServiceClient.trainProcessorVersionAsync(parent, processorVersion)
                .get();
        // System.out.println(response);
    }


    // If you are using CrowdCompute for Labeling or you have json files from train/test then use following code.
    // ArrayList<EntityType> entityList = new ArrayList<>();
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("invoice_id").
    //         setBaseType("string").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("receiver_name").
    //         setBaseType("string").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("supplier_name").
    //         setBaseType("string").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("invoice_date").
    //         setBaseType("datetime").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("total_amount").
    //         setBaseType("money").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("line_item/amount").
    //         setBaseType("money").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_MULTIPLE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("line_item/description").
    //         setBaseType("string").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_MULTIPLE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("supplier_address").
    //         setBaseType("address").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // entityList.add(
    //     EntityType.newBuilder().
    //         setType("receiver_address").
    //         setBaseType("address").
    //         setOccurrenceType(OccurrenceType.OPTIONAL_ONCE).
    //         build());
    // Schema schema = Schema.newBuilder().setDescription("test invoice schema desc")
    //     .setDisplayName("test invoice schema").addAllEntityTypes(entityList).build();
    // InputData inputData = InputData.newBuilder().setTrainingDocuments(
    //         BatchDocumentsInputConfig.newBuilder().setGcsPrefix(GcsPrefix.newBuilder()
    //                 .setGcsUriPrefix(
    //                     "gs://xxxxxxxx/xxxxxxxx/xxxxxxx/").build())
    //             .build())
    //     .setTestDocuments(
    //         BatchDocumentsInputConfig.newBuilder().setGcsPrefix(GcsPrefix.newBuilder()
    //             .setGcsUriPrefix(
    //                 "gs://xxxxxxx/xxxxxxxxxx/xxxxxxxx/").build()
    //         ).build()).build();
    // // Map<String, Integer> m1=new Map.of("abc",1,"def",2);
    //
    // // DocumentSchema docSchema= DocumentSchema.newBuilder().build()
    // try (DocumentProcessorServiceClient documentProcessorServiceClient =
    //     DocumentProcessorServiceClient.create()) {
    //   ProcessorVersion processorVersion = ProcessorVersion.newBuilder()
    //       .setDisplayName("java_sdk_training_test_v2").build();
    //   TrainProcessorVersionRequest request =
    //       TrainProcessorVersionRequest.newBuilder()
    //           .setParent(ProcessorName.of(projectID, location, processorID).toString())
    //           .setProcessorVersion(processorVersion)
    //           .setInputData(inputData)
    //           .setSchema(schema)
    //           .build();
    //   TrainProcessorVersionResponse response =
    //       documentProcessorServiceClient.trainProcessorVersionAsync(request).get();
    //   System.out.println(response);
    // }
  }

  /
  public static void eval(String projectID, String location, String processorID,
      String processorVersionID) throws ExecutionException, InterruptedException, IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      String processorVersion =
          ProcessorVersionName.of(projectID, location, processorID, processorVersionID)
              .toString();
      // System.out.println(processorVersion);
      EvaluateProcessorVersionResponse response =
          documentProcessorServiceClient.evaluateProcessorVersionAsync(processorVersion)
              .get();
      System.out.println(response);
    }
  }

  public static void deployProcessor(String projectID, String location, String processorID,
      String processorVersionID)
      throws ExecutionException, InterruptedException, IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      ProcessorVersionName name =
          ProcessorVersionName.of(projectID, location, processorID,
              processorVersionID);
      DeployProcessorVersionResponse response =
          documentProcessorServiceClient.deployProcessorVersionAsync(name).get();
    }
  }

  public static void undeployProcessor(String projectID, String location, String processorID,
      String processorVersionID)
      throws ExecutionException, InterruptedException, IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      ProcessorVersionName name =
          ProcessorVersionName.of(projectID, location, processorID, processorVersionID);
      UndeployProcessorVersionResponse response =
          documentProcessorServiceClient.undeployProcessorVersionAsync(name).get();
    }
  }

  public static ProcessorVersion getProcessor(String projectID, String location, String processorID,
      String processorVersionID)
      throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      ProcessorVersionName name =
          ProcessorVersionName.of(projectID, location, processorID, processorVersionID);
      ProcessorVersion response = documentProcessorServiceClient.getProcessorVersion(name);
      // System.out.println(response);
      // Schema s=response.getSchema();

      return response;
    }

  }

  public static void getEvaluation(String projectID, String location, String processorID,
      String processorVersionID, String evaluation)
      throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      EvaluationName name =
          EvaluationName.of(
              projectID, location, processorID, processorVersionID, evaluation.toString());
      Evaluation response = documentProcessorServiceClient.getEvaluation(name);
      System.out.println(response.getEntityMetricsMap());
    }
  }

  public static void getEvaluations(String projectID, String location, String processorID,
      String processorVersionID)
      throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      ProcessorVersionName parent =
          ProcessorVersionName.of(projectID, location, processorID, processorVersionID);
      for (Evaluation element :
          documentProcessorServiceClient.listEvaluations(parent).iterateAll()) {
        // doThingsWith(element);
        System.out.println(element.getEntityMetricsMap());
      }
    }
  }

  public static void getEvaluationDocumentList(String projectID, String location,
      String processorID, String processorVersionID, String evaluationID) throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      SearchEvaluationDocumentsRequest request =
          SearchEvaluationDocumentsRequest.newBuilder()
              .setEvaluation(
                  EvaluationName.of(
                          projectID,
                          location,
                          processorID,
                          processorVersionID,
                          evaluationID)
                      .toString())
              .build();
      while (true) {
        SearchEvaluationDocumentsResponse response =
            documentProcessorServiceClient.searchEvaluationDocumentsCallable().call(request);
        for (EvaluationDocument element : response.getEvaluationDocumentsList()) {
          // doThingsWith(element);
          System.out.println(element.getName());
        }
        String nextPageToken = response.getNextPageToken();
        if (!Strings.isNullOrEmpty(nextPageToken)) {
          request = request.toBuilder().setPageToken(nextPageToken).build();
        } else {
          break;
        }
      }
    }
  }

  public static void getEvaluationDocument(String projectID, String location, String processorID,
      String processorVersionID, String evaluation, String documents)
      throws IOException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      GetEvaluationDocumentRequest request =
          GetEvaluationDocumentRequest.newBuilder()
              .setName(
                  EvaluationDocumentName.of(
                          projectID,
                          location,
                          processorID,
                          processorVersionID,
                          evaluation,
                          documents)
                      .toString())
              .build();
      EvaluationDocument response = documentProcessorServiceClient.getEvaluationDocument(request);
      System.out.println(response);
    }
  }

  public static void evaluateProcessorVersion(String projectID, String location, String processorID,
      String processorVersionID)
      throws IOException, ExecutionException, InterruptedException {
    try (DocumentProcessorServiceClient documentProcessorServiceClient =
        DocumentProcessorServiceClient.create()) {
      EvaluateProcessorVersionRequest request =
          EvaluateProcessorVersionRequest.newBuilder()
              .setProcessorVersion(
                  ProcessorVersionName.of(
                          projectID, location, processorID, processorVersionID)
                      .toString())
              .setEvaluationDocuments(BatchDocumentsInputConfig.newBuilder().setGcsPrefix(
                  GcsPrefix.newBuilder().setGcsUriPrefix(
                          "gs://xxxx/xxxxx/")
                      .build()
              ).build())
              .setEvaluationOutput(DocumentOutputConfig.newBuilder().setGcsOutputConfig(
                  GcsOutputConfig.newBuilder().setGcsUri(
                          "gs://xxxxxxx/xxxxxxxxxx/xxxxxx/")
                      .build()))
              .build();
      EvaluateProcessorVersionResponse response =
          documentProcessorServiceClient.evaluateProcessorVersionAsync(request).get();
      System.out.println(response);
    }
  }

  // Extract shards from the text field
  private static String getText(Document.TextAnchor textAnchor, String text) {
    if (textAnchor.getTextSegmentsList().size() > 0) {
      int startIdx = (int) textAnchor.getTextSegments(0).getStartIndex();
      int endIdx = (int) textAnchor.getTextSegments(0).getEndIndex();
      return text.substring(startIdx, endIdx);
    }
    return "[NO TEXT]";
  }
}
<div style="padding-bottom:30px"></div>


BatchProcessDocument.java
This file describes the implementation of processing a batch of documents available in the GCS bucket and saves the output to the GCS location.
/*
* Copyright 2020 Google LLC
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/



// [START documentai_batch_process_document]

import com.google.api.HttpBody;
import com.google.api.gax.longrunning.OperationFuture;
import com.google.api.gax.paging.Page;
import com.google.cloud.documentai.v1.*;
import com.google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig;
import com.google.cloud.storage.Blob;
import com.google.cloud.storage.BlobId;
import com.google.cloud.storage.Bucket;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;
import com.google.protobuf.util.JsonFormat;
import com.sun.net.httpserver.HttpsParameters;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class BatchProcessDocument {
    public static void main(String []args){
        try{
            batchProcessDocument();
        } catch (Exception e){
            e.printStackTrace();
        }
    }
    public static void batchProcessDocument()
            throws IOException, InterruptedException, TimeoutException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
                
        String projectId = "PROJECT ID";
        
        String location = "us"; // Format is "us" or "eu".
                
        String processorId = "PROCESSOR ID";
                
        String outputGcsBucketName = "OUTPUT GCS BUCKET PATH"; // e.g. "bucket_name/"
                
        String outputGcsPrefix = "OUTPUT GCS PREFIX"; // e.g. "output_v1"
                
        String inputGcsUri = "INPUT GCS URI"; // e.g. "gs://bucket_name/document_folder_name/"
                
        batchProcessDocument(
                projectId, location, processorId, inputGcsUri, outputGcsBucketName, outputGcsPrefix);
    }

    public static void batchProcessDocument(
            String projectId,
            String location,
            String processorId,
            String gcsInputUri,
            String gcsOutputBucketName,
            String gcsOutputUriPrefix)
            throws IOException, InterruptedException, TimeoutException, ExecutionException {
        // Initialize client that is used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
                
                
        try (DocumentProcessorServiceClient client = DocumentProcessorServiceClient.create()) {
            // The full resource name of the processor, e.g.:
            // projects/project-id/locations/location/processor/processor-id
            // You must create new processors in the Cloud Console first
            String name =
                    String.format("projects/%s/locations/%s/processors/%s", projectId, location, processorId);

            GcsPrefix gcsInputUri_v2=GcsPrefix.newBuilder().setGcsUriPrefix(gcsInputUri).build();
//            System.out.println(gcsInputUri_v2);
            BatchDocumentsInputConfig inputConfig =
                    BatchDocumentsInputConfig.newBuilder().setGcsPrefix(gcsInputUri_v2).build();

            String fullGcsPath = String.format("gs://%s/%s/", gcsOutputBucketName, gcsOutputUriPrefix);
            GcsOutputConfig gcsOutputConfig = GcsOutputConfig.newBuilder().setGcsUri(fullGcsPath).build();
//            System.out.println(fullGcsPath);
            DocumentOutputConfig documentOutputConfig =
                    DocumentOutputConfig.newBuilder().setGcsOutputConfig(gcsOutputConfig).build();

            // Configure the batch process request.
            BatchProcessRequest request =
                    BatchProcessRequest.newBuilder()
                            .setName(name)
                            .setInputDocuments(inputConfig)
                            .setDocumentOutputConfig(documentOutputConfig)
                            .build();

            OperationFuture<BatchProcessResponse, BatchProcessMetadata> future =
                    client.batchProcessDocumentsAsync(request);

            // Batch process document using a long-running operation.
            // You can wait for now, or get results later.
            // Note: first request to the service takes longer than subsequent
            // requests.
            System.out.println("Waiting for operation to complete...");
            System.out.println(future.getName());
            future.get(240, TimeUnit.SECONDS);

            System.out.println("Document processing complete.");

            Storage storage = StorageOptions.newBuilder().setProjectId(projectId).build().getService();
            Bucket bucket = storage.get(gcsOutputBucketName);

            // List all of the files in the Storage bucket.
            Page<Blob> blobs = bucket.list(Storage.BlobListOption.prefix(gcsOutputUriPrefix + "/"));
            int idx = 0;
            for (Blob blob : blobs.iterateAll()) {
                if (!blob.isDirectory()) {
                    System.out.printf("Fetched file #%d\n", ++idx);
                    // Read the results

                    // Download and store json data in a temp file.
                    File tempFile = File.createTempFile("file", ".json");
                    Blob fileInfo = storage.get(BlobId.of(gcsOutputBucketName, blob.getName()));
                    fileInfo.downloadTo(tempFile.toPath());

                    // Parse json file into Document.
                    FileReader reader = new FileReader(tempFile);
                    Document.Builder builder = Document.newBuilder();
                    JsonFormat.parser().merge(reader, builder);

                    Document document = builder.build();

                    // Get all of the document text as one big string.
                    String text = document.getText();

                    // Read the text recognition output from the processor
                    System.out.println("The document contains the following paragraphs:");
                    Document.Page page1 = document.getPages(0);
                    List<Document.Page.Paragraph> paragraphList = page1.getParagraphsList();
                    for (Document.Page.Paragraph paragraph : paragraphList) {
                        String paragraphText = getText(paragraph.getLayout().getTextAnchor(), text);
                        System.out.printf("Paragraph text:%s\n", paragraphText);
                    }

                    // Form parsing provides additional output about
                    // form-formatted PDFs. You  must create a form
                    // processor in the Cloud Console to see full field details.
                    System.out.println("The following form key/value pairs were detected:");

                    for (Document.Page.FormField field : page1.getFormFieldsList()) {
                        String fieldName = getText(field.getFieldName().getTextAnchor(), text);
                        String fieldValue = getText(field.getFieldValue().getTextAnchor(), text);

                        System.out.println("Extracted form fields pair:");
                        System.out.printf("\t(%s, %s))", fieldName, fieldValue);
                    }

                    // Clean up temp file.
                    tempFile.deleteOnExit();
                }
            }
        }
    }

    // Extract shards from the text field
    private static String getText(Document.TextAnchor textAnchor, String text) {
        if (textAnchor.getTextSegmentsList().size() > 0) {
            int startIdx = (int) textAnchor.getTextSegments(0).getStartIndex();
            int endIdx = (int) textAnchor.getTextSegments(0).getEndIndex();
            return text.substring(startIdx, endIdx);
        }
        return "[NO TEXT]";
    }
}
// [END documentai_batch_process_document]
<div style="padding-bottom:30px"></div>
