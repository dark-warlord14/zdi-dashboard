# ZDI-14-004: Hewlett-Packard Data Protector Backup Client Service rrda Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-004
- **ZDI-CAN:** ZDI-CAN-1870
- **Date:** 2014-01-10
- **CVE:** CVE-2013-2346
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-004/
## Vulnerability Details

This vulnerability allows remote attackers directory traversal on vulnerable installations of HP OpenView Data Protector. Authentication is not required to exploit this vulnerability. This specific flaw exists in the Backup Client Service (OmniInet.exe). The Backup Client Service listens on TCP port 5555 for communications between systems in the cell. Omininet.exe starts rrda.exe for processing rrda request messages. This process blindly copies user supplied data into a fixed-length stack buffer. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03822422

## Disclosure Timeline

- 2013-05-24 - Vulnerability reported to vendor
- 2014-01-10 - Coordinated public release of advisory
