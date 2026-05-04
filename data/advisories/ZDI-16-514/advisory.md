# ZDI-16-514: Microsoft Windows JavaScript map Method Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-514
- **ZDI-CAN:** ZDI-CAN-3932
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3377
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-514/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the JavaScript map function, as implemented in chakra.dll. By performing actions in JavaScript an attacker can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-105

## Disclosure Timeline

- 2016-07-29 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
