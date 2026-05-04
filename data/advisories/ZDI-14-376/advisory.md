# ZDI-14-376: Microsoft Internet Explorer CStyleSheet::get_parentStyleSheet Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-376
- **ZDI-CAN:** ZDI-CAN-2433
- **Date:** 2014-11-19
- **CVE:** CVE-2014-6341
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** s3tm3m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-376/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to the way Internet Explorer tracks the relationship between two CSS stylesheets when one is imported by the other. The imported stylesheet continues to refer to its parent stylesheet even after the parent stylesheet is no longer valid. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-065.aspx

## Disclosure Timeline

- 2014-07-24 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
