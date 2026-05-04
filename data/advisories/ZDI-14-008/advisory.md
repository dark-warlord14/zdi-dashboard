# ZDI-14-008: Hewlett-Packard Data Protector Backup Client Service EXEC_BAR Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-008
- **ZDI-CAN:** ZDI-CAN-1885
- **Date:** 2014-01-10
- **CVE:** CVE-2013-2347
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute remote code on vulnerable installations of HP Data Protector. Authentication is not required to exploit this vulnerability. This specific flaw exists in the Backup Client Service (OmniInet.exe). The Backup Client Service listens on TCP port 5555 for communications between systems in the cell. The process has insufficient sanitization on user-supplied data when handling certain messages. Remote, unauthenticated attackers can exploit this vulnerability by sending malicious EXEC_BAR packet to the target that results in an arbitrary command execution in the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03822422

## Disclosure Timeline

- 2013-05-24 - Vulnerability reported to vendor
- 2014-01-10 - Coordinated public release of advisory
