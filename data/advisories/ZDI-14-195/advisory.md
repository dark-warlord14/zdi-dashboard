# ZDI-14-195: Hewlett-Packard AutoPass License Server Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-195
- **ZDI-CAN:** ZDI-CAN-2031
- **Date:** 2014-06-11
- **CVE:** CVE-2013-6221
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** AutoPass License Server
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-195/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard AutoPass License Server. Authentication is not required to exploit this vulnerability. The flaw exists within the CommunicationServlet. The specific flaw is a directory traversal vulnerability, which allows an unauthenticated user to write a file anywhere on the server. An attacker can leverage this vulnerability to execute arbitrary code in the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04333125

## Disclosure Timeline

- 2013-12-09 - Vulnerability reported to vendor
- 2014-06-11 - Coordinated public release of advisory
