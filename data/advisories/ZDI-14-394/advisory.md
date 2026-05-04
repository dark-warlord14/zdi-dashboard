# ZDI-14-394: (0Day) 3S Pocketnet Tech VMS PocketNetNVRMediaClientAxCtrl.NVRMediaViewer.1 SaveCurrentImage Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-394
- **ZDI-CAN:** ZDI-CAN-2406
- **Date:** 2014-12-04
- **CVE:** CVE-2014-9263
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** 3S Pocketnet Tech
- **Affected Products:** VMS
- **Credit:** Carsten Eiram, Risk Based Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-394/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of 3S Pocketnet Tech VMS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the PocketNetNVRMediaClientAxCtrl.NVRMediaViewer.1 control. The SaveCurrentImage method copies an attacker provided filename into a fixed size stack buffer. An attacker could leverage this to execute arbitrary code in the context of the browser.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: 08/13/2014 - ZDI emailed the vendor requesting a contact and PGP key 09/04/2014 - ZDI emailed the vendor requesting a contact and PGP key 10/13/2014 - ZDI emailed the vendor requesting a contact and PGP key 11/05/2014 - ZDI emailed ICS-CERT requesting a contact or guidance 11/21/2014 - ZDI emailed ICS-CERT requesting a contact or guidance -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\3075736A-FC03-452E-B155-721A1C2E9BCE If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2014-08-13 - Vulnerability reported to vendor
- 2014-12-04 - Coordinated public release of advisory
