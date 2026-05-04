# ZDI-10-291: Symantec Endpoint Protection Manager Reporting Server fw_charts.php Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-291
- **ZDI-CAN:** ZDI-CAN-756
- **Date:** 2010-12-15
- **CVE:** CVE-2010-0114
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Endpoint Protection. Authentication is not required to exploit this vulnerability. The specific flaw exists within the portion of the server that generates reports. Due to the combination of insufficient checks being performed on the application and failure to authenticate a user for generating a chart, an attacker can overwrite arbitrary files on a server. Careful exploitation can lead to code execution under the context of the php interpreter.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2010&suid=20101215_00

## Disclosure Timeline

- 2010-04-06 - Vulnerability reported to vendor
- 2010-12-15 - Coordinated public release of advisory
