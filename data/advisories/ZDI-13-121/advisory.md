# ZDI-13-121: Hewlett-Packard Data Protector Cell Manager crs.exe Multiple Opcodes Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-121
- **ZDI-CAN:** ZDI-CAN-1629
- **Date:** 2013-06-11
- **CVE:** CVE-2013-2324
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-121/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within crs.exe which listens by default on a random TCP port. When parsing opcodes 207/210/236/243/265, the process blindly copies user supplied data into a fixed-length stack buffer. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03781657

## Disclosure Timeline

- 2012-12-04 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
