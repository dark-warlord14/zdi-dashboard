# ZDI-16-178: Microsoft Edge GetLineBoxForReuse Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-178
- **ZDI-CAN:** ZDI-CAN-3411
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0123
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** d81b2a7b317c035a8da11d63122964c2
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-178/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Microsoft Edge processes HTML content with absolute positioning. By manipulating a document's elements an attacker can force Microsoft Edge to read memory outside the bounds of an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-024

## Disclosure Timeline

- 2015-11-24 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
