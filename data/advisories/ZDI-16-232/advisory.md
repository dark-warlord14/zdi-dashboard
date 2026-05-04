# ZDI-16-232: Microsoft Edge keyframes Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-232
- **ZDI-CAN:** ZDI-CAN-3471
- **Date:** 2016-04-12
- **CVE:** CVE-2016-0157
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** d81b2a7b317c035a8da11d63122964c2
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-232/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes CSS keyframes rules. By manipulating a document's elements an attacker can cause Edge to access memory outside the bounds of an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-038

## Disclosure Timeline

- 2016-01-05 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
