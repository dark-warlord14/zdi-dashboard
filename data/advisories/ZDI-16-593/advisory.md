# ZDI-16-593: Microsoft Windows JavaScript reverse Method Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-593
- **ZDI-CAN:** ZDI-CAN-4031
- **Date:** 2016-11-08
- **CVE:** CVE-2016-7202
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-593/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the JavaScript Array.reverse method, as implemented in chakra.dll. By performing actions in JavaScript an attacker can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-129

## Disclosure Timeline

- 2016-09-20 - Vulnerability reported to vendor
- 2016-11-08 - Coordinated public release of advisory
