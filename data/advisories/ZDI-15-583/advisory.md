# ZDI-15-583: Microsoft Edge CAttrArray Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-583
- **ZDI-CAN:** ZDI-CAN-3281
- **Date:** 2015-12-08
- **CVE:** CVE-2015-6168
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-583/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Microsoft Edge deletes elements from attribute arrays (as implemented by CAttrArray). By manipulating a document's elements an attacker can cause Edge to read memory outside the bounds of the array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-125.aspx

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
