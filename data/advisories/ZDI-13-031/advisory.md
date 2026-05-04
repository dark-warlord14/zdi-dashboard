# ZDI-13-031: Microsoft Internet Explorer CHTML Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-031
- **ZDI-CAN:** ZDI-CAN-1714
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0029
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSelectionManager objects. The issue lies in the usage of the focus() method on a textArea element. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS13-009

## Disclosure Timeline

- 2013-01-08 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
