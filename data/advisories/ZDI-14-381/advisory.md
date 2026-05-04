# ZDI-14-381: Microsoft Internet Explorer CSS Quotes Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-381
- **ZDI-CAN:** ZDI-CAN-2544
- **Date:** 2014-11-19
- **CVE:** CVE-2014-6351
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** ca0nguyen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-381/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes CSS-generated quotes. By creating a document with a particular structure that utilizes CSS-generated quotes, an attacker can force a CQuotes object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-065.aspx

## Disclosure Timeline

- 2014-10-05 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
