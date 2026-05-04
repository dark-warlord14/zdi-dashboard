# ZDI-26-284: DriveLock Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-284
- **ZDI-CAN:** ZDI-CAN-28746
- **Date:** 2026-04-15
- **CVE:** CVE-2026-5487
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** DriveLock
- **Affected Products:** DriveLock
- **Credit:** stuxxn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-284/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of DriveLock. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 4568 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

DriveLock has issued an update to correct this vulnerability. More details can be found at: https://www.drivelock.help/sb/Content/SecurityBulletins/26-003-PathValidation.htm

## Disclosure Timeline

- 2026-02-06 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
