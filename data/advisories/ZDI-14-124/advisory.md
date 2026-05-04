# ZDI-14-124: (0Day) Borland Silk Central TeeChart ActiveX Control GridLink Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-124
- **ZDI-CAN:** ZDI-CAN-2000
- **Date:** 2014-05-05
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Borland
- **Affected Products:** Silk Central
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Borland Silk Central. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Borland Silk Central TeeChart ActiveX control. The control suffers from an untrusted pointer dereference vulnerability because it blindly calls an attacker-supplied memory address. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: 2013-09-01: - Case received 2013-06-27 - 2014-02-19: - Multiple attempts to contact Borland (based on the timeline from ZDI-14-123) 2014-05-05: - Public release of advisory -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibilty Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\A92B03A8-D509-4D2F-A953-B26ED8498AB0 If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2013-09-01 - Vulnerability reported to vendor
- 2014-05-05 - Coordinated public release of advisory
