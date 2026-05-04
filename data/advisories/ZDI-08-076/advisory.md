# ZDI-08-076: EMC Control Center SST_SENDFILE Remote File Retrieval Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-076
- **ZDI-CAN:** ZDI-CAN-406
- **Date:** 2008-11-20
- **CVE:** CVE-2008-5420
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** Control Center
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-076/
## Vulnerability Details

This vulnerability allows remote attackers to retrieve arbitrary files on systems with vulnerable installations of EMC Control Center. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Master Agent service (msragent.exe) which listens by default on TCP port 10444. While processing SST_SENDFILE requests the service does not validate the requestor allowing any remote attacker to download arbitrary files.

## Additional Details

Customers should upgrade to version 6.1 which contains the fix.

## Disclosure Timeline

- 2008-11-10 - Vulnerability reported to vendor
- 2008-11-20 - Coordinated public release of advisory
