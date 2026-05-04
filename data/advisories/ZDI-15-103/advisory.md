# ZDI-15-103: (0Day) Oracle Data Quality LoaderWizard DataPreview Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-103
- **ZDI-CAN:** ZDI-CAN-2499
- **Date:** 2015-03-13
- **CVE:** CVE-2015-0446
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Data Quality
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-103/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Data Quality. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TSS12.LoaderWizard.lwctrl ActiveX control. The DataPreview method does not validate the type of data passed to it, instead treating any object passed in as if it were the expected type. An attacker could leverage this to execute arbitrary code in the context of the browser.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/04/2014 - Disclosed the reports to the vendor 01/13/2015 - Vendor wrote to ZDI indicating that "We have a dependency on a 3rd party vendor for these issues and we are continuing to work with them" 01/14/2015 - ZDI replied granted extension to 3/2/2015 02/23/2015 - ZDI reminded vendor of the pending deadline 02/24/2015 - Vendor's monthly status update to ZDI indicated "Under investigation / Being fixed in main codeline" for these related cases 02/24/2015 - Vendor replied to the email prompt from ZDI that they are looking into it 03/02/2015 - Vendor provided statement below to ZDI 07/15/2015 - Vendor released patch -- Vendor Response: The identified Oracle Data Quality vulnerabilities are due to software code supplied by a third party vendor. Despite Oracle's repeated and ongoing requests, the third party vendor has refused to provide Oracle with fixes for these issues. Oracle has been working on an alternative solution and is ready to offer a migration path to existing Oracle Data Quality customers. Oracle recommends that customers contact Oracle Customer Support for more details. -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\357DB9E3-72A6-41AA-9BA5-4A9D12E57ACD If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797 -- Vendor Patch: http://www.oracle.com/technetwork/topics/security/cpujul2015-2367936.html

## Disclosure Timeline

- 2014-09-04 - Vulnerability reported to vendor
- 2015-03-13 - Coordinated public release of advisory
