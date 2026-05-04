# ZDI-15-545: Microsoft Internet Explorer ShowSaveFileDialog Protected Mode Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-545
- **ZDI-CAN:** ZDI-CAN-3272
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6051
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-545/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of the CProtectedModeAPI::ShowSaveFileDialog API. An attacker can leverage this API to set the current working directory and allow for DLL planting. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-106

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
