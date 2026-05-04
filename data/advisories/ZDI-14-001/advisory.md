# ZDI-14-001: Hewlett-Packard Data Protector Backup Client Service RxNtSetup Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-001
- **ZDI-CAN:** ZDI-CAN-1866
- **Date:** 2014-01-10
- **CVE:** CVE-2013-2344
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Brian Gorenc HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute remote code on vulnerable installations of HP Data Protector. Authentication is not required to exploit this vulnerability. This specific flaw exists in the Backup Client Service (OmniInet.exe). The Backup Client Service listens on TCP port 5555 for communications between systems in the cell. The process has insufficient sanitization on user-supplied data when handling certain messages. Remote, unauthenticated attackers can instruct the client to access a file off of a share thus executing arbitrary code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03822422

## Disclosure Timeline

- 2013-05-24 - Vulnerability reported to vendor
- 2014-01-10 - Coordinated public release of advisory
