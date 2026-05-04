# ZDI-08-041: Novell eDirectory dhost Integer Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-041
- **ZDI-CAN:** ZDI-CAN-276
- **Date:** 2008-07-10
- **CVE:** CVE-2008-3159
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell eDirectory. Authentication is not required to exploit this vulnerability. The specific flaw exists within dhost.exe, bound by default to TCP port 524. Flawed arithmetic applied to a user-supplied value results in an integer overflow and subsequently a complete stack smash allowing an attacker to execute arbitrary code via SEH redirection.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&sliceId=SAL_Public&externalId=3694858

## Disclosure Timeline

- 2007-12-04 - Vulnerability reported to vendor
- 2008-07-10 - Coordinated public release of advisory
