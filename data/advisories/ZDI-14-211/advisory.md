# ZDI-14-211: Symantec Web Gateway user.php SQL Injection and snmpConfig.php Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-211
- **ZDI-CAN:** ZDI-CAN-2047
- **Date:** 2014-06-18
- **CVE:** CVE-2013-5017
- **CVSS:** 7.9
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:N
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-211/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Web Gateway. Authentication is required to exploit this vulnerability. The specific flaws exist within the user.php and snmpConfig.php files. SQL injection and command injection is possible through vulnerable request parameters. An attacker can leverage these vulnerabilities to read files and achieve remote code execution under the context of the root user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=&suid=20140616_00

## Disclosure Timeline

- 2013-12-18 - Vulnerability reported to vendor
- 2014-06-18 - Coordinated public release of advisory
