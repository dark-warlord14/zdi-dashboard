# ZDI-12-199: Microsoft Internet Explorer execCommand Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-199
- **ZDI-CAN:** ZDI-CAN-1586
- **Date:** 2012-12-21
- **CVE:** CVE-2012-4969
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 9
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-199/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CCommand::Exec function. It is possible to free certain objects in a callback function called from the CCommand::Exec function. Upon return from this function a local variable is being re-used without check. This can lead to a use-after-free issue that can result in remote code execution under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/advisory/2757760

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
