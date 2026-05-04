# ZDI-15-454: (0Day) Samsung XNS ActiveX SDK XnsSdkDevice Multiple Untrusted Pointer Dereference Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-15-454
- **ZDI-CAN:** ZDI-CAN-2533
- **Date:** 2015-10-02
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** XNS ActiveX SDK
- **Credit:** Carlo Di Dato (aka shinnai)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-454/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung XNS ActiveX SDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within multiple methods in the XnsSdkDevice control. The control suffers from untrusted pointer dereference vulnerabilities because it blindly dereferences attacker-supplied memory addresses. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/02/2015 - ZDI sent the case to their known vendor contact 02/04/2015 - The vendor replied that they could not open the encrypted mail 02/05/2015 - ZDI requested the contact re-send their current key 02/05/2015 - The vendor re-sent their PGP key 02/06/2015 - ZDI re-sent the case disclosure with the updated key 02/08/2015 - The contact replied that his key was expired and sent a new one 02/09/2015 - ZDI re-sent the case disclosure 05/22/2015 - ZDI requested an update 09/28/2015 - ZDI requested an update and notified of intent to 0-day -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\9BED9251-E8E7-4B67-B281-ADC06BA7988D If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2015-02-09 - Vulnerability reported to vendor
- 2015-10-02 - Coordinated public release of advisory
