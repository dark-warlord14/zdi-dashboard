# ZDI-13-024: Microsoft Windows OLE Automation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-024
- **ZDI-CAN:** ZDI-CAN-1674
- **Date:** 2013-02-14
- **CVE:** CVE-2013-1313
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows XP SP3
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Microsoft Common Controls when handling RTF files. A specially crafted length can result in an integer overflow in a value that gets used as a length in a call to SysAllocStringLen. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS13-020

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
