# ZDI-15-444: Symantec Web Gateway Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-444
- **ZDI-CAN:** ZDI-CAN-3057
- **Date:** 2015-09-16
- **CVE:** CVE-2015-5690 , CVE-2015-5693
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-444/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Web Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the path processing for command URLs accessed through the management port of the gateway. A crafted URL can cause the Web Gateway to execute a command that should not be available externally. An attacker can exploit this vulnerability to execute arbitrary commands under the context of root.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=&suid=20150916_00

## Disclosure Timeline

- 2015-08-03 - Vulnerability reported to vendor
- 2015-09-16 - Coordinated public release of advisory
