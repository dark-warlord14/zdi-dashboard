# ZDI-15-248: Microsoft Internet Explorer ShowSaveFileDialog Protected Mode Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-248
- **ZDI-CAN:** ZDI-CAN-2787
- **Date:** 2015-06-11
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-248/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of the CProtectedModeAPI::ShowSaveFileDialog API. An attacker can leverage this API to set the current working directory and allow for DLL planting. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
