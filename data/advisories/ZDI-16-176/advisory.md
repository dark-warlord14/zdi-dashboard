# ZDI-16-176: (0Day) SAP 3D Visual Enterprise Viewer SketchUp document Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-176
- **ZDI-CAN:** ZDI-CAN-2975
- **Date:** 2016-02-18
- **CVE:** CVE-2016-2536
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-176/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SketchUp documents. With a specially crafted SketchUp document, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/30/2015 - Disclosed vulnerability reports to vendor 09/28/2015 - The vendor let ZDI know that they would need an extension 09/29/2015 - ZDI agreed to an extension 02/09/2016 - ZDI notified the vendor that these would move to 0-day 02/09/2016 - The vendor replied that: "This issue is related to SketchUp having this vulnerability. SketchUp has refused to provide a patch. Is it still possible to ask for an 'exceptional' extension for us to manage a work-around?" 02/10/2016 - ZDI responded "No further extension can be granted." -- Mitigation: Given the stated purpose of SAP 3D Virtual Enterprise Viewer, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files. -- Vendor Response: On 2/26/2016 SAP notified ZDI of the following available updates: 2281195 <https://service.sap.com/sap/support/notes/2281195> - Potential remote termination of running processes in SAP Visual Enterprise Author, Generator and Viewer An attacker can remotely exploit SAP Visual Enterprise Author, Generator and Viewer version 8.0, which may lead to application termination. Customers are advised to apply Note 2281195 <https://service.sap.com/sap/support/notes/2281195> immediately. We would like to remind our customers to secure SAP systems by installing all available security patches. You can find security notes and patches in the SAP Support Portal here <https://support.sap.com/securitynotes> .

## Disclosure Timeline

- 2015-07-02 - Vulnerability reported to vendor
- 2016-02-18 - Coordinated public release of advisory
