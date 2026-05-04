# ZDI-15-023: Microsoft Internet Explorer CTreePos Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-023
- **ZDI-CAN:** ZDI-CAN-2546
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0041
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CTreePos objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-10-16 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
