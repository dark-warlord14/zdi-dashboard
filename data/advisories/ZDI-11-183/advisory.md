# ZDI-11-183: Oracle Java ICC Profile MultiLanguage 'mluc' Tag Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-183
- **ZDI-CAN:** ZDI-CAN-1029
- **Date:** 2011-06-08
- **CVE:** CVE-2011-0862
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-183/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the way Java handles color profiles. When parsing a color profile containing a invalid MultiLanguage 'mluc' tag it is possible to cause an integer to wrap during an arithmetic operation. This new value is used to allocate memory on the heap. A remote attacker can abuse the faulty code to execute code under the context of the user running the browser.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujune2011-313339.html

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-08 - Coordinated public release of advisory
