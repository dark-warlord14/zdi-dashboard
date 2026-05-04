# ZDI-14-136: Cogent DataHub Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-136
- **ZDI-CAN:** ZDI-CAN-2160
- **Date:** 2014-05-19
- **CVE:** CVE-2014-3789
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cogent Real-Time Systems
- **Affected Products:** Cogent Datahub
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cogent DataHub. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GetPermissions.asp component of the web server. This active server page is vulnerable to command injection which allows an attacker to execute arbitrary code in the context of the DataHub process.

## Additional Details

Cogent Real-Time Systems has issued an update to correct this vulnerability. More details can be found at: http://cogentdatahub.com/ReleaseNotes.html

## Disclosure Timeline

- 2014-04-07 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
