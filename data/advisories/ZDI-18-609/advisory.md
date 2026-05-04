# ZDI-18-609: Microsoft Edge CWUCLayer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-609
- **ZDI-CAN:** ZDI-CAN-6250
- **Date:** 2018-07-12
- **CVE:** CVE-2018-8274
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** akayn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-609/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the routines that render web pages to the display. By manipulating a document's elements, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8274

## Disclosure Timeline

- 2018-05-24 - Vulnerability reported to vendor
- 2018-07-12 - Coordinated public release of advisory
- 2018-07-12 - Advisory Updated
