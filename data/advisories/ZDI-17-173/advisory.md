# ZDI-17-173: Microsoft Edge JavaScript Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-173
- **ZDI-CAN:** ZDI-CAN-4470
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0067
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-173/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JavaScript. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms17-007.aspx

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
