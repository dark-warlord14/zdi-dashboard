# ZDI-14-350: Microsoft Word Style Tag Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-350
- **ZDI-CAN:** ZDI-CAN-2484
- **Date:** 2014-10-14
- **CVE:** CVE-2014-4117
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-350/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of style tags. By nesting a specific style tag within another, an attacker is able to cause a pointer to be used after the underlying object has been freed. This could be used to execute arbitrary code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-061

## Disclosure Timeline

- 2014-08-04 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
