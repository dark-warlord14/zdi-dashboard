# ZDI-15-463: (0Day) Samsung SmartViewer STWAxConfigNVR SendCustomPacket Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-463
- **ZDI-CAN:** ZDI-CAN-2711
- **Date:** 2015-10-13
- **CVE:** CVE-2015-8039
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** SmartViewer
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-463/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung SmartViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the STWAxConfigNVR control's SendCustomPacket method. The control contains an untrusted pointer dereference vulnerability. It dereferences an attacker-supplied memory address. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 02/04/2015 - ZDI disclosed vulnerability details to the vendor (ZDI sent to known contacts, but received no initial ACK) 05/14/2015 - ZDI requested any available update from the vendor 09/28/2015 - ZDI sent multiple requests to multiple parties with the vendor requesting any available update 09/29/2015 - The vendor replied they could not decrypt the request 10/02/2015 - ZDI replied without decryption simply asking the status of the report -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\EEDBA32E-5C2D-48f1-A58E-0AAB0BC230E3 If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797 -- Vendor Mitigation: We have resolved below issues as removing DVR setup function of N company. Resolved Version : SmartViewer v4.6.0 (August 2015) ~ v4.9.1 (Current Final Version)

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
