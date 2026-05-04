# ZDI-14-134: (0Day) Novell NetIQ Sentinel Agent Manager NQMcsVarSet DumpToFile Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-134
- **ZDI-CAN:** ZDI-CAN-1946
- **Date:** 2014-05-19
- **CVE:** CVE-2014-3460
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** NetIQ Sentinel Agent Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell NetIQ. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the NQMcsVarSet ActiveX control. The control exposes the DumpToFile method. The method does not properly sanitize the path for the filename, allowing for directory traversal. An attacker can leverage this vulnerability to write files under the context of the current process, which can then be used to execute code under the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: 09/04/2013 - Case disclosed to vendor 03/31/2014 - ZDI sent follow-up to Secure@novell.com , no reply 04/08/2014 - ZDI sent follow-up to Secure@novell.com , no reply 04/16/2014 - ZDI sent follow-up to Secure@novell.com , no reply (apparently an old address) 04/18/2014 - ZDI sent follow-up to security@novell.com (new address), no reply 04/23/2014 - ZDI sent follow-up to security@novell.com 04/24/2014 - Vendor replied and request for a number to call to discuss this 04/24/2014 - ZDI replied with phone number, but received no call in response 05/19/2014 - ZDI publicly disclosed -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibilty Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\B4B7CF9E-AD9E-11D8-AE3B-005056C00008 If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797 Vendor Patch: Vendor has issued an update to correct this vulnerability. More details can be found at: https://www.netiq.com/support/kb/doc.php?id=7015183

## Disclosure Timeline

- 2013-09-04 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
